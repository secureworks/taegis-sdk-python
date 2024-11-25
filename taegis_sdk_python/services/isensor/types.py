"""Isensor Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum


class ISensorMode(str, Enum):
    """ISensorMode."""

    INLINE_BLOCKING = "INLINE_BLOCKING"
    INLINE_PASSIVE = "INLINE_PASSIVE"
    SNIFFER = "SNIFFER"
    NONE = "NONE"


class IsensorJobState(str, Enum):
    """IsensorJobState."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PARTIAL = "PARTIAL"


class IsensorRvcState(str, Enum):
    """IsensorRvcState."""

    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class IsensorRuleAction(str, Enum):
    """IsensorRuleAction."""

    SHUN = "SHUN"
    BYPASS = "BYPASS"
    TRUST = "TRUST"


class IsensorRuleActionInput(str, Enum):
    """IsensorRuleActionInput."""

    SHUN = "SHUN"
    BYPASS = "BYPASS"
    TRUST = "TRUST"


class IsensorHealth(str, Enum):
    """IsensorHealth."""

    HEALTHY = "HEALTHY"
    NO_DATA = "NO_DATA"
    WARNING = "WARNING"
    UNREGISTERED = "UNREGISTERED"


class IsensorReportResultSortOrder(str, Enum):
    """IsensorReportResultSortOrder."""

    ASC = "ASC"
    DESC = "DESC"


class IsensorReportResultSortBy(str, Enum):
    """IsensorReportResultSortBy."""

    REPORT_TIME = "REPORT_TIME"
    REPORT_NAME = "REPORT_NAME"
    REPORT_TYPE = "REPORT_TYPE"


class IsensorReportFormat(str, Enum):
    """IsensorReportFormat."""

    PDF = "PDF"
    CSV = "CSV"
    JSON = "JSON"


class IsensorReportTimePeriod(str, Enum):
    """IsensorReportTimePeriod."""

    CUSTOM = "CUSTOM"
    TODAY = "TODAY"
    YESTERDAY = "YESTERDAY"
    LAST_24_HRS = "LAST_24_HRS"
    LAST_7_DAYS = "LAST_7_DAYS"
    LAST_15_DAYS = "LAST_15_DAYS"
    LAST_30_DAYS = "LAST_30_DAYS"
    LAST_60_DAYS = "LAST_60_DAYS"
    LAST_90_DAYS = "LAST_90_DAYS"
    MONTH_TO_DATE = "MONTH_TO_DATE"
    QUARTER_TO_DATE = "QUARTER_TO_DATE"
    YEAR_TO_DATE = "YEAR_TO_DATE"
    LAST_12_MONTHS = "LAST_12_MONTHS"
    PREVIOUS_MONTH = "PREVIOUS_MONTH"
    PREVIOUS_QUARTER = "PREVIOUS_QUARTER"
    PREVIOUS_YEAR = "PREVIOUS_YEAR"


class NdrMaintenanceFreq(str, Enum):
    """NdrMaintenanceFreq."""

    YEARLY = "YEARLY"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"
    DAILY = "DAILY"


class NdrWeekDay(str, Enum):
    """NdrWeekDay."""

    SUN = "SUN"
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"


