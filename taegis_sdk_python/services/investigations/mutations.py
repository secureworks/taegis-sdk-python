import inspect
from typing import List, Optional, Tuple

from taegis_sdk_python import GraphQLNoRowsInResultSetError, ServiceCore
from taegis_sdk_python.services.investigations.types import (
    AccessVector,
    ActivityLog,
    ActivityLogInput,
    Investigation,
    InvestigationInput,
    InvestigationProcessingResponse,
    SnowCredentials,
    UpdateInvestigationInput
)
from taegis_sdk_python.utils import get_args_from_frame


# noinspection PyUnusedLocal
class InvestigationMutation:
    def __init__(self, service: ServiceCore):
        self._service = service

    def create_investigation(
            self, investigation: Optional[InvestigationInput] = None
    ) -> Tuple[dict, Investigation]:
        """ Create new investigation """
        mutation_name = "createInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query createInvestigation")

    def delete_investigation(
            self, investigation_id: Optional[str] = None
    ) -> Tuple[dict, Investigation]:
        """
        Delete investigation
        :param investigation_id: the investigation id
        """
        mutation_name = "deleteInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query deleteInvestigation")

    def update_investigation(
            self, investigation_id: Optional[str] = None,
            investigation: Optional[UpdateInvestigationInput] = None
    ) -> Tuple[dict, Investigation]:
        """
        Update investigation
        :param investigation_id: the investigation id to update
        :param investigation: the investigation arguments
        """
        mutation_name = "updateInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query updateInvestigation")

    def bulk_delete_investigations(
            self, ids: Optional[List[str]] = None
    ) -> List[str]:
        """
        Bulk Delete Investigations
        :param ids: a list of investigations id's
        """
        mutation_name = "bulkDeleteInvestigations"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result
        raise GraphQLNoRowsInResultSetError("for query bulkDeleteInvestigations")

    def bulk_restore_investigations(
            self, ids: Optional[List[str]] = None
    ) -> List[str]:
        """
        Bulk Restore Investigations
        :param ids: a list of investigations id's
        """
        mutation_name = "bulkRestoreInvestigations"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result
        raise GraphQLNoRowsInResultSetError("for query bulkRestoreInvestigations")

    def create_activity_log_for_investigation(
            self, investigation_id: Optional[str] = None,
            activity_log: Optional[ActivityLogInput] = None
    ) -> Tuple[dict, ActivityLog]:
        """
        Create a new activity log for investigation
        :param investigation_id:
        :param activity_log:
        """
        mutation_name = "createActivityLogForInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, ActivityLog(result)
        raise GraphQLNoRowsInResultSetError("for query createActivityLogForInvestigation")

    def add_genesis_alerts_to_investigation(
            self, investigation_id: Optional[str] = None, genesis_alerts: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Add genesis alerts to investigation
        :param investigation_id: the investigation id
        :param genesis_alerts: a list of genesis alerts to add
        """
        mutation_name = "addGenesisAlertsToInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query addGenesisAlertsToInvestigation")

    def add_alerts_to_investigation(
            self, investigation_id: Optional[str] = None, alerts: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Add alerts to investigation
        :param investigation_id: the investigation id
        :param alerts: a list of alerts to add
        """
        mutation_name = "addAlertsToInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query addAlertsToInvestigation")

    def add_genesis_events_to_investigation(
            self, investigation_id: Optional[str] = None, genesis_events: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Add genesis events to investigation
        :param investigation_id: the investigation id
        :param genesis_events: a list of genesis events to add
        """
        mutation_name = "addGenesisEventsToInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query addGenesisEventsToInvestigation")

    def add_events_to_investigation(
            self, investigation_id: Optional[str] = None, events: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Add events to investigation
        :param investigation_id: the investigation id
        :param events: a list of events to add
        """
        mutation_name = "addEventsToInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query addEventsToInvestigation")

    def add_assets_to_investigation(
            self, investigation_id: Optional[str] = None, assets: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Add assets to investigation
        :param investigation_id: the investigation id
        :param assets: a list of assets to add
        """
        mutation_name = "addAssetsToInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query addAssetsToInvestigation")

    def add_auth_credentials_to_investigation(
            self, investigation_id: Optional[str] = None, auth_credentials: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Add auth_credentials to investigation
        :param investigation_id: the investigation id
        :param auth_credentials: a list of auth credentials to add
        """
        mutation_name = "addAuthCredentialsToInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query addAuthCredentialsToInvestigation")

    def add_search_queries_to_investigation(
            self, investigation_id: Optional[str] = None, search_queries: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Add search_queries to investigation
        :param investigation_id: the investigation id
        :param search_queries: a list of auth credentials to add
        """
        mutation_name = "addSearchQueriesToInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query addSearchQueriesToInvestigation")

    def add_access_vector_to_investigation(
            self, investigation_id: Optional[str] = None,
            vector_name: Optional[str] = None,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None
    ) -> Tuple[dict, AccessVector]:
        """
        Add an access vector to investigation
        :param investigation_id: the investigation id
        :param vector_name: the vector name
        :param created_at: a date representing the creation date
        :param updated_at: a date representing the updated date
        """
        mutation_name = "addAccessVector"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, AccessVector(result)
        raise GraphQLNoRowsInResultSetError("for query addAccessVector")

    def add_snow_credentials(
            self,
            url: Optional[str] = None,
            user: Optional[str] = None,
            password: Optional[str] = None
    ) -> Tuple[dict, SnowCredentials]:
        """
        Adds SNOW integration credentials for tenant
        :param url:
        :param user:
        :param password:
        """
        mutation_name = "addSnowCredentials"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, SnowCredentials(**result)
        raise GraphQLNoRowsInResultSetError("for query addSnowCredentials")

    def delete_snow_credentials(self) -> Tuple[dict, SnowCredentials]:
        """
        Deletes SNOW integration credentials for tenant
        """
        mutation_name = "deleteSnowCredentials"
        self._service.caller = inspect.currentframe().f_code.co_name
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name
        )
        if result is not None:
            return result, SnowCredentials(**result)
        raise GraphQLNoRowsInResultSetError("for query deleteSnowCredentials")

    def remove_assets_from_investigation(
            self, investigation_id: Optional[str] = None, assets: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        remove assets from investigation
        :param investigation_id: the investigation id
        :param assets: a list of assets to remove
        """
        mutation_name = "removeAssetsFromInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query removeAssetsFromInvestigation")

    def remove_events_from_investigation(
            self, investigation_id: Optional[str] = None, events: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Remove events from investigation
        :param investigation_id: the investigation id
        :param events: a list of events to remove
        """
        mutation_name = "removeEventsFromInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query removeEventsFromInvestigation")

    def remove_alerts_from_investigation(
            self, investigation_id: Optional[str] = None, alerts: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Remove alerts from investigation
        :param investigation_id: the investigation id
        :param alerts: a list of alerts to remove
        """
        mutation_name = "removeAlertsFromInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query removeAlertsFromInvestigation")

    def remove_search_queries_from_investigation(
            self, investigation_id: Optional[str] = None, search_queries: Optional[List[str]] = None
    ) -> Tuple[dict, Investigation]:
        """
        Remove search queries from investigation
        :param investigation_id: the investigation id
        :param search_queries: a list of search queries to remove
        """
        mutation_name = "removeSearchQueriesFromInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query removeSearchQueriesFromInvestigation")

    def add_bulk_alerts_to_investigation(
            self,
            investigation_id: Optional[str] = None,
            new_investigation: Optional[InvestigationInput] = None,
            search_query: Optional[str] = None
    ) -> Tuple[dict, Investigation]:
        """
        Bulk add alerts to an investigation using restdb search query
        :param investigation_id: the current investigation id
        :param new_investigation: the new investigation information
        :param search_query: a search query
        """
        mutation_name = "addBulkAlertsToInvestigation"
        self._service.caller = inspect.currentframe().f_code.co_name
        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, Investigation(result)
        raise GraphQLNoRowsInResultSetError("for query addBulkAlertsToInvestigation")

    def re_process_investigation_background_job(
            self, investigation_id: Optional[str] = None
    ) -> Tuple[dict, InvestigationProcessingResponse]:
        """
        Reprocess investigation background job by id
        :param investigation_id: the investigation id
        """
        mutation_name = "reProcessInvestigationBackgroundJob"
        self._service.caller = inspect.currentframe().f_code.co_name

        frame = inspect.currentframe()
        arguments = get_args_from_frame(frame)
        result = self._service.execute_gql_mutation(
            gql_name=mutation_name,
            **arguments
        )
        if result is not None:
            return result, InvestigationProcessingResponse(result)
        raise GraphQLNoRowsInResultSetError("for query reProcessInvestigationBackgroundJob")
