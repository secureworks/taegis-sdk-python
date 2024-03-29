"""Investigations2 Query."""
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
from taegis_sdk_python.services.investigations2.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.investigations2 import Investigations2Service

log = logging.getLogger(__name__)


class TaegisSDKInvestigations2Query:
    """Taegis Investigations2 Query operations."""

    def __init__(self, service: Investigations2Service):
        self.service = service

    def investigation_v2(self, arguments: InvestigationV2Arguments) -> InvestigationV2:
        """Get an Investigation."""
        endpoint = "investigationV2"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationV2),
        )
        if result.get(endpoint) is not None:
            return InvestigationV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationV2")

    def investigations_v2(
        self, arguments: InvestigationsV2Arguments
    ) -> InvestigationsV2:
        """Search investigations."""
        endpoint = "investigationsV2"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationsV2),
        )
        if result.get(endpoint) is not None:
            return InvestigationsV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationsV2")

    def investigation_rule(
        self, arguments: InvestigationRuleArguments
    ) -> InvestigationRule:
        """Get an auto-investigation rule."""
        endpoint = "investigationRule"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationRule),
        )
        if result.get(endpoint) is not None:
            return InvestigationRule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationRule")

    def investigation_rules(
        self, arguments: InvestigationRulesArguments
    ) -> InvestigationRules:
        """Get auto-investigation rules."""
        endpoint = "investigationRules"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationRules),
        )
        if result.get(endpoint) is not None:
            return InvestigationRules.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationRules")

    def investigation_template(
        self, arguments: InvestigationTemplateArguments
    ) -> InvestigationTemplate:
        """Get an auto-investigation template."""
        endpoint = "investigationTemplate"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationTemplate),
        )
        if result.get(endpoint) is not None:
            return InvestigationTemplate.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationTemplate")

    def investigation_templates(
        self, arguments: InvestigationTemplatesArguments
    ) -> InvestigationTemplates:
        """Get auto-investigation templates."""
        endpoint = "investigationTemplates"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationTemplates),
        )
        if result.get(endpoint) is not None:
            return InvestigationTemplates.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationTemplates")

    def export_investigation_resources(
        self, arguments: ExportInvestigationResourcesArguments
    ) -> InvestigationResourceExport:
        """Get the yaml string for auto-investigation resources (rules & templates)."""
        endpoint = "exportInvestigationResources"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationResourceExport),
        )
        if result.get(endpoint) is not None:
            return InvestigationResourceExport.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query exportInvestigationResources")

    def investigation_v2_timeline(
        self, arguments: InvestigationV2TimelineArguments
    ) -> InvestigationV2Timeline:
        """Get the investigation timeline."""
        endpoint = "investigationV2Timeline"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationV2Timeline),
        )
        if result.get(endpoint) is not None:
            return InvestigationV2Timeline.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationV2Timeline")

    def comments_v2(self, arguments: CommentsV2Arguments) -> CommentsV2:
        """Get all investigation comments."""
        endpoint = "commentsV2"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(CommentsV2),
        )
        if result.get(endpoint) is not None:
            return CommentsV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query commentsV2")

    def investigation_v2_types(self) -> List[InvestigationV2Type]:
        """Get investigation types list based on user."""
        endpoint = "investigationV2Types"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(InvestigationV2Type),
        )
        if result.get(endpoint) is not None:
            return InvestigationV2Type.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query investigationV2Types")

    def investigation_file_v2(
        self, arguments: InvestigationFileV2Arguments
    ) -> InvestigationFileV2:
        """Get investigation file meta details - includes presigned download url."""
        endpoint = "investigationFileV2"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationFileV2),
        )
        if result.get(endpoint) is not None:
            return InvestigationFileV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationFileV2")

    def investigation_files_v2(
        self, arguments: InvestigationFilesV2Arguments
    ) -> InvestigationFilesV2:
        """Get investigation files meta details - does not include presigned download urls."""
        endpoint = "investigationFilesV2"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationFilesV2),
        )
        if result.get(endpoint) is not None:
            return InvestigationFilesV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationFilesV2")
