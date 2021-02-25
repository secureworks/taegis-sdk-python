import json
from dataclasses import dataclass, field
from typing import List, Optional

import stringcase

from taegis_sdk_python.services.common_types import Epoch, Time
from taegis_sdk_python.services.investigations.enums import InvestigationProcessingState, InvestigationStatusEnum, \
    InvestigationTypes, PriorityEnum
from taegis_sdk_python.utils import is_valid_value


@dataclass
class Tenant:
    id: str
    name: str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"

    def __str__(self):
        return f'Tenant(id={self.id}, description={self.name if self.name else ""})'


@dataclass(repr=False)
class Assignee:
    """Describes the assignee of an investigation."""

    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "tenants" and value:
                setattr(self, key, [Tenant(**item) for item in value])
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    id: str
    name: str = field(init=False)
    roles: List[str] = field(default_factory=list)
    status: str = field(init=False)
    user_id: str = field(init=False)
    email: str = field(init=False)
    email_verified: bool = field(init=False)
    email_normalized: str = field(init=False)
    family_name: str = field(init=False)
    given_name: str = field(init=False)
    tenants: List[Tenant] = field(default_factory=list, init=False)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"

    def __str__(self):
        return f'Assignee(id={self.id}, description={self.name if self.name else ""})'

    def __eq__(self, other):
        if not isinstance(other, Assignee):
            return False
        fields = dir(self)
        for f in fields:
            if f.startswith("__"):
                continue
            if hasattr(self, f) and hasattr(other, f):
                if getattr(self, f) != getattr(other, f):
                    return False
        return True

    def __ne__(self, other):
        return not self == other


@dataclass(repr=False, order=True)
class TransitionState:
    """
    Represent both the initial transitions (if they exist)
    and the current state (handed off, acknowledged, resolved) of an investigation.
    """

    def __init__(self, data):
        for key, value in data.items():
            if key in ["initial_handoff_time",
                       "initial_acknowledge_time",
                       "initial_resolution_time",
                       "handoff_time",
                       "acknowledge_time",
                       "resolution_time"] and value:
                setattr(self, key, Time.convert(value))
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    handed_off_at_least_once: bool = field(init=False)
    initial_handoff_time: Time = field(init=False, default=None)
    acknowledged_at_least_once: bool = field(init=False)
    initial_acknowledge_time: Time = field(init=False)
    resolved_at_least_once: bool = field(init=False)
    initial_resolution_time: Time = field(init=False)
    handed_off: bool = field(init=False)
    handoff_time: Time = field(init=False)
    acknowledged: bool = field(init=False)
    acknowledge_time: Time = field(init=False)
    resolved: bool = field(init=False)
    resolution_time: Time = field(init=False)

    def __eq__(self, other):
        if not isinstance(other, TransitionState):
            return False
        fields = dir(self)
        for f in fields:
            if f.startswith("__"):
                continue
            if hasattr(self, f) and hasattr(other, f):
                if getattr(self, f) != getattr(other, f):
                    return False
        return True

    def __ne__(self, other):
        return not self == other


@dataclass(order=True)
class ActivityLog:
    """Stores details of an investigation activity (Create/Update, etc.)."""

    def __init__(self, data):
        for key, value in data.items():
            if key in ["created_at", "updated_at"] and value:
                setattr(self, key, Time.convert(value))
            elif is_valid_value(value):
                setattr(self, key, value)

    id: str
    created_at: Time = field(init=False)
    updated_at: Time = field(init=False)
    tenant_id: str = field(init=False)
    user_id: str = field(init=False)
    description: str = field(init=False)
    type: str = field(init=False)
    comment: str = field(init=False)
    target: str = field(init=False)
    investigation_id: str = field(init=False)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"

    def __str__(self):
        return (
            f'ActivityLog(id={self.id}, '
            f'created_at={self.created_at.date}, '
            f'tenant_id={self.tenant_id}, '
            f'user_id={self.user_id}, '
            f'type={self.type}, '
            f'investigation_id={self.investigation_id})'
        )

    def __eq__(self, other):
        if not isinstance(other, ActivityLog):
            return False
        fields = dir(self)
        for f in fields:
            if f.startswith("__"):
                continue
            if hasattr(self, f) and hasattr(other, f):
                if getattr(self, f) != getattr(other, f):
                    return False
        return True

    def __ne__(self, other):
        return not self == other


