"""Audits Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class SortBy(str, Enum):
    """SortBy."""

    TIMESTAMP = "timestamp"
    APPLICATION = "application"
    EVENT_NAME = "eventName"
    EVENT_DESC = "eventDesc"
    USERNAME = "username"
    EMAIL = "email"


class SortOrder(str, Enum):
    """SortOrder."""

    ASC = "asc"
    DESC = "desc"


class AuditEventEnum(str, Enum):
    """AuditEventEnum."""

    INVESTIGATIONS = "investigations"
    ALERTS = "alerts"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Audit:
    """Audit."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    log_type: Optional[str] = field(default=None, metadata=config(field_name="logType"))
    application: Optional[str] = field(
        default=None, metadata=config(field_name="application")
    )
    request_type: Optional[str] = field(
        default=None, metadata=config(field_name="requestType")
    )
    username: Optional[str] = field(
        default=None, metadata=config(field_name="username")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    token: Optional[dict] = field(default=None, metadata=config(field_name="token"))
    source: Optional[str] = field(default=None, metadata=config(field_name="source"))
    target_rn: Optional[str] = field(
        default=None, metadata=config(field_name="targetRn")
    )
    action: Optional[str] = field(default=None, metadata=config(field_name="action"))
    timestamp: Optional[str] = field(
        default=None, metadata=config(field_name="timestamp")
    )
    event_name: Optional[str] = field(
        default=None, metadata=config(field_name="eventName")
    )
    event_desc: Optional[str] = field(
        default=None, metadata=config(field_name="eventDesc")
    )
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    trace_id: Optional[str] = field(default=None, metadata=config(field_name="traceId"))
    metadata: Optional[dict] = field(
        default=None, metadata=config(field_name="metadata")
    )
    response_code: Optional[int] = field(
        default=None, metadata=config(field_name="responseCode")
    )
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))
    headers: Optional[dict] = field(default=None, metadata=config(field_name="headers"))
    request_params: Optional[dict] = field(
        default=None, metadata=config(field_name="requestParams")
    )
    before_state: Optional[dict] = field(
        default=None, metadata=config(field_name="beforeState")
    )
    after_state: Optional[dict] = field(
        default=None, metadata=config(field_name="afterState")
    )
    extras: Optional[dict] = field(default=None, metadata=config(field_name="extras"))
    ccdp_status: Optional[str] = field(
        default=None, metadata=config(field_name="ccdpStatus")
    )
    partner_internal_log: Optional[bool] = field(
        default=None, metadata=config(field_name="partnerInternalLog")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuditInput:
    """AuditInput."""

    log_type: Optional[str] = field(default=None, metadata=config(field_name="logType"))
    application: Optional[str] = field(
        default=None, metadata=config(field_name="application")
    )
    request_type: Optional[str] = field(
        default=None, metadata=config(field_name="requestType")
    )
    actor: Optional[str] = field(default=None, metadata=config(field_name="actor"))
    actor_name: Optional[str] = field(
        default=None, metadata=config(field_name="actorName")
    )
    actor_email: Optional[str] = field(
        default=None, metadata=config(field_name="actorEmail")
    )
    token: Optional[dict] = field(default=None, metadata=config(field_name="token"))
    source: Optional[str] = field(default=None, metadata=config(field_name="source"))
    target_rn: Optional[str] = field(
        default=None, metadata=config(field_name="targetRn")
    )
    action: Optional[str] = field(default=None, metadata=config(field_name="action"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    event_name_index: Optional[int] = field(
        default=None, metadata=config(field_name="eventNameIndex")
    )
    event_desc: Optional[str] = field(
        default=None, metadata=config(field_name="eventDesc")
    )
    trace_id: Optional[str] = field(default=None, metadata=config(field_name="traceId"))
    metadata: Optional[dict] = field(
        default=None, metadata=config(field_name="metadata")
    )
    response_code: Optional[int] = field(
        default=None, metadata=config(field_name="responseCode")
    )
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))
    headers: Optional[dict] = field(default=None, metadata=config(field_name="headers"))
    request_params: Optional[dict] = field(
        default=None, metadata=config(field_name="requestParams")
    )
    before_state: Optional[dict] = field(
        default=None, metadata=config(field_name="beforeState")
    )
    after_state: Optional[dict] = field(
        default=None, metadata=config(field_name="afterState")
    )
    extras: Optional[dict] = field(default=None, metadata=config(field_name="extras"))
    partner_internal_log: Optional[bool] = field(
        default=None, metadata=config(field_name="partnerInternalLog")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuditEvent:
    """AuditEvent."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    desc: Optional[str] = field(default=None, metadata=config(field_name="desc"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuditResult:
    """AuditResult."""

    total_results: Optional[int] = field(
        default=None, metadata=config(field_name="totalResults")
    )
    relation: Optional[str] = field(
        default=None, metadata=config(field_name="relation")
    )
    offset: Optional[int] = field(default=None, metadata=config(field_name="offset"))
    limit: Optional[int] = field(default=None, metadata=config(field_name="limit"))
    audits: Optional[List[Audit]] = field(
        default=None, metadata=config(field_name="audits")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuditEventResult:
    """AuditEventResult."""

    total_events: Optional[int] = field(
        default=None, metadata=config(field_name="totalEvents")
    )
    audit_events: Optional[List[AuditEvent]] = field(
        default=None, metadata=config(field_name="auditEvents")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AllAuditsInput:
    """AllAuditsInput."""

    tenant_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tenantIDs")
    )
    session_id: Optional[str] = field(
        default=None, metadata=config(field_name="sessionID")
    )
    offset: Optional[int] = field(default=None, metadata=config(field_name="offset"))
    limit: Optional[int] = field(default=None, metadata=config(field_name="limit"))
    before: Optional[str] = field(default=None, metadata=config(field_name="before"))
    after: Optional[str] = field(default=None, metadata=config(field_name="after"))
    sort_by: Optional[SortBy] = field(
        default=None, metadata=config(field_name="sortBy")
    )
    sort_order: Optional[SortOrder] = field(
        default=None, metadata=config(field_name="sortOrder")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuditSearchInput:
    """AuditSearchInput."""

    tenant_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tenantIDs")
    )
    session_id: Optional[str] = field(
        default=None, metadata=config(field_name="sessionID")
    )
    offset: Optional[int] = field(default=None, metadata=config(field_name="offset"))
    limit: Optional[int] = field(default=None, metadata=config(field_name="limit"))
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    log_type: Optional[str] = field(default=None, metadata=config(field_name="logType"))
    application: Optional[str] = field(
        default=None, metadata=config(field_name="application")
    )
    applications: Optional[List[str]] = field(
        default=None, metadata=config(field_name="applications")
    )
    request_type: Optional[str] = field(
        default=None, metadata=config(field_name="requestType")
    )
    username: Optional[str] = field(
        default=None, metadata=config(field_name="username")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    emails: Optional[List[str]] = field(
        default=None, metadata=config(field_name="emails")
    )
    source: Optional[str] = field(default=None, metadata=config(field_name="source"))
    target_rn: Optional[str] = field(
        default=None, metadata=config(field_name="targetRn")
    )
    target_rns: Optional[List[str]] = field(
        default=None, metadata=config(field_name="targetRns")
    )
    action: Optional[str] = field(default=None, metadata=config(field_name="action"))
    event_name: Optional[str] = field(
        default=None, metadata=config(field_name="eventName")
    )
    event_names: Optional[List[str]] = field(
        default=None, metadata=config(field_name="eventNames")
    )
    event_desc: Optional[str] = field(
        default=None, metadata=config(field_name="eventDesc")
    )
    trace_id: Optional[str] = field(default=None, metadata=config(field_name="traceId"))
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))
    search_by_all: Optional[str] = field(
        default=None, metadata=config(field_name="searchByAll")
    )
    before: Optional[str] = field(default=None, metadata=config(field_name="before"))
    after: Optional[str] = field(default=None, metadata=config(field_name="after"))
    sort_by: Optional[SortBy] = field(
        default=None, metadata=config(field_name="sortBy")
    )
    sort_order: Optional[SortOrder] = field(
        default=None, metadata=config(field_name="sortOrder")
    )
