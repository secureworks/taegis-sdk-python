"""utils.py

Taegis SDK Python General Utilities"""

import asyncio
import concurrent
import logging
from dataclasses import fields as dc_fields
from dataclasses import is_dataclass
from enum import Enum, EnumMeta
from typing import Any, Callable, Dict, Optional, Union

from graphql.language.ast import FieldNode
from graphql.language.location import SourceLocation
from graphql.type import is_object_type, is_scalar_type
from graphql.type import is_union_type as is_gql_union_type
from graphql.type import is_wrapping_type
from typing_inspect import get_args, is_union_type
from taegis_sdk_python._consts import TaegisEnum

log = logging.getLogger(__name__)


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
    if is_union_type(cls):
        fragments = ["__typename"]
        for item in get_args(cls):
            output_string = _build_dataclass_string(item)
            fragments.append(f"... on {item.__name__} {{{output_string}}}")
        return "\n".join(fragments)

    return _build_dataclass_string(cls)


def _build_dataclass_string(cls) -> str:
    """Build output string from a Dataclass."""

    output_fields = []
    for field in dc_fields(cls):
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

        # unwrap the field type
        # example: Optional[List[List[Event]]]
        # should submit Event for recursive iteration
        type_ = field.type
        while args := get_args(type_):
            type_ = args[0]

        if is_dataclass(type_):
            output_fields.append(f"{{ {_build_dataclass_string(type_)} }}")

    return " ".join(output_fields)


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


def parse_union_result(union, result: Dict[str, Any]) -> Any:
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
