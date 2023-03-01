"""Investigations Query."""
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
from taegis_sdk_python.services.investigations.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.investigations import InvestigationsService


class TaegisSDKInvestigationsQuery:
    """Teagis Investigations Query operations."""

    def __init__(self, service: InvestigationsService):
        self.service = service

    def investigation_summary(self) -> List[InvestigationSummary]:
        """Get summary of investigations (tag and counts for each tag)."""
        endpoint = "investigationSummary"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(InvestigationSummary),
        )
        if result.get(endpoint) is not None:
            return InvestigationSummary.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query investigationSummary")

    def investigation(self, investigation_id: str) -> Investigation:
        """Get an investigation by id."""
        endpoint = "investigation"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigation")

    def investigations(self, investigation_ids: List[str]) -> List[Investigation]:
        """Get investigations for the list of ids."""
        endpoint = "investigations"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_ids": prepare_input(investigation_ids),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query investigations")

    def all_investigations(
        self,
        status: Optional[List[str]] = None,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        updated_after: Optional[str] = None,
        updated_before: Optional[str] = None,
        order_by_field: Optional[OrderFieldInput] = None,
        order_direction: Optional[OrderDirectionInput] = None,
        is_deleted: Optional[bool] = None,
        hide_threat_hunting_investigations: Optional[bool] = None,
    ) -> List[Investigation]:
        """Get all investigations
        Max perPage Value is 100. If requesting over 100, only the first 100 will be returned.
        deprecated: Use `investigationsSearch` for better investigations query experience..
        """
        endpoint = "allInvestigations"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "status": prepare_input(status),
                "page": prepare_input(page),
                "perPage": prepare_input(per_page),
                "createdAfter": prepare_input(created_after),
                "createdBefore": prepare_input(created_before),
                "updatedAfter": prepare_input(updated_after),
                "updatedBefore": prepare_input(updated_before),
                "orderByField": prepare_input(order_by_field),
                "orderDirection": prepare_input(order_direction),
                "isDeleted": prepare_input(is_deleted),
                "hideThreatHuntingInvestigations": prepare_input(
                    hide_threat_hunting_investigations
                ),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query allInvestigations")

    def investigation_count_over_time(
        self,
        transition_status: Optional[str] = None,
        after: Optional[str] = None,
        before: Optional[str] = None,
    ) -> Count:
        """Get the number of investigations created during a given time frame. Can optionslly pass in a desired 'transition_status' (handoff, acknowledge, resolution)."""
        endpoint = "investigationCountOverTime"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "transition_status": prepare_input(transition_status),
                "after": prepare_input(after),
                "before": prepare_input(before),
            },
            output=build_output_string(Count),
        )
        if result.get(endpoint) is not None:
            return Count.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationCountOverTime")

    def mean_time_summary_over_period(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        include_threat_hunt_types: Optional[bool] = None,
    ) -> TimeSummaryForGroup:
        """Get the average times it took to hand off, acknowledge, and resolve all investigations over the course of the period."""
        endpoint = "meanTimeSummaryOverPeriod"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "after": prepare_input(after),
                "before": prepare_input(before),
                "includeThreatHuntTypes": prepare_input(include_threat_hunt_types),
            },
            output=build_output_string(TimeSummaryForGroup),
        )
        if result.get(endpoint) is not None:
            return TimeSummaryForGroup.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query meanTimeSummaryOverPeriod")

    def investigation_assets(
        self,
        investigation_id: str,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> InvestigationAssetOutput:
        """Get investigation assets by investigation id."""
        endpoint = "investigationAssets"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "page": prepare_input(page),
                "perPage": prepare_input(per_page),
            },
            output=build_output_string(InvestigationAssetOutput),
        )
        if result.get(endpoint) is not None:
            return InvestigationAssetOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationAssets")

    def investigation_events(
        self,
        investigation_id: str,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> InvestigationEventOutput:
        """Get investigation events by investigation id."""
        endpoint = "investigationEvents"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "page": prepare_input(page),
                "perPage": prepare_input(per_page),
            },
            output=build_output_string(InvestigationEventOutput),
        )
        if result.get(endpoint) is not None:
            return InvestigationEventOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationEvents")

    def investigation_alerts(
        self,
        investigation_id: str,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        filter_query: Optional[str] = None,
        order_by_field: Optional[str] = None,
        order_direction: Optional[OrderDirection] = None,
    ) -> InvestigationAlertOutput:
        """Get investigation alerts by investigation id
        deprecated: Use `investigation` query or alerts2 search query (paginated) to get alerts by investigation id.
        """
        endpoint = "investigationAlerts"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "page": prepare_input(page),
                "perPage": prepare_input(per_page),
                "filterQuery": prepare_input(filter_query),
                "orderByField": prepare_input(order_by_field),
                "orderDirection": prepare_input(order_direction),
            },
            output=build_output_string(InvestigationAlertOutput),
        )
        if result.get(endpoint) is not None:
            return InvestigationAlertOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationAlerts")

    def investigation_genesis_events(self, investigation_id: str) -> List[Event]:
        """Get investigation genesis events by investigation id."""
        endpoint = "investigationGenesisEvents"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output=build_output_string(Event),
        )
        if result.get(endpoint) is not None:
            return Event.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query investigationGenesisEvents")

    def investigation_genesis_alerts(self, investigation_id: str) -> List[Alert]:
        """Get investigation genesis alerts by investigation id."""
        endpoint = "investigationGenesisAlerts"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output=build_output_string(Alert),
        )
        if result.get(endpoint) is not None:
            return Alert.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query investigationGenesisAlerts")

    def investigation_auth_credentials(self, investigation_id: str) -> List[str]:
        """Get investigation auth credentials by investigation id."""
        endpoint = "investigationAuthCredentials"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query investigationAuthCredentials")

    def investigation_search_queries(self, investigation_id: str) -> List[SearchQuery]:
        """Get investigation search queries by investigation id."""
        endpoint = "investigationSearchQueries"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output=build_output_string(SearchQuery),
        )
        if result.get(endpoint) is not None:
            return SearchQuery.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query investigationSearchQueries")

    def investigations_bulk_events_alerts(
        self, query_strings: List[str]
    ) -> List[InvestigationBulkResponse]:
        """Get investigations by quering a string on events/alerts/genesis events/genesis alerts fields."""
        endpoint = "investigationsBulkEventsAlerts"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "queryStrings": prepare_input(query_strings),
            },
            output=build_output_string(InvestigationBulkResponse),
        )
        if result.get(endpoint) is not None:
            return InvestigationBulkResponse.schema().load(
                result.get(endpoint), many=True
            )
        raise GraphQLNoRowsInResultSetError("for query investigationsBulkEventsAlerts")

    def investigations_bulk_update_alerts(self) -> str:
        """Updates Investigation Alerts and Investigation information from Alerts (ie Access Vectors)."""
        endpoint = "investigationsBulkUpdateAlerts"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query investigationsBulkUpdateAlerts")

    def investigation_status_summary(
        self, updated_after: Optional[str] = None, updated_before: Optional[str] = None
    ) -> List[SummaryGroup]:
        """Get summary of investigations and status filtered by updated_at."""
        endpoint = "investigationStatusSummary"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "updatedAfter": prepare_input(updated_after),
                "updatedBefore": prepare_input(updated_before),
            },
            output=build_output_string(SummaryGroup),
        )
        if result.get(endpoint) is not None:
            return SummaryGroup.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query investigationStatusSummary")

    def investigations_search(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        query: Optional[str] = None,
        filter_text: Optional[str] = None,
        order_by_field: Optional[OrderFieldInput] = None,
        order_direction: Optional[OrderDirectionInput] = None,
    ) -> InvestigationsOutput:
        """Investigations Search.
        Query fields accepts a CQL string (non aggregations). Use filterText for free text search.
        Max perPage Value is 100. If requesting over 100, only the first 100 will be returned..
        """
        endpoint = "investigationsSearch"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "page": prepare_input(page),
                "perPage": prepare_input(per_page),
                "query": prepare_input(query),
                "filterText": prepare_input(filter_text),
                "orderByField": prepare_input(order_by_field),
                "orderDirection": prepare_input(order_direction),
            },
            output=build_output_string(InvestigationsOutput),
        )
        if result.get(endpoint) is not None:
            return InvestigationsOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationsSearch")

    def investigations_advanced_search(self, cql: str) -> List[Dict[str, Any]]:
        """Investigations Advanced Search can perform aggregations/sorting/filtering on investigations using CQL."""
        endpoint = "investigationsAdvancedSearch"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "cql": prepare_input(cql),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query investigationsAdvancedSearch")

    def investigation_processing_status(
        self, investigation_id: str
    ) -> InvestigationProcessingResponse:
        """Get investigation processing status by id."""
        endpoint = "investigationProcessingStatus"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output=build_output_string(InvestigationProcessingResponse),
        )
        if result.get(endpoint) is not None:
            return InvestigationProcessingResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationProcessingStatus")

    def get_false_positives(self, after: str, before: str) -> Dict[str, Any]:
        """MDR - false positives widget."""
        endpoint = "getFalsePositives"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "after": prepare_input(after),
                "before": prepare_input(before),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query getFalsePositives")

    def investigations_count(self, query: Optional[str] = None) -> int:
        """Get aggregated investigations counts based on CQL query."""
        endpoint = "investigationsCount"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "query": prepare_input(query),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query investigationsCount")

    def investigations_status_count(self) -> InvestigationStatusCountResponse:
        """Get aggregated investigations status counts."""
        endpoint = "investigationsStatusCount"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(InvestigationStatusCountResponse),
        )
        if result.get(endpoint) is not None:
            return InvestigationStatusCountResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationsStatusCount")

    def export_investigations_search(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        query: Optional[str] = None,
        filter_text: Optional[str] = None,
        order_by_field: Optional[OrderFieldInput] = None,
        order_direction: Optional[OrderDirectionInput] = None,
    ) -> InvestigationsExportOutput:
        """Export investigations Search Raw Content
        Max perPage Value is 100. If requesting over 100, only the first 100 will be returned..
        """
        endpoint = "exportInvestigationsSearch"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "page": prepare_input(page),
                "perPage": prepare_input(per_page),
                "query": prepare_input(query),
                "filterText": prepare_input(filter_text),
                "orderByField": prepare_input(order_by_field),
                "orderDirection": prepare_input(order_direction),
            },
            output=build_output_string(InvestigationsExportOutput),
        )
        if result.get(endpoint) is not None:
            return InvestigationsExportOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query exportInvestigationsSearch")

    def investigation_file(self, file_id: str) -> InvestigationFile:
        """Get investigation file details."""
        endpoint = "investigationFile"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "file_id": prepare_input(file_id),
            },
            output=build_output_string(InvestigationFile),
        )
        if result.get(endpoint) is not None:
            return InvestigationFile.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationFile")

    def investigation_files(self, investigation_id: str) -> List[InvestigationFile]:
        """Get investigation files details."""
        endpoint = "investigationFiles"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output=build_output_string(InvestigationFile),
        )
        if result.get(endpoint) is not None:
            return InvestigationFile.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query investigationFiles")

    def download_investigation_file(self, investigation_id: str, file_id: str) -> str:
        """Presigned URL to Download investigation file."""
        endpoint = "downloadInvestigationFile"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "file_id": prepare_input(file_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query downloadInvestigationFile")

    def investigations_by_session(
        self,
        session_id: str,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> List[Investigation]:
        """Get investigations by multi-tenant session
        DO NOT USE, this query is unsupported. Use investigationsSearch instead.
        Max perPage Value is 100. If requesting over 100, only the first 100 will be returned..
        """
        endpoint = "investigationsBySession"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "session_id": prepare_input(session_id),
                "page": prepare_input(page),
                "perPage": prepare_input(per_page),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query investigationsBySession")

    def get_handoff_investigations(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        include_threat_hunt_types_only: Optional[bool] = None,
        exclude_threat_hunt_types: Optional[bool] = None,
    ) -> InvestigationsOutput:
        """Return list of Investigations which are handed off at least once for the the given dates and status
        Max perPage Value is 100. If requesting over 100, only the first 100 will be returned..
        """
        endpoint = "getHandoffInvestigations"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "page": prepare_input(page),
                "perPage": prepare_input(per_page),
                "createdAfter": prepare_input(created_after),
                "createdBefore": prepare_input(created_before),
                "includeThreatHuntTypesOnly": prepare_input(
                    include_threat_hunt_types_only
                ),
                "excludeThreatHuntTypes": prepare_input(exclude_threat_hunt_types),
            },
            output=build_output_string(InvestigationsOutput),
        )
        if result.get(endpoint) is not None:
            return InvestigationsOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getHandoffInvestigations")

    def investigation_types(self) -> List[InvestigationKeyValuePair]:
        """Return investigation types list based on user."""
        endpoint = "investigationTypes"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(InvestigationKeyValuePair),
        )
        if result.get(endpoint) is not None:
            return InvestigationKeyValuePair.schema().load(
                result.get(endpoint), many=True
            )
        raise GraphQLNoRowsInResultSetError("for query investigationTypes")

    def investigation_status_list(self) -> List[InvestigationKeyValuePair]:
        """Return investigation status static list."""
        endpoint = "investigationStatusList"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(InvestigationKeyValuePair),
        )
        if result.get(endpoint) is not None:
            return InvestigationKeyValuePair.schema().load(
                result.get(endpoint), many=True
            )
        raise GraphQLNoRowsInResultSetError("for query investigationStatusList")

    def investigation_priority_list(self) -> List[InvestigationKeyValuePair]:
        """Return investigation priority static list."""
        endpoint = "investigationPriorityList"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(InvestigationKeyValuePair),
        )
        if result.get(endpoint) is not None:
            return InvestigationKeyValuePair.schema().load(
                result.get(endpoint), many=True
            )
        raise GraphQLNoRowsInResultSetError("for query investigationPriorityList")

    def investigation_timeline(
        self, arguments: InvestigationTimelineArguments
    ) -> InvestigationTimeline:
        """Return investigation timeline."""
        endpoint = "investigationTimeline"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationTimeline),
        )
        if result.get(endpoint) is not None:
            return InvestigationTimeline.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationTimeline")

    def investigation_entities(
        self, arguments: InvestigationEntitiesArguments
    ) -> InvestigationEntities:
        """Get an investigation by id."""
        endpoint = "investigationEntities"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(InvestigationEntities),
        )
        if result.get(endpoint) is not None:
            return InvestigationEntities.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query investigationEntities")
