# Taegis XDR Python SDK

`taegis-sdk-python` is Secureworks Taegis XDR Python SDK. It provides an easy to use API that enables Python developers to configure and manage Taegis XDR.

## Prerequisites

- Python 3.8 or higher.
- Set `CLIENT_ID` and `CLIENT_SECRET` environment variables as described in the [Taegis XDR Documenation](https://docs.ctpx.secureworks.com/apis/api_authenticate/). Credentials used to create these variables MUST have `Admin Privileges`  otherwise you wont have enough permissions to  issue calls.


## Setup

1. Install git secrets `brew install gitleaks`
2. Install pre-commit `brew install pre-commit`  & `pre-commit install`
2. Check for secrets  `make secrets` or commit and the pre-commit hook will install
4. Open a terminal
5. Change to your favorite local directory (i.e. `cd /opt`)
6. Clone the repository

   ```bash
   git clone git@github.com:secureworks/tdr-sdk-python.git
   ```

7. Create a Virtual Environment

   ```bash
   python -m venv venv
   ```

8. Activate Virtual Environment

   ```bash
   source ./venv/bin/activate
   ```

9. Install the SDK

   ```bash
       pip install "/path/to/local/sdk"

   For example:

       pip install /opt/taegis-sdk-python
   ```


## Using the SDK

To use the SDK, you must first import the `GraphQLService`

```python
from taegis_sdk_python.services import GraphQLService

# Instantiate GraphQL Service
service = GraphQLService()
```

Now that you have the `GraphQLService`, you can make requests and process responses for `Taegis XDR Services`. The following example uses the `Investigations Service` to send a query to get all available investigations

```python

# Get all Investigations
raw_data, all_investigations = service.investigations.query.get_all_investigations(page=1, per_page=20)

# Print list of Investigations as a dictionary
for data in raw_data:
    print(str(data))

# Print list of Investigation dataclasses
for investigation in all_investigations:
    print(investigation)

```

## Custom Examples
### Custom Output

The SDK enables users to override the output property of a query to retrieve specific response fields. For example, the following code will **ONLY** return the ids of all Closed Investigations. This query runs inside the `Service Context`.

```python
from taegis_sdk_python.services import GraphQLService
from taegis_sdk_python.services.investigations.enums import InvestigationStatusEnum

service = GraphQLService()

# specify the output fields, and start the service context
with service.core(output="{ id }"):
    raw_data, all_investigations = service.investigations.query.get_all_investigations(
        status=InvestigationStatusEnum.closed(),
        page=1,
        per_page=20
    )

for inv in all_investigations:
    print(inv.id)
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
result = service.core.execute_gql_string(gql_query)
```

## Execution History

The `GraphQLService` supports an execution history log. This feature is currently **NOT** supported for `Custom Queries`.

 ```python
for history_item in service.core.history:
    print(history_item.as_json())
 ```
