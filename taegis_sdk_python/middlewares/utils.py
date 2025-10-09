"""Taegis SDK Python Middlewares Utilities."""

from collections.abc import Mapping
from typing import List

from taegis_sdk_python.config import get_config


def get_access_tokens() -> List[str]:
    """Retrieve all cached access tokens."""
    config = get_config()

    tokens = []
    for section in config.sections():
        if token := config.get(section, "access_token", fallback=None):
            tokens.append(token)

    return tokens


def scrub_dict(d: Mapping):
    """Remove sensitive data from dictionary keys and values."""
    access_tokens = get_access_tokens()

    if "authorization" in d:
        token = d["Authorization"].replace("Bearer ", "")
        access_tokens.append(token)

    scrubbed = d.copy()
    for k, v in d.items():
        if isinstance(k, str):
            for token in access_tokens:
                k = k.replace(token, "<redacted>")
        if isinstance(v, str):
            for token in access_tokens:
                v = v.replace(token, "<redacted>")
        scrubbed[k] = v

    return scrubbed
