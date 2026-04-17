# Taegis SDK for Python

## Alerts Commons

### Function Summary

#### `alerts_search`
- **Parameters**:
  - `service`: A `GraphQLService` instance for interacting with the Taegis API.
  - `query`: A string representing the CQL query for searching alerts.
  - `limit`: Optional integer (default 10000) specifying the maximum number of alerts to retrieve. Automatically set to 1 if "aggregate" is in the query.
  - `caller_name`: Optional string (default "Taegis SDK Commons") for metadata.
- **Return Type**: `List[AlertsResponse]` – A list of response objects containing alert data.
- **Description**: Performs a search on the Taegis Alerts service using the provided CQL query. Handles pagination by polling additional parts if a search ID is present, with error handling for missing parts. Includes a workaround for issue CX-92571 to respect the limit.

#### Example Setup and Call

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.alerts.search import alerts_search

# Initialize the GraphQL service
service = GraphQLService()

# Example call: Search for alerts with a simple query
query = "FROM alert WHERE status = 'OPEN'"
responses = alerts_search(service, query, limit=500)

# Process the responses (e.g., print the number of alerts retrieved)
total_alerts = sum(len(response.alerts.list) for response in responses if response.alerts)
print(f"Total alerts retrieved: {total_alerts}")
```

#### `alerts_federated_search`
- **Parameters**:
  - `service`: A `GraphQLService` instance for interacting with the Taegis API.
  - `query`: A string representing the CQL query for searching alerts.
  - `limit`: Optional integer (default 10000) specifying the maximum number of alerts to retrieve. Automatically set to 1 if "aggregate" is in the query.
  - `caller_name`: Optional string (default "Taegis SDK Commons") for metadata.
  - `federated_call`: Optional callable (default alerts_service_search_with_events)
  - `federated_poll_call`: Optional callable (default alerts_service_poll_with_events)
- **Return Type**: `List[TaegisCommonsAlertsResponse]` – A list of response objects containing alert data.
- **Description**: Performs a search on the Taegis Alerts service using the provided CQL query and retrieves federated `event_data`. Handles pagination by polling additional parts if a search ID is present, with error handling for missing parts. Includes a workaround for issue CX-92571 to respect the limit.

`federated_call` and `federated_poll_call` may be replaced to federate other fields across GraphQL calls.

#### Example Setup and Call

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.alerts.federated_search import alerts_federated_search

# Initialize the GraphQL service
service = GraphQLService()

# Example call: Search for alerts with a simple query
query = "FROM alert WHERE status = 'OPEN'"
responses = alerts_federated_search(service, query, limit=500)

# Process the responses (e.g., print the number of alerts retrieved)
total_alerts = sum(len(response.alerts.list) for response in responses if response.alerts)
print(f"Total alerts retrieved: {total_alerts}")
```
