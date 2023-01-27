# Taegis SDK for Python

## Querying Alerts

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import SearchRequestInput

service = GraphQLService()
results = service.alerts.query.alerts_service_search(SearchRequestInput(
    cql_query="FROM alerts WHERE severity >= 0.6 AND severity = 'OPEN' EARLIEST=-3d",
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
    cql_query="FROM alerts WHERE severity >= 0.6 AND severity = 'OPEN' EARLIEST=-3d",
    limit=1000000,
    offset=0,
))

poll_responses = [results]
search_id = result.search_id
total_parts = result.alerts.total_parts

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
            isinstance(response, AlertsResponse)
            and response.alerts is not None
        ):
            poll_responses.append(response)

alerts = [
    alert
    for response in poll_responses
    for alert in response.alerts.list
]
```
