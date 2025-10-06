"""Taegis SDK Retry Middlewares."""

from http import HTTPStatus
from typing import Optional

import backoff
from aiohttp import ClientHandlerType, ClientRequest, ClientResponse

from taegis_sdk_python.config import get_config

SECTION = "backoff.retry"


def config_max_time() -> Optional[int]:
    """Provide Max Time elapsed for retry.

    Returns
    -------
    int
        Seconds.
    """
    config = get_config()

    return config.getint(SECTION, "max_time", fallback=10)


def config_max_tries() -> Optional[int]:
    """Provide Max Tries for retry.

    Returns
    -------
    Optional[int]
        Max tries.
    """
    config = get_config()

    return config.getint(SECTION, "max_tries", fallback=None)


@backoff.on_predicate(
    backoff.runtime,
    predicate=lambda r: r.status == HTTPStatus.TOO_MANY_REQUESTS,
    value=lambda r: int(r.headers.get("Retry-After")),
    max_time=config_max_time,
    max_tries=config_max_tries,
)
@backoff.on_predicate(
    backoff.expo,
    lambda r: r.status
    in (
        HTTPStatus.REQUEST_TIMEOUT,
        HTTPStatus.INTERNAL_SERVER_ERROR,
        HTTPStatus.BAD_GATEWAY,
        HTTPStatus.SERVICE_UNAVAILABLE,
        HTTPStatus.GATEWAY_TIMEOUT,
    ),
    max_time=config_max_time,
    max_tries=config_max_tries,
)
async def retry_middleware(
    req: ClientRequest, handler: ClientHandlerType
) -> ClientResponse:
    """Retry HTTP requests middleware.

    Retry on exponential backoff for REQUEST_TIMEOUT (408), INTERNAL_SERVER_ERROR (500),
    BAD_GATEWAY (502), SERVICE_UNAVAILABLE (503), GATEWAY_TIMEOUT (504).

    If TOO_MANY_REQUESTS (429) is encounted, the value in the "Retry-After" header
    will be used as the backoff timer.

    Parameters
    ----------
    req : ClientRequest
    handler : ClientHandlerType

    Returns
    -------
    ClientResponse
    """
    return await handler(req)
