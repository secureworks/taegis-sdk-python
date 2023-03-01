"""Threat Mutation."""
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
from taegis_sdk_python.services.threat.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.threat import ThreatService


class TaegisSDKThreatMutation:
    """Teagis Threat Mutation operations."""

    def __init__(self, service: ThreatService):
        self.service = service

    def indicator(self, id_: str) -> ThreatIndicator:
        """None."""
        endpoint = "indicator"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(ThreatIndicator),
        )
        if result.get(endpoint) is not None:
            return ThreatIndicator.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation indicator")

    def threat_delete_document(self, id_: str) -> bool:
        """threatDeleteDocument is used to delete a document by id in the configured index."""
        endpoint = "threatDeleteDocument"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation threatDeleteDocument")

    def create_list(self, input_: CreateListInput) -> List[ThreatList]:
        """None."""
        endpoint = "createList"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(ThreatList),
        )
        if result.get(endpoint) is not None:
            return ThreatList.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for mutation createList")

    def delete_list(self, input_: DeleteListInput) -> bool:
        """None."""
        endpoint = "deleteList"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation deleteList")

    def restore_list(self, input_: DeleteListInput) -> bool:
        """None."""
        endpoint = "restoreList"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation restoreList")
