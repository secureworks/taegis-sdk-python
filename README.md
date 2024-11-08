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
    query="FROM process EARLIEST=-1d",
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

### Getting Started Exploring the Schema

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()
schema = service.core.get_sync_schema()
```

For more in depth analysis see: [Exploring the Schema](docs/exploring_the_schema.md)


###

For more information see the [Getting Started](docs/getting_started.md)
