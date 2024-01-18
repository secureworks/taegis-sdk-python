# Taegis SDK for Python

The Taegis SDK is a Python library for interfacing with the GraphQL APIs in Taegis.

## Getting Started

### Installation

```bash
python -m pip install taegis-sdk-python
```

### Example Usage

```python
from taegis_sdk_python import GraphQLService

from pprint import pprint as pp

service = GraphQLService()

results = service.users.query.current_tdruser()

pp(results)
```

### Querying the Correct Region

Region or Environment identifiers:

* `US1` or `charlie` or `production` for https://ctpx.secureworks.com/
* `US2` or `delta` for https://delta.taegis.secureworks.com/
* `US3` or `foxtrot` forhttps://foxtrot.taegis.secureworks.com/
* `EU` or `echo` for  https://echo.taegis.secureworks.com/

**Note**: `production` is useful for partners with child tenants that want to interate API calls over multiple tenants using the Tenants API.  The Tenants API uses the `production` identifier rather than `charlie` or `US1`, but this will direct the SDK to the correct region.

```python
service = GraphQLService(environment="US1")
service = GraphQLService(environment="US2")
service = GraphQLService(environment="US3")
service = GraphQLService(environment="EU")

# change the environment for an individual call
with service(environment="US1"):
    results = service.users.query.current_tdruser()

with service(environment="US2"):
    results = service.users.query.current_tdruser()
```

## Exploring the SDK

The SDK was built around utilizing the Python built-in: `help`.  You can use help on any object
within the `GraphQLService` object structure to understand what is available and how to call it.  The help menu is a great resource for determining input types.  Each service is self contained so that if you need an input, like `SearchRequestInput`, you will find it under `taegis_sdk_python.services.<service>.types`.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import SearchRequestInput

service = GraphQLService()

# Find available services (Service Endpoints)
help(service)
# Find available service queries (or mutations or subscriptions)
help(service.alerts.query)
help(service.alerts.mutation)
help(service.alerts.subscription)
# Reference documentation on specific endpoint
help(service.alerts.query.alerts_service_search)
# Help on an Input variable
help(SearchRequestInput)
```

```
# service
class GraphQLService(builtins.object)
 |  GraphQLService(*, environment: Optional[str] = None, tenant_id: Optional[str] = None, environments: Optional[Dict[str, str]] = None, gateway: Optional[str] = None)
...
 |  agent
 |      Events Service Endpoint.
 |
 |  alerts
 |      Alerts2 Service Endpoint.
 |
 |  assets
 |      Assets
...
# Alerts Query
class TaegisSDKAlertsQuery(builtins.object)
 |  TaegisS
...
 |  alerts_service_aggregate_alerts_by_severity(self, in_: 'Optional[AggregateAlertsBySeverityInputInput]' = None) -> 'AlertsAggregateResponse'
 |      Pull alert severity aggregates based on `group_by` parameters: domain, watchlist, hostname, detector, user..
 |
 |  alerts_service_alerts_dashboard_triage(self, in_: 'Optional[TriageDashboardInputInput]' = None) -> 'TriageDashboardOutput'
 |      None.
 |
 |  alerts_service_poll(self, in_: 'Optional[PollRequestInput]' = None) -> 'AlertsResponse'
 |      Poll for results for a specific `search
...
# SearchRequestInput
class SearchRequestInput(builtins.object)
 |  SearchRequestInput(cql_query: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None) -> None
...
```

*Note: Output has been truncated for verbosity.*

## Context Manager

The service object is also a context manager to help temporarily override default values when making
an API call.  This can include fields like the `environment`, `tenant_id`, `output`, or `access_token`.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import SearchRequestInput

service = GraphQLService()

with service(
    environment="US2",
    tenant_id="00000",
    output="""
        reason
        alerts {
            total_results
            list {
                id
                tenant_id
                metadata {
                    title
                    severity
                }
                status
            }
        }
    """,
):
    result = service.alerts.query.alerts_service_search(SearchRequestInput(
        offset=0,
        limit=10,
        cql_query="""
        FROM alert
        WHERE
            severity >= 0.6
        EARLIEST=-1d
        """
    ))
```

### Change Tenant Context

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

# specify the output fields, and start the service context
with service(tenant_id="00000"):
    result = service.investigations.query.investigations_search(
        page=1,
        per_page=3,
        query="WHERE deleted_at IS NOT NULL EARLIEST=-90d"
    )
pp(result)
```

### Change the Environment

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

# specify the output fields, and start the service context
with service(environment="US2"):
    result = service.investigations.query.investigations_search(
        page=1,
        per_page=3,
        query="WHERE deleted_at IS NOT NULL EARLIEST=-90d"
    )