@dataclass(order=True)
class InvestigationProcessingResponse:
    def __init__(self, data):
        for key, value in data.items():
            if is_valid_value(value):
                setattr(self, stringcase.snakecase(key), InvestigationProcessingState(value))

    assets: InvestigationProcessingState = field(init=False)
    events: InvestigationProcessingState = field(init=False)
    alerts: InvestigationProcessingState = field(init=False)

    def __repr__(self):
        return (
            f'{{ assets: {self.assets}, events: {self.events}, alerts: {self.alerts} }}'
        )

    def __str__(self):
        return (
            f'InvestigationProcessingResponse(assets={self.assets}, '
            f'events={self.events}, '
            f'alerts={self.alerts})')

    def __eq__(self, other):
        if not isinstance(other, InvestigationProcessingResponse):
            return False
        fields = dir(self)
        for f in fields:
            if f.startswith("__"):
                continue
            if hasattr(self, f) and hasattr(other, f):
                if getattr(self, f) != getattr(other, f):
                    return False
        return True

    def __ne__(self, other):
        return not self == other


@dataclass
class SearchQuery:
    id: str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.id}>"

    def __str__(self) -> str:
        return f"SearchQuery(id={self.id})"


@dataclass
class Event:
    id: str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"

    def __str__(self) -> str:
        return f"Event: {self.id}"


@dataclass(order=True)
class Asset:
    """
    Describes an Asset in Taegis XDR.
    """

    id: str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"

    def __str__(self) -> str:
        return f"Asset: {self.id}"


@dataclass
class Alert:
    id: str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.id}>"

    def __str__(self) -> str:
        return f"{self.id}"

    def __eq__(self, other):
        if not isinstance(other, Alert):
            return False
        return self.id == other.id

    def __ne__(self, other):
        return not self == other


@dataclass(repr=False, order=True)
class MitreAttackInfo:
    """
    Describes fields related to MitreAttack information for an alert.
    """

    def __init__(self, data: dict):
        for key, value in data.items():
            if is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    technique_id: str = field(init=False)
    technique: str = field(init=False)
    tactics: List[str] = field(default_factory=list, init=False)
    type: str = field(init=False)
    description: str = field(init=False)
    platform: List[str] = field(default_factory=list, init=False)
    system_requirements: List[str] = field(default_factory=list, init=False)
    url: str = field(init=False)
    data_sources: List[str] = field(default_factory=list, init=False)
    defence_bypassed: List[str] = field(default_factory=list, init=False)
    contributors: List[str] = field(default_factory=list, init=False)
    version: str = field(init=False)

    def __eq__(self, other):
        if not isinstance(other, MitreAttackInfo):
            return False
        fields = dir(self)
        for f in fields:
            if f.startswith("__"):
                continue
            if hasattr(self, f) and hasattr(other, f):
                if getattr(self, f) != getattr(other, f):
                    return False
        return True

    def __ne__(self, other):
        return not self == other


