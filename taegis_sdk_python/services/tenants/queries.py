"""Tenants Query."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import (
    build_output_string,
    prepare_input,
    parse_union_result,
)
from taegis_sdk_python.services.tenants.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.tenants import TenantsService


class TaegisSDKTenantsQuery:
    """Teagis Tenants Query operations."""

    def __init__(self, service: TenantsService):
        self.service = service

    def assignable_services(
        self, service_ids: List[str], tenant_id: Optional[str] = None
    ) -> List[Service]:
        """Returns the assignable Services for the optional tenant, or assignable Services for all accessible tenants if a tenant is not specified.  Only Secureworks and Partners may manage Services, for other tenants this will return an empty list."""
        endpoint = "assignableServices"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "tenantID": prepare_input(tenant_id),
                "serviceIDs": prepare_input(service_ids),
            },
            output=build_output_string(Service),
        )
        if result.get(endpoint) is not None:
            return Service.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query assignableServices")

    def tenants(self, tenants_query: TenantsQuery) -> TenantResults:
        """Queries all tenants, can also be used to return a few or only one tenant if ids are known."""
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

    def get_sso_connection(self, id_: str) -> SSOConnection:
        """Retrieves the SSO connection specified by the ID. The ID can be either the local ID or the external ID."""
        endpoint = "getSSOConnection"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(SSOConnection),
        )
        if result.get(endpoint) is not None:
            return SSOConnection.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getSSOConnection")

    def sso_connections(
        self, connection_query: TenantSSOConnectionQueryInput
    ) -> List[SSOConnection]:
        """Retrieves the sso connections for the tenant in context."""
        endpoint = "SSOConnections"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "connectionQuery": prepare_input(connection_query),
            },
            output=build_output_string(SSOConnection),
        )
        if result.get(endpoint) is not None:
            return SSOConnection.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query SSOConnections")

    def get_sso_connection_config(
        self, metadata_url: Optional[str] = None, cert: Optional[str] = None
    ) -> SSOConnectionConfigResponse:
        """Downloads configuration for an SSO connection if metadataURL is provided, or the certificate attributes if that is provided. Currently applicable only to SAML connections."""
        endpoint = "getSSOConnectionConfig"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "metadataURL": prepare_input(metadata_url),
                "cert": prepare_input(cert),
            },
            output=build_output_string(SSOConnectionConfigResponse),
        )
        if result.get(endpoint) is not None:
            return SSOConnectionConfigResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getSSOConnectionConfig")

    def audits(self, audits_query: TenantAuditsQuery) -> AuditResults:
        """Audits query, search is constrained to tenants that the user has access to."""
        endpoint = "audits"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "auditsQuery": prepare_input(audits_query),
            },
            output=build_output_string(AuditResults),
        )
        if result.get(endpoint) is not None:
            return AuditResults.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query audits")

    def service_events(self, events_query: ServiceEventQuery) -> List[ServiceEvents]:
        """Returns a list of service events for the given query."""
        endpoint = "serviceEvents"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "eventsQuery": prepare_input(events_query),
            },
            output=build_output_string(ServiceEvents),
        )
        if result.get(endpoint) is not None:
            return ServiceEvents.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query serviceEvents")