pp(result)
```

### Use a preexisting access token

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

# specify the output fields, and start the service context
with service(access_token="<your access token>"):
    result = service.investigations.query.investigations_search(
        page=1,
        per_page=3,
        query="WHERE deleted_at IS NOT NULL EARLIEST=-90d"
    )
pp(result)
```

### Pruning GraphQL Output

One of the benefits of using GraphQL is that you can define which fields that you want returned.
By default we assume little to no knowledge of GraphQL to get you started, so we provide all the fields
in the API call for exploration reasons.  This may be unneeded for specific application or reporting
purposes.

To assist with this, we have a utility called `build_output_string`.  This will return a string
representation of the output object with all possible fields for the return type.  You can use
this as reference to build your own, or modify it to remove fields that are not needed.

```python
from taegis_sdk_python import build_output_string
from taegis_sdk_python.services.alerts.types import AlertsResponse

print(build_output_string(AlertsResponse))
```

```
reason search_id status alerts { previous_offset total_parts list { reference_details { reference {
description url type } } parent_tenant_id entities { entities relationships { relationship to_entity
from_entity type } } sensor_types suppression_rules { id version } resolution_history { timestamp {
nanos seconds } user_id status num_alerts_affected id reason } enrichment_details {
business_email_compromise { user_name source_address_geo_summary { country { confidence iso_code
geoname_id code } city { confidence locale_names { record { value key } } geoname_id name } location {
timezone latitude longitude us_metro_code radius metro_code gmt_offset } asn { autonomous_system_no
autonomous_system_org } continent { code geoname_id } } source_address }
...
```

*Note: Output has been truncated for verbosity.*

The service object can be called as a context manager with `output` assigned with the new GraphQL
output fields.  The same object will be returned, but fields not defined will be assigned a `None`
value.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import SearchRequestInput

from pprint import pprint as pp

service = GraphQLService()
with service(output="search_id alerts { list { id status metadata { title severity confidence } } }")
    results = service.alerts.query.alerts_service_search(
        SearchRequestInput(
            offset=0,
            limit=10,
            cql_query="""
            FROM alert
            WHERE
                severity >= 0.6
            EARLIEST=-1d
            """,
        )
    )
pp(results)
```

### Cascading Context

The Python SDK service can handle a cascading context.  Each invocation of the `service` context manager, now overwrites the context per stack.  The main use case for this is to change the `output` of a single API call within a greater context without needing to exit the context entirely.  Any new level will temporarily overwrite any previous context definitions, the previous definitions will be available after exiting the current context.

**Note**: The following example is for illustration purposes of the context manager.  The mix of API calls may not be useful together.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.investigations2.types import InvestigationsV2Arguments
from taegis_sdk_python.services.alerts.types import SearchRequestInput

service = GraphQLService()

with service(environment="US2", tenant_id="00000"):
    
    # Context
    #    environment: US2
    #    tenant_id: 00000

    with service(output="investigations { id alertsEvidence { id } }")
        
        # Context
        #    environment: US2
        #    tenant_id: 00000
        #    output: investigations { id alertsEvidence { id } }
        
        investigation_results = service.investigations2.query.investigations_v2(InvestigationsV2Arguments(
            page=1,
            per_page=3,
            cql="WHERE deleted_at IS NOT NULL EARLIEST=-90d"
        ))
    
    # Context
    #    environment: US2
    #    tenant_id: 00000

    alert_ids = [
        alert.id
        result for result in investigation_results
        alert for alert in result.alerts_evidence
    ]

    with service(output="alerts { list { id metadata { title } status } }"):
        
        # Context
        #    environment: US2
        #    tenant_id: 00000
        #    output: alerts { list { id metadata { title } status } }
        
        alert_results = service.alerts.query.alerts_search_search(SearchRequestInput(
            offset=0,
            limit=10000,
            cql_query=f"FROM alert WHERE resource_id IN ('{'\',\''.join(alert_ids)]}')"
        ))
    
    # Context
    #    environment: US2
    #    tenant_id: 00000

    # may be useful for users/applications that have access to a parent/child tenant relationship
    with service(tenant_id="00001", output="alerts { list { id metadata { title } status } }"):
        
        # Context
        #    environment: US2
        #    tenant_id: 00001
        #    output: alerts { list { id metadata { title } status } }
        
        alert_results = service.alerts.query.alerts_search_search(SearchRequestInput(
            offset=0,
            limit=10000,
            cql_query=f"FROM alert WHERE resource_id IN ('{'\',\''.join(alert_ids)]}')"
        ))

        with service(environment="US1", output="email"):

            # Context
            #    environment: US1
            #    tenant_id: 00001
            #    output: email

            user = service.users.query.current_tdruser()

        # Context
        #    environment: US2
        #    tenant_id: 00001
        #    output: alerts { list { id metadata { title } status } }
    
    # Context
    #    environment: US2
    #    tenant_id: 00000

# Context is now completely cleared
```

