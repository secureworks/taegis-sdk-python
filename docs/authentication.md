# Taegis SDK for Python

## Authentication

Authentication flow for the Taegis SDK for Python:

`Cached Token -> Authenticate via OAuth -> Authenticate via SSO or Username/Password/MFA`

Tokens will be cached in the `~/.taegis_sdk_python/config` file.  Please ensure that this path is writable by your script.

### OAuth

By default, OAuth tokens will be utilized from environment variables
CLIENT_ID and CLIENT_SECRET.

Generate a CLIENT_ID and CLIENT_SECRET:

```python
from taegis_sdk_python import GraphQLService
from pprint import pprint as pp
service = GraphQLService(environment="charlie")
result = service.clients.mutation.create_client(name="my_awesome_app", roles=None)
print(f"CLIENT_ID: {result.client.client_id}")
print(f"CLIENT_SECRET: {result.client_secret}")
pp(result)
```
* IMPORTANT! : *store these results in an encrypted vault*

Replace <client_id> and <client_secret> with your values from above:

```bash
CLIENT_ID=<client_id> CLIENT_SECRET=<client_secret> python script.py
```

#### Customizing environment variables

You can use `write_to_config` to set custom environment variable names for your application.  This is useful if you are automating and you need to access different environments from the same script.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.config import write_to_config

# write_to_config(environment, default_reference, custom_reference)
# these are not template strings, but environment reference names
# see next cell for usage example
write_to_config("charlie", "CLIENT_ID", "CHARLIE_CLIENT_ID")
write_to_config("charlie", "CLIENT_SECRET", "CHARLIE_CLIENT_SECRET")

service = GraphQLService()
```

```bash
CHARLIE_CLIENT_ID=<client_id> CHARLIE_CLIENT_SECRET=<client_secret> python script.py
```

### Username

If you don't provide OAuth tokens in the environment, you will be prompted for a username.  If your organization has enabled single sign-on, then you will prompted with a link.  Otherwise you will be asked for a password and MFA token.

### Clearing authorization tokens

If you would like to manually clear the authentication tokens:

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

service.clear_access_token()
```
