"""Taegis SDK Logging Middlewares."""

import logging

from aiohttp import ClientHandlerType, ClientRequest, ClientResponse

from taegis_sdk_python.middlewares.utils import scrub_dict

log = logging.getLogger(__name__)


async def headers_logging_middleware(
    req: ClientRequest, handler: ClientHandlerType
) -> ClientResponse:
    """Debug Log AIOHTTP Request and Response Headers.  Remove access tokens from headers and values.

    Parameters
    ----------
    req : ClientRequest
    handler : ClientHandlerType

    Returns
    -------
    ClientResponse
    """
    headers = scrub_dict(req.headers)
    log.debug(f"Request Headers: {headers}")
    resp = await handler(req)
    headers = scrub_dict(resp.headers)
    log.debug(f"Response Headers: {headers}")
    return resp
