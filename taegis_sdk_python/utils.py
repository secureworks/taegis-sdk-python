"""utils.py

Taegis SDK Python General Utilities"""
import asyncio
import concurrent
from dataclasses import is_dataclass
from enum import Enum
from typing import Any, Callable, Dict, Optional, Union

from typing_inspect import get_args, is_union_type


def build_output_string(dataclass) -> str:
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
    if is_union_type(dataclass):
        fragments = ["__typename"]
        for item in get_args(dataclass):
            output_string = _build_dataclass_string(item)
            fragments.append(f"... on {item.__name__} {{{output_string}}}")
        return "\n".join(fragments)

    return _build_dataclass_string(dataclass)


def _build_dataclass_string(dataclass) -> str:
    """Build output string from a Dataclass."""

    def get_nested_field(dataclass) -> str:
        fields = []
        for _, field in dataclass.fields.items():
            fields.append(field.data_key)
            if hasattr(field, "nested"):
                fields.append(f"{{ {get_nested_field(field.nested)} }}")
            if hasattr(field, "inner") and hasattr(field.inner, "nested"):
                fields.append(f"{{ {get_nested_field(field.inner.nested)} }}")
        return " ".join(fields)

    fields = []
    for _, field in dataclass.schema().declared_fields.items():
        fields.append(field.data_key)
        if hasattr(field, "nested"):
            fields.append(f"{{ {get_nested_field(field.nested)} }}")
        if hasattr(field, "inner") and hasattr(field.inner, "nested"):
            fields.append(f"{{ {get_nested_field(field.inner.nested)} }}")
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
        # return Dict[str. Any] where Any is not None
        return {
            key: value
            for key, value in value.to_dict(encode_json=True).items()
            if value is not None
        }
    # return value of Enum instead of the object
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, list):
        return [prepare_input(item) for item in value]
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
    return (
        {key: value for key, value in variables.items() if value is not None}
        if variables
        else None
    )


__all__ = ["build_output_string", "async_block", "prepare_input", "prepare_variables"]
