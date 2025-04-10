"""utils.py

Taegis SDK Python General Utilities"""

import asyncio
import concurrent
import logging
from dataclasses import Field
from dataclasses import fields as dc_fields
from dataclasses import is_dataclass
from enum import Enum, EnumMeta
from typing import Any, Callable, Dict, List, Optional, Union

from graphql.language.ast import FieldNode
from graphql.language.location import SourceLocation
from graphql.type import is_object_type, is_scalar_type
from graphql.type import is_union_type as is_gql_union_type
from graphql.type import is_wrapping_type
from typing_inspect import get_args, is_union_type

from taegis_sdk_python._consts import TaegisEnum

log = logging.getLogger(__name__)


def unwrap(t: Field) -> Any:
    """Unwarp the provided fields

        Example conversions:
            Optional[str] -> str,
            Optional[List[str]] -> str,
            Optional[TDRUser] -> TDRUser,
            Optional[SubjectIdentity] -> (TDRUser, Client),
            Optional[List[List[Union[SubjectIdentity, str]]]] -> (TDRUser, Client, str)

    Parameters
    ----------
    t : Field
        DataClass Field

    Returns
    -------
    Any
    """

    log.debug(f"Unwrapping {t=}")

    # NoneType are added to Optional types
    # TaegisEnum are SDK specific types to handle
    # unknown Enum values returned from the API
    #
    # Neither of these need to be included to
    # generate GraphQL strings sent to the server
    args = [arg for arg in get_args(t) if arg != type(None) and arg != TaegisEnum]

    # Unwrap List[type]
    if hasattr(t, "_name") and t._name == "List":  # pylint: disable=protected-access
        log.debug(f"{t} is List...")
        return unwrap(args[0])

    if is_union_type(t):
        log.debug(f"{t} is Union...")

        # Unwrap Optional Type
        if len(args) == 1:
            return unwrap(args[0])

        # Unwrap Full Union Type
        return tuple(unwrap(a) for a in args)

    log.debug(f"{t} is unwrapped...")
    return t


def build_output_dataclass(cls: Any) -> Any:
    """Build Output String from Dataclass

    Parameters
    ----------
    cls : Any
        Python Class

    Returns
    -------
    Any
    """
    output_fields = []
    for field in dc_fields(cls):
        log.debug(f"{field=}")
        letter_case = field.metadata.get("dataclasses_json", {}).get("letter_case")
        if letter_case:
            field_name = letter_case(...)
        else:
            field_name = field.name

        if field.metadata.get("deprecated"):
            log.warning(
                f"Output field `{field_name}` is deprecated: "
                f"'{field.metadata.get('deprecation_reason')}', "
                "removing from default output..."
            )
            continue

        output_fields.append(field_name)

        type_ = unwrap(field.type)
        log.debug(f"{type_=}")

        if is_dataclass(type_):
            log.debug("Dataclass type detected, generating output string...")
            output_fields.append(f"{{ {build_output_string(type_)} }}")
            log.debug("Generating output string.  Done...")

        else:
            output_fields.append(build_output_string(type_))

    return output_fields


def build_output_string(cls) -> str:
    """
    Generate GraphQL output string from defined Dataclass.

    Parameters
    ----------
    dataclass : dataclass
        Dataclass class reference

    Returns
    -------
    str
        GraphQL Output
    """
    output_fields = []

    if is_dataclass(cls):
        log.debug(f"{cls} is dataclass...")
        output_fields.extend(build_output_dataclass(cls))

    elif is_union_type(cls):
        log.debug(f"{cls} is union...")
        output_fields.append("__typename")
        for item in get_args(cls):
            if item == type(None):
                continue
            output_string = build_output_string(item)
            output_fields.append(f"... on {item.__name__} {{ {output_string} }}")

    elif isinstance(cls, (list, tuple)):
        if len(cls) == 1:
            return ""

        log.debug("List or Tuple type detected, generating output string...")
        output_fields.append("{")
        output_fields.append("__typename")
        for item in cls:
            if item == type(None):
                continue
            output_string = build_output_string(item)
            output_fields.append(f"... on {item.__name__} {{ {output_string} }}")
        output_fields.append("}")
        log.debug("Generating output string.  Done...")

    else:
        log.debug(f"{cls} is scalar...")

        return ""

    log.debug(f"{output_fields=}...")

    output = " ".join(output_fields)

    return " ".join(output.split())


def graphql_unwrap_field(field: Any) -> Any:
    """
    Unwrap GraphQL objects to the internal scalar/object.

    Parameters
    ----------
    field : Any
        Any GraphQL object.

    Returns
    -------
    Any
        The base GraphQL object.
    """
    if hasattr(field, "type"):
        field_type = field.type
    elif hasattr(field, "of_type"):
        field_type = field.of_type
    else:
        return field

    if is_wrapping_type(field_type):
        return graphql_unwrap_field(field_type.of_type)
    return field_type


def build_output_string_from_introspection(field: Any) -> str:
    """
    Generate the fields string representation from a schema field.

    Parameters
    ----------
    field : Any
        A GraphQL schema field type.

    Returns
    -------
    str
        Output Fields
    """
    fields = []
    field = graphql_unwrap_field(field)

    if is_scalar_type(field):
        return ""

    if is_gql_union_type(field):
        fragments = ["__typename"]
        for gql_type in field.types:
            fragments.append(
                f"... on {gql_type.name} {{ {build_output_string_from_introspection(gql_type)} }}"
            )
        return "\n".join(fragments)

    for name, gql_type in field.fields.items():
        fields.append(name)
        scalar = graphql_unwrap_field(gql_type)
        if is_object_type(scalar):
            fields.append(f"{{ {build_output_string_from_introspection(scalar)} }}")
    return " ".join(fields)


