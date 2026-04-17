# Taegis SDK for Python

## Cases Commons

### Function Summary

### cases_search
- **Signature**: `cases_search(service: GraphQLService, query: str, *, limit: int = 10000) -> List[InvestigationsV2]`
- **Parameters**:
  - `service`: GraphQLService instance used to call the Taegis Investigations API.
  - `query`: CQL query string to filter investigations/cases. Supports inline `head`/`tail` syntax (e.g., `| head 10`).
  - `limit`: Optional maximum number of investigations to retrieve (default 10000).
- **Returns**: A list of `InvestigationsV2` response objects (paged responses).
- **Behavior / Notes**:
  - Pages results using `page` and `per_page` (default per_page = 100).
  - Parses and honors `head` or `tail` in the query as a limit (CX-99036 fixes).
  - Builds the GraphQL output for `InvestigationsV2` and removes `metric`/`metrics` nodes (CX-103490 fixes).
  - Uses a `service(output=...)` context for each request.
  - Continues paging until the requested `limit` is reached or no more results.

#### Example setup and call

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.cases.search import cases_search

service = GraphQLService()

query = "FROM investigation WHERE status = 'OPEN' | head 50"
responses = cases_search(service, query, limit=50)

total_investigations = sum(len(r.investigations) for r in responses)
print(f"Total investigations retrieved: {total_investigations}")
```

### cases_federated_search
- **Signature**: `cases_federated_search(service: GraphQLService, query: str, *, limit: int = 10000, federated_call: Callable = investigations_search_with_sub) -> List[InvestigationsV2]`
- **Parameters**:
  - `service`: GraphQLService instance used to call the Taegis Investigations API.
  - `query`: CQL query string to filter investigations/cases. Supports inline `head`/`tail` syntax (e.g., `| head 10`).
  - `limit`: Optional maximum number of investigations to retrieve (default 10000).
  - `federated_call`: Optional callable (default investigations_search_with_subjects)
- **Returns**: A list of `InvestigationsV2` response objects (paged responses).
- **Behavior / Notes**:
  - Pages results using `page` and `per_page` (default per_page = 100).
  - Parses and honors `head` or `tail` in the query as a limit (CX-99036 fixes).
  - Builds the GraphQL output for `InvestigationsV2` and removes `metric`/`metrics` nodes (CX-103490 fixes).
  - Uses a `service(output=...)` context for each request.
  - Continues paging until the requested `limit` is reached or no more results.

`federated_call` may be replaced with any federating callable.

#### Example setup and call

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.cases.search import cases_federated_search

service = GraphQLService()

query = "FROM investigation WHERE status = 'OPEN' | head 50"
responses = cases_federated_search(service, query, limit=50)

total_investigations = sum(len(r.investigations) for r in responses)
print(f"Total investigations retrieved: {total_investigations}")
```
