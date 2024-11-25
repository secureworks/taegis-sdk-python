"""Tenants4 Query."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)
from taegis_sdk_python.services.tenants4.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.tenants4 import Tenants4Service

log = logging.getLogger(__name__)


class TaegisSDKTenants4Query:
    """Taegis Tenants4 Query operations."""

    def __init__(self, service: Tenants4Service):
        self.service = service

    def tenants(self, tenants_query: TenantsQuery) -> TenantResults:
        """Allows to query tenants using various filters, if running on a public endpoint, this results will be filtered to show only tenants that the subject has access to."""
        endpoint = "tenants"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "tenantsQuery": prepare_input(tenants_query),
            },
            output=build_output_string(TenantResults),
        )
        if result.get(endpoint) is not None:
            return TenantResults.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query tenants")

    def tenant(self, id_: str) -> TenantV4:
        """Retrieves a single tenant, tenant won't be returned if the subject does not have access to it (and requesting on an endpoint with authorization enabled)."""
        endpoint = "tenant"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(TenantV4),
        )
        if result.get(endpoint) is not None:
            return TenantV4.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query tenant")

    def available_regions(self) -> List[TenantRegion]:
        """Returns the regions where the tenant in XTC can be enabled at (excluding any regions currently enabled at), If a partner tenant id is provided in XTC, this returns the regions where the partner can enable children at. If more than one tenant is provided in XTC, then only the first one will be provided. If no XTC is provided, error will be returned."""
        endpoint = "availableRegions"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return [TenantRegion(r) for r in result.get(endpoint)]
        raise GraphQLNoRowsInResultSetError("for query availableRegions")