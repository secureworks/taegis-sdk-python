"""Exports Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class ExportStatus(str, Enum):
    """ExportStatus."""

    SCHEDULED = "Scheduled"
    PROCESSING = "Processing"
    EXPIRED = "Expired"
    CANCELLED = "Cancelled"
    DELETED = "Deleted"
    READY = "Ready"
    ERRORED = "Errored"
    PAUSED = "Paused"


class RelativeTimeRange(str, Enum):
    """RelativeTimeRange."""

    LAST_MONTH = "LAST_MONTH"
    CURRENT_MONTH_TO_DATE = "CURRENT_MONTH_TO_DATE"


class ExportType(str, Enum):
    """ExportType."""

    CSV = "CSV"
    JSON = "JSON"
    ZIP = "ZIP"


class ReportChartType(str, Enum):
    """ReportChartType."""

    VERTICAL_BAR = "VERTICAL_BAR"
    STACKED_VERTICAL_BAR = "STACKED_VERTICAL_BAR"
    HORIZONTAL_BAR = "HORIZONTAL_BAR"
    STACKED_HORIZONTAL_BAR = "STACKED_HORIZONTAL_BAR"
    LINE = "LINE"
    AREA = "AREA"
    SCATTERPLOT = "SCATTERPLOT"
    PIE = "PIE"
    DATA_TABLE = "DATA_TABLE"
    CSV = "CSV"
    OTHER = "OTHER"
    EXECUTIVE = "EXECUTIVE"
    DASHBOARD = "DASHBOARD"
    DATASOURCETRENDING = "DATASOURCETRENDING"
    ALERT_SUMMARY = "ALERT_SUMMARY"
    INVESTIGATION_SUMMARY = "INVESTIGATION_SUMMARY"
    USER_ADMINISTRATION = "USER_ADMINISTRATION"
    INVESTIGATION_REPORT = "INVESTIGATION_REPORT"
    ISENSOR_REPORT = "ISENSOR_REPORT"
    PERFORMANCE_SUMMARY_REPORT = "PERFORMANCE_SUMMARY_REPORT"


class ReportType(str, Enum):
    """ReportType."""

    STANDARD = "STANDARD"
    DASHBOARD = "DASHBOARD"
    PREDEFINED = "PREDEFINED"
    INVESTIGATION = "INVESTIGATION"


class Cadence(str, Enum):
    """Cadence."""

    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    ONCE = "Once"
    ANNUALLY = "Annually"
    OTHER = "Other"


class SchedulesSortBy(str, Enum):
    """SchedulesSortBy."""

    ID = "id"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    NAME = "name"
    STATUS = "status"
    DESCRIPTION = "description"
    CADENCE = "cadence"
    LAST_RUN = "last_run"
    FIRST_RUN = "first_run"
    REDQL_QUERY = "redql_query"
    CREATOR = "creator"


class ReportsSortBy(str, Enum):
    """ReportsSortBy."""

    ID = "id"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    RUN_AT = "run_at"
    RUN_FROM = "run_from"
    REPORT_STATUS = "report_status"
    EXPORT_STATUS = "export_status"
    FILE_NAME = "file_name"
    FILE_SIZE = "file_size"
    FILE_REQUESTED = "file_requested"
    ERROR_DESCRIPTION = "error_description"
    GENERATED = "generated"
    CREATOR = "creator"
    SCHEDULE_ID = "schedule_id"
    SCHEDULE_NAME = "schedule_name"
    SCHEDULE_CADENCE = "schedule_cadence"


class SortOrder(str, Enum):
    """SortOrder."""

    ASC = "asc"
    DESC = "desc"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Cursor:
    """Cursor."""

    page: Optional[int] = field(default=None, metadata=config(field_name="page"))
    per_page: Optional[int] = field(default=None, metadata=config(field_name="perPage"))
    order_by: Optional[str] = field(default=None, metadata=config(field_name="OrderBy"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Visualization:
    """Visualization."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    visualization_type: Optional[str] = field(
        default=None, metadata=config(field_name="visualization_type")
    )
    source: Optional[str] = field(default=None, metadata=config(field_name="source"))
    config_: Optional[dict] = field(default=None, metadata=config(field_name="config"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VisualizationInput:
    """VisualizationInput."""

    visualization_type: Optional[str] = field(
        default=None, metadata=config(field_name="visualization_type")
    )
    source: Optional[str] = field(default=None, metadata=config(field_name="source"))
    config_: Optional[dict] = field(default=None, metadata=config(field_name="config"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ReportTimeframeInput:
    """ReportTimeframeInput."""

    begin_at: Optional[str] = field(default=None, metadata=config(field_name="beginAt"))
    end_at: Optional[str] = field(default=None, metadata=config(field_name="endAt"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Unsubscription:
    """Unsubscription."""

    user_id: Optional[str] = field(default=None, metadata=config(field_name="userID"))
    schedule_id: Optional[str] = field(
        default=None, metadata=config(field_name="scheduleID")
    )
    schedule_creator: Optional[str] = field(
        default=None, metadata=config(field_name="scheduleCreator")
    )
    schedule_name: Optional[str] = field(
        default=None, metadata=config(field_name="scheduleName")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AbsoluteTimeRedQLQueryInput:
    """AbsoluteTimeRedQLQueryInput."""

    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    reference_time: Optional[str] = field(
        default=None, metadata=config(field_name="referenceTime")
    )
    current_time: Optional[str] = field(
        default=None, metadata=config(field_name="currentTime")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AttachExportToReportInput:
    """AttachExportToReportInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    export_id: Optional[str] = field(
        default=None, metadata=config(field_name="exportID")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUser:
    """TDRUser."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NewExportInput:
    """NewExportInput."""

    dataset: Optional[str] = field(default=None, metadata=config(field_name="dataset"))
    filters: Optional[dict] = field(default=None, metadata=config(field_name="filters"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    override_user_id: Optional[str] = field(
        default=None, metadata=config(field_name="overrideUserID")
    )
    descriptive_file_name: Optional[str] = field(
        default=None, metadata=config(field_name="descriptiveFileName")
    )
    send_notification: Optional[bool] = field(
        default=None, metadata=config(field_name="sendNotification")
    )
    selected_columns: Optional[List[str]] = field(
        default=None, metadata=config(field_name="selectedColumns")
    )
    renamed_columns: Optional[dict] = field(
        default=None, metadata=config(field_name="renamedColumns")
    )
    locale: Optional[str] = field(default=None, metadata=config(field_name="locale"))
    export_type: Optional[ExportType] = field(
        default=None, metadata=config(field_name="exportType")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class QueryWithTimeRangeInput:
    """QueryWithTimeRangeInput."""

    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    reference_time: Optional[str] = field(
        default=None, metadata=config(field_name="referenceTime")
    )
    time_range: Optional[RelativeTimeRange] = field(
        default=None, metadata=config(field_name="timeRange")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NewReportFromSchedule:
    """NewReportFromSchedule."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    run_at: Optional[str] = field(default=None, metadata=config(field_name="runAt"))
    timeframe: Optional[ReportTimeframeInput] = field(
        default=None, metadata=config(field_name="timeframe")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SchedulesFilters:
    """SchedulesFilters."""

    created_before: Optional[str] = field(
        default=None, metadata=config(field_name="createdBefore")
    )
    created_after: Optional[str] = field(
        default=None, metadata=config(field_name="createdAfter")
    )
    updated_before: Optional[str] = field(
        default=None, metadata=config(field_name="updatedBefore")
    )
    updated_after: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAfter")
    )
    first_run: Optional[str] = field(
        default=None, metadata=config(field_name="firstRun")
    )
    filters: Optional[dict] = field(default=None, metadata=config(field_name="filters"))
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    red_ql_query: Optional[str] = field(
        default=None, metadata=config(field_name="redQLQuery")
    )
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    search_all: Optional[str] = field(
        default=None, metadata=config(field_name="searchAll")
    )
    sort_by: Optional[SchedulesSortBy] = field(
        default=None, metadata=config(field_name="sortBy")
    )
    sort_order: Optional[SortOrder] = field(
        default=None, metadata=config(field_name="sortOrder")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ReportsFilters:
    """ReportsFilters."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_before: Optional[str] = field(
        default=None, metadata=config(field_name="createdBefore")
    )
    created_after: Optional[str] = field(
        default=None, metadata=config(field_name="createdAfter")
    )
    updated_before: Optional[str] = field(
        default=None, metadata=config(field_name="updatedBefore")
    )
    updated_after: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAfter")
    )
    run_at_before: Optional[str] = field(
        default=None, metadata=config(field_name="runAtBefore")
    )
    run_at_after: Optional[str] = field(
        default=None, metadata=config(field_name="runAtAfter")
    )
    run_from_before: Optional[str] = field(
        default=None, metadata=config(field_name="runFromBefore")
    )
    run_from_after: Optional[str] = field(
        default=None, metadata=config(field_name="runFromAfter")
    )
    report_status: Optional[str] = field(
        default=None, metadata=config(field_name="reportStatus")
    )
    report_statuses: Optional[List[str]] = field(
        default=None, metadata=config(field_name="reportStatuses")
    )
    export_status: Optional[str] = field(
        default=None, metadata=config(field_name="exportStatus")
    )
    file_name: Optional[str] = field(
        default=None, metadata=config(field_name="fileName")
    )
    file_requested_before: Optional[str] = field(
        default=None, metadata=config(field_name="fileRequestedBefore")
    )
    file_requested_after: Optional[str] = field(
        default=None, metadata=config(field_name="fileRequestedAfter")
    )
    error_description: Optional[str] = field(
        default=None, metadata=config(field_name="errorDescription")
    )
    generated_before: Optional[str] = field(
        default=None, metadata=config(field_name="generatedBefore")
    )
    generated_after: Optional[str] = field(
        default=None, metadata=config(field_name="generatedAfter")
    )
    schedule_name: Optional[str] = field(
        default=None, metadata=config(field_name="scheduleName")
    )
    schedule_cadence: Optional[str] = field(
        default=None, metadata=config(field_name="scheduleCadence")
    )
    schedule_id: Optional[str] = field(
        default=None, metadata=config(field_name="scheduleID")
    )
    search_all: Optional[str] = field(
        default=None, metadata=config(field_name="searchAll")
    )
    sort_by: Optional[ReportsSortBy] = field(
        default=None, metadata=config(field_name="sortBy")
    )
    sort_order: Optional[SortOrder] = field(
        default=None, metadata=config(field_name="sortOrder")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ReportsFromScheduleInput:
    """ReportsFromScheduleInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    cursor: Optional[Cursor] = field(default=None, metadata=config(field_name="cursor"))
    filters: Optional[ReportsFilters] = field(
        default=None, metadata=config(field_name="filters")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AllReportsInput:
    """AllReportsInput."""

    cursor: Optional[Cursor] = field(default=None, metadata=config(field_name="cursor"))
    filters: Optional[ReportsFilters] = field(
        default=None, metadata=config(field_name="filters")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AllSchedulesInput:
    """AllSchedulesInput."""

    cursor: Optional[Cursor] = field(default=None, metadata=config(field_name="cursor"))
    filters: Optional[SchedulesFilters] = field(
        default=None, metadata=config(field_name="filters")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ScheduleEditInput:
    """ScheduleEditInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    filters: Optional[dict] = field(default=None, metadata=config(field_name="filters"))
    interval: Optional[int] = field(
        default=None, metadata=config(field_name="interval")
    )
    day_of_month: Optional[int] = field(
        default=None, metadata=config(field_name="dayOfMonth")
    )
    recipients: Optional[List[str]] = field(
        default=None, metadata=config(field_name="recipients")
    )
    red_ql_query: Optional[str] = field(
        default=None, metadata=config(field_name="redQLQuery")
    )
    generate_csv_export: Optional[bool] = field(
        default=None, metadata=config(field_name="generateCSVExport")
    )
    run_at: Optional[str] = field(default=None, metadata=config(field_name="runAt"))
    share_with_admin_group: Optional[bool] = field(
        default=None, metadata=config(field_name="shareWithAdminGroup")
    )
    locale: Optional[str] = field(default=None, metadata=config(field_name="locale"))
    chart_type: Optional[ReportChartType] = field(
        default=None, metadata=config(field_name="chartType")
    )
    cadence: Optional[Cadence] = field(
        default=None, metadata=config(field_name="cadence")
    )
    export_types: Optional[List[ExportType]] = field(
        default=None, metadata=config(field_name="exportTypes")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Export:
    """Export."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    dataset: Optional[str] = field(default=None, metadata=config(field_name="dataset"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    filters: Optional[dict] = field(default=None, metadata=config(field_name="filters"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    user_id: Optional[str] = field(default=None, metadata=config(field_name="userID"))
    tenant: Optional[str] = field(default=None, metadata=config(field_name="tenant"))
    file_name: Optional[str] = field(
        default=None, metadata=config(field_name="fileName")
    )
    descriptive_file_name: Optional[str] = field(
        default=None, metadata=config(field_name="descriptiveFileName")
    )
    file_size: Optional[str] = field(
        default=None, metadata=config(field_name="fileSize")
    )
    file_requested: Optional[str] = field(
        default=None, metadata=config(field_name="fileRequested")
    )
    error_description: Optional[str] = field(
        default=None, metadata=config(field_name="errorDescription")
    )
    export_generated: Optional[str] = field(
        default=None, metadata=config(field_name="exportGenerated")
    )
    in_progress_as_of: Optional[str] = field(
        default=None, metadata=config(field_name="inProgressAsOf")
    )
    retry_count: Optional[int] = field(
        default=None, metadata=config(field_name="retryCount")
    )
    selected_columns: Optional[List[str]] = field(
        default=None, metadata=config(field_name="selectedColumns")
    )
    renamed_columns: Optional[dict] = field(
        default=None, metadata=config(field_name="renamedColumns")
    )
    locale: Optional[str] = field(default=None, metadata=config(field_name="locale"))
    creator: Optional[TDRUser] = field(
        default=None, metadata=config(field_name="creator")
    )
    creator_v2: Optional[TDRUser] = field(
        default=None, metadata=config(field_name="creatorV2")
    )
    status: Optional[ExportStatus] = field(
        default=None, metadata=config(field_name="status")
    )
    export_type: Optional[ExportType] = field(
        default=None, metadata=config(field_name="exportType")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NewScheduleInput:
    """NewScheduleInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    filters: Optional[dict] = field(default=None, metadata=config(field_name="filters"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    interval: Optional[int] = field(
        default=None, metadata=config(field_name="interval")
    )
    day_of_month: Optional[int] = field(
        default=None, metadata=config(field_name="dayOfMonth")
    )
    recipients: Optional[List[str]] = field(
        default=None, metadata=config(field_name="recipients")
    )
    red_ql_query: Optional[str] = field(
        default=None, metadata=config(field_name="redQLQuery")
    )
    creator: Optional[str] = field(default=None, metadata=config(field_name="creator"))
    first_run: Optional[str] = field(
        default=None, metadata=config(field_name="firstRun")
    )
    generate_csv_export: Optional[bool] = field(
        default=None, metadata=config(field_name="generateCSVExport")
    )
    custom_report_path: Optional[str] = field(
        default=None, metadata=config(field_name="customReportPath")
    )
    share_with_admin_group: Optional[bool] = field(
        default=None, metadata=config(field_name="shareWithAdminGroup")
    )
    locale: Optional[str] = field(default=None, metadata=config(field_name="locale"))
    chart_type: Optional[ReportChartType] = field(
        default=None, metadata=config(field_name="chartType")
    )
    report_type: Optional[ReportType] = field(
        default=None, metadata=config(field_name="reportType")
    )
    cadence: Optional[Cadence] = field(
        default=None, metadata=config(field_name="cadence")
    )
    export_types: Optional[List[ExportType]] = field(
        default=None, metadata=config(field_name="exportTypes")
    )
    visualizations: Optional[List[VisualizationInput]] = field(
        default=None, metadata=config(field_name="visualizations")
    )
    report_timeframe: Optional[ReportTimeframeInput] = field(
        default=None, metadata=config(field_name="reportTimeframe")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Schedule:
    """Schedule."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    filters: Optional[dict] = field(default=None, metadata=config(field_name="filters"))
    tenant: Optional[str] = field(default=None, metadata=config(field_name="tenant"))
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    interval: Optional[int] = field(
        default=None, metadata=config(field_name="interval")
    )
    last_run: Optional[str] = field(default=None, metadata=config(field_name="lastRun"))
    first_run: Optional[str] = field(
        default=None, metadata=config(field_name="firstRun")
    )
    red_ql_query: Optional[str] = field(
        default=None, metadata=config(field_name="redQLQuery")
    )
    generate_csv_export: Optional[bool] = field(
        default=None, metadata=config(field_name="generateCSVExport")
    )
    custom_report_path: Optional[str] = field(
        default=None, metadata=config(field_name="customReportPath")
    )
    share_with_admin_group: Optional[bool] = field(
        default=None, metadata=config(field_name="shareWithAdminGroup")
    )
    locale: Optional[str] = field(default=None, metadata=config(field_name="locale"))
    chart_type: Optional[ReportChartType] = field(
        default=None, metadata=config(field_name="chartType")
    )
    report_type: Optional[ReportType] = field(
        default=None, metadata=config(field_name="reportType")
    )
    cadence: Optional[Cadence] = field(
        default=None, metadata=config(field_name="cadence")
    )
    recipients: Optional[List[TDRUser]] = field(
        default=None, metadata=config(field_name="recipients")
    )
    recipients_v2: Optional[List[TDRUser]] = field(
        default=None, metadata=config(field_name="recipientsV2")
    )
    creator: Optional[TDRUser] = field(
        default=None, metadata=config(field_name="creator")
    )
    creator_v2: Optional[TDRUser] = field(
        default=None, metadata=config(field_name="creatorV2")
    )
    export_types: Optional[List[ExportType]] = field(
        default=None, metadata=config(field_name="exportTypes")
    )
    visualizations: Optional[List[Visualization]] = field(
        default=None, metadata=config(field_name="visualizations")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SchedulesOutput:
    """SchedulesOutput."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    schedules: Optional[List[Schedule]] = field(
        default=None, metadata=config(field_name="schedules")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Report:
    """Report."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    run_at: Optional[str] = field(default=None, metadata=config(field_name="runAt"))
    run_from: Optional[str] = field(default=None, metadata=config(field_name="runFrom"))
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    previous_status: Optional[str] = field(
        default=None, metadata=config(field_name="previousStatus")
    )
    tenant: Optional[str] = field(default=None, metadata=config(field_name="tenant"))
    file_name: Optional[str] = field(
        default=None, metadata=config(field_name="fileName")
    )
    file_size: Optional[str] = field(
        default=None, metadata=config(field_name="fileSize")
    )
    file_requested: Optional[str] = field(
        default=None, metadata=config(field_name="fileRequested")
    )
    error_description: Optional[str] = field(
        default=None, metadata=config(field_name="errorDescription")
    )
    generated: Optional[str] = field(
        default=None, metadata=config(field_name="generated")
    )
    manual_run: Optional[bool] = field(
        default=None, metadata=config(field_name="manualRun")
    )
    chart_type: Optional[str] = field(
        default=None, metadata=config(field_name="chartType")
    )
    retry_count: Optional[int] = field(
        default=None, metadata=config(field_name="retryCount")
    )
    begin_at: Optional[str] = field(default=None, metadata=config(field_name="beginAt"))
    end_at: Optional[str] = field(default=None, metadata=config(field_name="endAt"))
    locale: Optional[str] = field(default=None, metadata=config(field_name="locale"))
    creator: Optional[TDRUser] = field(
        default=None, metadata=config(field_name="creator")
    )
    creator_v2: Optional[TDRUser] = field(
        default=None, metadata=config(field_name="creatorV2")
    )
    schedule: Optional[Schedule] = field(
        default=None, metadata=config(field_name="schedule")
    )
    export: Optional[Export] = field(default=None, metadata=config(field_name="export"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ReportsOutput:
    """ReportsOutput."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    reports: Optional[List[Report]] = field(
        default=None, metadata=config(field_name="reports")
    )
