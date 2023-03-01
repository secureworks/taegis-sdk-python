# Taegis SDK for Python

## Querying Alerts

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import SearchRequestInput

service = GraphQLService()
results = service.alerts.query.alerts_service_search(SearchRequestInput(
    cql_query="FROM alert WHERE severity >= 0.6 AND status = 'OPEN' EARLIEST=-3d",
    limit=10000,
    offset=0,
))
```

## Pagination

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import SearchRequestInput, PollRequestInput, AlertsResponse

service = GraphQLService()
results = service.alerts.query.alerts_service_search(SearchRequestInput(
    cql_query="FROM alert WHERE severity >= 0.6 AND status = 'OPEN' EARLIEST=-3d",
    limit=1000000,
    offset=0,
))

poll_responses = [results]
search_id = results.search_id
total_parts = results.alerts.total_parts

if search_id:
    for part in range(2, total_parts + 1):
        results = None
        try:
            results = service.alerts.query.alerts_service_poll(
                PollRequestInput(
                    search_id=search_id,
                    part_id=part,
                )
            )
        except Exception as exc:
            if "not found" in str(exc):
                break
            raise exc

        if (
            isinstance(results, AlertsResponse)
            and results.alerts is not None
        ):
            poll_responses.append(results)

print(sum(
    len(response.alerts.list)
    for response in poll_responses
))
```
