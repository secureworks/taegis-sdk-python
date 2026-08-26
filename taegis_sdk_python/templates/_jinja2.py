"""Taegis SDK Jinja2 Support."""

import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Union

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


def filter_or(value: list[str], field_name: Optional[str] = None, operator: str = "="):
    """Format values for Taegis QL OR statement."""
    if not isinstance(value, list):
        raise TypeError("Input is not list.")

    return " OR ".join(
        [
            f"{field_name} {operator} {escape_value(item)}" if field_name else value
            for item in value
        ]
    )


def filter_and(value: list[str], field_name: str, operator: str = "="):
    """Format values for Taegis QL AND statement."""
    if not isinstance(value, list):
        raise TypeError("Input is not list.")

    return " AND ".join(
        [f"{field_name} {operator} {escape_value(item)}" for item in value]
    )


def filter_in(value: list[str], field_name: str):
    """Format values for Taegis QL IN statement."""
    if not isinstance(value, list):
        raise TypeError("Input is not list.")

    in_ = ",".join([escape_value(item) for item in value])
    return f"{field_name} IN ({in_})"


def filter_not_in(value: list[str], field_name: str):
    """Format values for Taegis QL !IN statement."""
    if not isinstance(value, list):
        raise TypeError("Input is not list.")

    in_ = ",".join([escape_value(item) for item in value])
    return f"{field_name} !IN ({in_})"


def filter_regex(value: list[str], field_name: str, separator="|"):
    """Format values for Taegis QL MATCHES_REGEX statement."""
    if not isinstance(value, list):
        raise TypeError("Input is not list.")

    pattern = separator.join([re.escape(rf"{item}") for item in value])

    return f"{field_name} MATCHES_REGEX '{pattern}'"


def filter_not_regex(value: list[str], field_name: str, separator="|"):
    """Format values for Taegis QL !MATCHES_REGEX statement."""
    if not isinstance(value, list):
        raise TypeError("Input is not list.")

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


##########


@dataclass(frozen=True)
class TimeWindow:
    """An inclusive Taegis QL time range with formatted earliest and latest bounds."""

    earliest: str
    latest: str


def parse_timedelta(value: str) -> timedelta:
    """Parse a duration string into a timedelta."""
    match = re.fullmatch(r"\s*(\d+)\s*([smhdwy]|mo)\s*", value.lower())
    if not match:
        raise ValueError(f"Invalid duration: {value!r}")

    amount, unit = match.groups()
    amount = int(amount)

    if amount <= 0:
        raise ValueError("Duration must be greater than zero.")

    if unit == "s":
        delta = timedelta(seconds=amount)
    elif unit == "m":
        delta = timedelta(minutes=amount)
    elif unit == "h":
        delta = timedelta(hours=amount)
    elif unit == "d":
        delta = timedelta(days=amount)
    elif unit == "w":
        delta = timedelta(weeks=amount)
    elif unit == "mo":
        delta = timedelta(days=amount * 30)
    elif unit == "y":
        delta = timedelta(days=amount * 365)
    else:
        raise ValueError(f"Invalid duration unit: {unit!r}")

    return delta


def time_split_windows(initial_duration: str, chunk_duration: str) -> list[TimeWindow]:
    """Create contiguous UTC time windows for a query."""
    initial_delta = parse_timedelta(initial_duration)
    chunk_delta = parse_timedelta(chunk_duration)

    # Exclude the current second from the query range.
    latest_allowed = datetime.now(timezone.utc).replace(microsecond=0) - timedelta(
        seconds=1
    )
    start = latest_allowed - initial_delta

    windows = []
    while start < latest_allowed:
        end = min(start + chunk_delta, latest_allowed)

        windows.append(
            TimeWindow(
                earliest=(start + timedelta(seconds=1)).strftime("%Y-%m-%dT%H:%M:%S"),
                latest=end.strftime("%Y-%m-%dT%H:%M:%S"),
            )
        )

        start = end

    return windows


def time_split(
    *, environment: Environment, template_text: str, initial: str, chunk: str, **kwargs
):
    """Render a template once for each generated time window."""
    if (
        "EARLIEST='{{ window.earliest }}'" not in template_text
        or "LATEST='{{ window.latest }}'" not in template_text
    ):
        raise ValueError(
            "The template must contain the placeholders for window.earliest and window.latest."
        )

    windows = time_split_windows(initial, chunk)
    template = environment.from_string(template_text)

    return "\n---".join(template.render(window=window, **kwargs) for window in windows)
