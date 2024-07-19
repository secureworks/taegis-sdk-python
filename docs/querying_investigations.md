# Taegis SDK for Python

## Querying Investigations

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.investigations2.types import InvestigationsV2Arguments

page = 1
per_page = 30
cql = "WHERE deleted_at IS NULL EARLIEST=-30d | sort updated_at asc"

service = GraphQLService()

investigation_output = service.investigations2.query.investigations_v2(
    InvestigationsV2Arguments(
        page=page,
        per_page=per_page,
        cql=cql,
    )
)
investigation_output
```

## Pagination

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.investigations2.types import InvestigationsV2Arguments

page = 1
per_page = 30
cql = "WHERE deleted_at IS NULL EARLIEST=-30d | sort updated_at asc"

results = []

service = GraphQLService()

investigation_output = service.investigations2.query.investigations_v2(
    InvestigationsV2Arguments(
        page=page,
        per_page=per_page,
        cql=cql,
    )
)
results.append(investigation_output)

total_count = investigation_output.total_count

while (
    sum_total := sum(len(result.investigations) for result in results)
) < total_count:
    page += 1
    investigation_output = service.investigations2.query.investigations_v2(
        InvestigationsV2Arguments(
            page=page,
            per_page=per_page,
            cql=cql,
        )
    )
    results.append(investigation_output)

investigations = [
    investigation for result in results for investigation in result.investigations
]
```
