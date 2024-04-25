"""Exports Mutation."""
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
from taegis_sdk_python.services.exports.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.exports import ExportsService

log = logging.getLogger(__name__)


class TaegisSDKExportsMutation:
    """Taegis Exports Mutation operations."""

    def __init__(self, service: ExportsService):
        self.service = service

    def new_export(self, input_: NewExportInput) -> Export:
        """None."""
        endpoint = "newExport"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Migration to V2 backend; Use 'createReportSpecV2''"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Export),
        )
        if result.get(endpoint) is not None:
            return Export.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation newExport")

    def cancel_export(self, input_: str) -> Export:
        """None."""
        endpoint = "cancelExport"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Migration to V2 backend; Use 'cancelReportArtifactV2''"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Export),
        )
        if result.get(endpoint) is not None:
            return Export.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation cancelExport")

    def delete_export(self, id_: str) -> Export:
        """None."""
        endpoint = "deleteExport"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Migration to V2 backend; Use 'deleteReportArtifactV2''"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Export),
        )
        if result.get(endpoint) is not None:
            return Export.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteExport")

    def retry_export(self, id_: str) -> Export:
        """None."""
        endpoint = "retryExport"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'Migration to V2 backend; Use 'retryReportArtifactV2''"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Export),
        )
        if result.get(endpoint) is not None:
            return Export.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation retryExport")

    def schedule_report(self, input_: NewScheduleInput) -> Schedule:
        """None."""
        endpoint = "scheduleReport"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Schedule),
        )
        if result.get(endpoint) is not None:
            return Schedule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation scheduleReport")

    def delete_schedule(self, id_: str) -> Schedule:
        """None."""
        endpoint = "deleteSchedule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Schedule),
        )
        if result.get(endpoint) is not None:
            return Schedule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteSchedule")

    def edit_schedule(self, edits: ScheduleEditInput) -> Schedule:
        """None."""
        endpoint = "editSchedule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "edits": prepare_input(edits),
            },
            output=build_output_string(Schedule),
        )
        if result.get(endpoint) is not None:
            return Schedule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation editSchedule")

    def report_from_schedule(
        self,
        id_: str,
        run_at: str,
        manual_run: Optional[bool] = None,
        timeframe: Optional[ReportTimeframeInput] = None,
    ) -> Report:
        """None."""
        endpoint = "reportFromSchedule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "runAt": prepare_input(run_at),
                "manualRun": prepare_input(manual_run),
                "timeframe": prepare_input(timeframe),
            },
            output=build_output_string(Report),
        )
        if result.get(endpoint) is not None:
            return Report.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation reportFromSchedule")

    def attach_export_to_report(self, id_: str, export_id: str) -> Report:
        """None."""
        endpoint = "attachExportToReport"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "exportID": prepare_input(export_id),
            },
            output=build_output_string(Report),
        )
        if result.get(endpoint) is not None:
            return Report.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation attachExportToReport")

    def retry_report(self, id_: str) -> Report:
        """None."""
        endpoint = "retryReport"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Report),
        )
        if result.get(endpoint) is not None:
            return Report.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation retryReport")

    def archive_report(self, id_: str) -> Report:
        """None."""
        endpoint = "archiveReport"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Report),
        )
        if result.get(endpoint) is not None:
            return Report.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation archiveReport")

    def unarchive_report(self, id_: str) -> Report:
        """None."""
        endpoint = "unarchiveReport"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Report),
        )
        if result.get(endpoint) is not None:
            return Report.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation unarchiveReport")

    def delete_report(self, id_: str) -> Report:
        """None."""
        endpoint = "deleteReport"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Report),
        )
        if result.get(endpoint) is not None:
            return Report.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteReport")

    def delete_reports(self, report_ids: List[str]) -> List[Report]:
        """None."""
        endpoint = "deleteReports"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "reportIDs": prepare_input(report_ids),
            },
            output=build_output_string(Report),
        )
        if result.get(endpoint) is not None:
            return Report.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation deleteReports")

    def pause_schedule(self, schedule_id: str) -> Schedule:
        """None."""
        endpoint = "pauseSchedule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "scheduleID": prepare_input(schedule_id),
            },
            output=build_output_string(Schedule),
        )
        if result.get(endpoint) is not None:
            return Schedule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation pauseSchedule")

    def resume_schedule(self, schedule_id: str) -> Schedule:
        """None."""
        endpoint = "resumeSchedule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "scheduleID": prepare_input(schedule_id),
            },
            output=build_output_string(Schedule),
        )
        if result.get(endpoint) is not None:
            return Schedule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation resumeSchedule")

    def create_exports_zip(
        self, name: str, exports_input: List[NewExportInput]
    ) -> Export:
        """None."""
        endpoint = "createExportsZip"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "name": prepare_input(name),
                "exportsInput": prepare_input(exports_input),
            },
            output=build_output_string(Export),
        )
        if result.get(endpoint) is not None:
            return Export.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createExportsZip")

    def manually_run_report_from_schedule(
        self, input_: NewReportFromSchedule
    ) -> Report:
        """None."""
        endpoint = "manuallyRunReportFromSchedule"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Report),
        )
        if result.get(endpoint) is not None:
            return Report.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation manuallyRunReportFromSchedule"
        )

    def attach_export_to_report_v2(self, input_: AttachExportToReportInput) -> Report:
        """None."""
        endpoint = "attachExportToReportV2"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Report),
        )
        if result.get(endpoint) is not None:
            return Report.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation attachExportToReportV2")

    def unsubscribe(self, schedule_id: str) -> Unsubscription:
        """None."""
        endpoint = "unsubscribe"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "scheduleID": prepare_input(schedule_id),
            },
            output=build_output_string(Unsubscription),
        )
        if result.get(endpoint) is not None:
            return Unsubscription.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation unsubscribe")

    def resubscribe(self, schedule_id: str) -> Schedule:
        """None."""
        endpoint = "resubscribe"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "scheduleID": prepare_input(schedule_id),
            },
            output=build_output_string(Schedule),
        )
        if result.get(endpoint) is not None:
            return Schedule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation resubscribe")

    def share_with_users(self, schedule_id: str, user_ids: List[str]) -> Schedule:
        """None."""
        endpoint = "shareWithUsers"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "scheduleID": prepare_input(schedule_id),
                "userIDs": prepare_input(user_ids),
            },
            output=build_output_string(Schedule),
        )
        if result.get(endpoint) is not None:
            return Schedule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation shareWithUsers")

    def unshare_with_users(self, schedule_id: str, user_ids: List[str]) -> Schedule:
        """None."""
        endpoint = "unshareWithUsers"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "scheduleID": prepare_input(schedule_id),
                "userIDs": prepare_input(user_ids),
            },
            output=build_output_string(Schedule),
        )
        if result.get(endpoint) is not None:
            return Schedule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation unshareWithUsers")
