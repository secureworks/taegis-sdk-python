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
from taegis_sdk_python.services import GraphQLService
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
from taegis_sdk_python.services import GraphQLService

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
from taegis_sdk_python.services import GraphQLService

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
from taegis_sdk_python.services import GraphQLService

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
from taegis_sdk_python.services import GraphQLService

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

### Arbitrary Query

```python
results = service.investigations.execute_query(
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
results = service.investigations.execute_mutation(
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

### Custom Query
Advanced users can leverage the power of the SDK to execute custom queries. If an invalid query is passed the system will respond with `GraphQLSyntaxError -> Syntax Error`, otherwise the query will be executed and results will be returned as a dictionary of data.

```python
from taegis_sdk_python.services import GraphQLService

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
result = service.investigations.execute(gql_query)
```

### Deprecation Warnings

Deprecated input fields, output fields and endpoints are set to log a warning.  For more information, see the [docs](docs/deprecation.md).

Example:

```
GraphQL Query `allInvestigations` is deprecated: 'replaced by investigationsSearch'
Output field `activity_logs` is deprecated: 'Not Supported - Use audit logs', removing from default output...
Output field `assignee` is deprecated: 'No longer supported', removing from default output...
```
