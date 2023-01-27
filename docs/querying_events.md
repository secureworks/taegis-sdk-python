# Taegis SDK for Python

## Querying Events

```python
from taegis_sdk_python.services import GraphQLService
from taegis_sdk_python.services.events.types import EventQueryOptions

service = GraphQLService()
options = EventQueryOptions(
    timestamp_ascending=True,
    page_size=1000,
    max_rows=1000,
    skip_cache=True,
    aggregation_off=False,
)

results = service.events.subscription.event_query("FROM process EARLIEST=-1d | head 10", options=options)
```

## Pagination

```python
from taegis_sdk_python.services import GraphQLService
from taegis_sdk_python.services.events.types import EventQueryResults, EventQueryOptions
from typing import List, Optional

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

service = GraphQLService()
options = EventQueryOptions(
    timestamp_ascending=True,
    page_size=1000,
    max_rows=100000,
    skip_cache=True,
    aggregation_off=False,
)
results = []

result = service.events.subscription.event_query("FROM process EARLIEST=-1d | head 10", options=options)
results.extend(result)
next_page = get_next_page(result)

while next_page:
    result = service.events.subscription.event_page(next_page)
    results.extend(result)
    next_page = get_next_page(result)
```