@dataclass(order=True)
class AccessVector:
    def __init__(self, data: dict):
        for key, value in data.items():
            if key in ["created_at", "updated_at"] and value:
                setattr(self, key, Time.convert(value))
            elif key == "mitre_info" and value:
                setattr(self, "mitre_info", MitreAttackInfo(value))
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    id: str
    investigation_id: str = field(init=False)
    name: str = field(init=False)
    created_at: Time = field(init=False)
    updated_at: Time = field(init=False)
    mitre_info: MitreAttackInfo = field(init=False)

    def __repr__(self):
        return str(
            {
                'id': self.id,
                'investigation_id': self.investigation_id,
                'name': self.name,
                'created_at': self.created_at.date,
            }
        )

    def __str__(self):
        return (
            f'AccessVector(id={self.id}, '
            f'investigation_id={self.investigation_id}, '
            f'name={self.name}, '
            f'created_at={self.created_at.date})'
        )

    def __eq__(self, other):
        if not isinstance(other, AccessVector):
            return False
        fields = dir(self)
        for f in fields:
            if f.startswith("__"):
                continue
            if hasattr(self, f) and hasattr(other, f):
                if getattr(self, f) != getattr(other, f):
                    return False
        return True

    def __ne__(self, other):
        return not self == other


@dataclass
class InvestigationAlertOutput:
    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "alerts" and value:
                setattr(self, key, [Alert(id=item.get("id")) for item in value])
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    alerts: List[Alert] = field(default_factory=list, init=False)
    total_count: int

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.total_count}>"

    def __str__(self) -> str:
        return f"InvestigationAlertOutput: {self.total_count}"


@dataclass(order=True)
class Investigation:

    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "priority" and value is not None:
                setattr(self, key, PriorityEnum(value))
            elif key == "status" and value:
                setattr(self, key, InvestigationStatusEnum(value))
            elif key == "type" and value:
                setattr(self, key, InvestigationTypes(value))
            elif key in ["tags", "contributors", "auth_credentials"] and value:
                setattr(self, key, value)
            elif key == "processing_status" and value:
                if value.get("assets") and value.get("events") and value.get("alerts"):
                    setattr(self, key, InvestigationProcessingResponse(value))
            elif key == "activity_logs" and value:
                setattr(self, key, [ActivityLog(item) for item in value])
            elif key == "assignee" and value:
                setattr(self, key, Assignee(value))
            elif key == "transition_state" and value:
                setattr(self, key, TransitionState(value))
            elif key in ["genesis_events", "events"] and value:
                setattr(self, key, [Event(id=item.get("id")) for item in value])
            elif key == "search_queries" and value:
                setattr(self, key, [SearchQuery(id=item.get("id")) for item in value])
            elif key == "access_vectors" and value:
                setattr(self, key, [AccessVector(item) for item in value])
            elif key in ["genesis_alerts", "alerts"] and value:
                setattr(self, key, [Alert(id=item.get("id")) for item in value])
            elif key == "assets" and value:
                setattr(self, key, [Asset(id=item.get("id")) for item in value])
            elif key in ["created_at", "updated_at", "notified_at", "deleted_at"] and value:
                setattr(self, key, Time.convert(value))
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    id: str
    description: str
    tenant_id: str = field(init=False)
    tags: List[str] = field(init=False)
    genesis_alerts: List[Alert] = field(default_factory=list, init=False)
    genesis_events: List[Event] = field(default_factory=list, init=False)
    alerts: List[Alert] = field(default_factory=list, init=False)
    events: List[Event] = field(default_factory=list, init=False)
    assets: List[Asset] = field(default_factory=list, init=False)
    search_queries: List[SearchQuery] = field(default_factory=list, init=False)
    auth_credentials: List[str] = field(default_factory=list, init=False)
    key_findings: str = field(init=False)
    created_at: Time = field(init=False)
    updated_at: Time = field(init=False)
    notified_at: Time = field(init=False)
    activity_logs: List[ActivityLog] = field(default_factory=list, init=False)
    created_by: str = field(init=False)
    status: InvestigationStatusEnum = field(init=False)
    contributors: List[str] = field(default_factory=list, init=False)
    service_desk_id: str = field(init=False)
    service_desk_type: str = field(init=False)
    assignee_id: str = field(init=False)
    assignee: Optional[Assignee] = field(init=False)
    latest_activity: str = field(init=False)
    access_vectors: List[AccessVector] = field(default_factory=list, init=False, repr=False)
    transition_state: Optional[TransitionState] = field(init=False, repr=False)
    deleted_at: Time = field(init=False)
    created_by_scwx: bool = field(init=False)
    investigation_type: str = field(init=False)
    processing_status: InvestigationProcessingResponse = field(init=False)
    priority: PriorityEnum = field(init=False)
    type: InvestigationTypes = field(init=False)
    genesis_alerts_count: int = field(init=False)
    genesis_events_count: int = field(init=False)
    alerts_count: int = field(init=False)
    events_count: int = field(init=None)
    assets_count: int = field(init=None)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"

    def __str__(self):
        return f'Investigation: {self.id}, {self.description}'

    def __eq__(self, other):
        if not isinstance(other, Investigation):
            return False
        fields = dir(self)
        for f in fields:
            if f.startswith("__"):
                continue
            if hasattr(self, f) and hasattr(other, f):
                if getattr(self, f) != getattr(other, f):
                    return False
        return True

    def __ne__(self, other):
        return not self == other


