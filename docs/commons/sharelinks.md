# Taegis SDK for Python

## Sharelinks Commons

### Function Summary

#### create_sharelink
- **Signature**: `create_sharelink(service: GraphQLService, input_: ShareLinkCreateInput) -> str`
- **Parameters**:
	- `service`: `GraphQLService` instance used to call the Taegis Sharelinks API.
	- `input_`: `ShareLinkCreateInput` containing link reference, target, type, tenant ID, and optional extra parameters.
- **Returns**: `str` — a shareable URL constructed from the service sync URL and the created sharelink id.
- **Behavior / Notes**:
	- Invokes the GraphQL mutation `create_share_link` with the provided input.
	- Constructs and returns a shareable URL in the format `https://{sync_url_without_api}/share/{result.id}`.

#### create_alerts_query_sharelink
- **Signature**: `create_alerts_query_sharelink(service: GraphQLService, query_identifier: str) -> str`
- **Parameters**:
	- `service`: `GraphQLService` instance used to call the Taegis Sharelinks API.
	- `query_identifier`: A CQL query identifier string.
- **Returns**: `str` — a shareable URL for the alerts query.
- **Behavior / Notes**:
	- Helper function that builds a `ShareLinkCreateInput` with `link_target="cql"`, `link_type="queryId"`, and an extra parameter `sourceType=alert`.
	- Delegates to `create_sharelink` to perform the actual mutation.

#### create_events_query_sharelink
- **Signature**: `create_events_query_sharelink(service: GraphQLService, query_identifier: str) -> str`
- **Parameters**:
	- `service`: `GraphQLService` instance used to call the Taegis Sharelinks API.
	- `query_identifier`: A CQL query identifier string.
- **Returns**: `str` — a shareable URL for the events query.
- **Behavior / Notes**:
	- Helper function that builds a `ShareLinkCreateInput` with `link_target="cql"`, `link_type="queryId"`, and an extra parameter `sourceType=event`.
	- Delegates to `create_sharelink` to perform the actual mutation.

#### create_investigations_sharelink
- **Signature**: `create_investigations_sharelink(service: GraphQLService, investigation_id: str) -> str`
- **Parameters**:
	- `service`: `GraphQLService` instance used to call the Taegis Sharelinks API.
	- `investigation_id`: An investigation UUID or identifier string.
- **Returns**: `str` — a shareable URL for the investigation.
- **Behavior / Notes**:
	- Helper function that builds a `ShareLinkCreateInput` with `link_type="investigationId"`.
	- Delegates to `create_sharelink` to perform the actual mutation.

#### create_cases_sharelink
- **Signature**: `create_cases_sharelink(service: GraphQLService, case_id: str) -> str`
- **Parameters**:
	- `service`: `GraphQLService` instance used to call the Taegis Sharelinks API.
	- `case_id`: A case UUID or identifier string.
- **Returns**: `str` — a shareable URL for the case.
- **Behavior / Notes**:
	- Helper function that builds a `ShareLinkCreateInput` with `link_type="investigationId"` (cases are treated as investigation references).
	- Delegates to `create_sharelink` to perform the actual mutation.

#### unfurl_sharelink
- **Signature**: `unfurl_sharelink(service: GraphQLService, id_: str) -> Any`
- **Parameters**:
	- `service`: `GraphQLService` instance used to call the Taegis Sharelinks API.
	- `id_`: A sharelink id string or full sharelink URL (e.g., `https://example.taegis.com/share/{id}`).
- **Returns**: `Any` — the underlying resource matching the sharelink type (alerts, events, investigation, or rule object).
- **Behavior / Notes**:
	- If `id_` contains `/share/`, extracts the id from the URL path.
	- Queries `share_link_by_id` to retrieve sharelink metadata.
	- Based on `results.link_type`, fetches the underlying resource using the appropriate service (alerts, events, investigations2, or rules).
	- Switches tenant context using `with service(tenant_id=results.tenant_id)` when querying the underlying resource.
	- For `link_type="rules"`, catches `GraphQLNoRowsInResultSetError` and returns an empty `Rule()` object as fallback.
	- Raises `ValueError` if `link_type` is unrecognized.

### Example setup and call

Below examples demonstrate how to call the sharelinks functions. Per request, `GraphQLService` constructor parameters are not filled — supply your runtime configuration as needed.

#### create_sharelink example

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.sharelinks.create import create_sharelink
from taegis_sdk_python.services.sharelinks.types import ShareLinkCreateInput

service = GraphQLService()

input_ = ShareLinkCreateInput(
    link_ref="query-abc-123",
    link_target="cql",
    link_type="queryId",
    tenant_id="tenant-xyz",
)
share_url = create_sharelink(service, input_)
print("Share URL:", share_url)
```

#### create_alerts_query_sharelink example

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.sharelinks.create import create_alerts_query_sharelink

service = GraphQLService()

# Create a shareable link for an alerts query
alerts_url = create_alerts_query_sharelink(service, "query-id-123")
print("Alerts Share URL:", alerts_url)
```

#### create_events_query_sharelink example

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.sharelinks.create import create_events_query_sharelink

service = GraphQLService()

# Create a shareable link for an events query
events_url = create_events_query_sharelink(service, "query-id-123")
print("Events Share URL:", events_url)
```

#### create_investigations_sharelink and create_cases_sharelink example

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.sharelinks.create import (
    create_investigations_sharelink,
    create_cases_sharelink,
)

service = GraphQLService()

# Create a shareable link for an investigation
inv_url = create_investigations_sharelink(service, "investigation-uuid-001")
print("Investigation Share URL:", inv_url)

# Create a shareable link for a case
case_url = create_cases_sharelink(service, "case-uuid-002")
print("Case Share URL:", case_url)
```

#### unfurl_sharelink example with URL

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.sharelinks.unfurl import unfurl_sharelink

service = GraphQLService()

# Unfurl a full sharelink URL
share_url = "https://example.taegis.com/share/abcdef-123456"
result = unfurl_sharelink(service, share_url)
print("Unfurled result:", result)
```

#### unfurl_sharelink example with sharelink id

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.commons.sharelinks.unfurl import unfurl_sharelink

service = GraphQLService()

# Unfurl using just the sharelink id
result = unfurl_sharelink(service, "abcdef-123456")
# result type depends on the underlying link_type:
# - "alertId" or "alertV2Id" -> alerts response
# - "eventId" -> events response
# - "investigationId" -> InvestigationV2 response
# - "rules" -> Rule object or empty Rule()
print("Unfurled result:", result)
```

- Example: unfurl by share id
```python
from taegis_sdk_python.commons.sharelinks.unfurl import unfurl_sharelink
# service = GraphQLService(...)
result = unfurl_sharelink(service, "abcdef-123456")
# result's type depends on the sharelink's link_type:
# - "alertId" or "alertV2Id" -> alerts response
# - "eventId" -> events response
# - "investigationId" -> InvestigationV2 response
# - "rules" -> Rule or empty Rule()
print(type(result), result)
```
- What it does: Directly uses the id to fetch sharelink metadata and then returns the appropriate underlying resource (switching `service` tenant context via `with service(tenant_id=...)` where required).
