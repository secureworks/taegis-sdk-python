"""Events Mutation."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import build_output_string, prepare_input
from taegis_sdk_python.services.events.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.events import EventsService


class TaegisSDKEventsMutation:
    """Teagis Events Mutation operations."""

    def __init__(self, service: EventsService):
        self.service = service

    def delete_event_query(self, id_: str) -> bool:
        """Remove the query from the cached query catalog.."""
        endpoint = "deleteEventQuery"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation deleteEventQuery")
