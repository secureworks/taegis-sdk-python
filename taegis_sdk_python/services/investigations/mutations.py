"""Investigations Mutation."""
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
from taegis_sdk_python.services.investigations.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.investigations import InvestigationsService

log = logging.getLogger(__name__)


class TaegisSDKInvestigationsMutation:
    """Taegis Investigations Mutation operations."""

    def __init__(self, service: InvestigationsService):
        self.service = service

    def create_investigation(self, investigation: InvestigationInput) -> Investigation:
        """Create new investigation."""
        endpoint = "createInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the createInvestigationV2 mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation": prepare_input(investigation),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createInvestigation")

    def update_investigation(
        self, investigation_id: str, investigation: UpdateInvestigationInput
    ) -> Investigation:
        """Update investigation."""
        endpoint = "updateInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the updateInvestigationV2 mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "investigation": prepare_input(investigation),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateInvestigation")

    def archive_investigation(self, investigation_id: str) -> Investigation:
        """Archive investigation."""
        endpoint = "archiveInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the archiveInvestigationV2 mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation archiveInvestigation")

    def bulk_archive_investigations(self, ids: List[str]) -> List[str]:
        """Bulk Archive Investigations."""
        endpoint = "bulkArchiveInvestigations"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the archiveInvestigationsV2 mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation bulkArchiveInvestigations")

    def un_archive_investigation(self, investigation_id: str) -> Investigation:
        """UnArchive Investigation."""
        endpoint = "unArchiveInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the unarchiveInvestigationV2 mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation unArchiveInvestigation")

    def bulk_un_archive_investigations(self, ids: List[str]) -> List[str]:
        """Bulk UnArchive Investigations."""
        endpoint = "bulkUnArchiveInvestigations"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the unarchiveInvestigationsV2 mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation bulkUnArchiveInvestigations")

    def create_activity_log_for_investigation(
        self, investigation_id: str, activity_log: ActivityLogInput
    ) -> ActivityLog:
        """Create a new activity log for investigation."""
        endpoint = "createActivityLogForInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Not Supported - Use audit logs'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "activityLog": prepare_input(activity_log),
            },
            output=build_output_string(ActivityLog),
        )
        if result.get(endpoint) is not None:
            return ActivityLog.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation createActivityLogForInvestigation"
        )

    def add_assets_to_investigation(
        self, investigation_id: str, assets: List[str]
    ) -> Investigation:
        """Add assets to investigation."""
        endpoint = "addAssetsToInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "assets": prepare_input(assets),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation addAssetsToInvestigation")

    def add_events_to_investigation(
        self, investigation_id: str, events: List[str]
    ) -> Investigation:
        """Add events to investigation."""
        endpoint = "addEventsToInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "events": prepare_input(events),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation addEventsToInvestigation")

    def add_alerts_to_investigation(
        self, investigation_id: str, alerts: List[str]
    ) -> Investigation:
        """Add alerts to investigation."""
        endpoint = "addAlertsToInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "alerts": prepare_input(alerts),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation addAlertsToInvestigation")

    def add_genesis_events_to_investigation(
        self, investigation_id: str, genesis_events: List[str]
    ) -> Investigation:
        """Add genesis events to investigation."""
        endpoint = "addGenesisEventsToInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "genesis_events": prepare_input(genesis_events),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation addGenesisEventsToInvestigation"
        )

    def add_genesis_alerts_to_investigation(
        self, investigation_id: str, genesis_alerts: List[str]
    ) -> Investigation:
        """Add genesis alerts to investigation."""
        endpoint = "addGenesisAlertsToInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "genesis_alerts": prepare_input(genesis_alerts),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation addGenesisAlertsToInvestigation"
        )

    def add_auth_credentials_to_investigation(
        self, investigation_id: str, auth_credentials: List[str]
    ) -> Investigation:
        """Add auth credentials to investigation."""
        endpoint = "addAuthCredentialsToInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "auth_credentials": prepare_input(auth_credentials),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation addAuthCredentialsToInvestigation"
        )

    def add_search_queries_to_investigation(
        self, investigation_id: str, search_queries: List[str]
    ) -> Investigation:
        """Add search queries to investigation."""
        endpoint = "addSearchQueriesToInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "search_queries": prepare_input(search_queries),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation addSearchQueriesToInvestigation"
        )

    def add_access_vector(
        self,
        investigation_id: str,
        vector_name: str,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ) -> AccessVector:
        """Access Vectors."""
        endpoint = "addAccessVector"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Not currently supported and may not be supported in the future.'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "vectorName": prepare_input(vector_name),
                "created_at": prepare_input(created_at),
                "updated_at": prepare_input(updated_at),
            },
            output=build_output_string(AccessVector),
        )
        if result.get(endpoint) is not None:
            return AccessVector.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation addAccessVector")

    def remove_access_vector(self, id_: str) -> AccessVector:
        """None."""
        endpoint = "removeAccessVector"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Not currently supported and may not be supported in the future.'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(AccessVector),
        )
        if result.get(endpoint) is not None:
            return AccessVector.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation removeAccessVector")

    def remove_assets_from_investigation(
        self, investigation_id: str, assets: List[str]
    ) -> Investigation:
        """Remove assets from investigation."""
        endpoint = "removeAssetsFromInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the removeEvidenceFromInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "assets": prepare_input(assets),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation removeAssetsFromInvestigation"
        )

    def remove_events_from_investigation(
        self, investigation_id: str, events: List[str]
    ) -> Investigation:
        """Remove events from investigation."""
        endpoint = "removeEventsFromInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the removeEvidenceFromInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "events": prepare_input(events),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation removeEventsFromInvestigation"
        )

    def remove_alerts_from_investigation(
        self, investigation_id: str, alerts: List[str]
    ) -> Investigation:
        """Remove alerts from investigation."""
        endpoint = "removeAlertsFromInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the removeEvidenceFromInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "alerts": prepare_input(alerts),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation removeAlertsFromInvestigation"
        )

    def remove_search_queries_from_investigation(
        self, investigation_id: str, search_queries: List[str]
    ) -> Investigation:
        """Remove search queries from investigation."""
        endpoint = "removeSearchQueriesFromInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the removeEvidenceFromInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "search_queries": prepare_input(search_queries),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation removeSearchQueriesFromInvestigation"
        )

    def add_bulk_alerts_to_investigation(
        self,
        search_query: str,
        investigation_id: Optional[str] = None,
        new_investigation: Optional[InvestigationInput] = None,
    ) -> Investigation:
        """Bulk add alerts to an investigation using restdb search query."""
        endpoint = "addBulkAlertsToInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "new_investigation": prepare_input(new_investigation),
                "search_query": prepare_input(search_query),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation addBulkAlertsToInvestigation")

    def add_bulk_alerts2_to_investigation(
        self, new_investigation: InvestigationInput, cql: str
    ) -> Investigation:
        """Bulk add alerts2 to an new investigation using cql query."""
        endpoint = "addBulkAlerts2ToInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "new_investigation": prepare_input(new_investigation),
                "cql": prepare_input(cql),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation addBulkAlerts2ToInvestigation"
        )

    def add_bulk_alerts2_to_existing_investigation(
        self, investigation_id: str, cql: str
    ) -> Investigation:
        """Bulk add alerts2 to an existing investigation using cql query."""
        endpoint = "addBulkAlerts2ToExistingInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the addEvidenceToInvestigation mutation'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "cql": prepare_input(cql),
            },
            output=build_output_string(Investigation),
        )
        if result.get(endpoint) is not None:
            return Investigation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation addBulkAlerts2ToExistingInvestigation"
        )

    def re_process_investigation_background_job(
        self, investigation_id: str, process_only_events: Optional[bool] = None
    ) -> InvestigationProcessingResponse:
        """Reprocess investigation background job by id."""
        endpoint = "reProcessInvestigationBackgroundJob"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "process_only_events": prepare_input(process_only_events),
            },
            output=build_output_string(InvestigationProcessingResponse),
        )
        if result.get(endpoint) is not None:
            return InvestigationProcessingResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation reProcessInvestigationBackgroundJob"
        )

    def delete_investigation(self, investigation_id: str) -> str:
        """Hard delete of investigation (Supported only in development environments)."""
        endpoint = "deleteInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Not supported - deleting investigations is not allowed'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation deleteInvestigation")

    def acknowledge_investigation(self, investigation_id: str) -> str:
        """Update state_transitions table to acknowledge if current state is handoff, without changing the investigation itself."""
        endpoint = "acknowledgeInvestigation"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the investigationV2 query'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation acknowledgeInvestigation")

    def file_upload(self, input_: FileUploadInput) -> InvestigationFile:
        """Upload File for an investigation."""
        endpoint = "fileUpload"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the initInvestigationFileUpload query'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(InvestigationFile),
        )
        if result.get(endpoint) is not None:
            return InvestigationFile.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation fileUpload")

    def delete_file(self, investigation_id: str, file_id: str) -> bool:
        """Delete investigation files from S3 bucket."""
        endpoint = "deleteFile"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the deleteInvestigationFile query'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "file_id": prepare_input(file_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation deleteFile")

    def init_file_upload(self, input_: FileUploadRequest) -> FileUploadResponse:
        """Initialize file upload to get Presigned URL to upload file."""
        endpoint = "initFileUpload"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Use the initInvestigationFileUpload query'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(FileUploadResponse),
        )
        if result.get(endpoint) is not None:
            return FileUploadResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation initFileUpload")

    def update_file_status(
        self, investigation_id: str, file_id: str, status: str
    ) -> InvestigationFile:
        """Update investigation file  status."""
        endpoint = "updateFileStatus"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'No longer supported, migrate to the InvestigationsV2-API'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "investigation_id": prepare_input(investigation_id),
                "file_id": prepare_input(file_id),
                "status": prepare_input(status),
            },
            output=build_output_string(InvestigationFile),
        )
        if result.get(endpoint) is not None:
            return InvestigationFile.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateFileStatus")
