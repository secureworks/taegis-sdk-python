# Taegis SDK for Python

## Proxy

The Taegis SDK supports proxies through the AIOHTTP client library for both query/mutation and subscriptions.

Relevant inputs:

* `trust_env`
* `proxy`
* `proxy_auth`
* `proxy_headers`
* `ssl`

`trust_env` may be passed into the constructor or the context manager to pull the proxy configuration from the environment.  This is handled by the [AIOHTTP transport](https://docs.aiohttp.org/en/stable/client_advanced.html#proxy-support).  Authentication can be passed via environment variables `HTTP_PROXY`, `HTTPS_PROXY`, `WS_PROXY` and `WSS_PROXY`.  NetRC may also be used to provide authentication.  `trust_env` and the proxy parameters are mutually exclusive, the proxy, proxy_auth and proxy_headers parameters will take precedence when both are provided, or passed to the service context.

```bash
export HTTPS_PROXY=http://$USERNAME:$PASSWORD@your.proxy.domain:port
```

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService(trust_env=True)

results = service.subjects.query.current_subject()
print(results)
```

or 

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()

with service(trust_env=True):
    results = service.subjects.query.current_subject()
print(results)
```

Proxy settings may also be passed directly into the constructor or service manager.

```python
from taegis_sdk_python import GraphQLService
from aiohttp import BasicAuth

service = GraphQLService(
    proxy="http://your.proxy.domain:port",
    proxy_auth=BasicAuth("<username>", "<password>")
)

results = service.subjects.query.current_subject()
print(results)
```

or

```python
from taegis_sdk_python import GraphQLService
from aiohttp import BasicAuth

service = GraphQLService()

with service(
    proxy="http://your.proxy.domain:port", proxy_auth=BasicAuth("<username>", "<password>")
):
    results = service.subjects.query.current_subject()
print(results)
```

SSL settings may also be passed via the SSLContext:

https://docs.aiohttp.org/en/stable/client_advanced.html#ssl-control-for-tcp-sockets



## References

* https://docs.aiohttp.org/en/stable/client_advanced.html#proxy-support
* https://docs.python.org/3/library/urllib.request.html#urllib.request.getproxies
