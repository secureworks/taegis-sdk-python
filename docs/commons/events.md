# Taegis SDK for Python

## Events Commons

### Function Summary

#### get_next_page
- **Signature**: `get_next_page(events_results: List[EventQueryResults]) -> Optional[str]`
- **Parameters**:
	- `events_results`: List of `EventQueryResults` pages returned by the events API.
- **Returns**: `Optional[str]` — a page token / indicator for the next page, or `None` when there is no next page.
- **Behavior / Notes**:
	- Scans the provided result pages for any non-None `.next` values and returns the first unique token found.
	- Returns `None` if no `.next` token is present in any page.

#### events_search
- **Signature**: `events_search(service: GraphQLService, query: str, *, options: Optional[EventQueryOptions] = None, caller_name: str = "Taegis SDK Commons") -> List[EventQueryResults]`
- **Parameters**:
	- `service`: `GraphQLService` instance used to call the Taegis Events API.
	- `query`: CQL/query string used to request events.
	- `options`: Optional `EventQueryOptions` to control ordering, page size, maximum rows, and aggregation.
	- `caller_name`: Optional metadata string used for caller identification (default: "Taegis SDK Commons").
- **Returns**: A list of `EventQueryResults` pages containing events and pagination tokens.
- **Behavior / Notes**:
	- If `options` is not provided, defaults are used: `timestamp_ascending=True`, `page_size=1000`, `max_rows=100000`, `aggregation_off=False`.
	- Performs an initial `event_query` subscription call and then follows subsequent pages by using `event_page` with the `.next` token discovered via `get_next_page`.
	- Continues paging until no next page token is found.

#### Example setup and call

Below example demonstrates how to call `events_search`. Per request, `GraphQLService` constructor parameters are not filled — supply your runtime configuration as needed.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.events.search import events_search

service = GraphQLService()

# Example query (replace with a valid events query for your environment)
query = "WHERE @ip = '1.1.1.1'"

# Execute the search
responses = events_search(service, query)

# Count total events across all pages
total_events = sum(len(r.events) for r in responses)
print(f"Total events retrieved: {total_events}")
```
