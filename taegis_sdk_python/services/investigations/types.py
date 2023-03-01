"""Investigations Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class InvestigationTimelineEntityType(str, Enum):
    """InvestigationTimelineEntityType."""

    ALERT = "ALERT"
    EVENT = "EVENT"
    AUDIT = "AUDIT"
    NOTE = "NOTE"


class OrderDirection(str, Enum):
    """OrderDirection."""

    ASC = "asc"
    DESC = "desc"


class InvestigationProcessingState(str, Enum):
    """InvestigationProcessingState."""

    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    RUNNING = "RUNNING"


class OrderFieldInput(str, Enum):
    """OrderFieldInput."""

    ID = "id"
    TENANT_ID = "tenant_id"
    TAGS = "tags"
    GENESIS_ALERTS = "genesis_alerts"
    GENESIS_EVENTS = "genesis_events"
    ALERTS = "alerts"
    EVENTS = "events"
    ASSETS = "assets"
    AUTH_CREDENTIALS = "auth_credentials"
    KEY_FINDINGS = "key_findings"
    DESCRIPTION = "description"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    NOTIFIED_AT = "notified_at"
    CREATED_BY = "created_by"
    STATUS = "status"
    CONTRIBUTORS = "contributors"
    SERVICE_DESK_ID = "service_desk_id"
    SERVICE_DESK_TYPE = "service_desk_type"
    ALL_ALERTS = "all_alerts"
    ALL_EVENTS = "all_events"
    SHORT_ID = "short_id"
    PRIORITY = "priority"
    TYPE = "type"


class OrderDirectionInput(str, Enum):
    """OrderDirectionInput."""

    ASC = "asc"
    DESC = "desc"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationEntitiesArguments:
    """InvestigationEntitiesArguments."""

    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigationId")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationEntity:
    """InvestigationEntity."""

    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    rn: Optional[str] = field(default=None, metadata=config(field_name="rn"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationTimelineEntity:
    """InvestigationTimelineEntity."""

    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    subtype: Optional[str] = field(default=None, metadata=config(field_name="subtype"))
    document: Optional[dict] = field(
        default=None, metadata=config(field_name="document")
    )
    creation_timestamp: Optional[str] = field(
        default=None, metadata=config(field_name="creationTimestamp")
    )
    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigationId")
    )
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationKeyValuePair:
    """InvestigationKeyValuePair."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationFile:
    """InvestigationFile."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigation_id")
    )
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_id")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    deleted_at: Optional[str] = field(
        default=None, metadata=config(field_name="deleted_at")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    path: Optional[str] = field(default=None, metadata=config(field_name="path"))
    size: Optional[int] = field(default=None, metadata=config(field_name="size"))
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    uploaded_by: Optional[str] = field(
        default=None, metadata=config(field_name="uploaded_by")
    )
    deleted_by: Optional[str] = field(
        default=None, metadata=config(field_name="deleted_by")
    )
    additional_metadata: Optional[dict] = field(
        default=None, metadata=config(field_name="additional_metadata")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationStatusCountResponse:
    """InvestigationStatusCountResponse."""

    open: Optional[int] = field(default=None, metadata=config(field_name="open"))
    closed: Optional[int] = field(default=None, metadata=config(field_name="closed"))
    active: Optional[int] = field(default=None, metadata=config(field_name="active"))
    awaiting_action: Optional[int] = field(
        default=None, metadata=config(field_name="awaiting_action")
    )
    suspended: Optional[int] = field(
        default=None, metadata=config(field_name="suspended")
    )
    total: Optional[int] = field(default=None, metadata=config(field_name="total"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationsExportOutput:
    """InvestigationsExportOutput."""

    column_def: Optional[List[str]] = field(
        default=None, metadata=config(field_name="columnDef")
    )
    rows: Optional[List[List[str]]] = field(
        default=None, metadata=config(field_name="rows")
    )
    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SummaryGroup:
    """SummaryGroup."""

    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    count: Optional[int] = field(default=None, metadata=config(field_name="count"))
    date: Optional[str] = field(default=None, metadata=config(field_name="date"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FileUploadRequest:
    """FileUploadRequest."""

    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigationId")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    size: Optional[int] = field(default=None, metadata=config(field_name="size"))
    content_type: Optional[str] = field(
        default=None, metadata=config(field_name="contentType")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FileUploadInput:
    """FileUploadInput."""

    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigationId")
    )
    file: Optional[str] = field(default=None, metadata=config(field_name="file"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationSummary:
    """InvestigationSummary."""

    tag: Optional[str] = field(default=None, metadata=config(field_name="tag"))
    count: Optional[int] = field(default=None, metadata=config(field_name="count"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Event:
    """Event."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Alert:
    """Alert."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Alert2:
    """Alert2."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Asset:
    """Asset."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ParentCount:
    """ParentCount."""

    parent_id: Optional[str] = field(
        default=None, metadata=config(field_name="parent_id")
    )
    parent_type: Optional[str] = field(
        default=None, metadata=config(field_name="parent_type")
    )
    total: Optional[int] = field(default=None, metadata=config(field_name="total"))
    unread: Optional[int] = field(default=None, metadata=config(field_name="unread"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUser:
    """TDRUser."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SearchQuery:
    """SearchQuery."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Tenant:
    """Tenant."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ActivityLog:
    """ActivityLog."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_id")
    )
    user_id: Optional[str] = field(default=None, metadata=config(field_name="user_id"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    comment: Optional[str] = field(default=None, metadata=config(field_name="comment"))
    target: Optional[str] = field(default=None, metadata=config(field_name="target"))
    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigation_id")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TransitionState:
    """TransitionState."""

    handed_off_at_least_once: Optional[bool] = field(
        default=None, metadata=config(field_name="handed_off_at_least_once")
    )
    initial_handoff_time: Optional[str] = field(
        default=None, metadata=config(field_name="initial_handoff_time")
    )
    acknowledged_at_least_once: Optional[bool] = field(
        default=None, metadata=config(field_name="acknowledged_at_least_once")
    )
    initial_acknowledge_time: Optional[str] = field(
        default=None, metadata=config(field_name="initial_acknowledge_time")
    )
    resolved_at_least_once: Optional[bool] = field(
        default=None, metadata=config(field_name="resolved_at_least_once")
    )
    initial_resolution_time: Optional[str] = field(
        default=None, metadata=config(field_name="initial_resolution_time")
    )
    handed_off: Optional[bool] = field(
        default=None, metadata=config(field_name="handed_off")
    )
    handoff_time: Optional[str] = field(
        default=None, metadata=config(field_name="handoff_time")
    )
    acknowledged: Optional[bool] = field(
        default=None, metadata=config(field_name="acknowledged")
    )
    acknowledge_time: Optional[str] = field(
        default=None, metadata=config(field_name="acknowledge_time")
    )
    resolved: Optional[bool] = field(
        default=None, metadata=config(field_name="resolved")
    )
    resolution_time: Optional[str] = field(
        default=None, metadata=config(field_name="resolution_time")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Count:
    """Count."""

    count: Optional[int] = field(default=None, metadata=config(field_name="count"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationInfo:
    """InvestigationInfo."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    genesis_alerts: Optional[List[str]] = field(
        default=None, metadata=config(field_name="genesis_alerts")
    )
    alerts: Optional[List[str]] = field(
        default=None, metadata=config(field_name="alerts")
    )
    tenant: Optional[str] = field(default=None, metadata=config(field_name="tenant"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Hostname:
    """Hostname."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    host_id: Optional[str] = field(default=None, metadata=config(field_name="host_id"))
    hostname: Optional[str] = field(
        default=None, metadata=config(field_name="hostname")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EthernetAddress:
    """EthernetAddress."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    host_id: Optional[str] = field(default=None, metadata=config(field_name="host_id"))
    mac: Optional[str] = field(default=None, metadata=config(field_name="mac"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IpAddress:
    """IpAddress."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    host_id: Optional[str] = field(default=None, metadata=config(field_name="host_id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class User:
    """User."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    host_id: Optional[str] = field(default=None, metadata=config(field_name="host_id"))
    username: Optional[str] = field(
        default=None, metadata=config(field_name="username")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MitreAttackInfo:
    """MitreAttackInfo."""

    technique_id: Optional[str] = field(
        default=None, metadata=config(field_name="technique_id")
    )
    technique: Optional[str] = field(
        default=None, metadata=config(field_name="technique")
    )
    tactics: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tactics")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    platform: Optional[List[str]] = field(
        default=None, metadata=config(field_name="platform")
    )
    system_requirements: Optional[List[str]] = field(
        default=None, metadata=config(field_name="system_requirements")
    )
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))
    data_sources: Optional[List[str]] = field(
        default=None, metadata=config(field_name="data_sources")
    )
    defence_bypassed: Optional[List[str]] = field(
        default=None, metadata=config(field_name="defence_bypassed")
    )
    contributors: Optional[List[str]] = field(
        default=None, metadata=config(field_name="contributors")
    )
    version: Optional[str] = field(default=None, metadata=config(field_name="version"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationInput:
    """InvestigationInput."""

    tags: Optional[List[str]] = field(default=None, metadata=config(field_name="tags"))
    genesis_alerts: Optional[List[str]] = field(
        default=None, metadata=config(field_name="genesis_alerts")
    )
    genesis_events: Optional[List[str]] = field(
        default=None, metadata=config(field_name="genesis_events")
    )
    alerts: Optional[List[str]] = field(
        default=None, metadata=config(field_name="alerts")
    )
    events: Optional[List[str]] = field(
        default=None, metadata=config(field_name="events")
    )
    assets: Optional[List[str]] = field(
        default=None, metadata=config(field_name="assets")
    )
    auth_credentials: Optional[List[str]] = field(
        default=None, metadata=config(field_name="auth_credentials")
    )
    search_queries: Optional[List[str]] = field(
        default=None, metadata=config(field_name="search_queries")
    )
    key_findings: Optional[str] = field(
        default=None, metadata=config(field_name="key_findings")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    notified_at: Optional[str] = field(
        default=None, metadata=config(field_name="notified_at")
    )
    created_by: Optional[str] = field(
        default=None, metadata=config(field_name="created_by")
    )
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    contributors: Optional[List[str]] = field(
        default=None, metadata=config(field_name="contributors")
    )
    service_desk_id: Optional[str] = field(
        default=None, metadata=config(field_name="service_desk_id")
    )
    service_desk_type: Optional[str] = field(
        default=None, metadata=config(field_name="service_desk_type")
    )
    assignee_id: Optional[str] = field(
        default=None, metadata=config(field_name="assignee_id")
    )
    notes: Optional[str] = field(default=None, metadata=config(field_name="notes"))
    priority: Optional[int] = field(
        default=None, metadata=config(field_name="priority")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateInvestigationInput:
    """UpdateInvestigationInput."""

    tags: Optional[List[str]] = field(default=None, metadata=config(field_name="tags"))
    genesis_alerts: Optional[List[str]] = field(
        default=None, metadata=config(field_name="genesis_alerts")
    )
    genesis_events: Optional[List[str]] = field(
        default=None, metadata=config(field_name="genesis_events")
    )
    alerts: Optional[List[str]] = field(
        default=None, metadata=config(field_name="alerts")
    )
    events: Optional[List[str]] = field(
        default=None, metadata=config(field_name="events")
    )
    assets: Optional[List[str]] = field(
        default=None, metadata=config(field_name="assets")
    )
    auth_credentials: Optional[List[str]] = field(
        default=None, metadata=config(field_name="auth_credentials")
    )
    search_queries: Optional[List[str]] = field(
        default=None, metadata=config(field_name="search_queries")
    )
    key_findings: Optional[str] = field(
        default=None, metadata=config(field_name="key_findings")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    notified_at: Optional[str] = field(
        default=None, metadata=config(field_name="notified_at")
    )
    created_by: Optional[str] = field(
        default=None, metadata=config(field_name="created_by")
    )
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    contributors: Optional[List[str]] = field(
        default=None, metadata=config(field_name="contributors")
    )
    service_desk_id: Optional[str] = field(
        default=None, metadata=config(field_name="service_desk_id")
    )
    service_desk_type: Optional[str] = field(
        default=None, metadata=config(field_name="service_desk_type")
    )
    assignee_id: Optional[str] = field(
        default=None, metadata=config(field_name="assignee_id")
    )
    notes: Optional[str] = field(default=None, metadata=config(field_name="notes"))
    acknowledgment: Optional[bool] = field(
        default=None, metadata=config(field_name="acknowledgment")
    )
    priority: Optional[int] = field(
        default=None, metadata=config(field_name="priority")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    comment_event: Optional[dict] = field(
        default=None, metadata=config(field_name="comment_event")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ActivityLogInput:
    """ActivityLogInput."""

    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    comment: Optional[str] = field(default=None, metadata=config(field_name="comment"))
    target: Optional[str] = field(default=None, metadata=config(field_name="target"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationEntities:
    """InvestigationEntities."""

    entities: Optional[List[InvestigationEntity]] = field(
        default=None, metadata=config(field_name="entities")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationTimelineEntityFilters:
    """InvestigationTimelineEntityFilters."""

    entity_types: Optional[List[str]] = field(
        default=None, metadata=config(field_name="entityTypes")
    )
    entities: Optional[List[InvestigationTimelineEntityType]] = field(
        default=None, metadata=config(field_name="entities")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationTimeline:
    """InvestigationTimeline."""

    total_entities: Optional[int] = field(
        default=None, metadata=config(field_name="totalEntities")
    )
    entities: Optional[List[InvestigationTimelineEntity]] = field(
        default=None, metadata=config(field_name="entities")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationEventOutput:
    """InvestigationEventOutput."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    events: Optional[List[Event]] = field(
        default=None, metadata=config(field_name="events")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationAssetOutput:
    """InvestigationAssetOutput."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    assets: Optional[List[Asset]] = field(
        default=None, metadata=config(field_name="assets")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AccessVector:
    """AccessVector."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigation_id")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    mitre_info: Optional[MitreAttackInfo] = field(
        default=None, metadata=config(field_name="mitre_info")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FileUploadResponse:
    """FileUploadResponse."""

    presigned_url: Optional[str] = field(
        default=None, metadata=config(field_name="presignedUrl")
    )
    investigation_file: Optional[InvestigationFile] = field(
        default=None, metadata=config(field_name="investigationFile")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Assignee:
    """Assignee."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    roles: Optional[List[str]] = field(
        default=None, metadata=config(field_name="roles")
    )
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    user_id: Optional[str] = field(default=None, metadata=config(field_name="user_id"))
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    email_verified: Optional[bool] = field(
        default=None, metadata=config(field_name="email_verified")
    )
    email_normalized: Optional[str] = field(
        default=None, metadata=config(field_name="email_normalized")
    )
    family_name: Optional[str] = field(
        default=None, metadata=config(field_name="family_name")
    )
    given_name: Optional[str] = field(
        default=None, metadata=config(field_name="given_name")
    )
    tenants: Optional[List[Tenant]] = field(
        default=None, metadata=config(field_name="tenants")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Investigations:
    """Investigations."""

    investigations: Optional[List[InvestigationInfo]] = field(
        default=None, metadata=config(field_name="investigations")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationTimelineArguments:
    """InvestigationTimelineArguments."""

    investigation_id: Optional[str] = field(
        default=None, metadata=config(field_name="investigationId")
    )
    page: Optional[int] = field(default=None, metadata=config(field_name="page"))
    per_page: Optional[int] = field(default=None, metadata=config(field_name="perPage"))
    created_after: Optional[str] = field(
        default=None, metadata=config(field_name="createdAfter")
    )
    created_before: Optional[str] = field(
        default=None, metadata=config(field_name="createdBefore")
    )
    order_by: Optional[OrderDirectionInput] = field(
        default=None, metadata=config(field_name="orderBy")
    )
    entity_filters: Optional[InvestigationTimelineEntityFilters] = field(
        default=None, metadata=config(field_name="entityFilters")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationAlertOutput:
    """InvestigationAlertOutput."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    alerts: Optional[List[Alert]] = field(
        default=None, metadata=config(field_name="alerts")
    )
    alerts2: Optional[List[Alert2]] = field(
        default=None, metadata=config(field_name="alerts2")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationProcessingResponse:
    """InvestigationProcessingResponse."""

    assets: Optional[InvestigationProcessingState] = field(
        default=None, metadata=config(field_name="assets")
    )
    events: Optional[InvestigationProcessingState] = field(
        default=None, metadata=config(field_name="events")
    )
    alerts: Optional[InvestigationProcessingState] = field(
        default=None, metadata=config(field_name="alerts")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Investigation:
    """Investigation."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_id")
    )
    tags: Optional[List[str]] = field(default=None, metadata=config(field_name="tags"))
    auth_credentials: Optional[List[str]] = field(
        default=None, metadata=config(field_name="auth_credentials")
    )
    key_findings: Optional[str] = field(
        default=None, metadata=config(field_name="key_findings")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    notified_at: Optional[str] = field(
        default=None, metadata=config(field_name="notified_at")
    )
    first_notified_at: Optional[str] = field(
        default=None, metadata=config(field_name="first_notified_at")
    )
    first_notified_at_scwx: Optional[str] = field(
        default=None, metadata=config(field_name="first_notified_at_scwx")
    )
    created_by: Optional[str] = field(
        default=None, metadata=config(field_name="created_by")
    )
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    contributors: Optional[List[str]] = field(
        default=None, metadata=config(field_name="contributors")
    )
    service_desk_id: Optional[str] = field(
        default=None, metadata=config(field_name="service_desk_id")
    )
    service_desk_type: Optional[str] = field(
        default=None, metadata=config(field_name="service_desk_type")
    )
    assignee_id: Optional[str] = field(
        default=None, metadata=config(field_name="assignee_id")
    )
    latest_activity: Optional[str] = field(
        default=None, metadata=config(field_name="latest_activity")
    )
    archived_at: Optional[str] = field(
        default=None, metadata=config(field_name="archived_at")
    )
    deleted_at: Optional[str] = field(
        default=None, metadata=config(field_name="deleted_at")
    )
    created_by_scwx: Optional[bool] = field(
        default=None, metadata=config(field_name="created_by_scwx")
    )
    created_by_partner: Optional[bool] = field(
        default=None, metadata=config(field_name="created_by_partner")
    )
    investigation_type: Optional[str] = field(
        default=None, metadata=config(field_name="investigationType")
    )
    priority: Optional[int] = field(
        default=None, metadata=config(field_name="priority")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    genesis_alerts_count: Optional[int] = field(
        default=None, metadata=config(field_name="genesis_alerts_count")
    )
    genesis_events_count: Optional[int] = field(
        default=None, metadata=config(field_name="genesis_events_count")
    )
    alerts_count: Optional[int] = field(
        default=None, metadata=config(field_name="alerts_count")
    )
    events_count: Optional[int] = field(
        default=None, metadata=config(field_name="events_count")
    )
    assets_count: Optional[int] = field(
        default=None, metadata=config(field_name="assets_count")
    )
    files_count: Optional[int] = field(
        default=None, metadata=config(field_name="files_count")
    )
    rn: Optional[str] = field(default=None, metadata=config(field_name="rn"))
    short_id: Optional[str] = field(default=None, metadata=config(field_name="shortId"))
    genesis_alerts: Optional[List[Alert]] = field(
        default=None, metadata=config(field_name="genesis_alerts")
    )
    genesis_alerts2: Optional[List[Alert2]] = field(
        default=None, metadata=config(field_name="genesis_alerts2")
    )
    genesis_events: Optional[List[Event]] = field(
        default=None, metadata=config(field_name="genesis_events")
    )
    alerts: Optional[List[Alert]] = field(
        default=None, metadata=config(field_name="alerts")
    )
    alerts2: Optional[List[Alert2]] = field(
        default=None, metadata=config(field_name="alerts2")
    )
    events: Optional[List[Event]] = field(
        default=None, metadata=config(field_name="events")
    )
    assets: Optional[List[Asset]] = field(
        default=None, metadata=config(field_name="assets")
    )
    search_queries: Optional[List[SearchQuery]] = field(
        default=None, metadata=config(field_name="search_queries")
    )
    activity_logs: Optional[List[ActivityLog]] = field(
        default=None, metadata=config(field_name="activity_logs")
    )
    created_by_user: Optional[TDRUser] = field(
        default=None, metadata=config(field_name="created_by_user")
    )
    contributed_users: Optional[List[TDRUser]] = field(
        default=None, metadata=config(field_name="contributed_users")
    )
    assignee_user: Optional[TDRUser] = field(
        default=None, metadata=config(field_name="assignee_user")
    )
    assignee: Optional[Assignee] = field(
        default=None, metadata=config(field_name="assignee")
    )
    access_vectors: Optional[List[AccessVector]] = field(
        default=None, metadata=config(field_name="access_vectors")
    )
    transition_state: Optional[TransitionState] = field(
        default=None, metadata=config(field_name="transition_state")
    )
    processing_status: Optional[InvestigationProcessingResponse] = field(
        default=None, metadata=config(field_name="processing_status")
    )
    comments_count: Optional[ParentCount] = field(
        default=None, metadata=config(field_name="comments_count")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationsOutput:
    """InvestigationsOutput."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    investigations: Optional[List[Investigation]] = field(
        default=None, metadata=config(field_name="investigations")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IndividualTimeSummary:
    """IndividualTimeSummary."""

    time_to_handoff: Optional[int] = field(
        default=None, metadata=config(field_name="time_to_handoff")
    )
    time_to_acknowledge: Optional[int] = field(
        default=None, metadata=config(field_name="time_to_acknowledge")
    )
    time_to_resolution: Optional[int] = field(
        default=None, metadata=config(field_name="time_to_resolution")
    )
    is_closed: Optional[bool] = field(
        default=None, metadata=config(field_name="is_closed")
    )
    investigation: Optional[Investigation] = field(
        default=None, metadata=config(field_name="investigation")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class InvestigationBulkResponse:
    """InvestigationBulkResponse."""

    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    investigations: Optional[List[Investigation]] = field(
        default=None, metadata=config(field_name="investigations")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TransitionSummary:
    """TransitionSummary."""

    transition_time: Optional[str] = field(
        default=None, metadata=config(field_name="transition_time")
    )
    time_summary: Optional[IndividualTimeSummary] = field(
        default=None, metadata=config(field_name="time_summary")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TimeSummaryForGroup:
    """TimeSummaryForGroup."""

    mean_time_to_handoff: Optional[int] = field(
        default=None, metadata=config(field_name="mean_time_to_handoff")
    )
    mean_time_to_acknowledge: Optional[int] = field(
        default=None, metadata=config(field_name="mean_time_to_acknowledge")
    )
    mean_time_to_resolution: Optional[int] = field(
        default=None, metadata=config(field_name="mean_time_to_resolution")
    )
    time_summaries: Optional[List[IndividualTimeSummary]] = field(
        default=None, metadata=config(field_name="time_summaries")
    )
