"""EndpointManagementService Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class EndpointPlatform(str, Enum):
    """EndpointPlatform."""

    WINDOWS = "WINDOWS"
    MAC = "MAC"
    LINUX = "LINUX"


class PolicyType(str, Enum):
    """PolicyType."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"


class BulkAssignRequestStatus(str, Enum):
    """BulkAssignRequestStatus."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETE = "COMPLETE"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EndpointGroup:
    """EndpointGroup."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    registration_key: Optional[str] = field(
        default=None, metadata=config(field_name="registrationKey")
    )
    registration_key_expires_at: Optional[str] = field(
        default=None, metadata=config(field_name="registrationKeyExpiresAt")
    )
    policy_name: Optional[str] = field(
        default=None, metadata=config(field_name="policyName")
    )
    is_system_generated: Optional[bool] = field(
        default=None, metadata=config(field_name="isSystemGenerated")
    )
    is_default: Optional[bool] = field(
        default=None, metadata=config(field_name="isDefault")
    )
    desired_agent_version: Optional[str] = field(
        default=None, metadata=config(field_name="desiredAgentVersion")
    )
    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    skip_upgrade: Optional[bool] = field(
        default=None, metadata=config(field_name="skipUpgrade")
    )
    archive_endpoint_after_days: Optional[int] = field(
        default=None, metadata=config(field_name="ArchiveEndpointAfterDays")
    )
    is_archive_endpoint_enabled: Optional[bool] = field(
        default=None, metadata=config(field_name="IsArchiveEndpointEnabled")
    )
    file_analysis_flag: Optional[bool] = field(
        default=None, metadata=config(field_name="fileAnalysisFlag")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DeleteEndpointGrpInput:
    """DeleteEndpointGrpInput."""

    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Policy:
    """Policy."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    platform: Optional[str] = field(
        default=None, metadata=config(field_name="platform")
    )
    format: Optional[str] = field(default=None, metadata=config(field_name="format"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EndpointGroupArguments:
    """EndpointGroupArguments."""

    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BulkAssignRequestInput:
    """BulkAssignRequestInput."""

    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))
    endpoint_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="endpointIds")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PartialPageInfo:
    """PartialPageInfo."""

    last_evaluated_key: Optional[str] = field(
        default=None, metadata=config(field_name="lastEvaluatedKey")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CreateEndpointGroupInput:
    """CreateEndpointGroupInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    desired_agent_version: Optional[str] = field(
        default=None, metadata=config(field_name="desiredAgentVersion")
    )
    is_default: Optional[bool] = field(
        default=None, metadata=config(field_name="isDefault")
    )
    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    archive_endpoint_after_days: Optional[int] = field(
        default=None, metadata=config(field_name="ArchiveEndpointAfterDays")
    )
    file_analysis_flag: Optional[bool] = field(
        default=None, metadata=config(field_name="fileAnalysisFlag")
    )
    policy_name: Optional[PolicyType] = field(
        default=None, metadata=config(field_name="policyName")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateEndpointGroupInput:
    """UpdateEndpointGroupInput."""

    group_id: Optional[str] = field(default=None, metadata=config(field_name="groupId"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    desired_version: Optional[str] = field(
        default=None, metadata=config(field_name="desiredVersion")
    )
    channel: Optional[str] = field(default=None, metadata=config(field_name="channel"))
    archive_endpoint_after_days: Optional[int] = field(
        default=None, metadata=config(field_name="ArchiveEndpointAfterDays")
    )
    file_analysis_flag: Optional[bool] = field(
        default=None, metadata=config(field_name="fileAnalysisFlag")
    )
    policy_name: Optional[PolicyType] = field(
        default=None, metadata=config(field_name="policyName")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BulkAssignRequestOutput:
    """BulkAssignRequestOutput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    status: Optional[BulkAssignRequestStatus] = field(
        default=None, metadata=config(field_name="status")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PolicyArguments:
    """PolicyArguments."""

    policy_name: Optional[PolicyType] = field(
        default=None, metadata=config(field_name="policyName")
    )
    platform: Optional[EndpointPlatform] = field(
        default=None, metadata=config(field_name="platform")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CreatePolicyInput:
    """CreatePolicyInput."""

    format: Optional[str] = field(default=None, metadata=config(field_name="format"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    policy_name: Optional[PolicyType] = field(
        default=None, metadata=config(field_name="policyName")
    )
    platform: Optional[EndpointPlatform] = field(
        default=None, metadata=config(field_name="platform")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EndpointGroupsPagedOutput:
    """EndpointGroupsPagedOutput."""

    groups: Optional[List[EndpointGroup]] = field(
        default=None, metadata=config(field_name="groups")
    )
    partial_page_info: Optional[PartialPageInfo] = field(
        default=None, metadata=config(field_name="partialPageInfo")
    )
