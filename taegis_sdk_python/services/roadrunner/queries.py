"""Roadrunner Query."""

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
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.roadrunner.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.roadrunner import RoadrunnerService

log = logging.getLogger(__name__)


class TaegisSDKRoadrunnerQuery:
    """Taegis Roadrunner Query operations."""

    def __init__(self, service: RoadrunnerService):
        self.service = service

    def syslog_sample(self, filter_: SyslogSampleFilter) -> List[SyslogSample]:
        """None."""
        endpoint = "syslogSample"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "filter": prepare_input(filter_),
            },
            output=build_output_string(SyslogSample),
        )
        if result.get(endpoint) is not None:
            return SyslogSample.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query syslogSample")

    def all_parsers(self) -> List[Parser]:
        """None."""
        endpoint = "allParsers"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(Parser)
        )
        if result.get(endpoint) is not None:
            return Parser.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query allParsers")

    def parser(self, filter_: ParserFilterInput) -> Parser:
        """None."""
        endpoint = "parser"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "filter": prepare_input(filter_),
            },
            output=build_output_string(Parser),
        )
        if result.get(endpoint) is not None:
            return Parser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query parser")

    def native_sensor_types(self) -> List[str]:
        """None."""
        endpoint = "nativeSensorTypes"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query nativeSensorTypes")

    def validate_parser(
        self, unvalidated_parser: UnvalidatedParserInput
    ) -> ValidateResult:
        """None."""
        endpoint = "validateParser"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "unvalidatedParser": prepare_input(unvalidated_parser),
            },
            output=build_output_string(ValidateResult),
        )
        if result.get(endpoint) is not None:
            return ValidateResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query validateParser")

    def sample_parser(
        self,
        messages: List[str],
        parser: Optional[UnvalidatedParserInput] = None,
        run_isolated: Optional[bool] = None,
        run_disabled: Optional[bool] = None,
    ) -> List[SampleResult]:
        """None."""
        endpoint = "sampleParser"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "messages": prepare_input(messages),
                "parser": prepare_input(parser),
                "runIsolated": prepare_input(run_isolated),
                "runDisabled": prepare_input(run_disabled),
            },
            output=build_output_string(SampleResult),
        )
        if result.get(endpoint) is not None:
            return SampleResult.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query sampleParser")

    def parser_schemas(self) -> List[str]:
        """None."""
        endpoint = "parserSchemas"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query parserSchemas")

    def directory(
        self, filter_: Optional[DirectoryFilterInput] = None
    ) -> List[Directory]:
        """None."""
        endpoint = "directory"

        log.warning(
            f"GraphQL Query `{endpoint}` is deprecated: 'Deprecated for MVP 10/2022 remove after suitable time if not used'"
        )

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "filter": prepare_input(filter_),
            },
            output=build_output_string(Directory),
        )
        if result.get(endpoint) is not None:
            return Directory.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query directory")

    def all_samples(self) -> List[Sample]:
        """None."""
        endpoint = "allSamples"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(Sample)
        )
        if result.get(endpoint) is not None:
            return Sample.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query allSamples")

    def sample(self, filter_: SampleFilterInput) -> Sample:
        """None."""
        endpoint = "sample"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "filter": prepare_input(filter_),
            },
            output=build_output_string(Sample),
        )
        if result.get(endpoint) is not None:
            return Sample.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query sample")
