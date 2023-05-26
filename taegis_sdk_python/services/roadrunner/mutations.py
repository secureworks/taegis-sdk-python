"""Roadrunner Mutation."""
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
from taegis_sdk_python.services.roadrunner.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.roadrunner import RoadrunnerService


class TaegisSDKRoadrunnerMutation:
    """Teagis Roadrunner Mutation operations."""

    def __init__(self, service: RoadrunnerService):
        self.service = service

    def create_parser(self, parser: ParserInput) -> Parser:
        """None."""
        endpoint = "createParser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "parser": prepare_input(parser),
            },
            output=build_output_string(Parser),
        )
        if result.get(endpoint) is not None:
            return Parser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createParser")

    def update_parser(self, id_: int, updated_parser: UpdatedParserInput) -> Parser:
        """None."""
        endpoint = "updateParser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "updatedParser": prepare_input(updated_parser),
            },
            output=build_output_string(Parser),
        )
        if result.get(endpoint) is not None:
            return Parser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateParser")

    def delete_parser(self, id_: int) -> Parser:
        """None."""
        endpoint = "deleteParser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Parser),
        )
        if result.get(endpoint) is not None:
            return Parser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteParser")

    def create_directory(self, directory: DirectoryInput) -> Directory:
        """None."""
        endpoint = "createDirectory"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "directory": prepare_input(directory),
            },
            output=build_output_string(Directory),
        )
        if result.get(endpoint) is not None:
            return Directory.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createDirectory")

    def update_directory(
        self, id_: int, updated_directory: UpdatedDirectoryInput
    ) -> Directory:
        """None."""
        endpoint = "updateDirectory"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "updatedDirectory": prepare_input(updated_directory),
            },
            output=build_output_string(Directory),
        )
        if result.get(endpoint) is not None:
            return Directory.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateDirectory")

    def delete_directory(self, id_: int) -> Directory:
        """None."""
        endpoint = "deleteDirectory"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Directory),
        )
        if result.get(endpoint) is not None:
            return Directory.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteDirectory")

    def create_sample(self, sample: CreateSampleInput) -> Sample:
        """None."""
        endpoint = "createSample"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "sample": prepare_input(sample),
            },
            output=build_output_string(Sample),
        )
        if result.get(endpoint) is not None:
            return Sample.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createSample")

    def update_sample(self, id_: int, updated_sample: UpdatedSampleInput) -> Sample:
        """None."""
        endpoint = "updateSample"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "updatedSample": prepare_input(updated_sample),
            },
            output=build_output_string(Sample),
        )
        if result.get(endpoint) is not None:
            return Sample.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateSample")

    def delete_sample(self, id_: int) -> Sample:
        """None."""
        endpoint = "deleteSample"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Sample),
        )
        if result.get(endpoint) is not None:
            return Sample.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteSample")
