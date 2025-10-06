# Taegis SDK for Python

## Middlewares

The Taegis SDK uses AIOHTTP for a transport.  Middlewares can be injected for all HTTP calls.  Middleware will be wrapped around the initiating Websockets requests, but not the messages.

Middlewares may be assigned by default for API calls or overridden in the context manager.  Overriding middleswares will replace the entire middleware flow.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.middlewares import retry_middleware, headers_logging_middleware

# Assign defaults
service = GraphQLService(middlewares=(retry_middleware,))

# Override
with service(middlewares=(headers_logging_middleware, retry_middleware)):
     results = service.subjects.query.current_subject()
```

## Examples

The Taegis SDK for Python provides 2 example middlewares, `headers_logging_middleware` and `retry_middleware`.

`headers_logging_middleware` logs at the debug logging level the Request and Response headers.  Access Tokens cached by the SDK are replaced with a `<redacted>` string.

`retry_middleware` provides a retry on exponential backoff for REQUEST_TIMEOUT (408), INTERNAL_SERVER_ERROR (500), BAD_GATEWAY (502), SERVICE_UNAVAILABLE (503), GATEWAY_TIMEOUT (504).  If TOO_MANY_REQUESTS (429) is encounted, the value in the "Retry-After" header will be used as the backoff timer.

The SDK may be configured to provide a maximum amount of seconds or calls before giving up.  Defaults to 10 seconds with no call maximum.

```python
from taegis_sdk_python.config import write_to_config

write_to_config("backoff.retry", "max_time", 60)  # specifies the maximum amount of total time in seconds that can elapse before giving up
write_to_config("backoff.retry", "max_tries", 5)  # specifies the maximum number of calls to make to the target function before giving up
```

## References

* https://docs.aiohttp.org/en/stable/client_advanced.html#client-middleware
* https://docs.aiohttp.org/en/stable/client_middleware_cookbook.html#aiohttp-client-middleware-cookbook
