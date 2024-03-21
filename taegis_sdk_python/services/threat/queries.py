"""Threat Query."""
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
from taegis_sdk_python.services.threat.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.threat import ThreatService

log = logging.getLogger(__name__)


class TaegisSDKThreatQuery:
    """Taegis Threat Query operations."""

    def __init__(self, service: ThreatService):
        self.service = service

    def threat_publication(self, id_: str) -> ThreatPublication:
        """Retreives a publication by ID.."""
        endpoint = "threatPublication"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ID": prepare_input(id_),
            },
            output=build_output_string(ThreatPublication),
        )
        if result.get(endpoint) is not None:
            return ThreatPublication.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query threatPublication")

    def threat_publications(self, text: str) -> List[ThreatPublication]:
        """Searches publications for text.."""
        endpoint = "threatPublications"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "text": prepare_input(text),
            },
            output=build_output_string(ThreatPublication),
        )
        if result.get(endpoint) is not None:
            return ThreatPublication.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query threatPublications")

    def threat_publications_search(self, text: List[str]) -> List[ThreatPublication]:
        """Gets publications for multiple indicators.."""
        endpoint = "threatPublicationsSearch"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "text": prepare_input(text),
            },
            output=build_output_string(ThreatPublication),
        )
        if result.get(endpoint) is not None:
            return ThreatPublication.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query threatPublicationsSearch")

    def threat_latest_publications(
        self, from_: int, size: int
    ) -> List[ThreatPublication]:
        """Gets the latest publications from an offset with a size.."""
        endpoint = "threatLatestPublications"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "from": prepare_input(from_),
                "size": prepare_input(size),
            },
            output=build_output_string(ThreatPublication),
        )
        if result.get(endpoint) is not None:
            return ThreatPublication.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query threatLatestPublications")

    def threat_object_by_id(
        self, id_: str, object_type: ThreatObjectType
    ) -> ThreatResult:
        """Gets an object by `id`, `name` or `sharing_id`.."""
        endpoint = "threatObjectById"

        log.warning(f"GraphQL Query `{endpoint}` is deprecated: 'No longer supported'")

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "objectType": prepare_input(object_type),
            },
            output=build_output_string(ThreatResult),
        )
        if result.get(endpoint) is not None:
            return parse_union_result(ThreatResult, result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query threatObjectById")

    def threat_identities_by_confidence(self, confidence: int) -> List[ThreatResult]:
        """Gets identities by confidence score.."""
        endpoint = "threatIdentitiesByConfidence"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "confidence": prepare_input(confidence),
            },
            output=build_output_string(ThreatResult),
        )
        if result.get(endpoint) is not None:
            return [parse_union_result(ThreatResult, r) for r in result.get(endpoint)]
        raise GraphQLNoRowsInResultSetError("for query threatIdentitiesByConfidence")

    def threat_objects_related(self, source_id: str, target_id: str) -> bool:
        """Checks if a relationship between source and target exists.."""
        endpoint = "threatObjectsRelated"

        log.warning(f"GraphQL Query `{endpoint}` is deprecated: 'No longer supported'")

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "sourceID": prepare_input(source_id),
                "targetID": prepare_input(target_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query threatObjectsRelated")

    def threat_get_related(self, source_id: str) -> List[ThreatResult]:
        """Gets relationship(s) between source and target(s).."""
        endpoint = "threatGetRelated"

        log.warning(f"GraphQL Query `{endpoint}` is deprecated: 'No longer supported'")

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "sourceID": prepare_input(source_id),
            },
            output=build_output_string(ThreatResult),
        )
        if result.get(endpoint) is not None:
            return [parse_union_result(ThreatResult, r) for r in result.get(endpoint)]
        raise GraphQLNoRowsInResultSetError("for query threatGetRelated")

    def threat_watchlist(self, type_: ThreatParentType) -> List[ThreatRelationship]:
        """Gets a watchlist by type. All results are considered **high confidence**.."""
        endpoint = "threatWatchlist"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "type": prepare_input(type_),
            },
            output=build_output_string(ThreatRelationship),
        )
        if result.get(endpoint) is not None:
            return ThreatRelationship.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query threatWatchlist")

    def threat_indicator_publications(self, id_: str) -> List[ThreatReport]:
        """Gets publications related to indicators.."""
        endpoint = "threatIndicatorPublications"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ID": prepare_input(id_),
            },
            output=build_output_string(ThreatReport),
        )
        if result.get(endpoint) is not None:
            return ThreatReport.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query threatIndicatorPublications")

    def threat_indicator_intelligence(self, id_: str) -> ThreatIndicatorIntelligence:
        """Retrieves all intelligence associated with an indicator.."""
        endpoint = "threatIndicatorIntelligence"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ID": prepare_input(id_),
            },
            output=build_output_string(ThreatIndicatorIntelligence),
        )
        if result.get(endpoint) is not None:
            return ThreatIndicatorIntelligence.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query threatIndicatorIntelligence")

    def threat_relationship(self, id_: str) -> ThreatRelationship:
        """Gets relationship by `id`.."""
        endpoint = "threatRelationship"

        log.warning(f"GraphQL Query `{endpoint}` is deprecated: 'No longer supported'")

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ID": prepare_input(id_),
            },
            output=build_output_string(ThreatRelationship),
        )
        if result.get(endpoint) is not None:
            return ThreatRelationship.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query threatRelationship")

    def threat_identity(self, id_: str) -> ThreatIdentity:
        """Gets identity by `id`.."""
        endpoint = "threatIdentity"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ID": prepare_input(id_),
            },
            output=build_output_string(ThreatIdentity),
        )
        if result.get(endpoint) is not None:
            return ThreatIdentity.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query threatIdentity")

    def threat_malware(self, id_: str) -> ThreatMalware:
        """Gets malware by `id`.."""
        endpoint = "threatMalware"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ID": prepare_input(id_),
            },
            output=build_output_string(ThreatMalware),
        )
        if result.get(endpoint) is not None:
            return ThreatMalware.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query threatMalware")

    def threat_identities(
        self, confidence: Optional[int] = None
    ) -> List[ThreatIdentity]:
        """Gets identities by confidence score.."""
        endpoint = "threatIdentities"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "confidence": prepare_input(confidence),
            },
            output=build_output_string(ThreatIdentity),
        )
        if result.get(endpoint) is not None:
            return ThreatIdentity.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query threatIdentities")

    def threat_vid_intelligence(self, vid: str) -> ThreatVidIntelligence:
        """Retrieves all intelligence associated with a `VID`.."""
        endpoint = "threatVidIntelligence"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "vid": prepare_input(vid),
            },
            output=build_output_string(ThreatVidIntelligence),
        )
        if result.get(endpoint) is not None:
            return ThreatVidIntelligence.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query threatVidIntelligence")

    def threat_indicators_intelligence(
        self, id_: Optional[List[str]] = None
    ) -> List[ThreatIndicatorIntelligence]:
        """Retrieves all intelligence associated with a list of indicators.."""
        endpoint = "threatIndicatorsIntelligence"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ID": prepare_input(id_),
            },
            output=build_output_string(ThreatIndicatorIntelligence),
        )
        if result.get(endpoint) is not None:
            return ThreatIndicatorIntelligence.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query threatIndicatorsIntelligence")

    def lists(self, arguments: ListsArguments) -> Lists:
        """Retrieves Custom Lists for the respective tenant."""
        endpoint = "lists"

        log.warning(f"GraphQL Query `{endpoint}` is deprecated: 'No longer supported'")

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(Lists),
        )
        if result.get(endpoint) is not None:
            return Lists.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query lists")

    def list(self, id_: str, arguments: ListsArguments) -> ThreatList:
        """Retrieves a custom list by ID."""
        endpoint = "list"

        log.warning(f"GraphQL Query `{endpoint}` is deprecated: 'No longer supported'")

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(ThreatList),
        )
        if result.get(endpoint) is not None:
            return ThreatList.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query list")

    def list_items_by_tag(self, tag: str, arguments: ListsArguments) -> ListItems:
        """Retrieves list items that contains the specified tag (case sensitive)."""
        endpoint = "listItemsByTag"

        log.warning(f"GraphQL Query `{endpoint}` is deprecated: 'No longer supported'")

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "tag": prepare_input(tag),
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(ListItems),
        )
        if result.get(endpoint) is not None:
            return ListItems.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query listItemsByTag")

    def list_items_by_name(self, name: str, arguments: ListsArguments) -> ListItems:
        """Retrieves list items by indicator name."""
        endpoint = "listItemsByName"

        log.warning(f"GraphQL Query `{endpoint}` is deprecated: 'No longer supported'")

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "name": prepare_input(name),
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(ListItems),
        )
        if result.get(endpoint) is not None:
            return ListItems.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query listItemsByName")
