# Taegis SDK for Python

## Deprecation Warnings

The Taegis SDK for Python now supports warnings for deprecated items within the Taegis APIs.  These warnings are meant to inform users and developers of upcoming changes to the APIs and provide enough time to migrate to supported features.  Deprecated fields and endpoints are subject to change at any time.

Types of Deprecation Warnings:

* Input field warnings
    * these are warnings on input fields that are submitted to APIs
* Output field warnings
    * these are warning on return fields that come from APIs
* Endpoint warnings
    * these are warnings when an entire API endpoint has been deprecated

## Deprecated Input Fields

The SDK does not modify or change deprecated input fields, although they are subject to removal at any time.

Logging for these warning may be turned off by:

```python
import logging

logging.getLogger("taegis_sdk_python.utils").setLevel(logging.ERROR)
```

## Deprecated Output Fields

The SDK removes deprecated output fields from the generated fields.  If deprecated fields are still needed, they be included by changing the [output](https://github.com/secureworks/taegis-sdk-python#custom-output) field within the GraphQLService context manager.  Logging for the deprecated fields will still be available.

Example:

```python
from taegis_sdk_python import GraphQLService
import logging

service = GraphQLService()
results = service.investigations.query.all_investigations(
    page=1,
    per_page=3,
)
print(results[0].assignee)
```

```
GraphQL Query `allInvestigations` is deprecated: 'replaced by investigationsSearch'
Output field `activity_logs` is deprecated: 'Not Supported - Use audit logs', removing from default output...
Output field `assignee` is deprecated: 'No longer supported', removing from default output...
None
```

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

with service(output='id tenant_id ... assignee { id name ... }'):
    results = service.investigations.query.all_investigations(
        page=1,
        per_page=3,
    )
print(results[0].assignee)
```

> **Note:** `output` has been truncated for readability.

```
...
Output field `assignee` is deprecated: 'No longer supported', removing from default output...
Assignee(id='<id>', name='<name>', roles=None, status=None, user_id=None, email=None, email_verified=None, email_normalized=None, family_name=None, given_name=None, tenants=None)
```

Logging for these warning may be turned off by:

```python
import logging

logging.getLogger("taegis_sdk_python.utils").setLevel(logging.ERROR)
```

## Deprecated Endpoints

The SDK does not modify or change deprecated endpoints, although they are subject to removal at any time.

Logging for these warning may be turned off by:

All endpoint warnings:

```python
import logging

logging.getLogger("taegis_sdk_python.services").setLevel(logging.ERROR)
```

Specific service warnings:

```python
import logging

# logging.getLogger("taegis_sdk_python.services.<service>").setLevel(logging.ERROR)

logging.getLogger("taegis_sdk_python.services.investigations").setLevel(logging.ERROR)
```

Specific service type warnings:


```python
import logging

# logging.getLogger("taegis_sdk_python.services.<service>.<type>").setLevel(logging.ERROR)

logging.getLogger("taegis_sdk_python.services.investigations.queries").setLevel(logging.ERROR)
```

## Additional Resources

Additional options how to handle logging can be found in the [Python documentation](https://docs.python.org/3.9/howto/logging.html).
