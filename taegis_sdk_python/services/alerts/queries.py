"""Alerts Query."""

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
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.alerts.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.alerts import AlertsService

log = logging.getLogger(__name__)


class TaegisSDKAlertsQuery:
    """Taegis Alerts Query operations."""

    def __init__(self, service: AlertsService):
        self.service = service

    def alerts_service_retrieve_alerts_by_id(
        self, in_: Optional[GetByIDRequestInput] = None
    ) -> AlertsResponse:
        """Provide a list of Alert IDs to retrieve each alert&#8217;s detail.."""
        endpoint = "alertsServiceRetrieveAlertsById"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AlertsResponse),
        )
        if result.get(endpoint) is not None:
            return AlertsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query alertsServiceRetrieveAlertsById")

    def alerts_service_retrieve_alerts_by_host(
        self, in_: Optional[GetByIDRequestInput] = None
    ) -> AlertsResponse:
        """Provide a list of Host IDs to retrieve alert details about each alert that contains those hosts.."""
        endpoint = "alertsServiceRetrieveAlertsByHost"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AlertsResponse),
        )
        if result.get(endpoint) is not None:
            return AlertsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for query alertsServiceRetrieveAlertsByHost"
        )

    def alerts_service_retrieve_alerts_by_entity(
        self, in_: Optional[GetByIDRequestInput] = None
    ) -> AlertsResponse:
        """Provide a list of entities to retrieve alert details about each alert that contains those entities.."""
        endpoint = "alertsServiceRetrieveAlertsByEntity"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AlertsResponse),
        )
        if result.get(endpoint) is not None:
            return AlertsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for query alertsServiceRetrieveAlertsByEntity"
        )

    def alerts_service_retrieve_alerts_by_group_key(
        self, in_: Optional[GetByIDRequestInput] = None
    ) -> AlertsResponse:
        """Provide a list of entities to retrieve alert details about each alert that contains the group_key. This is used by the service to aid in alert deduplication. This would not commonly be used by a tenant of XDR.."""
        endpoint = "alertsServiceRetrieveAlertsByGroupKey"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AlertsResponse),
        )
        if result.get(endpoint) is not None:
            return AlertsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for query alertsServiceRetrieveAlertsByGroupKey"
        )

    def alerts_count_by_tenant(
        self, in_: AlertsCountByTenantInput
    ) -> AlertsCountByTenantResponse:
        """Returns the count of alerts per tenant. Allows a CQL query, but any aggregation or pipe will be ignored.."""
        endpoint = "alertsCountByTenant"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AlertsCountByTenantResponse),
        )
        if result.get(endpoint) is not None:
            return AlertsCountByTenantResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query alertsCountByTenant")

    def alerts_service_search(
        self, in_: Optional[SearchRequestInput] = None
    ) -> AlertsResponse:
        """Search alerts using Query Language. This is the same query language provided in Advanced Search page in Taegis XDR.."""
        endpoint = "alertsServiceSearch"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AlertsResponse),
        )
        if result.get(endpoint) is not None:
            return AlertsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query alertsServiceSearch")

    def alerts_service_poll(
        self, in_: Optional[PollRequestInput] = None
    ) -> AlertsResponse:
        """Poll for results for a specific `search_id`.."""
        endpoint = "alertsServicePoll"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AlertsResponse),
        )
        if result.get(endpoint) is not None:
            return AlertsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query alertsServicePoll")

    def alerts_service_aggregate_alerts_by_severity(
        self, in_: Optional[AggregateAlertsBySeverityInputInput] = None
    ) -> AlertsAggregateResponse:
        """Pull alert severity aggregates based on `group_by` parameters: domain, watchlist, hostname, detector, user.."""
        endpoint = "alertsServiceAggregateAlertsBySeverity"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AlertsAggregateResponse),
        )
        if result.get(endpoint) is not None:
            return AlertsAggregateResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for query alertsServiceAggregateAlertsBySeverity"
        )
