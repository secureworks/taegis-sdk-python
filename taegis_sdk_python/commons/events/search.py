"""Taegis Commons Events search implementations."""

import logging
from typing import List, Optional

from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.events.types import EventQueryOptions, EventQueryResults

log = logging.getLogger(__name__)


def get_next_page(events_results: List[EventQueryResults]) -> Optional[str]:
    """Retrieve events  next page indicator."""
    try:
        # the next page could be found in any of the result pages,
        # but we cannot garuntee which result it will be found in
        return next(
            iter({result.next for result in events_results if result.next is not None})
        )
    except StopIteration:
        return None


def events_search(
    service: GraphQLService,
    query: str,
    *,
    options: Optional[EventQueryOptions] = None,
    caller_name: str = "Taegis SDK Commons",
) -> List[EventQueryResults]:
    """Taegis Events search."""
    if not options:
        options = EventQueryOptions(
            timestamp_ascending=True,
            page_size=1000,
            max_rows=100000,
            aggregation_off=False,
        )

    results = []

    result = service.events.subscription.event_query(
        query=query,
        options=options,
        metadata={"callerName": caller_name},
    )
    results.append(result)
    next_page = get_next_page(result)

    while next_page:
        result = service.events.subscription.event_page(next_page)
        results.append(result)
        next_page = get_next_page(result)

    return results
