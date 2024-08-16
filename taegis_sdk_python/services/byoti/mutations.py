"""Byoti Mutation."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.byoti.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.byoti import ByotiService

log = logging.getLogger(__name__)


class TaegisSDKByotiMutation:
    """Taegis Byoti Mutation operations."""

    def __init__(self, service: ByotiService):
        self.service = service

    def upsert_stix_documents(
        self, input_: List[STIXDocumentInput]
    ) -> UpsertIndicatorsResponse:
        """Mutation for adding or updating STIX documents as indicators."""
        endpoint = "upsertSTIXDocuments"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(UpsertIndicatorsResponse),
        )
        if result.get(endpoint) is not None:
            return UpsertIndicatorsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation upsertSTIXDocuments")

    def upsert_indicators(
        self, input_: List[IndicatorInput]
    ) -> UpsertIndicatorsResponse:
        """Mutation for adding or updating indicators."""
        endpoint = "upsertIndicators"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(UpsertIndicatorsResponse),
        )
        if result.get(endpoint) is not None:
            return UpsertIndicatorsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation upsertIndicators")

    def delete_indicators(self, query: str) -> DeleteIndicatorResponse:
        """Mutation for deleting indicators using CQL queries."""
        endpoint = "deleteIndicators"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "query": prepare_input(query),
            },
            output=build_output_string(DeleteIndicatorResponse),
        )
        if result.get(endpoint) is not None:
            return DeleteIndicatorResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteIndicators")
