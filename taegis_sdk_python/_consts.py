"""Taegis Constants."""

from enum import Enum

TAEGIS_ENVIRONMENT_URLS = {
    "charlie": "https://api.ctpx.secureworks.com",
    "production": "https://api.ctpx.secureworks.com",
    "US1": "https://api.ctpx.secureworks.com",
    "delta": "https://api.delta.taegis.secureworks.com",
    "US2": "https://api.delta.taegis.secureworks.com",
    "echo": "https://api.echo.taegis.secureworks.com",
    "EU": "https://api.echo.taegis.secureworks.com",
    "foxtrot": "https://api.foxtrot.taegis.secureworks.com",
    "US3": "https://api.foxtrot.taegis.secureworks.com",
}


TAEGIS_TENANTS_URLS = {
    "charlie": "https://api.tenants.ctpx.secureworks.com",
    "production": "https://api.tenants.ctpx.secureworks.com",
    "US1": "https://api.tenants.ctpx.secureworks.com",
    "delta": "https://api-tenants.delta.taegis.secureworks.com",
    "US2": "https://api-tenants.delta.taegis.secureworks.com",
    "echo": "https://api-tenants.echo.taegis.secureworks.com",
    "EU": "https://api-tenants.echo.taegis.secureworks.com",
    "foxtrot": "https://api-tenants.foxtrot.taegis.secureworks.com",
    "US3": "https://api-tenants.foxtrot.taegis.secureworks.com",
}


class TaegisEnum(str, Enum):
    """Handler for Unknown Enums."""

    UNKNOWN = "TAEGIS_SDK_PYTHON_UNKNOWN"
