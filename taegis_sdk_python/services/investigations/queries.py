import inspect
from typing import List, Optional, Tuple, Union

from .enums import (
    InvestigationStatusEnum,
    OrderDirectionInput,
    OrderFieldInput
)
# noinspection PyUnusedLocal
from .types import (
    Alert,
    Count,
    Event,
    Investigation,
    InvestigationAlertOutput,
    InvestigationAssetOutput, InvestigationBulkResponse, InvestigationEventOutput, InvestigationProcessingResponse,
    InvestigationsExportOutput,
    InvestigationsOutput,
    InvestigationStatusCountResponse,
    InvestigationSummary,
    SearchQuery,
    SummaryGroup,
    TimeSummaryForGroup
)
from ... import GraphQLNoRowsInResultSetError, ServiceCore
from ...utils import get_args_from_frame


class InvestigationQuery:
    def __init__(self, service: ServiceCore):
        self._service = service

    def get_investigation_summary(self) -> Tuple[List[dict], List[InvestigationSummary]]:
        """
        Get summary of investigations (tag and counts for each tag)
        """
        query_name = "investigationSummary"
        self._service.caller = inspect.currentframe().f_code.co_name
        results = self._service.execute_gql_query(
            gql_name=query_name
        )
        if results is not None:
            return results, [InvestigationSummary(**item) for item in results]
        raise GraphQLNoRowsInResultSetError("for query investigationSummary")

    def get_investigation_by_id(
            self, investigation_id: Optional[str] = None
    ) -> Tuple[dict, Investigation]:
        """ Get an investigation by id
        :param investigation_id: the investigation id
        """
        self._service.caller = inspect.currentframe().f_code.co_name
        result = self._service.execute_gql_query(
            "investigation",
            investigation_id=investigation_id
        )
        if result:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query investigation")

    def get_all_investigations(
            self,
            status: Optional[Union[List[InvestigationStatusEnum], List[str]]] = None,
            page: Optional[int] = None,
            per_page: Optional[int] = None,
            created_after: Optional[str] = None,
            created_before: Optional[str] = None,
            updated_after: Optional[str] = None,
            updted_before: Optional[str] = None,
            order_by_field: Optional[OrderFieldInput] = None,
            order_direction: Optional[OrderDirectionInput] = None,
            is_deleted: Optional[bool] = None,
            hide_threat_hunting_investigations: Optional[bool] = None
    ) -> Tuple[List[dict], List[Investigation]]:
        """ Get All Investigations

        :param status: a list of requested statuses - InvestigationStatusEnum
        :param page: the page number ( server paging )
        :param per_page: number of records per page
        :param created_after: a utc time offset e.g. 2020-10-24T03:28:41Z
        :param created_before: a utc time offset e.g. 2020-10-24T03:28:41Z
        :param updated_after: a utc time offset e.g. 2020-10-24T03:28:41Z
        :param updted_before: a utc time offset e.g. 2020-10-24T03:28:41Z
        :param order_by_field: a enum value from OrderFieldInput
        :param order_direction: required if 'order_by_field' supplied. a value from OrderDirectionInput
        :param is_deleted: flag for the deleted_at field
        :param hide_threat_hunting_investigations: boolean argument
        """
        query_name = "allInvestigations"
        self._service.caller = inspect.currentframe().f_code.co_name
        if status and all(isinstance(s, InvestigationStatusEnum) for s in status):
            status = InvestigationStatusEnum.as_value_list(*status)

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        results = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if results is not None:
            return results, [Investigation(item) for item in results]
        raise GraphQLNoRowsInResultSetError("for query allInvestigations")

    def get_investigation_count_over_time(
            self,
            transition_status: Optional[str] = None,
            after: Optional[str] = None,
            before: Optional[str] = None
    ) -> Tuple[dict, Count]:
        """
        Get the number of investigations created during a given time frame.
        Can optionally pass in a desired 'transition_status' (handoff, acknowledge, resolution)
        :param transition_status: (handoff, acknowledge, resolution)
        :param after: a utc time offset e.g. 2020-10-24T03:28:41Z
        :param before: a utc time offset e.g. 2020-10-24T03:28:41Z
        """
        query_name = "investigationCountOverTime"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if result is not None:
            return result, Count(**result)
        raise GraphQLNoRowsInResultSetError("for query investigationCountOverTime")

    def get_meantime_summary_over_period(
            self,
            after: Optional[str] = None,
            before: Optional[str] = None
    ) -> Tuple[dict, TimeSummaryForGroup]:
        """
        Get the average times it took to hand off, acknowledge,
        and resolve all investigations over the course of the period
        :param after: a utc time offset e.g. 2020-10-24T03:28:41Z
        :param before: a utc time offset e.g. 2020-10-24T03:28:41Z
        """
        query_name = "meanTimeSummaryOverPeriod"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if result is not None:
            return result, TimeSummaryForGroup(result)
        raise GraphQLNoRowsInResultSetError("for query meanTimeSummaryOverPeriod")

    def investigation_assets(
            self, investigation_id: Optional[str] = None,
            page: Optional[int] = None,
            per_page: Optional[int] = None
    ) -> Tuple[dict, InvestigationAssetOutput]:
        query_name = "investigationAssets"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if result is not None:
            return result, InvestigationAssetOutput(result)
        raise GraphQLNoRowsInResultSetError("for query investigationAssets")

    def get_investigation_events(
            self, investigation_id: Optional[str] = None
    ) -> Tuple[List[dict], InvestigationEventOutput]:
        """
        Get investigation events by investigation id
        :param investigation_id: the investigation id
        """
        self._service.caller = inspect.currentframe().f_code.co_name
        result = self._service.execute_gql_query(
            "investigationEvents",
            investigation_id=investigation_id
        )
        if result is not None:
            return result, InvestigationEventOutput(result)
        raise GraphQLNoRowsInResultSetError("for query investigationEvents")

    def get_investigation_alerts(
            self,
            investigation_id: Optional[str] = None,
            page: Optional[int] = None,
            per_page: Optional[int] = None,
            filter_query: Optional[str] = None,
            order_by_field: Optional[OrderFieldInput] = None,
            order_direction: Optional[OrderDirectionInput] = None
    ) -> Tuple[dict, InvestigationAlertOutput]:
        query_name = "investigationAlerts"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if result is not None:
            return result, InvestigationAlertOutput(result)
        raise GraphQLNoRowsInResultSetError("for query investigationAlerts")

    def get_investigation_genesis_events(
            self, investigation_id: Optional[str] = None
    ) -> Tuple[List[dict], List[Event]]:
        """
        Get investigation genesis events by investigation id
        :param investigation_id: the investigation id
        """
        self._service.caller = inspect.currentframe().f_code.co_name
        results = self._service.execute_gql_query(
            "investigationGenesisEvents",
            investigation_id=investigation_id
        )
        if results is not None:
            return results, [Event(id=item.get("id")) for item in results]
        raise GraphQLNoRowsInResultSetError("for query investigationGenesisEvents")

    def get_investigation_genesis_alerts(
            self, investigation_id: Optional[str] = None
    ) -> Tuple[List[dict], List[Alert]]:
        self._service.caller = inspect.currentframe().f_code.co_name
        results = self._service.execute_gql_query(
            "investigationGenesisAlerts",
            investigation_id=investigation_id
        )
        if results is not None:
            return results, [Alert(id=item.get("id")) for item in results]
        raise GraphQLNoRowsInResultSetError("for query investigationGenesisAlerts")

    def get_investigation_auth_credentials(
            self, investigation_id: Optional[str] = None
    ) -> List[str]:
        """ Get investigation auth credentials by investigation id
        :param investigation_id: the investigation id
        """
        self._service.caller = inspect.currentframe().f_code.co_name
        result = self._service.execute_gql_query(
            "investigationAuthCredentials",
            investigation_id=investigation_id
        )

        if result is not None:
            return result
        raise GraphQLNoRowsInResultSetError("for query investigationAuthCredentials")

    def get_investigation_search_queries(
        self, investigation_id: Optional[str] = None
    ) -> Tuple[List[dict], List[SearchQuery]]:
        """ Get investigation search queries by investigation id
        :param investigation_id: the investigation id
        """
        self._service.caller = inspect.currentframe().f_code.co_name
        result = self._service.execute_gql_query(
            "investigationSearchQueries",
            investigation_id=investigation_id
        )

        if result is not None:
            return result, [SearchQuery(id=item.get("id")) for item in result]
        raise GraphQLNoRowsInResultSetError("for query investigationSearchQueries")

    def investigations_bulk_events_alerts(
            self, query_strings: Optional[str] = None
    ) -> Tuple[List[dict], List[InvestigationBulkResponse]]:
        query_name = "investigationsBulkEventsAlerts"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if InvestigationBulkResponse is not None:
            return result, [InvestigationBulkResponse(item) for item in result]
        raise GraphQLNoRowsInResultSetError("for query investigationsBulkEventsAlerts")

    def investigations_bulk_update_alerts(self) -> str:
        """
        Updates Investigation Alerts and Investigation information from Alerts (ie Access Vectors)
        """
        self._service.caller = inspect.currentframe().f_code.co_name
        response = self._service.execute_gql_query(
            "investigationsBulkUpdateAlerts"
        )

        if isinstance(response, str):
            return response

    def get_investigation_status_summary(
            self, updated_after: Optional[str] = None, updated_before: Optional[str] = None
    ) -> Tuple[List[dict], List[SummaryGroup]]:
        query_name = "investigationStatusSummary"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        results = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if results is not None:
            return results, list(map(lambda x: SummaryGroup(**x), results))
        raise GraphQLNoRowsInResultSetError("for query investigationStatusSummary")

    def investigations_search(
            self,
            page: Optional[int] = None,
            per_page: Optional[int] = None,
            query: Optional[str] = None,
            filter_text: Optional[str] = None,
            order_by_field: Optional[OrderFieldInput] = None,
            order_direction: Optional[OrderDirectionInput] = None,
    ) -> Tuple[dict, InvestigationsOutput]:
        query_name = "investigationsSearch"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if result is not None:
            return result, InvestigationsOutput(result)
        raise GraphQLNoRowsInResultSetError("for query investigationsSearch")

    def get_investigation_processing_status(
            self, investigation_id: Optional[str] = None
    ) -> Tuple[dict, InvestigationProcessingResponse]:
        """ Get investigation processing status by id
        :param investigation_id: the investigation id
        """
        self._service.caller = inspect.currentframe().f_code.co_name
        result = self._service.execute_gql_query(
            "investigationProcessingStatus",
            investigation_id=investigation_id
        )

        if result:
            return result, InvestigationProcessingResponse(result)
        raise GraphQLNoRowsInResultSetError("for query investigationProcessingStatus")

    def get_false_positives(
            self, after: Optional[str] = None, before: Optional[str] = None
    ) -> dict:
        query_name = "getFalsePositives"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if result is not None:
            return result
        raise GraphQLNoRowsInResultSetError("for query getFalsePositives")

    def get_investigations_count(self, query: Optional[str] = None) -> int:
        """
        Get aggregated investigations counts based on CQL query
        :param query: cql query
        """
        query_name = "investigationsCount"
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        return int(result)

    def get_investigations_status_count(self) -> Tuple[dict, InvestigationStatusCountResponse]:
        """
        Get aggregated investigations status counts
        """
        query_name = "investigationsStatusCount"
        self._service.caller = inspect.currentframe().f_code.co_name

        result = self._service.execute_gql_query(
            gql_name=query_name
        )
        if result is not None:
            return result, InvestigationStatusCountResponse(**result)
        raise GraphQLNoRowsInResultSetError("for query investigationsStatusCount")

    def export_investigations_search(
            self,
            page: Optional[int] = None,
            per_page: Optional[int] = None,
            query: Optional[str] = None,
            filter_text: Optional[str] = None,
            order_by_field: Optional[OrderFieldInput] = None,
            order_direction: Optional[OrderDirectionInput] = None,
    ) -> Tuple[dict, InvestigationsExportOutput]:
        """
        Export investigations Search Raw Content
        :param page: the page number ( server paging )
        :param per_page: number of records per page
        :param query: a search query
        :param filter_text: a filter text
        :param order_by_field: a enum value from OrderFieldInput
        :param order_direction: required if 'order_by_field' supplied. a value from OrderDirectionInput
        """
        query_name = "exportInvestigationsSearch"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_query(
            gql_name=query_name,
            **arguments
        )
        if result is not None:
            return result, InvestigationsExportOutput(result)
        raise GraphQLNoRowsInResultSetError("for query exportInvestigationsSearch")
