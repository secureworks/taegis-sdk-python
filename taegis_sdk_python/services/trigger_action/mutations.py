"""TriggerAction Mutation."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.trigger_action.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.trigger_action import TriggerActionService

log = logging.getLogger(__name__)


class TaegisSDKTriggerActionMutation:
    """Taegis Trigger_action Mutation operations."""

    def __init__(self, service: TriggerActionService):
        self.service = service

    def execute_action(self, input_: ExecuteActionInput) -> PlaybookExecution:
        """executeAction executes a playbook against an object."""
        endpoint = "executeAction"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(PlaybookExecution),
        )
        if result.get(endpoint) is not None:
            return PlaybookExecution.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation executeAction")

    def execute_bulk_action(self, input_: ExecuteBulkActionInput) -> BulkActions:
        """executeBulkAction executes a playbook against a list of entities."""
        endpoint = "executeBulkAction"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkActions),
        )
        if result.get(endpoint) is not None:
            return BulkActions.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation executeBulkAction")

    def execute_playbook_action(
        self,
        playbook_action: str,
        inputs: Any,
        target_resource: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> PlaybookExecution:
        """executePlaybookAction is deprecated, use executePlaybookActionsV2 instead. This endpoint does not support entities."""
        endpoint = "executePlaybookAction"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use executeBulkAction instead'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "playbookAction": prepare_input(playbook_action),
                "inputs": prepare_input(inputs),
                "targetResource": prepare_input(target_resource),
                "reason": prepare_input(reason),
            },
            output=build_output_string(PlaybookExecution),
        )
        if result.get(endpoint) is not None:
            return PlaybookExecution.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation executePlaybookAction")

    def execute_playbook_actions(
        self, input_: List[ExecutePlaybookActionInput]
    ) -> List[PlaybookExecution]:
        """executePlaybookActions is deprecated, use executePlaybookActionsV2 instead. This endpoint does not support entities."""
        endpoint = "executePlaybookActions"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use executeBulkAction instead'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(PlaybookExecution),
        )
        if result.get(endpoint) is not None:
            return PlaybookExecution.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation executePlaybookActions")

    def execute_playbook_actions_v2(
        self, input_: List[ExecutePlaybookActionV2Input]
    ) -> List[PlaybookExecution]:
        """executePlaybookActionsV2 starts a playbook response or context lookup action."""
        endpoint = "executePlaybookActionsV2"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use executeBulkAction instead'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(PlaybookExecution),
        )
        if result.get(endpoint) is not None:
            return PlaybookExecution.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation executePlaybookActionsV2")
