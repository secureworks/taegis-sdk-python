"""Alerts Mutation."""
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
from taegis_sdk_python.services.alerts.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.alerts import AlertsService


class TaegisSDKAlertsMutation:
    """Teagis Alerts Mutation operations."""

    def __init__(self, service: AlertsService):
        self.service = service

    def alerts_service_update_investigation_info(
        self, in_: Optional[UpdateInvestigationRequestInput] = None
    ) -> UpdateInvestigationResponse:
        """None."""
        endpoint = "alertsServiceUpdateInvestigationInfo"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(UpdateInvestigationResponse),
        )
        if result.get(endpoint) is not None:
            return UpdateInvestigationResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation alertsServiceUpdateInvestigationInfo"
        )

    def alerts_service_update_resolution_info(
        self, in_: Optional[UpdateResolutionRequestInput] = None
    ) -> UpdateResolutionResponse:
        """Add a resolution or modify an existing resolution for a give list of alert IDs.."""
        endpoint = "alertsServiceUpdateResolutionInfo"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(UpdateResolutionResponse),
        )
        if result.get(endpoint) is not None:
            return UpdateResolutionResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation alertsServiceUpdateResolutionInfo"
        )

    def alerts_service_bulk_investigations_processor(
        self, in_: Optional[BulkInvestigationsRequestInput] = None
    ) -> BulkInvestigationsResponse:
        """Bulk add alerts to an existing investigation by providing either a query or list of alert IDs. If a query is provided, then all alerts matching the query will be added to the investigation.."""
        endpoint = "alertsServiceBulkInvestigationsProcessor"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(BulkInvestigationsResponse),
        )
        if result.get(endpoint) is not None:
            return BulkInvestigationsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation alertsServiceBulkInvestigationsProcessor"
        )

    def alerts_service_evict(
        self, in_: Optional[EvictRequestInput] = None
    ) -> EvictResponse:
        """DEPRECATED: Does not do anything other than to return OK. No replacement necessary.."""
        endpoint = "alertsServiceEvict"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(EvictResponse),
        )
        if result.get(endpoint) is not None:
            return EvictResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation alertsServiceEvict")
