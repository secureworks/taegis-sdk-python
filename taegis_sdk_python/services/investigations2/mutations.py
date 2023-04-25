"""Investigations2 Mutation."""
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
from taegis_sdk_python.services.investigations2.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.investigations2 import Investigations2Service


class TaegisSDKInvestigations2Mutation:
    """Teagis Investigations2 Mutation operations."""

    def __init__(self, service: Investigations2Service):
        self.service = service

    def create_investigation_v2(
        self, input_: CreateInvestigationInput
    ) -> InvestigationV2:
        """Create new investigation."""
        endpoint = "createInvestigationV2"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationV2),
        )
        if result.get(endpoint) is not None:
            return InvestigationV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createInvestigationV2")

    def update_investigation_v2(
        self, input_: UpdateInvestigationV2Input
    ) -> InvestigationV2:
        """Update an existing investigation."""
        endpoint = "updateInvestigationV2"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationV2),
        )
        if result.get(endpoint) is not None:
            return InvestigationV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateInvestigationV2")

    def add_evidence_to_investigation(
        self, input_: AddEvidenceToInvestigationInput
    ) -> AddEvidenceToInvestigationResult:
        """Add more evidence to an existing investigation

        This is a background job, it will be pretty quick, but added alerts/events will likely not show up in the returned investigation
        The processing status will reflect where the the investigation is at in the processing job.
        """
        endpoint = "addEvidenceToInvestigation"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(AddEvidenceToInvestigationResult),
        )
        if result.get(endpoint) is not None:
            return AddEvidenceToInvestigationResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation addEvidenceToInvestigation")

    def create_investigation_rule(
        self, input_: CreateInvestigationRuleInput
    ) -> InvestigationRule:
        """Create a new investigation rule."""
        endpoint = "createInvestigationRule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationRule),
        )
        if result.get(endpoint) is not None:
            return InvestigationRule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createInvestigationRule")

    def update_investigation_rule(
        self, input_: UpdateInvestigationRuleInput
    ) -> InvestigationRule:
        """Update an existing investigation rule."""
        endpoint = "updateInvestigationRule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationRule),
        )
        if result.get(endpoint) is not None:
            return InvestigationRule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateInvestigationRule")

    def delete_investigation_rule(
        self, input_: DeleteInvestigationRuleInput
    ) -> InvestigationRule:
        """Delete an existing investigation rule - this is a hard delete at this time. Data will not be recoverable.."""
        endpoint = "deleteInvestigationRule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationRule),
        )
        if result.get(endpoint) is not None:
            return InvestigationRule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteInvestigationRule")

    def create_investigation_template(
        self, input_: CreateInvestigationTemplateInput
    ) -> InvestigationTemplate:
        """Create a new investigation template."""
        endpoint = "createInvestigationTemplate"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationTemplate),
        )
        if result.get(endpoint) is not None:
            return InvestigationTemplate.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createInvestigationTemplate")

    def update_investigation_template(
        self, input_: UpdateInvestigationTemplateInput
    ) -> InvestigationTemplate:
        """Update an existing investigation template."""
        endpoint = "updateInvestigationTemplate"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationTemplate),
        )
        if result.get(endpoint) is not None:
            return InvestigationTemplate.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateInvestigationTemplate")

    def delete_investigation_template(
        self, input_: DeleteInvestigationTemplateInput
    ) -> InvestigationTemplate:
        """Delete an existing investigation template - this is a hard delete. Data will not be recoverable.."""
        endpoint = "deleteInvestigationTemplate"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationTemplate),
        )
        if result.get(endpoint) is not None:
            return InvestigationTemplate.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteInvestigationTemplate")

    def import_investigation_resources(
        self, input_: ImportInvestigationResourcesInput
    ) -> List[InvestigationResource]:
        """Create or update investigation resource(s)."""
        endpoint = "importInvestigationResources"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationResource),
        )
        if result.get(endpoint) is not None:
            return [
                parse_union_result(InvestigationResource, r)
                for r in result.get(endpoint)
            ]
        raise GraphQLNoRowsInResultSetError("for mutation importInvestigationResources")

    def add_comment_to_investigation(
        self, input_: AddCommentToInvestigationInput
    ) -> CommentV2:
        """Add new comment to the provided investigation id."""
        endpoint = "addCommentToInvestigation"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(CommentV2),
        )
        if result.get(endpoint) is not None:
            return CommentV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation addCommentToInvestigation")

    def update_investigation_comment(
        self, input_: UpdateInvestigationCommentInput
    ) -> CommentV2:
        """Update existing comment."""
        endpoint = "updateInvestigationComment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(CommentV2),
        )
        if result.get(endpoint) is not None:
            return CommentV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateInvestigationComment")

    def delete_investigation_comment(
        self, input_: DeleteInvestigationCommentInput
    ) -> CommentV2:
        """Delete an investigation comment- this is a hard delete at this time. Data will not be recoverable.."""
        endpoint = "deleteInvestigationComment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(CommentV2),
        )
        if result.get(endpoint) is not None:
            return CommentV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteInvestigationComment")

    def close_investigation(self, input_: CloseInvestigationInput) -> InvestigationV2:
        """Close an investigation and resolve associated alerts (if exists) asynchronously."""
        endpoint = "closeInvestigation"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationV2),
        )
        if result.get(endpoint) is not None:
            return InvestigationV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation closeInvestigation")