## Arbitrary Queries

If you would like to run an API call that is different from the provided method or which the SDK
does not support, you can craft your own query/mutation/subscription.  Certain services may be
configured differently; it is recommended to use the service endpoint you want to query against
when available.

* `execute_query`
* `execute_mutation`
* `execute_subscription`

```python
from taegis_sdk_python import GraphQLService

from pprint import pprint as pp

service = GraphQLService()

results = service.alerts.execute_query(
    endpoint="alertsServiceSearch",
    variables={
        "in": {
            "limit": 3,
            "offset": 0,
            "cql_query": """
            FROM alert
            WHERE
                severity >= 0.6
            EARLIEST=-1d
            """
        }
    },
    output="""
        search_id
        alerts {
            list {
                id
                tenant_id
                metadata {
                    title
                    severity
                }
                status
            }
        }
    """
)
pp(results)
```

### Arbitrary Mutation

```python
results = service.core.execute_mutation(
    "createInvestigation",
    variables={
        "investigation": {
            "description": "SDK Test Investigation",
            "key_findings": "This is a test.",
            "priority": 1
        }
    },
    output="""
    id
    created_at
    created_by_user {
        id
        given_name
        family_name
    }
    description
    key_findings
    """
)
print(results)
```

## Raw Queries

You can also run your own raw GraphQL strings.  This provides the most flexibility
but least amount of guard rails.

* `execute`
* `subscribe`

```python
from taegis_sdk_python import GraphQLService

from pprint import pprint as pp

service = GraphQLService()

results = service.investigations.execute("""
    query investigationsStatusCount
    {
        investigationsStatusCount
        {
            open closed active awaiting_action suspended total
        }
    }
""")
pp(results)
```

## Helpers

### `build_output_string`

There is a utility called `build_output_string`.   This will return a string
representation of the output object with all possible fields for the return type.

```python
from taegis_sdk_python import build_output_string
from taegis_sdk_python.services.alerts.types import AlertsResponse

print(build_output_string(AlertsResponse))
```

### `_build_output_query`

If you want some assistance in building a complete GraphQL query string,
you can call the service endpoint `_build_output_query` to help.  This does build
the query from the schema, so ensure you are pulling the schema from the correct
service endpoint.

```python
from taegis_sdk_python import GraphQLService, build_output_string
from taegis_sdk_python.services.investigations.types import InvestigationStatusCountResponse

service = GraphQLService()
schema = service.alerts.get_sync_schema()

print(service.alerts._build_output_query(
    operation_type="query",
    endpoint="investigationsStatusCount",
    graphql_field=schema.query_type.fields.get("investigationsStatusCount"),
    output=build_output_string(InvestigationStatusCountResponse)
))
```

### Deprecation Warnings

Deprecated input fields, output fields and endpoints are set to log a warning.  For more information, see the [docs](docs/deprecation.md).

Example:

```
GraphQL Query `allInvestigations` is deprecated: 'replaced by investigationsSearch'
Output field `activity_logs` is deprecated: 'Not Supported - Use audit logs', removing from default output...
Output field `assignee` is deprecated: 'No longer supported', removing from default output...
```

### Schema Fetching

The Python SDK caches the schema for 5 minutes.  The fetched schema is used to help generate query strings and for error handling.  For applications that are time sensitive or have a large number of API calls, this funcationality will help amoratize the time needed to fetch the schema for validation and errors. This can be configured with the `schema_epiry` (in minutes) attribute on the `GraphQLService`.  The schema is fetched per service (alerts will cache a schema separate from investigations).  Expiration can be configured per service via context manager on the first API call to the service.

> **Note:** This may have an effect on error handling the longer the expiration time is.  If the server side schema updates with a breaking change between caching and an API call, the SDK may build and validate a query string that is inconsistent with the deployed schema.

```python
from taegis_sdk_python import GraphQLService

# all schemas will be cached for 15 minutes
service = GraphQLService(schema_expiry=15)

with service(schema_expiry=30): # users schema will now be cached for 30 minutes
    results = service.users.query.current_tdruser()
```

The schema may be cleared per service using the `service.<service>.clear_schema()` method.

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

user = service.users.query.current_tdruser() # schema will be cached for the users service

service.users.clear_schema()  # local schema will be cleared and re-fetched on next call
```