@dataclass(repr=False, order=True)
class InvestigationStatusCountResponse:
    open: int
    closed: int
    active: int
    awaiting_action: int
    suspended: int
    total: int


@dataclass
class EventInfo:
    """
        Describes the fields common to all event types.
    """

    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "original_data" and value:
                setattr(self, stringcase.snakecase(key), json.loads(value))
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    type: str = field(init=False)
    message: str = field(init=False)
    resource_id: str = field(init=False)
    tenant_id: str = field(init=False)
    visibility: str = field(init=False)
    normalizer: str = field(init=False)
    sensor_type: str = field(init=False)
    sensor_event_id: str = field(init=False)
    sensor_tenant: str = field(init=False)
    sensor_id: str = field(init=False)
    sensor_cpe: str = field(init=False)
    original_data: dict = field(init=False)
    event_time_usec: int = field(init=False)
    ingest_time_usec: int = field(init=False)
    event_time_fidelity: str = field(init=False)
    host_id: str = field(init=False)
    source_address: str = field(init=False)
    destination_address: str = field(init=False)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.sensor_id}>"

    def __str__(self):
        return {self.sensor_id}

    def __eq__(self, other):
        if not isinstance(other, Investigation):
            return False
        fields = dir(self)
        for f in fields:
            if f.startswith("__"):
                continue
            if hasattr(self, f) and hasattr(other, f):
                if getattr(self, f) != getattr(other, f):
                    return False
        return True

    def __ne__(self, other):
        return not self == other


@dataclass(repr=False, order=True)
class InvestigationEventOutput:
    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "events" and value:
                setattr(self, key, [EventInfo(item) for item in value])
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    events: List[EventInfo] = field(default_factory=list, init=False)
    total_count: int

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.total_count}>"

    def __str__(self):
        return f'InvestigationEventOutput(total count={self.total_count})'


@dataclass
class InvestigationAssetOutput:
    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "assets" and value:
                setattr(self, key, [Asset(id=item.get("id")) for item in value])
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    assets: List[Asset] = field(default_factory=list, init=False)
    total_count: int

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.total_count}>"

    def __str__(self):
        return f'InvestigationAssetOutput(total count={self.total_count})'


@dataclass
class SummaryGroup:
    """
        Describes the summary of investigations by status filtered by date.
    """
    status: str
    count: int
    date: str
    date_time: Time = field(init=False)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.status}, {self.count}>"

    def __str__(self):
        return f'SummaryGroup(status={self.status}, count={self.count}, date={self.date})'

    def __post_init__(self):
        if hasattr(self, "date"):
            from dateutil.parser import parse
            dt_str = parse(self.date).strftime('%Y-%m-%dT%H:%M:%SZ')
            converted = Time.convert(dt_str)
            setattr(self, "date_time", converted)


