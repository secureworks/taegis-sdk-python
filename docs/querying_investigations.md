# Taegis SDK for Python

## Querying Investigations

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

results = service.investigations.query.investigations_search(
    page=1,
    per_page=500,
    query="WHERE deleted_at IS NULL EARLIEST=-30d",
    filter_text=None,
    order_by_field="updated_at",
    order_direction="asc",
)
```

## Pagination

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

investigations = []
page = 1
per_page = 500

results = service.investigations.query.investigations_search(
    page=page,
    per_page=per_page,
    query="WHERE deleted_at IS NULL EARLIEST=-365d",
    filter_text=None,
    order_by_field="updated_at",
    order_direction="asc",
)
investigations.extend(results.investigations)

while len(results.investigations) == per_page:
    page += 1

    results = service.investigations.query.investigations_search(
        page=page,
        per_page=per_page,
        query="WHERE deleted_at IS NULL EARLIEST=-365d",
        filter_text=None,
        order_by_field="updated_at",
        order_direction="asc",
    )
    investigations.extend(results.investigations)
```