def async_block(coro: Callable):
    """Decorator for running async function synchronously in another thread.

    This is used to ensure that our async calls are called separately from IPython's
    async event loop.
    """

    def wrapper(*args, **kwargs):
        def run_async(coro, *args, **kwargs):
            return asyncio.run(coro(*args, **kwargs))

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(run_async, coro, *args, **kwargs)
            result = future.result()

        return result

    return wrapper


def prepare_input(value: Any) -> Any:
    """Prepare input objects for submitting to GraphQL.

    Parameters
    ----------
    value : Any
        Input value

    Returns
    -------
    Any
        _description_
    """
    if is_dataclass(value):
        for field in dc_fields(value):
            letter_case = field.metadata.get("dataclasses_json", {}).get("letter_case")
            if letter_case:
                field_name = letter_case(...)
            else:
                field_name = field.name

            if field.metadata.get("deprecated"):
                log.warning(
                    f"Input field `{field_name}` is deprecated: "
                    f"'{field.metadata.get('deprecation_reason')}'"
                )

        # return Dict[str. Any] where Any is not None
        return {
            key: value
            for key, value in value.to_dict(encode_json=True).items()
            if value is not None and not value == TaegisEnum.UNKNOWN.value
        }
    # return value of Enum instead of the object
    if isinstance(value, Enum):
        if value is TaegisEnum.UNKNOWN:
            log.error(
                "Input is of value TaegisEnum.UNKNOWN, "
                "this is a placeholder that does not represent "
                "a valid value to submit to Taegis APIs."
            )
            return None
        return value.value
    if isinstance(value, list):
        return [prepare_input(item) for item in value]

    if value == TaegisEnum.UNKNOWN.value:
        log.error(
            "Input is of value TaegisEnum.UNKNOWN, "
            "this is a placeholder that does not represent "
            "a valid value to submit to Taegis APIs."
        )
        return None

    return value


def prepare_variables(
    variables: Optional[Dict[str, Any]] = None
) -> Union[None, Dict[str, Any]]:
    """
    Remove None values from a dictionary.

    Parameters
    ----------
    variables : Optional[Dict[str, Any]]
        Variables

    Returns
    -------
    Union[None, Dict[str, Any]]
        Variables
    """
    if variables is None:
        return None

    for key, value in variables.items():
        if value is TaegisEnum.UNKNOWN or value == TaegisEnum.UNKNOWN.value:
            raise ValueError(
                f"{key} is of value TaegisEnum.UNKNOWN, "
                "this is a placeholder that does not represent "
                "a valid value to submit to Taegis APIs."
            )

    return {key: value for key, value in variables.items() if value is not None}


def parse_union_result(
    union, result: Union[List[Dict[str, Any]], Dict[str, Any]]
) -> Any:
    """
    Coerse result into a type from union.

    Parameters
    ----------
    union : UnionType
        UnionType object
    result : Dict[str, Any]
        Result object

    Returns
    -------
    Any
        Union of union types or result object
    """
    if isinstance(result, list):
        return [parse_union_result(union, item) for item in result]
    for item in get_args(union):
        if result.get("__typename") == item.__name__:
            return item.from_dict(result)
    return result


def remove_node(query: str, node: FieldNode, location: SourceLocation) -> str:
    """Remove a GraphQL node with subnodes.

    Parameters
    ----------
    query : str
        GraphQL Query string
    node : FieldNode
        GraphQL Node
    location : SourceLocation
        GraphQL Node Location

    Returns
    -------
    str
        GraphQL Query string without erroring node (and subnodes)
    """
    key = node.name.value
    start_idx = location.column - 1
    end_idx = None

    brackets_found = 0
    for idx, char in enumerate(query):
        if idx < start_idx + len(key):
            continue

        if char == " ":
            continue

        if brackets_found == 0 and char != "{":
            end_idx = idx
            break

        if char == "{":
            brackets_found += 1

        elif char == "}":
            brackets_found -= 1

        end_idx = idx

    return query[:start_idx] + query[end_idx:]


def encode_enum(value: Any) -> Any:
    """Encode Enum to string value.

    Parameters
    ----------
    value : Any
        Enum Object

    Returns
    -------
    str
        Enum Value
    """
    if isinstance(value, list):
        return [encode_enum(v) for v in value]
    if isinstance(value, Enum):
        return value.value
    return value


def decode_enum(type_: Union[Enum, EnumMeta], value: str):
    """Decode Enum from string value.

    Parameters
    ----------
    type_ : Union[Enum, EnumMeta]
        Enum Type
    value : str
        Enum Value

    Returns
    -------
    Enum
        Enum Object
    """
    if isinstance(value, list):
        return [decode_enum(type_, v) for v in value]
    try:
        return type_(value)
    except ValueError:
        return TaegisEnum.UNKNOWN


__all__ = [
    "build_output_string",
    "async_block",
    "prepare_input",
    "prepare_variables",
    "parse_union_result",
    "build_output_string_from_introspection",
    "remove_node",
]
