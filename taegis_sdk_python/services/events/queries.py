"""Events Query."""
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
from taegis_sdk_python.services.events.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.events import EventsService


class TaegisSDKEventsQuery:
    """Teagis Events Query operations."""

    def __init__(self, service: EventsService):
        self.service = service

    def events(
        self, ids: List[str], options: Optional[EventFetchOptions] = None
    ) -> List[Event]:
        """Resolve events by their ID. Accepts options for crafting events.."""
        endpoint = "events"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
                "options": prepare_input(options),
            },
            output=build_output_string(Event),
        )
        if result.get(endpoint) is not None:
            return Event.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query events")

    def event_query(self, id_: str) -> EventQuery:
        """Return the query's status. Query IDs are included in EventQueryResult.."""
        endpoint = "eventQuery"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(EventQuery),
        )
        if result.get(endpoint) is not None:
            return EventQuery.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query eventQuery")

    def event_queries(
        self, metadata: Optional[Dict[str, Any]] = None
    ) -> List[EventQuery]:
        """Provide a catalog of cached queries.."""
        endpoint = "eventQueries"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "metadata": prepare_input(metadata),
            },
            output=build_output_string(EventQuery),
        )
        if result.get(endpoint) is not None:
            return EventQuery.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query eventQueries")
