from enum import Enum, IntEnum
from typing import List


class PriorityEnum(IntEnum):
    Critical = 4
    High = 3
    Medium = 2
    Low = 1


class InvestigationTypes(str):
    SECURITY_INVESTIGATION = "Security Investigation"
    MDR_THREAT = "MDR Threat Hunt"
    INCIDENT_RESPONSE = "Incident Response"
    THREAT_HUNT = "Threat Hunt"
    CTU_THREAT_HUNT = "CTU Threat Hunt"


class InvestigationStatusEnum(Enum):
    """A class to define investigation status states"""

    Open = "Open"
    Active = "Active"
    AwaitingAction = "Awaiting Action"
    Suspended = "Suspended"
    ClosedConfirmedSecIncident = "Closed: Confirmed Security Incident"
    ClosedAuthorizedActivity = "Closed: Authorized Activity"
    ClosedThreatMitigated = "Closed: Threat Mitigated"
    ClosedNotVulnerable = "Closed: Not Vulnerable"
    ClosedFalsePositiveAlert = "Closed: False Positive Alert"
    ClosedInconclusive = "Closed: Inconclusive"

    @staticmethod
    def as_value_list(*args):
        """
        To get all statuses no args
        """
        if not args:
            return list(map(lambda c: c.value, InvestigationStatusEnum))
        else:
            return list(map(lambda c: c.value, args))

    @staticmethod
    def closed() -> List["InvestigationStatusEnum"]:
        return list(filter(lambda x: x.name.startswith("Closed"), InvestigationStatusEnum))


class OrderFieldInput(str):
    id = "id"
    tenant_id = "tenant_id"
    tags = "tags"
    genesis_alerts = "genesis_alerts"
    genesis_events = "genesis_events"
    alerts = "alerts"
    events = "events"
    assets = "assets"
    auth_credentials = "auth_credentials"
    key_findings = "key_findings"
    description = "description"
    created_at = "created_at"
    updated_at = "updated_at"
    notified_at = "notified_at"
    created_by = "created_by"
    status = "status"
    contributors = "contributors"
    service_desk_id = "service_desk_id"
    service_desk_type = "service_desk_type"
    all_alerts = "all_alerts"
    all_events = "all_events"
    priority = "priority"
    type = "type"


class OrderDirectionInput(str):
    asc = "asc"
    desc = "desc"


class InvestigationProcessingState(str):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
