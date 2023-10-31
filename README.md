# Taegis SDK for Python

The Taegis SDK is a Python library for interfacing with the GraphQL APIs in Taegis.

## Prerequisites

- Python 3.8 or higher.

## Authentication

- Set `CLIENT_ID` and `CLIENT_SECRET` environment variables as described in the [Taegis XDR Documenation](https://docs.ctpx.secureworks.com/apis/api_authenticate/).

OR

- Login using username/password with mfa upon service creation

OR

- Device Code SSO


## Installation

```bash
python -m pip install taegis-sdk-python
```


## Using the SDK

To use the SDK, you must first import the `GraphQLService`


```python
from taegis_sdk_python import GraphQLService
from pprint import pprint as pp
service = GraphQLService()
```

Now that you have the `GraphQLService`, you can make requests and process responses for `Taegis XDR Services`. The following example uses the `Investigations Service` to send a query to get all available investigations

```python
result = service.investigations.query.investigations_search(
    page=1,
    per_page=3,
    query="WHERE deleted_at IS NOT NULL EARLIEST=-90d"
)
pp(result)
```

```python
result = service.tenants.query.tenants(tenants_query=TenantsQuery(
    max_results=10,
    page_num=1,
))
pp(result)
```

```python
results = service.events.subscription.event_query(
    query="FROM process EARLIEST=-30d",
    options=EventQueryOptions(
        max_rows=20,
        page_size=10,
        skip_cache=True,
    ),
)
pp(results)
print()
try:
    next_page = next(
        iter(
            {
                result.next
                for result in results
                if result.next
            }
        )
    )
except StopIteration:
    next_page = None

if next_page:
    results = service.events.subscription.event_page(page_id=next_page)
    pp(results)
```

## Custom Examples

### Custom Output

The SDK enables users to override the output property of a query to retrieve specific response fields. For example, the following code will **ONLY** return the ids, description and status of all Closed Investigations. This query runs inside the `Service Context`.

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

# specify the output fields, and start the service context
with service(output="investigations { id description status } totalCount"):
    result = service.investigations.query.investigations_search(
        page=1,
        per_page=3,
        query="WHERE deleted_at IS NOT NULL EARLIEST=-90d"
    )
pp(result)
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
with service(environment="delta"):
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

### Cascading Context

The Python SDK service can handle a cascading context.  Each invocation of the `service` context manager, now overwrites the context per stack.  The main use case for this is to change the `output` of a single API call within a greater context without needing to exit the context entirely.  Any new level will temporarily overwrite any previous context definitions, the previous definitions will be available after exiting the current context.

**Note**: The following example is for illustration purposes of the context manager.  The mix of API calls may not be useful together.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.investigations2.types import InvestigationsV2Arguments
from taegis_sdk_python.services.alerts.types import SearchRequestInput

service = GraphQLService()

with service(environment="delta", tenant_id="00000"):
    
    # Context
    #    environment: delta
    #    tenant_id: 00000

    with service(output="investigations { id alertsEvidence { id } }")
        
        # Context
        #    environment: delta
        #    tenant_id: 00000
        #    output: investigations { id alertsEvidence { id } }
        
        investigation_results = service.investigations2.query.investigations_v2(InvestigationsV2Arguments(
            page=1,
            per_page=3,
            cql="WHERE deleted_at IS NOT NULL EARLIEST=-90d"
        ))
    
    # Context
    #    environment: delta
    #    tenant_id: 00000

    alert_ids = [
        alert.id
        result for result in investigation_results
        alert for alert in result.alerts_evidence
    ]

    with service(output="alerts { list { id metadata { title } status } }"):
        
        # Context
        #    environment: delta
        #    tenant_id: 00000
        #    output: alerts { list { id metadata { title } status } }
        
        alert_results = service.alerts.query.alerts_search_search(SearchRequestInput(
            offset=0,
            limit=10000,
            cql_query=f"FROM alert WHERE resource_id IN ('{'\',\''.join(alert_ids)]}')"
        ))
    
    # Context
    #    environment: delta
    #    tenant_id: 00000

    # may be useful for users/applications that have access to a parent/child tenant relationship
    with service(tenant_id="00001", output="alerts { list { id metadata { title } status } }"):
        
        # Context
        #    environment: delta
        #    tenant_id: 00001
        #    output: alerts { list { id metadata { title } status } }
        
        alert_results = service.alerts.query.alerts_search_search(SearchRequestInput(
            offset=0,
            limit=10000,
            cql_query=f"FROM alert WHERE resource_id IN ('{'\',\''.join(alert_ids)]}')"
        ))

        with service(environment="charlie", output="email"):

            # Context
            #    environment: charlie
            #    tenant_id: 00001
            #    output: email

            user = service.users.query.current_tdruser()

        # Context
        #    environment: delta
        #    tenant_id: 00001
        #    output: alerts { list { id metadata { title } status } }
    
    # Context
    #    environment: delta
    #    tenant_id: 00000

# Context is now completely cleared
```

### Arbitrary Query

The Python SDK can handle user maintained queries/mutations/subscriptions.  These will require some basic GraphQL knowledge as well as knowledge of schema.  There are 3 parts of a GraphQL query: the endpoint, the output fields and the variables (optional).  See [Exploring the Schema](docs/exploring_the_schema.md) for more information.

```python
results = service.core.execute_query(
    "alertsServiceSearch",
    variables={
        "in": {
            "limit": 3,
            "offset": 0,
            "cql_query": "FROM alert EARLIEST=-1d"
        }
    },
    output="""
        search_id
        alerts {
            list {
                id
                metadata {
                    title
                }
                status
            }
        }
    """
)
print(results)
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

### Getting Started Exploring the Schema

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()
schema = service.core.get_sync_schema()
```

For more in depth analysis see: [Exploring the Schema](docs/exploring_the_schema.md)

### Custom Query
Advanced users can leverage the power of the SDK to execute custom queries. If an invalid query is passed the system will respond with `GraphQLSyntaxError -> Syntax Error`, otherwise the query will be executed and results will be returned as a dictionary of data.

```python
from taegis_sdk_python import GraphQLService

gql_query = """
    query investigationsStatusCount {
        investigationsStatusCount {
            open
            closed
            active
            awaiting_action
            suspended
            total
        }
    }
"""
result = service.core.execute(gql_query)
```

### Deprecation Warnings

Deprecated input fields, output fields and endpoints are set to log a warning.  For more information, see the [docs](docs/deprecation.md).

Example:

```
GraphQL Query `allInvestigations` is deprecated: 'replaced by investigationsSearch'
Output field `activity_logs` is deprecated: 'Not Supported - Use audit logs', removing from default output...
Output field `assignee` is deprecated: 'No longer supported', removing from default output...
```
