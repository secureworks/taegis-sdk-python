"""EventSearch Query."""

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
from taegis_sdk_python.services.event_search.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.event_search import EventSearchService

log = logging.getLogger(__name__)


class TaegisSDKEventSearchQuery:
    """Taegis Event_search Query operations."""

    def __init__(self, service: EventSearchService):
        self.service = service

    def auxiliary_events_by_id(
        self, in_: Optional[GetEventByIDRequestInput] = None
    ) -> AuxiliaryEventsSearchResponse:
        """None."""
        endpoint = "auxiliaryEventsById"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AuxiliaryEventsSearchResponse),
        )
        if result.get(endpoint) is not None:
            return AuxiliaryEventsSearchResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query auxiliaryEventsById")

    def auxiliary_events_search(
        self, in_: AuxiliaryEventsSearchInput
    ) -> AuxiliaryEventsSearchResponse:
        """None."""
        endpoint = "auxiliaryEventsSearch"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(AuxiliaryEventsSearchResponse),
        )
        if result.get(endpoint) is not None:
            return AuxiliaryEventsSearchResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query auxiliaryEventsSearch")

    def alert_ids_from_aux_events_search(
        self, in_: AuxiliaryEventsSearchInput
    ) -> List[str]:
        """Will perform a more efficient search for auxiliary events that will only return a list of
        alert IDs associated with the events found.."""
        endpoint = "alertIdsFromAuxEventsSearch"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query alertIdsFromAuxEventsSearch")
