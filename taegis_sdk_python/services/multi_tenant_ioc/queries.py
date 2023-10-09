"""MultiTenantIoc Query."""
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
from taegis_sdk_python.services.multi_tenant_ioc.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.multi_tenant_ioc import MultiTenantIocService

log = logging.getLogger(__name__)


class TaegisSDKMultiTenantIocQuery:
    """Taegis Multi_tenant_ioc Query operations."""

    def __init__(self, service: MultiTenantIocService):
        self.service = service

    def event_window(self, arguments: EventAggregationArguments) -> EventWindow:
        """Return the earliest and latest timestamps found for events within provided time range."""
        endpoint = "eventWindow"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(EventWindow),
        )
        if result.get(endpoint) is not None:
            return EventWindow.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query eventWindow")

    def event_count_by_logical_type(
        self, arguments: EventAggregationArguments
    ) -> EventCountResult:
        """Generate a breakdown (histogram) of the aggregated count of events
        that match the given constraints. The result rows are broken down per eventType and per day..
        """
        endpoint = "eventCountByLogicalType"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(EventCountResult),
        )
        if result.get(endpoint) is not None:
            return EventCountResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query eventCountByLogicalType")

    def event_count_page(
        self,
        next_token: str,
        session_key: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> EventCountResult:
        """Returns next page of results for eventCountByLogicalType if available.
        If sessionKey not provided will fallback to auth header (single tenant search only)..
        """
        endpoint = "eventCountPage"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "nextToken": prepare_input(next_token),
                "sessionKey": prepare_input(session_key),
                "limit": prepare_input(limit),
            },
            output=build_output_string(EventCountResult),
        )
        if result.get(endpoint) is not None:
            return EventCountResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query eventCountPage")
