"""TenantProfiles Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class CustomerContactPreferenceMtp(str, Enum):
    """CustomerContactPreferenceMtp."""

    CSE_PRIMARY = "CsePrimary"
    CSE_SECONDARY = "CseSecondary"
    CSE_TERTIARY = "CseTertiary"
    HEALTH_INCIDENTS = "HealthIncidents"


class MtpNetworkType(str, Enum):
    """MtpNetworkType."""

    INTERNAL = "Internal"
    PUBLIC = "Public"
    VPN = "VPN"
    DMZ = "DMZ"
    GUEST = "Guest"
    NAT = "NAT"
    OTHER = "Other"


class FileStatusMtp(str, Enum):
    """FileStatusMtp."""

    PENDING = "PENDING"
    READY = "READY"
    FAILED = "FAILED"
    DELETED = "DELETED"
    OBSOLETE = "OBSOLETE"


class FileHashAlgorithmMtp(str, Enum):
    """FileHashAlgorithmMtp."""

    MD5 = "MD5"
    SHA256 = "SHA256"


class MfaServiceMtp(str, Enum):
    """MfaServiceMtp."""

    VPN = "VPN"
    CITRIX = "CITRIX"
    OWA = "OWA"
    OTHER = "OTHER"


class SecurityControlServiceMtp(str, Enum):
    """SecurityControlServiceMtp."""

    OTHER_ENDPOINT_TECHNOLOGIES = "OTHER_ENDPOINT_TECHNOLOGIES"
    NETWORKS_IDS_IPS = "NETWORKS_IDS_IPS"
    SIEM = "SIEM"
    IR_FORENSICS_SERVICES = "IR_FORENSICS_SERVICES"
    MALWARE_ANALYSIS_AND_OR_SANDBOX = "MALWARE_ANALYSIS_AND_OR_SANDBOX"
    PENETRATION_TESTING = "PENETRATION_TESTING"
    PROXY = "PROXY"
    SECURE_EMAIL_GATEWAY = "SECURE_EMAIL_GATEWAY"
    VPN_GATEWAY = "VPN_GATEWAY"
    VULNERABILITY_SCANNING = "VULNERABILITY_SCANNING"
    OTHER = "OTHER"


class SecurityControlSourceMtp(str, Enum):
    """SecurityControlSourceMtp."""

    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"


class MtpAuthzObject(str, Enum):
    """MtpAuthzObject."""

    TENANT_PROFILE = "TenantProfile"
    TENANT_PROFILE_CSE_CONTACT = "TenantProfileCseContact"
    TENANT_PROFILE_NETWORK_INFO = "TenantProfileNetworkInfo"
    TENANT_PROFILE_NETWORK_RANGE = "TenantProfileNetworkRange"
    TENANT_PROFILE_NOTES = "TenantProfileNotes"
    TENANT_PROFILE_ATTACHMENT = "TenantProfileAttachment"


class MtpAuthzAction(str, Enum):
    """MtpAuthzAction."""

    CREATE = "CREATE"
    READ = "READ"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    EXPORT = "EXPORT"
    READ_PUBLIC = "READ_PUBLIC"
    READ_PRIVATE = "READ_PRIVATE"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class VersionMtp:
    """VersionMtp."""

    tag: Optional[str] = field(default=None, metadata=config(field_name="tag"))
    revision: Optional[str] = field(
        default=None, metadata=config(field_name="revision")
    )
    timestamp: Optional[str] = field(
        default=None, metadata=config(field_name="timestamp")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUser:
    """TDRUser."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NoteMtp:
    """NoteMtp."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    profile_id: Optional[str] = field(
        default=None, metadata=config(field_name="profileId")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    contents: Optional[str] = field(
        default=None, metadata=config(field_name="contents")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FileUpdateInputMtp:
    """FileUpdateInputMtp."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    client_visible: Optional[bool] = field(
        default=None, metadata=config(field_name="clientVisible")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NetworkRangeMtp:
    """NetworkRangeMtp."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    profile_id: Optional[str] = field(
        default=None, metadata=config(field_name="profileId")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    cidr: Optional[str] = field(default=None, metadata=config(field_name="cidr"))
    cidr_family: Optional[str] = field(
        default=None, metadata=config(field_name="cidrFamily")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    is_critical: Optional[bool] = field(
        default=None, metadata=config(field_name="isCritical")
    )
    added_by: Optional[str] = field(default=None, metadata=config(field_name="addedBy"))
    date_added: Optional[str] = field(
        default=None, metadata=config(field_name="dateAdded")
    )
    network_type: Optional[MtpNetworkType] = field(
        default=None, metadata=config(field_name="networkType")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FileAttachmentMtp:
    """FileAttachmentMtp."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    profile_id: Optional[str] = field(
        default=None, metadata=config(field_name="profileID")
    )
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    uploaded_by: Optional[str] = field(
        default=None, metadata=config(field_name="uploadedBy")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    created_by: Optional[str] = field(
        default=None, metadata=config(field_name="createdBy")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    updated_by: Optional[str] = field(
        default=None, metadata=config(field_name="updatedBy")
    )
    filename: Optional[str] = field(
        default=None, metadata=config(field_name="filename")
    )
    filesize: Optional[int] = field(
        default=None, metadata=config(field_name="filesize")
    )
    filetype: Optional[str] = field(
        default=None, metadata=config(field_name="filetype")
    )
    version: Optional[int] = field(default=None, metadata=config(field_name="version"))
    client_visible: Optional[bool] = field(
        default=None, metadata=config(field_name="clientVisible")
    )
    status: Optional[FileStatusMtp] = field(
        default=None, metadata=config(field_name="status")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FileDownloadMtp:
    """FileDownloadMtp."""

    download_url: Optional[str] = field(
        default=None, metadata=config(field_name="downloadUrl")
    )
    file_info: Optional[FileAttachmentMtp] = field(
        default=None, metadata=config(field_name="fileInfo")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MfaAccessMtp:
    """MfaAccessMtp."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    profile_id: Optional[str] = field(
        default=None, metadata=config(field_name="profileId")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    mfa_required: Optional[bool] = field(
        default=None, metadata=config(field_name="mfa_required")
    )
    exceptions: Optional[str] = field(
        default=None, metadata=config(field_name="exceptions")
    )
    details: Optional[str] = field(default=None, metadata=config(field_name="details"))
    service: Optional[MfaServiceMtp] = field(
        default=None, metadata=config(field_name="service")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CriticalContactMtpInput:
    """CriticalContactMtpInput."""

    tdr_user_id: Optional[str] = field(
        default=None, metadata=config(field_name="tdrUserId")
    )
    preference: Optional[CustomerContactPreferenceMtp] = field(
        default=None, metadata=config(field_name="preference")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CriticalExternalContactMtpInput:
    """CriticalExternalContactMtpInput."""

    first_name: Optional[str] = field(
        default=None, metadata=config(field_name="firstName")
    )
    last_name: Optional[str] = field(
        default=None, metadata=config(field_name="lastName")
    )
    primary_phone: Optional[str] = field(
        default=None, metadata=config(field_name="primaryPhone")
    )
    primary_phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="primaryPhoneExtension")
    )
    secondary_phone: Optional[str] = field(
        default=None, metadata=config(field_name="secondaryPhone")
    )
    secondary_phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="secondaryPhoneExtension")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    external_email_verified: Optional[bool] = field(
        default=None, metadata=config(field_name="externalEmailVerified")
    )
    preference: Optional[CustomerContactPreferenceMtp] = field(
        default=None, metadata=config(field_name="preference")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NetworkRangeCreateMtpInput:
    """NetworkRangeCreateMtpInput."""

    cidr: Optional[str] = field(default=None, metadata=config(field_name="cidr"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    is_critical: Optional[bool] = field(
        default=None, metadata=config(field_name="isCritical")
    )
    network_type: Optional[MtpNetworkType] = field(
        default=None, metadata=config(field_name="networkType")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NetworkRangeUpdateMtpInput:
    """NetworkRangeUpdateMtpInput."""

    cidr: Optional[str] = field(default=None, metadata=config(field_name="cidr"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    is_critical: Optional[bool] = field(
        default=None, metadata=config(field_name="isCritical")
    )
    network_type: Optional[MtpNetworkType] = field(
        default=None, metadata=config(field_name="networkType")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FileHashInputMtp:
    """FileHashInputMtp."""

    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    algorithm: Optional[FileHashAlgorithmMtp] = field(
        default=None, metadata=config(field_name="algorithm")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MfaAccessCreateMtpInput:
    """MfaAccessCreateMtpInput."""

    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    mfa_required: Optional[bool] = field(
        default=None, metadata=config(field_name="mfaRequired")
    )
    exceptions: Optional[str] = field(
        default=None, metadata=config(field_name="exceptions")
    )
    details: Optional[str] = field(default=None, metadata=config(field_name="details"))
    service: Optional[MfaServiceMtp] = field(
        default=None, metadata=config(field_name="service")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MfaAccessUpdateMtpInput:
    """MfaAccessUpdateMtpInput."""

    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    mfa_required: Optional[bool] = field(
        default=None, metadata=config(field_name="mfaRequired")
    )
    exceptions: Optional[str] = field(
        default=None, metadata=config(field_name="exceptions")
    )
    details: Optional[str] = field(default=None, metadata=config(field_name="details"))
    service: Optional[MfaServiceMtp] = field(
        default=None, metadata=config(field_name="service")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CustomerContactMtp:
    """CustomerContactMtp."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    profile_id: Optional[str] = field(
        default=None, metadata=config(field_name="profileId")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    first_name: Optional[str] = field(
        default=None, metadata=config(field_name="firstName")
    )
    last_name: Optional[str] = field(
        default=None, metadata=config(field_name="lastName")
    )
    primary_phone: Optional[str] = field(
        default=None, metadata=config(field_name="primaryPhone")
    )
    primary_phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="primaryPhoneExtension")
    )
    secondary_phone: Optional[str] = field(
        default=None, metadata=config(field_name="secondaryPhone")
    )
    secondary_phone_extension: Optional[str] = field(
        default=None, metadata=config(field_name="secondaryPhoneExtension")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    tdr_user_id: Optional[str] = field(
        default=None, metadata=config(field_name="tdrUserId")
    )
    tdr_user_status: Optional[str] = field(
        default=None, metadata=config(field_name="tdrUserStatus")
    )
    tenant_status: Optional[str] = field(
        default=None, metadata=config(field_name="tenantStatus")
    )
    is_external: Optional[bool] = field(
        default=None, metadata=config(field_name="isExternal")
    )
    external_email_verified: Optional[bool] = field(
        default=None, metadata=config(field_name="externalEmailVerified")
    )
    contact_preference: Optional[CustomerContactPreferenceMtp] = field(
        default=None, metadata=config(field_name="contactPreference")
    )
    tdr_user: Optional[TDRUser] = field(
        default=None, metadata=config(field_name="tdrUser")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SecurityControlMtp:
    """SecurityControlMtp."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    profile_id: Optional[str] = field(
        default=None, metadata=config(field_name="profileId")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    details: Optional[str] = field(default=None, metadata=config(field_name="details"))
    service: Optional[SecurityControlServiceMtp] = field(
        default=None, metadata=config(field_name="service")
    )
    source: Optional[SecurityControlSourceMtp] = field(
        default=None, metadata=config(field_name="source")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SecurityControlCreateMtpInput:
    """SecurityControlCreateMtpInput."""

    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    details: Optional[str] = field(default=None, metadata=config(field_name="details"))
    service: Optional[SecurityControlServiceMtp] = field(
        default=None, metadata=config(field_name="service")
    )
    source: Optional[SecurityControlSourceMtp] = field(
        default=None, metadata=config(field_name="source")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SecurityControlUpdateMtpInput:
    """SecurityControlUpdateMtpInput."""

    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    details: Optional[str] = field(default=None, metadata=config(field_name="details"))
    service: Optional[SecurityControlServiceMtp] = field(
        default=None, metadata=config(field_name="service")
    )
    source: Optional[SecurityControlSourceMtp] = field(
        default=None, metadata=config(field_name="source")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CseCustomerContacts:
    """CseCustomerContacts."""

    primary: Optional[CustomerContactMtp] = field(
        default=None, metadata=config(field_name="primary")
    )
    secondary: Optional[CustomerContactMtp] = field(
        default=None, metadata=config(field_name="secondary")
    )
    tertiary: Optional[CustomerContactMtp] = field(
        default=None, metadata=config(field_name="tertiary")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ManagedTenantProfile:
    """ManagedTenantProfile."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    cse_contacts: Optional[CseCustomerContacts] = field(
        default=None, metadata=config(field_name="cseContacts")
    )
    network_ranges: Optional[List[NetworkRangeMtp]] = field(
        default=None, metadata=config(field_name="networkRanges")
    )
    note: Optional[NoteMtp] = field(default=None, metadata=config(field_name="note"))
    security_controls: Optional[List[SecurityControlMtp]] = field(
        default=None, metadata=config(field_name="securityControls")
    )
    mfa_accesses: Optional[List[MfaAccessMtp]] = field(
        default=None, metadata=config(field_name="mfaAccesses")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FileUploadInputMtp:
    """FileUploadInputMtp."""

    file: Optional[str] = field(default=None, metadata=config(field_name="file"))
    hash: Optional[FileHashInputMtp] = field(
        default=None, metadata=config(field_name="hash")
    )
