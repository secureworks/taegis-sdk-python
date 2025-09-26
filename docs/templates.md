# Taegis SDK for Python

## Templates

Taegis SDK has support for Jinja2 templates.  Templates are helpful for abstracting complex queries within Taegis and standardizing list of values generation.  By default, templates will be relative to the Python script.  Template loaders are configurable per Jinja2 documentation.

https://jinja.palletsprojects.com/en/stable/templates/

## Taegis QL Filters

Templates loaded from the Taegis SDK for Python will come with the following Jinja2 filters for assistance in writing Taegis QL queries for Advanced Search:

https://docs.taegis.secureworks.com/search/querylanguage/advanced_search/

```
{{ list | or(field_name, operator='=') }}
```

```
{{ list | and(field_name, operator='=') }}
```

```
{{ list | in(field_name) }}
```

```
{{ list | not_in(field_name) }}
```

```
{{ list | regex(field_name, separator='|') }}
```

```
{{ list | matches_regex(field_name, separator='|') }}
```

```
{{ list | not_regex(field_name, separator='|') }}
```

```
{{ list | not_matches_regex(field_name, separator='|') }}
```

### Example

example.jinja
```
FROM alert 
WHERE
    ( 
        {{ ips | in('@ip') }}  OR
        {{ domains | regex('@domain') }}
    ) AND
    severity >= {{ severity }}
EARLIEST={{ earliest }}
```

example output
```
FROM alert 
WHERE
    ( 
        @ip IN ('1.1.1.1','8.8.8.8') OR
        @domain MATCHES_REGEX 'secureworks\.com|sophos\.com'
    ) AND
    severity >= 0.6
EARLIEST=-1d
```

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.templates import load_jinja2_template_environment

service = GraphQLService()

environment = load_jinja2_template_environment()
template = environment.get_template('example.jinja')

ips = ['1.1.1.1', '8.8.8.8']
domains = ['secureworks.com', 'sophos.com']
severity = 0.6
earliest = '-1d'

cql_query = template.render(
    ips=ips,
    domains=domains,
    severity=severity,
    earliest=earliest,
)

results = service.alerts.query.alerts_service_search(SearchRequestInput(
    cql_query=cql_query,
    limit=10000,
    offset=0,
))

print(results)
```
