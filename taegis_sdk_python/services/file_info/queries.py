"""FileInfo Query."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.file_info.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.file_info import FileInfoService


log = logging.getLogger(__name__)


class TaegisSDKFileInfoQuery:
    """Taegis File_info Query operations."""

    def __init__(self, service: FileInfoService):
        self.service = service

    def file_info(
        self, file_hash: str, include_all_rules: Optional[bool] = None
    ) -> File:
        """Returns details for a single file identified by the given hash. Set includeAllRules = true to include research rule matches."""
        endpoint = "fileInfo"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "fileHash": prepare_input(file_hash),
                "includeAllRules": prepare_input(include_all_rules),
            },
            output=build_output_string(File),
        )
        if result.get(endpoint) is not None:
            return File.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query fileInfo")

    def file_info_counts(self, file_hash: str) -> FileCounts:
        """Returns the affected host and tenant counts for a single file."""
        endpoint = "fileInfoCounts"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "fileHash": prepare_input(file_hash),
            },
            output=build_output_string(FileCounts),
        )
        if result.get(endpoint) is not None:
            return FileCounts.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query fileInfoCounts")

    def search_file_info(
        self, query: str, include_all_rules: Optional[bool] = None
    ) -> List[File]:
        """Returns details for all files matching the given CQL query. Set includeAllRules = true to include research rule matches."""
        endpoint = "searchFileInfo"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "query": prepare_input(query),
                "includeAllRules": prepare_input(include_all_rules),
            },
            output=build_output_string(File),
        )
        if result.get(endpoint) is not None:
            return File.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query searchFileInfo")

    def event_has_fetchable_file_appearances(
        self, event_id: str
    ) -> FetchableFileAppearancesResponse:
        """Returns true if fetchable file appearances can be extracted from the given event."""
        endpoint = "eventHasFetchableFileAppearances"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "eventID": prepare_input(event_id),
            },
            output=build_output_string(FetchableFileAppearancesResponse),
        )
        if result.get(endpoint) is not None:
            return FetchableFileAppearancesResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for query eventHasFetchableFileAppearances"
        )

    def file_info_exists(self, file_hash: str) -> bool:
        """Returns true if we have details for a file with the given hash."""
        endpoint = "fileInfoExists"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "fileHash": prepare_input(file_hash),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query fileInfoExists")

    def get_file_marking_status(
        self, file_hash: str, file_metadata_id: Optional[str] = None
    ) -> FileMarkingStatus:
        """Returns FileMarkingStatus for a file with the given file-hash or fileMetadataId."""
        endpoint = "getFileMarkingStatus"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "fileHash": prepare_input(file_hash),
                "fileMetadataId": prepare_input(file_metadata_id),
            },
            output=build_output_string(FileMarkingStatus),
        )
        if result.get(endpoint) is not None:
            return FileMarkingStatus.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getFileMarkingStatus")
