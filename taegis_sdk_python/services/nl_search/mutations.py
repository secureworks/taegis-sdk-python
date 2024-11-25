"""NlSearch Mutation."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.nl_search.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.nl_search import NlSearchService

log = logging.getLogger(__name__)


class TaegisSDKNlSearchMutation:
    """Taegis Nl_search Mutation operations."""

    def __init__(self, service: NlSearchService):
        self.service = service

    def nl_search_feedback(self, in_: NLSearchFeedback) -> NLSearchFeedbackOutput:
        """nlSearchFeedback records user feedback on efficacy of the generated output."""
        endpoint = "nlSearchFeedback"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(NLSearchFeedbackOutput),
        )
        if result.get(endpoint) is not None:
            return NLSearchFeedbackOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation nlSearchFeedback")