class NdrEventDeviceStatus(str, Enum):
    """NdrEventDeviceStatus."""

    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    NEW = "NEW"
    PREVIEWED = "PREVIEWED"
    RESCHEDULED = "RESCHEDULED"
    SCHEDULED = "SCHEDULED"
    SUCCEEDED = "SUCCEEDED"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorJobLogs:
    """IsensorJobLogs."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    text: Optional[str] = field(default=None, metadata=config(field_name="text"))
    time_stamp: Optional[str] = field(
        default=None, metadata=config(field_name="timeStamp")
    )
    more_entries: Optional[bool] = field(
        default=None, metadata=config(field_name="moreEntries")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorFirewallRuleInput:
    """IsensorFirewallRuleInput."""

    src_addr: Optional[str] = field(default=None, metadata=config(field_name="srcAddr"))
    dst_addr: Optional[str] = field(default=None, metadata=config(field_name="dstAddr"))
    src_port: Optional[str] = field(default=None, metadata=config(field_name="srcPort"))
    dst_port: Optional[str] = field(default=None, metadata=config(field_name="dstPort"))
    protocol: Optional[str] = field(
        default=None, metadata=config(field_name="protocol")
    )
    end_date: Optional[str] = field(default=None, metadata=config(field_name="endDate"))
    start_date: Optional[str] = field(
        default=None, metadata=config(field_name="startDate")
    )
    optional: Optional[str] = field(
        default=None, metadata=config(field_name="optional")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorDeployCustomizationsPayload:
    """IsensorDeployCustomizationsPayload."""

    job_name: Optional[str] = field(default=None, metadata=config(field_name="jobName"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ISensorArtifact:
    """ISensorArtifact."""

    location: Optional[str] = field(
        default=None, metadata=config(field_name="location")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorRuleVariableCustomizationsInput:
    """IsensorRuleVariableCustomizationsInput."""

    rule_variable_name: Optional[str] = field(
        default=None, metadata=config(field_name="ruleVariableName")
    )
    rule_variable_new_value: Optional[str] = field(
        default=None, metadata=config(field_name="ruleVariableNewValue")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorChangeMgmtReportList:
    """IsensorChangeMgmtReportList."""

    ack_required: Optional[bool] = field(
        default=None, metadata=config(field_name="ackRequired")
    )
    acknowledged: Optional[str] = field(
        default=None, metadata=config(field_name="acknowledged")
    )
    is_shared: Optional[bool] = field(
        default=None, metadata=config(field_name="isShared")
    )
    is_viewed: Optional[bool] = field(
        default=None, metadata=config(field_name="isViewed")
    )
    report_category: Optional[str] = field(
        default=None, metadata=config(field_name="reportCategory")
    )
    report_id: Optional[str] = field(
        default=None, metadata=config(field_name="reportId")
    )
    report_name: Optional[str] = field(
        default=None, metadata=config(field_name="reportName")
    )
    report_time: Optional[str] = field(
        default=None, metadata=config(field_name="reportTime")
    )
    report_type: Optional[str] = field(
        default=None, metadata=config(field_name="reportType")
    )
    run_frequency: Optional[str] = field(
        default=None, metadata=config(field_name="runFrequency")
    )
    start_time: Optional[str] = field(
        default=None, metadata=config(field_name="startTime")
    )
    submission_time: Optional[str] = field(
        default=None, metadata=config(field_name="submissionTime")
    )
    state: Optional[str] = field(default=None, metadata=config(field_name="state"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorReportRule:
    """IsensorReportRule."""

    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorJob:
    """IsensorJob."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    status: Optional[Union[IsensorJobState, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(IsensorJobState, x),
            field_name="status",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorFirewallRule:
    """IsensorFirewallRule."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    src_addr: Optional[str] = field(default=None, metadata=config(field_name="srcAddr"))
    dst_addr: Optional[str] = field(default=None, metadata=config(field_name="dstAddr"))
    src_port: Optional[str] = field(default=None, metadata=config(field_name="srcPort"))
    dst_port: Optional[str] = field(default=None, metadata=config(field_name="dstPort"))
    protocol: Optional[str] = field(
        default=None, metadata=config(field_name="protocol")
    )
    end_date: Optional[str] = field(default=None, metadata=config(field_name="endDate"))
    start_date: Optional[str] = field(
        default=None, metadata=config(field_name="startDate")
    )
    optional: Optional[str] = field(
        default=None, metadata=config(field_name="optional")
    )
    rule: Optional[Union[IsensorRuleAction, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(IsensorRuleAction, x),
            field_name="rule",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorFirewallRulePayload:
    """IsensorFirewallRulePayload."""

    job_name: Optional[str] = field(default=None, metadata=config(field_name="jobName"))
    firewall_rules: Optional[List[IsensorFirewallRule]] = field(
        default=None, metadata=config(field_name="firewallRules")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorRuleVariableCustomizationsPayload:
    """IsensorRuleVariableCustomizationsPayload."""

    rule_variable_name: Optional[str] = field(
        default=None, metadata=config(field_name="ruleVariableName")
    )
    rule_variable_new_value: Optional[str] = field(
        default=None, metadata=config(field_name="ruleVariableNewValue")
    )
    message: Optional[str] = field(default=None, metadata=config(field_name="message"))
    status: Optional[Union[IsensorRvcState, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(IsensorRvcState, x),
            field_name="status",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorChangeMgmtReportInput:
    """IsensorChangeMgmtReportInput."""

    schedule_name: Optional[str] = field(
        default=None, metadata=config(field_name="scheduleName")
    )
    from_date: Optional[str] = field(
        default=None, metadata=config(field_name="fromDate")
    )
    to_date: Optional[str] = field(default=None, metadata=config(field_name="toDate"))
    recurrence_type: Optional[str] = field(
        default=None, metadata=config(field_name="recurrenceType")
    )
    include_details: Optional[bool] = field(
        default=None, metadata=config(field_name="includeDetails")
    )
    preferred_report_output: Optional[str] = field(
        default=None, metadata=config(field_name="preferredReportOutput")
    )
    time_period: Optional[Union[IsensorReportTimePeriod, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(IsensorReportTimePeriod, x),
            field_name="timePeriod",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NdrMaintenanceWindowInput:
    """NdrMaintenanceWindowInput."""

    internal_device_name: Optional[str] = field(
        default=None, metadata=config(field_name="internalDeviceName")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    start_hour: Optional[int] = field(
        default=None, metadata=config(field_name="startHour")
    )
    timezone: Optional[str] = field(
        default=None, metadata=config(field_name="timezone")
    )
    start_date: Optional[str] = field(
        default=None, metadata=config(field_name="startDate")
    )
    duration: Optional[int] = field(
        default=None, metadata=config(field_name="duration")
    )
    all_tenant_devices: Optional[bool] = field(
        default=None, metadata=config(field_name="allTenantDevices")
    )
    outage_permitted: Optional[bool] = field(
        default=None, metadata=config(field_name="outagePermitted")
    )
    week_day: Optional[Union[NdrWeekDay, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(NdrWeekDay, x),
            field_name="weekDay",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorChangeMgmtReportPayload:
    """IsensorChangeMgmtReportPayload."""

    schedule_name: Optional[str] = field(
        default=None, metadata=config(field_name="scheduleName")
    )
    from_date: Optional[str] = field(
        default=None, metadata=config(field_name="fromDate")
    )
    to_date: Optional[str] = field(default=None, metadata=config(field_name="toDate"))
    recurrence_type: Optional[str] = field(
        default=None, metadata=config(field_name="recurrenceType")
    )
    include_details: Optional[bool] = field(
        default=None, metadata=config(field_name="includeDetails")
    )
    preferred_report_output: Optional[str] = field(
        default=None, metadata=config(field_name="preferredReportOutput")
    )
    location: Optional[str] = field(
        default=None, metadata=config(field_name="location")
    )
    time_period: Optional[Union[IsensorReportTimePeriod, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(IsensorReportTimePeriod, x),
            field_name="timePeriod",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorReportRuleset:
    """IsensorReportRuleset."""

    rollout_date: Optional[str] = field(
        default=None, metadata=config(field_name="rolloutDate")
    )
    rules_added: Optional[str] = field(
        default=None, metadata=config(field_name="rulesAdded")
    )
    rules_changed: Optional[str] = field(
        default=None, metadata=config(field_name="rulesChanged")
    )
    rules_deleted: Optional[str] = field(
        default=None, metadata=config(field_name="rulesDeleted")
    )
    ruleset_version: Optional[str] = field(
        default=None, metadata=config(field_name="rulesetVersion")
    )
    rules: Optional[List[IsensorReportRule]] = field(
        default=None, metadata=config(field_name="rules")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NdrEventDeviceResult:
    """NdrEventDeviceResult."""

    event_device_id: Optional[str] = field(
        default=None, metadata=config(field_name="eventDeviceId")
    )
    internal_device_name: Optional[str] = field(
        default=None, metadata=config(field_name="internalDeviceName")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    start_date: Optional[str] = field(
        default=None, metadata=config(field_name="startDate")
    )
    deferrable: Optional[bool] = field(
        default=None, metadata=config(field_name="deferrable")
    )
    status: Optional[Union[NdrEventDeviceStatus, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(NdrEventDeviceStatus, x),
            field_name="status",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NdrDeferEventDeviceResult:
    """NdrDeferEventDeviceResult."""

    event_device_id: Optional[str] = field(
        default=None, metadata=config(field_name="eventDeviceId")
    )
    internal_device_name: Optional[str] = field(
        default=None, metadata=config(field_name="internalDeviceName")
    )
    start_date: Optional[str] = field(
        default=None, metadata=config(field_name="startDate")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    status: Optional[Union[NdrEventDeviceStatus, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(NdrEventDeviceStatus, x),
            field_name="status",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorDetail:
    """IsensorDetail."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    uin: Optional[str] = field(default=None, metadata=config(field_name="uin"))
    rule_set_version: Optional[str] = field(
        default=None, metadata=config(field_name="ruleSetVersion")
    )
    subscription_type: Optional[str] = field(
        default=None, metadata=config(field_name="subscriptionType")
    )
    home_net: Optional[str] = field(default=None, metadata=config(field_name="homeNet"))
    external_net: Optional[str] = field(
        default=None, metadata=config(field_name="externalNet")
    )
    http_ports: Optional[str] = field(
        default=None, metadata=config(field_name="httpPorts")
    )
    dhcp: Optional[bool] = field(default=None, metadata=config(field_name="dhcp"))
    ip_address: Optional[str] = field(
        default=None, metadata=config(field_name="ipAddress")
    )
    tenant_name: Optional[str] = field(
        default=None, metadata=config(field_name="tenantName")
    )
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    is_partner: Optional[bool] = field(
        default=None, metadata=config(field_name="isPartner")
    )
    ndr_software_version: Optional[str] = field(
        default=None, metadata=config(field_name="ndrSoftwareVersion")
    )
    ips_engine_version: Optional[str] = field(
        default=None, metadata=config(field_name="ipsEngineVersion")
    )
    hw_type: Optional[str] = field(default=None, metadata=config(field_name="hwType"))
    mode: Optional[Union[ISensorMode, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(ISensorMode, x),
            field_name="mode",
        ),
    )
    health: Optional[Union[IsensorHealth, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(IsensorHealth, x),
            field_name="health",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NdrMaintenanceWindowResult:
    """NdrMaintenanceWindowResult."""

    internal_device_name: Optional[str] = field(
        default=None, metadata=config(field_name="internalDeviceName")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    device_id: Optional[str] = field(
        default=None, metadata=config(field_name="deviceId")
    )
    start_hour: Optional[int] = field(
        default=None, metadata=config(field_name="startHour")
    )
    timezone: Optional[str] = field(
        default=None, metadata=config(field_name="timezone")
    )
    start_date: Optional[str] = field(
        default=None, metadata=config(field_name="startDate")
    )
    duration: Optional[int] = field(
        default=None, metadata=config(field_name="duration")
    )
    all_tenant_devices: Optional[bool] = field(
        default=None, metadata=config(field_name="allTenantDevices")
    )
    outage_permitted: Optional[bool] = field(
        default=None, metadata=config(field_name="outagePermitted")
    )
    no_device: Optional[bool] = field(
        default=None, metadata=config(field_name="noDevice")
    )
    freq: Optional[Union[NdrMaintenanceFreq, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(NdrMaintenanceFreq, x),
            field_name="freq",
        ),
    )
    week_day: Optional[Union[NdrWeekDay, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(NdrWeekDay, x),
            field_name="weekDay",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorFirewallRules:
    """IsensorFirewallRules."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    shuns: Optional[List[IsensorFirewallRule]] = field(
        default=None, metadata=config(field_name="shuns")
    )
    trusts: Optional[List[IsensorFirewallRule]] = field(
        default=None, metadata=config(field_name="trusts")
    )
    bypasses: Optional[List[IsensorFirewallRule]] = field(
        default=None, metadata=config(field_name="bypasses")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorRuleChange:
    """IsensorRuleChange."""

    device_ip: Optional[str] = field(
        default=None, metadata=config(field_name="deviceIp")
    )
    device_name: Optional[str] = field(
        default=None, metadata=config(field_name="deviceName")
    )
    rules_added: Optional[str] = field(
        default=None, metadata=config(field_name="rulesAdded")
    )
    rules_changed: Optional[str] = field(
        default=None, metadata=config(field_name="rulesChanged")
    )
    rules_deleted: Optional[str] = field(
        default=None, metadata=config(field_name="rulesDeleted")
    )
    ruleset_rollouts: Optional[str] = field(
        default=None, metadata=config(field_name="rulesetRollouts")
    )
    rulesets: Optional[List[IsensorReportRuleset]] = field(
        default=None, metadata=config(field_name="rulesets")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsensorReportResult:
    """IsensorReportResult."""

    report_id: Optional[str] = field(
        default=None, metadata=config(field_name="reportId")
    )
    end_date: Optional[str] = field(default=None, metadata=config(field_name="endDate"))
    locale: Optional[str] = field(default=None, metadata=config(field_name="locale"))
    report_variation: Optional[str] = field(
        default=None, metadata=config(field_name="reportVariation")
    )
    start_date: Optional[str] = field(
        default=None, metadata=config(field_name="startDate")
    )
    user_time_zone: Optional[str] = field(
        default=None, metadata=config(field_name="userTimeZone")
    )
    isensor_rule_changes: Optional[List[IsensorRuleChange]] = field(
        default=None, metadata=config(field_name="isensorRuleChanges")
    )