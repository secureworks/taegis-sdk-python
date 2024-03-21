"""Queries Mutation."""
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
from taegis_sdk_python.services.queries.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.queries import QueriesService

log = logging.getLogger(__name__)


class TaegisSDKQueriesMutation:
    """Taegis Queries Mutation operations."""

    def __init__(self, service: QueriesService):
        self.service = service

    def add_ql_query_to_history(self, input_: AddQLQueryToHistoryInput) -> QLQuery:
        """Creates a new search query entry.."""
        endpoint = "addQLQueryToHistory"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use createQLQuery.'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(QLQuery),
        )
        if result.get(endpoint) is not None:
            return QLQuery.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation addQLQueryToHistory")

    def create_saved_ql_query(self, input_: CreateSavedQLQueryInput) -> SavedQLQuery:
        """Creates a new search query entry that is marked as Saved.."""
        endpoint = "createSavedQLQuery"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use createQLQuery.'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(SavedQLQuery),
        )
        if result.get(endpoint) is not None:
            return SavedQLQuery.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createSavedQLQuery")

    def delete_ql_queries(self, input_: DeleteQLQueriesInput) -> DeleteQLQueriesResults:
        """Deletes search queries by their resource names.."""
        endpoint = "deleteQLQueries"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(DeleteQLQueriesResults),
        )
        if result.get(endpoint) is not None:
            return DeleteQLQueriesResults.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteQLQueries")

    def update_saved_ql_query(self, input_: UpdateSavedQLQueryInput) -> SavedQLQuery:
        """None."""
        endpoint = "updateSavedQLQuery"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'No longer supported'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(SavedQLQuery),
        )
        if result.get(endpoint) is not None:
            return SavedQLQuery.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateSavedQLQuery")

    def delete_saved_ql_queries(
        self, input_: DeleteQLQueriesInput
    ) -> DeleteQLQueriesResults:
        """None."""
        endpoint = "deleteSavedQLQueries"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'No longer supported'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(DeleteQLQueriesResults),
        )
        if result.get(endpoint) is not None:
            return DeleteQLQueriesResults.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteSavedQLQueries")
