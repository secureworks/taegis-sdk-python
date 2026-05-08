"""Logs a curl command representation that makes the same HTTP request as the provided request"""

import logging
from shlex import quote

from aiohttp import (
    BytesPayload,
    ClientHandlerType,
    ClientRequest,
    ClientResponse,
)

from taegis_sdk_python.middlewares.utils import scrub_dict

log = logging.getLogger(__name__)


async def to_curl(request: ClientRequest, handler: ClientHandlerType) -> ClientResponse:
    """
    Logs a curl command representation that makes the same HTTP request as
    the provided request object.
    """
    command = []

    inferred_method = "GET"
    if request.body is not None:
        inferred_method = "POST"
    if request.method != inferred_method:
        command.append("-X " + quote(request.method))

    headers = scrub_dict(request.headers)

    for k, v in headers.items():
        if v:
            command.append("-H " + quote(f"{k}: {v}"))
        else:
            # -H 'Accept:' disables sending the Accept header, use semicolon to send
            # empty header
            command.append("-H " + quote(f"{k};"))

    if body := request.body:
        if isinstance(body, (bytes, BytesPayload)):
            body = body.decode("utf-8")
        else:
            log.error(f"Unsupported body type for curl middleware: {type(body)}, request.body must be bytes or BytesPayload")
            return await handler(request)

        data_type = "-d"
        if body.startswith("@"):  # -d @filename causes curl to read from file
            data_type = "--data-raw"
        command.append(data_type + " " + quote(body))

    command.append(quote(str(request.url)))

    joiner = " "
    if len(command) > 3:
        joiner = " \\\n  "
    log.info(f"curl {joiner.join(command)}")

    return await handler(request)