@dataclass
class InvestigationSummary:
    """
    Provides a count of investigations per tag.
    """
    tag: str
    count: int

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.tag}, {self.count}>"

    def __str__(self):
        return f'InvestigationSummary(tag={self.tag}, count={self.count})'


@dataclass
class Count:
    """
    Represents a int count of a given object.
    """
    count: int

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.count}>"

    def __str__(self):
        return str(self.count)


@dataclass(repr=False)
class IndividualTimeSummary:
    """
    Represents the amounts of time it took before an investigation transitioned into the handoff,
    acknowledge, and resolution states.
    """

    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "investigation" and value is not None:
                setattr(self, key, Investigation(value))
            elif key in ["time_to_handoff", "time_to_acknowledge", "time_to_resolution"] and value:
                setattr(self, key, Epoch(value))
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    time_to_handoff: Epoch
    time_to_acknowledge: Epoch
    time_to_resolution: Epoch
    is_closed: bool
    investigation: Investigation


@dataclass(repr=False)
class TimeSummaryForGroup:
    """
    Used by MeanTimeSummaryOverPeriod query to represent the average times it took to hand off,
    acknowledge, and resolve all investigations over the course of the period.
    """

    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "time_summaries" and value is not None:
                setattr(self, key, [IndividualTimeSummary(item) for item in value])
            elif key in ["mean_time_to_handoff", "mean_time_to_acknowledge", "mean_time_to_resolution"]:
                setattr(self, key, Epoch(value))
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    mean_time_to_handoff: Epoch
    mean_time_to_acknowledge: Epoch
    mean_time_to_resolution: Epoch
    time_summaries: List[IndividualTimeSummary] = field(default_factory=list, init=False, repr=False)


@dataclass(repr=False)
class InvestigationsOutput:
    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "investigations" and value:
                setattr(self, key, [Investigation(item) for item in value])
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    investigations: List[Investigation] = field(default_factory=list, init=False, repr=False)
    total_count: int


@dataclass
class InvestigationsExportOutput:
    def __init__(self, data: dict):
        for key, value in data.items():
            if is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    column_def: List[str]
    rows: List[List[str]]
    total_count: int


@dataclass
class InvestigationBulkResponse:
    def __init__(self, data: dict):
        for key, value in data.items():
            if key == "investigations" and value:
                setattr(self, key, [Investigation(item) for item in value])
            elif is_valid_value(value):
                setattr(self, stringcase.snakecase(key), value)

    query: str
    investigations: List[Investigation] = field(default_factory=list, init=False, repr=False)


@dataclass
class InvestigationInput:
    tags: List[str] = field(default=None)
    genesis_alerts: List[str] = field(default=None)
    genesis_events: List[str] = field(default=None)
    alerts: List[str] = field(default=None)
    events: List[str] = field(default=None)
    assets: List[str] = field(default=None)
    auth_credentials: List[str] = field(default=None)
    search_queries: List[str] = field(default=None)
    key_findings: str = field(default=None)
    description: str = field(default=None)
    notified_at: str = field(default=None)
    created_by: str = field(default=None)
    status: str = field(default=None)
    contributors: List[str] = field(default=None)
    service_desk_id: str = field(default=None)
    service_desk_type: str = field(default=None)
    assignee_id: str = field(default=None)
    notes: str = field(default=None)
    acknowledgment: bool = field(default=None)
    priority: int = field(default=None)
    type: str = field(default=None)


@dataclass
class UpdateInvestigationInput(InvestigationInput):
    """ Describes the fields available for updating an investigation. """
    pass


@dataclass
class SnowCredentials:
    """ Represents credentials required for SNOW authentication """
    user: str = field(default=None)
    password: str = field(default=None)


@dataclass
class ActivityLogInput:
    """ Describes the fields available for creating a new Activity Log. """
    description: str = field(default=None)
    type: str = field(default=None)
    comment: str = field(default=None)
    target: str = field(default=None)
