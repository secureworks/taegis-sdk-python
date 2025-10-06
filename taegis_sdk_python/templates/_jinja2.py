"""Taegis SDK Jinja2 Support."""

import re
from pathlib import Path
from typing import List, Union

from jinja2 import Environment, FileSystemLoader

from taegis_sdk_python.config import get_config


def escape_value(value):
    """Escape values for Taegis QL."""
    if not isinstance(value, str):
        return str(value)

    if "'" in value:
        value = value.replace("'", r"\'")
        return f"e'{value}'"

    return f"'{value}'"


# Filters


def filter_or(value: List[str], field_name: str = None, operator: str = "="):
    """Format values for Taegis QL OR statement."""
    if not isinstance(value, list):
        raise ValueError("Input is not list.")

    return " OR ".join(
        [
            f"{field_name} {operator} {escape_value(item)}" if field_name else value
            for item in value
        ]
    )


def filter_and(value: List[str], field_name: str, operator: str = "="):
    """Format values for Taegis QL AND statement."""
    if not isinstance(value, list):
        raise ValueError("Input is not list.")

    return " AND ".join(
        [f"{field_name} {operator} {escape_value(item)}" for item in value]
    )


def filter_in(value: List[str], field_name: str):
    """Format values for Taegis QL IN statement."""
    if not isinstance(value, list):
        raise ValueError("Input is not list.")

    in_ = ",".join([escape_value(item) for item in value])
    return f"{field_name} IN ({in_})"


def filter_not_in(value: List[str], field_name: str):
    """Format values for Taegis QL !IN statement."""
    if not isinstance(value, list):
        raise ValueError("Input is not list.")

    in_ = ",".join([escape_value(item) for item in value])
    return f"{field_name} !IN ({in_})"


def filter_regex(value: List[str], field_name: str, separator="|"):
    """Format values for Taegis QL MATCHES_REGEX statement."""
    if not isinstance(value, list):
        raise ValueError("Input is not list.")

    pattern = separator.join([re.escape(rf"{item}") for item in value])

    return f"{field_name} MATCHES_REGEX '{pattern}'"


def filter_not_regex(value: List[str], field_name: str, separator="|"):
    """Format values for Taegis QL !MATCHES_REGEX statement."""
    if not isinstance(value, list):
        raise ValueError("Input is not list.")

    pattern = separator.join([re.escape(rf"{item}") for item in value])

    return f"{field_name} !MATCHES_REGEX '{pattern}'"


#########


def load_jinja2_template_environment(
    *args, searchpath: Union[str, Path, None] = None, **kwargs
) -> Environment:
    """Standardized Jinja2 Environment with Taegis QL filters."""
    config = get_config()

    if "loader" not in kwargs:
        if not searchpath:
            searchpath = config.get("templates", "jinja2", fallback=".")

        if isinstance(searchpath, str):
            searchpath = Path(searchpath)

        if not searchpath.exists():
            raise OSError(f"{searchpath} does exist")

        if not searchpath.is_dir():
            raise OSError(f"{searchpath} is not a directory")

        kwargs["loader"] = FileSystemLoader(searchpath=searchpath)

    if "trim_blocks" not in kwargs:
        kwargs["trim_blocks"] = True

    if "lstrip_blocks" not in kwargs:
        kwargs["lstrip_blocks"] = True

    environment = Environment(*args, **kwargs)

    environment.filters["or"] = filter_or
    environment.filters["and"] = filter_and
    environment.filters["in"] = filter_in
    environment.filters["not_in"] = filter_not_in

    environment.filters["regex"] = filter_regex
    environment.filters["not_regex"] = filter_not_regex
    environment.filters["matches_regex"] = filter_regex
    environment.filters["not_matches_regex"] = filter_not_regex

    return environment
