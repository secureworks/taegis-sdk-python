"""Taegis Constants."""

from enum import Enum

from multidict import CIMultiDict

TAEGIS_ENVIRONMENT_URLS = CIMultiDict(
    charlie="https://api.ctpx.secureworks.com",
    production="https://api.ctpx.secureworks.com",
    us1="https://api.ctpx.secureworks.com",
    delta="https://api.delta.taegis.secureworks.com",
    us2="https://api.delta.taegis.secureworks.com",
    echo="https://api.echo.taegis.secureworks.com",
    eu="https://api.echo.taegis.secureworks.com",
    foxtrot="https://api.foxtrot.taegis.secureworks.com",
    us3="https://api.foxtrot.taegis.secureworks.com",
    golf="https://api.golf.taegis.secureworks.com",
    euw1="https://api.golf.taegis.secureworks.com",
    hotel="https://api.hotel.taegis.secureworks.com",
    apse2="https://api.hotel.taegis.secureworks.com",
    india="https://api.india.taegis.secureworks.com",
    aps1="https://api.india.taegis.secureworks.com",
    juliet="https://api.juliet.taegis.secureworks.com",
    apne1="https://api.juliet.taegis.secureworks.com",
    kilo="https://api.kilo.taegis.secureworks.com",
    sae1="https://api.kilo.taegis.secureworks.com",
    quebec="https://api.quebec.taegis.secureworks.com",
    cac1="https://api.quebec.taegis.secureworks.com",
)


TAEGIS_TENANTS_URLS = CIMultiDict(
    charlie="https://api.tenants.ctpx.secureworks.com",
    production="https://api.tenants.ctpx.secureworks.com",
    us1="https://api.tenants.ctpx.secureworks.com",
    delta="https://api-tenants.delta.taegis.secureworks.com",
    us2="https://api-tenants.delta.taegis.secureworks.com",
    echo="https://api-tenants.echo.taegis.secureworks.com",
    eu="https://api-tenants.echo.taegis.secureworks.com",
    foxtrot="https://api-tenants.foxtrot.taegis.secureworks.com",
    us3="https://api-tenants.foxtrot.taegis.secureworks.com",
    golf="https://api-tenants.golf.taegis.secureworks.com",
    euw1="https://api-tenants.golf.taegis.secureworks.com",
    hotel="https://api-tenants.hotel.taegis.secureworks.com",
    apse2="https://api-tenants.hotel.taegis.secureworks.com",
    india="https://api-tenants.india.taegis.secureworks.com",
    aps1="https://api-tenants.india.taegis.secureworks.com",
    juliet="https://api-tenants.juliet.taegis.secureworks.com",
    apne1="https://api-tenants.juliet.taegis.secureworks.com",
    kilo="https://api-tenants.kilo.taegis.secureworks.com",
    sae1="https://api-tenants.kilo.taegis.secureworks.com",
    quebec="https://api-tenants.quebec.taegis.secureworks.com",
    cac1="https://api-tenants.quebec.taegis.secureworks.com",
)


UNIVERSAL_ENVIRONMENT = "universal"
UNIVERSAL_AUTHENTICATION_URL = "https://api.taegis.secureworks.com"

DEFAULT_GATEWAY = "/graphql"


class TaegisEnum(str, Enum):
    """Handler for Unknown Enums."""

    UNKNOWN = "TAEGIS_SDK_PYTHON_UNKNOWN"
