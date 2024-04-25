"""ContractedEndpoint Query."""
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
from taegis_sdk_python.services.contracted_endpoint.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.contracted_endpoint import ContractedEndpointService

log = logging.getLogger(__name__)


class TaegisSDKContractedEndpointQuery:
    """Taegis Contracted_endpoint Query operations."""

    def __init__(self, service: ContractedEndpointService):
        self.service = service

    def endpoint_count_for_tenant_id(
        self, service_date: Optional[str] = None
    ) -> ContractedEndpoints:
        """None."""
        endpoint = "endpointCountForTenantID"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "serviceDate": prepare_input(service_date),
            },
            output=build_output_string(ContractedEndpoints),
        )
        if result.get(endpoint) is not None:
            return ContractedEndpoints.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query endpointCountForTenantID")

    def project_ir_hours_for_tenant_id(self) -> float:
        """None."""
        endpoint = "projectIRHoursForTenantID"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query projectIRHoursForTenantID")

    def get_historical_endpoint_count_for_tenant_id(
        self, start_date: str, end_date: str
    ) -> List[EndpointHistory]:
        """None."""
        endpoint = "getHistoricalEndpointCountForTenantID"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "startDate": prepare_input(start_date),
                "endDate": prepare_input(end_date),
            },
            output=build_output_string(EndpointHistory),
        )
        if result.get(endpoint) is not None:
            return EndpointHistory.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError(
            "for query getHistoricalEndpointCountForTenantID"
        )