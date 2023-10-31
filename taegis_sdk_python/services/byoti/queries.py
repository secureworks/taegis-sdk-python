"""Byoti Query."""
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
from taegis_sdk_python.services.byoti.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.byoti import ByotiService

log = logging.getLogger(__name__)


class TaegisSDKByotiQuery:
    """Taegis Byoti Query operations."""

    def __init__(self, service: ByotiService):
        self.service = service

    def search_indicators(
        self, input_: SearchIndicatorsInput
    ) -> SearchIndicatorsResponse:
        """Query to support searching for indicators using Taegis QL."""
        endpoint = "searchIndicators"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(SearchIndicatorsResponse),
        )
        if result.get(endpoint) is not None:
            return SearchIndicatorsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query searchIndicators")

    def get_indicators(
        self, input_: Optional[GetIndicatorsInput] = None
    ) -> SearchIndicatorsResponse:
        """Query Indicators using the API.  getIndicators will search and return indicators based on provided search parameters. If parameters are empty the query will return any indicators belonging to the caller up to the default of 100 per page."""
        endpoint = "getIndicators"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(SearchIndicatorsResponse),
        )
        if result.get(endpoint) is not None:
            return SearchIndicatorsResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getIndicators")
