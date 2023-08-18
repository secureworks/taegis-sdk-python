# Taegis SDK for Python

## Logging Examples

### Turn on debug logging for everything

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Turn on debug logging for just the Taegis SDK for Python

```python
import logging
logging.getLogger('taegis_sdk_python').setLevel(level=logging.DEBUG)
```

### Turn on debug logging for a specific service just the Taegis SDK for Python

```python
import logging
logging.getLogger('taegis_sdk_python.services.alerts').setLevel(level=logging.DEBUG)
```

Replace `alerts` with the service you want to debug.
