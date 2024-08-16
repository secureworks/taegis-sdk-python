"""Vdr Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum


class VdrSortOrder(str, Enum):
    """VdrSortOrder."""

    ASC = "ASC"
    DESC = "DESC"


class VdrAssetType(str, Enum):
    """VdrAssetType."""

    SERVERS = "servers"
    SITES = "sites"


class VdrAssetsSortMode(str, Enum):
    """VdrAssetsSortMode."""

    SCORE = "SCORE"
    LOCATION = "LOCATION"
    LAST_REPORT = "LAST_REPORT"


class VdrVulnerabilitiesSortMode(str, Enum):
    """VdrVulnerabilitiesSortMode."""

    SEVERITY = "SEVERITY"
    DESCRIPTION = "DESCRIPTION"
    PRIORITY = "PRIORITY"


class VdrVulnerabilitySeverity(str, Enum):
    """VdrVulnerabilitySeverity."""

    CRITICAL = "CRITICAL"
    MEDIUM = "MEDIUM"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrApiEntityLinks:
    """VdrApiEntityLinks."""

    default_response: Optional[str] = field(
        default=None, metadata=config(field_name="defaultResponse")
    )
    delete: Optional[str] = field(default=None, metadata=config(field_name="delete"))
    edit: Optional[str] = field(default=None, metadata=config(field_name="edit"))
    history: Optional[str] = field(default=None, metadata=config(field_name="history"))
    logs: Optional[str] = field(default=None, metadata=config(field_name="logs"))
    reports: Optional[str] = field(default=None, metadata=config(field_name="reports"))
    scan: Optional[str] = field(default=None, metadata=config(field_name="scan"))
    schedule: Optional[str] = field(
        default=None, metadata=config(field_name="schedule")
    )
    self: Optional[str] = field(default=None, metadata=config(field_name="self"))
    tag: Optional[str] = field(default=None, metadata=config(field_name="tag"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrAssetFeatures:
    """VdrAssetFeatures."""

    content_type: Optional[List[str]] = field(
        default=None, metadata=config(field_name="contentType")
    )
    recognized_response: Optional[List[str]] = field(
        default=None, metadata=config(field_name="recognizedResponse")
    )
    scheme: Optional[List[str]] = field(
        default=None, metadata=config(field_name="scheme")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrAssetFingerprint:
    """VdrAssetFingerprint."""

    creation_date: Optional[str] = field(
        default=None, metadata=config(field_name="creationDate")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrAssetSchedule:
    """VdrAssetSchedule."""

    kill_time: Optional[str] = field(
        default=None, metadata=config(field_name="killTime")
    )
    monthday: Optional[int] = field(
        default=None, metadata=config(field_name="monthday")
    )
    period: Optional[str] = field(default=None, metadata=config(field_name="period"))
    retry_count: Optional[int] = field(
        default=None, metadata=config(field_name="retryCount")
    )
    retry_delay: Optional[int] = field(
        default=None, metadata=config(field_name="retryDelay")
    )
    start_time: Optional[str] = field(
        default=None, metadata=config(field_name="startTime")
    )
    weekday: Optional[str] = field(default=None, metadata=config(field_name="weekday"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrAssetInputArgs:
    """VdrAssetInputArgs."""

    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrNetConfig:
    """VdrNetConfig."""

    dns: Optional[List[str]] = field(default=None, metadata=config(field_name="dns"))
    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    gateway: Optional[str] = field(default=None, metadata=config(field_name="gateway"))
    netmask: Optional[str] = field(default=None, metadata=config(field_name="netmask"))
    static_ip: Optional[str] = field(
        default=None, metadata=config(field_name="staticIP")
    )
    use_dhcp: Optional[bool] = field(
        default=None, metadata=config(field_name="useDHCP")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrStatistics:
    """VdrStatistics."""

    cpu_count: Optional[int] = field(
        default=None, metadata=config(field_name="cpuCount")
    )
    cpu_load_average: Optional[float] = field(
        default=None, metadata=config(field_name="cpuLoadAverage")
    )
    deploy_mode: Optional[str] = field(
        default=None, metadata=config(field_name="deployMode")
    )
    memory_available: Optional[int] = field(
        default=None, metadata=config(field_name="memoryAvailable")
    )
    memory_total: Optional[int] = field(
        default=None, metadata=config(field_name="memoryTotal")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrAffectedHost:
    """VdrAffectedHost."""

    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))
    address: Optional[str] = field(default=None, metadata=config(field_name="address"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrInspectHostArgs:
    """VdrInspectHostArgs."""

    hosts: Optional[List[str]] = field(
        default=None, metadata=config(field_name="hosts")
    )
    alert_detail: Optional[str] = field(
        default=None, metadata=config(field_name="alertDetail")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrTenant:
    """VdrTenant."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    instance: Optional[str] = field(
        default=None, metadata=config(field_name="instance")
    )
    xdr_tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="xdrTenantId")
    )
    host_url: Optional[str] = field(default=None, metadata=config(field_name="hostUrl"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrVulnerabilityDetailsInputArgs:
    """VdrVulnerabilityDetailsInputArgs."""

    vulnerability_group_id: Optional[str] = field(
        default=None, metadata=config(field_name="vulnerabilityGroupId")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrVulnerabilityDetail:
    """VdrVulnerabilityDetail."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    assessment_date: Optional[str] = field(
        default=None, metadata=config(field_name="assessmentDate")
    )
    assessment_user_id: Optional[int] = field(
        default=None, metadata=config(field_name="assessmentUserId")
    )
    classification: Optional[str] = field(
        default=None, metadata=config(field_name="classification")
    )
    cve_number: Optional[str] = field(
        default=None, metadata=config(field_name="cveNumber")
    )
    definition_hash: Optional[str] = field(
        default=None, metadata=config(field_name="definitionHash")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    detail: Optional[str] = field(default=None, metadata=config(field_name="detail"))
    detection_hash: Optional[str] = field(
        default=None, metadata=config(field_name="detectionHash")
    )
    detection_identity: Optional[str] = field(
        default=None, metadata=config(field_name="detectionIdentity")
    )
    first_discovery_date: Optional[str] = field(
        default=None, metadata=config(field_name="firstDiscoveryDate")
    )
    fixed_in_version: Optional[str] = field(
        default=None, metadata=config(field_name="fixedInVersion")
    )
    host: Optional[str] = field(default=None, metadata=config(field_name="host"))
    host_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="hostIds")
    )
    http_code: Optional[int] = field(
        default=None, metadata=config(field_name="httpCode")
    )
    http_method: Optional[str] = field(
        default=None, metadata=config(field_name="httpMethod")
    )
    installed_version: Optional[str] = field(
        default=None, metadata=config(field_name="installedVersion")
    )
    is_verified: Optional[bool] = field(
        default=None, metadata=config(field_name="isVerified")
    )
    kb_number: Optional[str] = field(
        default=None, metadata=config(field_name="kbNumber")
    )
    last_seen_date: Optional[str] = field(
        default=None, metadata=config(field_name="lastSeenDate")
    )
    param: Optional[str] = field(default=None, metadata=config(field_name="param"))
    payload: Optional[str] = field(default=None, metadata=config(field_name="payload"))
    plan_assign_date: Optional[str] = field(
        default=None, metadata=config(field_name="planAssignDate")
    )
    plan_number: Optional[str] = field(
        default=None, metadata=config(field_name="planNumber")
    )
    plan_user_id: Optional[str] = field(
        default=None, metadata=config(field_name="planUserID")
    )
    port: Optional[int] = field(default=None, metadata=config(field_name="port"))
    protocol: Optional[str] = field(
        default=None, metadata=config(field_name="protocol")
    )
    score_base: Optional[float] = field(
        default=None, metadata=config(field_name="scoreBase")
    )
    score_final_normalized: Optional[float] = field(
        default=None, metadata=config(field_name="scoreFinalNormalized")
    )
    severity: Optional[str] = field(
        default=None, metadata=config(field_name="severity")
    )
    snooze_until_date: Optional[str] = field(
        default=None, metadata=config(field_name="snoozeUntilDate")
    )
    software: Optional[str] = field(
        default=None, metadata=config(field_name="software")
    )
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))
    verify_date: Optional[str] = field(
        default=None, metadata=config(field_name="verifyDate")
    )
    verify_user_id: Optional[str] = field(
        default=None, metadata=config(field_name="verifyUserId")
    )
    vulnerability_identity: Optional[str] = field(
        default=None, metadata=config(field_name="vulnerabilityIdentity")
    )
    vulnerable_range: Optional[str] = field(
        default=None, metadata=config(field_name="vulnerableRange")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrVulnerabilityDetailsHttpHeaders:
    """VdrVulnerabilityDetailsHttpHeaders."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrVulnScore:
    """VdrVulnScore."""

    base: Optional[float] = field(default=None, metadata=config(field_name="base"))
    codes: Optional[List[str]] = field(
        default=None, metadata=config(field_name="codes")
    )
    path40: Optional[str] = field(default=None, metadata=config(field_name="path40"))
    sortable: Optional[float] = field(
        default=None, metadata=config(field_name="sortable")
    )
    step_base: Optional[float] = field(
        default=None, metadata=config(field_name="stepBase")
    )
    step_final: Optional[float] = field(
        default=None, metadata=config(field_name="stepFinal")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrTimeFilterInputArgs:
    """VdrTimeFilterInputArgs."""

    from_: Optional[str] = field(default=None, metadata=config(field_name="from"))
    to: Optional[str] = field(default=None, metadata=config(field_name="to"))
    relative: Optional[int] = field(
        default=None, metadata=config(field_name="relative")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrAssetsFiltersInputArgs:
    """VdrAssetsFiltersInputArgs."""

    cve: Optional[List[str]] = field(default=None, metadata=config(field_name="cve"))
    asset_type: Optional[List[Union[VdrAssetType, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(VdrAssetType, x),
            field_name="assetType",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrDefinition:
    """VdrDefinition."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    cvssv2: Optional[str] = field(default=None, metadata=config(field_name="cvssv2"))
    cvssv3: Optional[str] = field(default=None, metadata=config(field_name="cvssv3"))
    references: Optional[List[str]] = field(
        default=None, metadata=config(field_name="references")
    )
    is_detectable_externally: Optional[bool] = field(
        default=None, metadata=config(field_name="isDetectableExternally")
    )
    is_detectable_internally: Optional[bool] = field(
        default=None, metadata=config(field_name="isDetectableInternally")
    )
    affected_hosts: Optional[List[VdrAffectedHost]] = field(
        default=None, metadata=config(field_name="affectedHosts")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrVulnerabilityDetails:
    """VdrVulnerabilityDetails."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    vulnerability_details: Optional[List[VdrVulnerabilityDetail]] = field(
        default=None, metadata=config(field_name="vulnerabilityDetails")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrVulnerability:
    """VdrVulnerability."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    affected_tcp_ports: Optional[List[str]] = field(
        default=None, metadata=config(field_name="affectedTCPPorts")
    )
    affected_udp_ports: Optional[List[str]] = field(
        default=None, metadata=config(field_name="affectedUDPPorts")
    )
    aggregate_group: Optional[str] = field(
        default=None, metadata=config(field_name="aggregateGroup")
    )
    assessment_date: Optional[str] = field(
        default=None, metadata=config(field_name="assessmentDate")
    )
    assessment_user_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="assessmentUserIds")
    )
    attack_class: Optional[List[str]] = field(
        default=None, metadata=config(field_name="attackClass")
    )
    classification: Optional[str] = field(
        default=None, metadata=config(field_name="classification")
    )
    columns: Optional[List[str]] = field(
        default=None, metadata=config(field_name="columns")
    )
    cve_number: Optional[str] = field(
        default=None, metadata=config(field_name="cveNumber")
    )
    definition_hash: Optional[str] = field(
        default=None, metadata=config(field_name="definitionHash")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    differentiator: Optional[str] = field(
        default=None, metadata=config(field_name="differentiator")
    )
    first_discovery_date: Optional[str] = field(
        default=None, metadata=config(field_name="firstDiscoveryDate")
    )
    fixed_in_version: Optional[str] = field(
        default=None, metadata=config(field_name="fixedInVersion")
    )
    has_note: Optional[bool] = field(
        default=None, metadata=config(field_name="hasNote")
    )
    has_threat_intel: Optional[bool] = field(
        default=None, metadata=config(field_name="hasThreatIntel")
    )
    has_verified: Optional[bool] = field(
        default=None, metadata=config(field_name="hasVerified")
    )
    host: Optional[str] = field(default=None, metadata=config(field_name="host"))
    host_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="hostIds")
    )
    http_code: Optional[int] = field(
        default=None, metadata=config(field_name="httpCode")
    )
    http_method: Optional[str] = field(
        default=None, metadata=config(field_name="httpMethod")
    )
    identity: Optional[str] = field(
        default=None, metadata=config(field_name="identity")
    )
    is_verified: Optional[bool] = field(
        default=None, metadata=config(field_name="isVerified")
    )
    last_seen_date: Optional[str] = field(
        default=None, metadata=config(field_name="lastSeenDate")
    )
    note_date: Optional[str] = field(
        default=None, metadata=config(field_name="noteDate")
    )
    param: Optional[str] = field(default=None, metadata=config(field_name="param"))
    payload: Optional[str] = field(default=None, metadata=config(field_name="payload"))
    plan_assign_date: Optional[str] = field(
        default=None, metadata=config(field_name="planAssignDate")
    )
    plan_id: Optional[str] = field(default=None, metadata=config(field_name="planId"))
    plan_user_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="planUserIds")
    )
    port: Optional[int] = field(default=None, metadata=config(field_name="port"))
    priority: Optional[str] = field(
        default=None, metadata=config(field_name="priority")
    )
    protocol: Optional[str] = field(
        default=None, metadata=config(field_name="protocol")
    )
    related_exploit_urls: Optional[List[str]] = field(
        default=None, metadata=config(field_name="relatedExploitUrls")
    )
    severity: Optional[str] = field(
        default=None, metadata=config(field_name="severity")
    )
    top_cve_numbers: Optional[List[str]] = field(
        default=None, metadata=config(field_name="topCveNumbers")
    )
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))
    verify_date: Optional[str] = field(
        default=None, metadata=config(field_name="verifyDate")
    )
    verify_user_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="verifyUserIds")
    )
    score: Optional[VdrVulnScore] = field(
        default=None, metadata=config(field_name="score")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrInspectHost:
    """VdrInspectHost."""

    definitions: Optional[List[VdrDefinition]] = field(
        default=None, metadata=config(field_name="definitions")
    )
    matching_vulnerability_groups: Optional[List[VdrVulnerability]] = field(
        default=None, metadata=config(field_name="matchingVulnerabilityGroups")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrVulnerabilitiesFiltersInputArgs:
    """VdrVulnerabilitiesFiltersInputArgs."""

    cve: Optional[List[str]] = field(default=None, metadata=config(field_name="cve"))
    severity: Optional[List[Union[VdrVulnerabilitySeverity, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(VdrVulnerabilitySeverity, x),
            field_name="severity",
        ),
    )
    first_discovery_date: Optional[VdrTimeFilterInputArgs] = field(
        default=None, metadata=config(field_name="firstDiscoveryDate")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrEdgeService:
    """VdrEdgeService."""

    id: Optional[int] = field(default=None, metadata=config(field_name="id"))
    concurrency_limit: Optional[int] = field(
        default=None, metadata=config(field_name="concurrencyLimit")
    )
    creation_date: Optional[str] = field(
        default=None, metadata=config(field_name="creationDate")
    )
    creation_status: Optional[str] = field(
        default=None, metadata=config(field_name="creationStatus")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    download_url: Optional[str] = field(
        default=None, metadata=config(field_name="downloadURL")
    )
    identifier: Optional[str] = field(
        default=None, metadata=config(field_name="identifier")
    )
    is_assigned: Optional[bool] = field(
        default=None, metadata=config(field_name="isAssigned")
    )
    is_available: Optional[bool] = field(
        default=None, metadata=config(field_name="isAvailable")
    )
    is_connected: Optional[bool] = field(
        default=None, metadata=config(field_name="isConnected")
    )
    keys_status: Optional[str] = field(
        default=None, metadata=config(field_name="keysStatus")
    )
    label: Optional[str] = field(default=None, metadata=config(field_name="label"))
    last_connect_date: Optional[str] = field(
        default=None, metadata=config(field_name="lastConnectDate")
    )
    platform: Optional[str] = field(
        default=None, metadata=config(field_name="platform")
    )
    port: Optional[int] = field(default=None, metadata=config(field_name="port"))
    scan_cluster: Optional[str] = field(
        default=None, metadata=config(field_name="scanCluster")
    )
    current_net_config: Optional[VdrNetConfig] = field(
        default=None, metadata=config(field_name="currentNetConfig")
    )
    net_config: Optional[VdrNetConfig] = field(
        default=None, metadata=config(field_name="netConfig")
    )
    statistics: Optional[VdrStatistics] = field(
        default=None, metadata=config(field_name="statistics")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrAssetsInputArgs:
    """VdrAssetsInputArgs."""

    offset: Optional[int] = field(default=None, metadata=config(field_name="offset"))
    limit: Optional[int] = field(default=None, metadata=config(field_name="limit"))
    sort_by: Optional[Union[VdrAssetsSortMode, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(VdrAssetsSortMode, x),
            field_name="sortBy",
        ),
    )
    sort_order: Optional[Union[VdrSortOrder, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(VdrSortOrder, x),
            field_name="sortOrder",
        ),
    )
    filters: Optional[VdrAssetsFiltersInputArgs] = field(
        default=None, metadata=config(field_name="filters")
    )
    exclude_filters: Optional[VdrAssetsFiltersInputArgs] = field(
        default=None, metadata=config(field_name="excludeFilters")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrVulnerabilitiesInputArgs:
    """VdrVulnerabilitiesInputArgs."""

    host_id: Optional[str] = field(default=None, metadata=config(field_name="hostId"))
    host_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="hostIds")
    )
    offset: Optional[int] = field(default=None, metadata=config(field_name="offset"))
    limit: Optional[int] = field(default=None, metadata=config(field_name="limit"))
    sort_by: Optional[Union[VdrVulnerabilitiesSortMode, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(VdrVulnerabilitiesSortMode, x),
            field_name="sortBy",
        ),
    )
    sort_order: Optional[Union[VdrSortOrder, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(VdrSortOrder, x),
            field_name="sortOrder",
        ),
    )
    filters: Optional[VdrVulnerabilitiesFiltersInputArgs] = field(
        default=None, metadata=config(field_name="filters")
    )
    exclude_filters: Optional[VdrVulnerabilitiesFiltersInputArgs] = field(
        default=None, metadata=config(field_name="excludeFilters")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrAsset:
    """VdrAsset."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    authentication_status: Optional[List[str]] = field(
        default=None, metadata=config(field_name="authenticationStatus")
    )
    contact_information: Optional[str] = field(
        default=None, metadata=config(field_name="contactInformation")
    )
    creation_date: Optional[str] = field(
        default=None, metadata=config(field_name="creationDate")
    )
    creation_type: Optional[str] = field(
        default=None, metadata=config(field_name="creationType")
    )
    days_until_autoremove: Optional[int] = field(
        default=None, metadata=config(field_name="daysUntilAutoremove")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    deterrents: Optional[List[str]] = field(
        default=None, metadata=config(field_name="deterrents")
    )
    exposure: Optional[List[str]] = field(
        default=None, metadata=config(field_name="exposure")
    )
    high_cps: Optional[float] = field(
        default=None, metadata=config(field_name="highCps")
    )
    high_cvss: Optional[float] = field(
        default=None, metadata=config(field_name="highCvss")
    )
    host_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="hostIds")
    )
    hostname: Optional[str] = field(
        default=None, metadata=config(field_name="hostname")
    )
    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    is_active: Optional[bool] = field(
        default=None, metadata=config(field_name="isActive")
    )
    is_discovered: Optional[bool] = field(
        default=None, metadata=config(field_name="isDiscovered")
    )
    last_report_date: Optional[str] = field(
        default=None, metadata=config(field_name="lastReportDate")
    )
    last_seen_date: Optional[str] = field(
        default=None, metadata=config(field_name="lastSeenDate")
    )
    location: Optional[str] = field(
        default=None, metadata=config(field_name="location")
    )
    mac_vendor: Optional[str] = field(
        default=None, metadata=config(field_name="macVendor")
    )
    os_family: Optional[str] = field(
        default=None, metadata=config(field_name="osFamily")
    )
    os_name: Optional[str] = field(default=None, metadata=config(field_name="osName"))
    os_type: Optional[str] = field(default=None, metadata=config(field_name="osType"))
    scan_duration: Optional[float] = field(
        default=None, metadata=config(field_name="scanDuration")
    )
    status: Optional[str] = field(default=None, metadata=config(field_name="status"))
    tags: Optional[List[str]] = field(default=None, metadata=config(field_name="tags"))
    team_id: Optional[int] = field(default=None, metadata=config(field_name="teamID"))
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))
    has_ping: Optional[bool] = field(
        default=None, metadata=config(field_name="hasPing")
    )
    has_default_response_har: Optional[bool] = field(
        default=None, metadata=config(field_name="hasDefaultResponseHar")
    )
    start_url: Optional[str] = field(
        default=None, metadata=config(field_name="startURL")
    )
    static_ip_address: Optional[str] = field(
        default=None, metadata=config(field_name="staticIPAddress")
    )
    type: Optional[Union[VdrAssetType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(VdrAssetType, x),
            field_name="type",
        ),
    )
    links: Optional[VdrApiEntityLinks] = field(
        default=None, metadata=config(field_name="links")
    )
    features: Optional[VdrAssetFeatures] = field(
        default=None, metadata=config(field_name="features")
    )
    fingerprints: Optional[List[VdrAssetFingerprint]] = field(
        default=None, metadata=config(field_name="fingerprints")
    )
    schedule: Optional[VdrAssetSchedule] = field(
        default=None, metadata=config(field_name="schedule")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrAssets:
    """VdrAssets."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    assets: Optional[List[VdrAsset]] = field(
        default=None, metadata=config(field_name="assets")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrEdgeServices:
    """VdrEdgeServices."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    edge_services: Optional[List[VdrEdgeService]] = field(
        default=None, metadata=config(field_name="edgeServices")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VdrVulnerabilities:
    """VdrVulnerabilities."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    vulnerabilities: Optional[List[VdrVulnerability]] = field(
        default=None, metadata=config(field_name="vulnerabilities")
    )
