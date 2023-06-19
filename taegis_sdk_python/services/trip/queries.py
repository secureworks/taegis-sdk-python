"""Trip Query."""
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
from taegis_sdk_python.services.trip.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.trip import TripService

log = logging.getLogger(__name__)


class TaegisSDKTripQuery:
    """Teagis Trip Query operations."""

    def __init__(self, service: TripService):
        self.service = service

    def list_active_api_products(
        self, application: ApiProductGroup
    ) -> List[ApiProduct]:
        """None."""
        endpoint = "listActiveApiProducts"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "application": prepare_input(application),
            },
            output=build_output_string(ApiProduct),
        )
        if result.get(endpoint) is not None:
            return ApiProduct.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query listActiveApiProducts")

    def list_api_integrations(self) -> List[ApiIntegrationSummary]:
        """None."""
        endpoint = "listApiIntegrations"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(ApiIntegrationSummary),
        )
        if result.get(endpoint) is not None:
            return ApiIntegrationSummary.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query listApiIntegrations")

    def api_integration(self, id_: int) -> ApiIntegration:
        """None."""
        endpoint = "apiIntegration"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(ApiIntegration),
        )
        if result.get(endpoint) is not None:
            return ApiIntegration.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query apiIntegration")

    def list_api_integration_history(
        self, id_: int, start_time: str, end_time: str
    ) -> List[ApiIntegrationHistory]:
        """None."""
        endpoint = "listApiIntegrationHistory"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "startTime": prepare_input(start_time),
                "endTime": prepare_input(end_time),
            },
            output=build_output_string(ApiIntegrationHistory),
        )
        if result.get(endpoint) is not None:
            return ApiIntegrationHistory.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query listApiIntegrationHistory")

    def get_api_integration_form(self, product_id: int) -> ApiForm:
        """None."""
        endpoint = "getApiIntegrationForm"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "productId": prepare_input(product_id),
            },
            output=build_output_string(ApiForm),
        )
        if result.get(endpoint) is not None:
            return ApiForm.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getApiIntegrationForm")
