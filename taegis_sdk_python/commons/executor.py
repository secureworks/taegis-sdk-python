"""Parse and execute delimiter-separated Taegis query work items."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Callable, Optional, TypeVar

ResultT = TypeVar("ResultT")
QueryCallable = Callable[[str], ResultT]


@dataclass
class QueryError:
    """An error associated with one query item."""

    item: str
    error: Exception


def parse_delimited_queries(value: str) -> list[str]:
    """Split a delimiter-separated query string into normalized items."""
    return [item.strip() for item in value.split("---") if item.strip()]


def execute_queries(
    items: list[str],
    query: QueryCallable[ResultT],
    max_workers: Optional[int] = None,
    error_handling: str = "propagate",
) -> tuple[list[ResultT], list[QueryError]]:
    """Execute query work items concurrently with selectable error handling."""
    if error_handling not in ("propagate", "partial"):
        raise ValueError("error_handling must be 'propagate' or 'partial'")

    if not items:
        return [], []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(query, item): (index, item)
            for index, item in enumerate(items)
        }

        if error_handling == "propagate":
            for future in as_completed(futures):
                future.result()
            return [future.result() for future in futures], []

        results = []
        errors = []
        for future in as_completed(futures):
            index, item = futures[future]
            try:
                results.append((index, future.result()))
            except Exception as error:  # pylint: disable=broad-except
                errors.append((index, QueryError(item=item, error=error)))

    return [result for _, result in results], [error for _, error in errors]


def execute_delimited_queries(
    value: str,
    query: QueryCallable[ResultT],
    max_workers: Optional[int] = None,
    error_handling: str = "propagate",
) -> tuple[list[ResultT], list[QueryError]]:
    """Parse and concurrently execute delimiter-separated query items."""
    return execute_queries(
        parse_delimited_queries(value),
        query,
        max_workers=max_workers,
        error_handling=error_handling,
    )
