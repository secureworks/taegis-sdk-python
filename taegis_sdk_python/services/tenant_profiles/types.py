"""TenantProfiles Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum


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
    DOMAIN_CONTROLLER = "DOMAIN_CONTROLLER"
    OTHER = "OTHER"


class SecurityControlSourceMtp(str, Enum):
    """SecurityControlSourceMtp."""

    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"


class EntityOfInterestIdentifierTypeMtp(str, Enum):
    """EntityOfInterestIdentifierTypeMtp."""

    HOST = "HOST"
    USER = "USER"
    PROCESS = "PROCESS"
    CLOUD_RESOURCE = "CLOUD_RESOURCE"
    CLOUD_OBJECT = "CLOUD_OBJECT"
    CLOUD_USER = "CLOUD_USER"
    EMAIL = "EMAIL"
    EMAIL_ADDRESS = "EMAIL_ADDRESS"
    FILE = "FILE"
    FILE_HASH = "FILE_HASH"
    SCRIPT = "SCRIPT"
    IP_ADDRESS = "IP_ADDRESS"
    DOMAIN_NAME = "DOMAIN_NAME"
    AUTH_DOMAIN = "AUTH_DOMAIN"
    CERTIFICATE = "CERTIFICATE"
    DNS_SERVER = "DNS_SERVER"
    FUNCTION = "FUNCTION"
    REGISTRY_KEY = "REGISTRY_KEY"
    SCHEDULED_TASK = "SCHEDULED_TASK"
    TASK_ACTION = "TASK_ACTION"
    SERVICE = "SERVICE"


class MtpAuthzObject(str, Enum):
    """MtpAuthzObject."""

    TENANT_PROFILE = "TenantProfile"
    TENANT_PROFILE_CSE_CONTACT = "TenantProfileCseContact"
    TENANT_PROFILE_ENTITY_OF_INTEREST = "TenantProfileEntityOfInterest"
    TENANT_PROFILE_NETWORK_INFO = "TenantProfileNetworkInfo"
    TENANT_PROFILE_NETWORK_RANGE = "TenantProfileNetworkRange"
    TENANT_PROFILE_NOTES = "TenantProfileNotes"
    TENANT_PROFILE_ATTACHMENT = "TenantProfileAttachment"


class MtpAuthzAction(str, Enum):
    """MtpAuthzAction."""

    CREATE = "CREATE"
    READ = "READ"
    LIST_ALL = "LIST_ALL"
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
    network_type: Optional[Union[MtpNetworkType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(MtpNetworkType, x),
            field_name="networkType",
        ),
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
    status: Optional[Union[FileStatusMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(FileStatusMtp, x),
            field_name="status",
        ),
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
    service: Optional[Union[MfaServiceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(MfaServiceMtp, x),
            field_name="service",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CriticalContactMtpInput:
    """CriticalContactMtpInput."""

    tdr_user_id: Optional[str] = field(
        default=None, metadata=config(field_name="tdrUserId")
    )
    preference: Optional[Union[CustomerContactPreferenceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(CustomerContactPreferenceMtp, x),
            field_name="preference",
        ),
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
    preference: Optional[Union[CustomerContactPreferenceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(CustomerContactPreferenceMtp, x),
            field_name="preference",
        ),
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
    network_type: Optional[Union[MtpNetworkType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(MtpNetworkType, x),
            field_name="networkType",
        ),
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
    network_type: Optional[Union[MtpNetworkType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(MtpNetworkType, x),
            field_name="networkType",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FileHashInputMtp:
    """FileHashInputMtp."""

    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    algorithm: Optional[Union[FileHashAlgorithmMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(FileHashAlgorithmMtp, x),
            field_name="algorithm",
        ),
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
    service: Optional[Union[MfaServiceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(MfaServiceMtp, x),
            field_name="service",
        ),
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
    service: Optional[Union[MfaServiceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(MfaServiceMtp, x),
            field_name="service",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EntityOfInterestMtp:
    """EntityOfInterestMtp."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    profile_id: Optional[str] = field(
        default=None, metadata=config(field_name="profileId")
    )
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    identifier_value: Optional[str] = field(
        default=None, metadata=config(field_name="identifierValue")
    )
    metadata: Optional[dict] = field(
        default=None, metadata=config(field_name="metadata")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    identifier_type: Optional[Union[EntityOfInterestIdentifierTypeMtp, TaegisEnum]] = (
        field(
            default=None,
            metadata=config(
                encoder=encode_enum,
                decoder=lambda x: decode_enum(EntityOfInterestIdentifierTypeMtp, x),
                field_name="identifierType",
            ),
        )
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EntityOfInterestMtps:
    """EntityOfInterestMtps."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    entities_of_interest: Optional[List[EntityOfInterestMtp]] = field(
        default=None, metadata=config(field_name="entitiesOfInterest")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EntityOfInterestCreateMtpInput:
    """EntityOfInterestCreateMtpInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    identifier_value: Optional[str] = field(
        default=None, metadata=config(field_name="identifierValue")
    )
    metadata: Optional[dict] = field(
        default=None, metadata=config(field_name="metadata")
    )
    identifier_type: Optional[Union[EntityOfInterestIdentifierTypeMtp, TaegisEnum]] = (
        field(
            default=None,
            metadata=config(
                encoder=encode_enum,
                decoder=lambda x: decode_enum(EntityOfInterestIdentifierTypeMtp, x),
                field_name="identifierType",
            ),
        )
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EntityOfInterestUpdateMtpInput:
    """EntityOfInterestUpdateMtpInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    identifier_value: Optional[str] = field(
        default=None, metadata=config(field_name="identifierValue")
    )
    metadata: Optional[dict] = field(
        default=None, metadata=config(field_name="metadata")
    )
    identifier_type: Optional[Union[EntityOfInterestIdentifierTypeMtp, TaegisEnum]] = (
        field(
            default=None,
            metadata=config(
                encoder=encode_enum,
                decoder=lambda x: decode_enum(EntityOfInterestIdentifierTypeMtp, x),
                field_name="identifierType",
            ),
        )
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ListAllTenantEntitiesOfInterestMtpInput:
    """ListAllTenantEntitiesOfInterestMtpInput."""

    identifier_values: Optional[List[str]] = field(
        default=None, metadata=config(field_name="identifierValues")
    )
    identifier_types: Optional[
        List[Union[EntityOfInterestIdentifierTypeMtp, TaegisEnum]]
    ] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(EntityOfInterestIdentifierTypeMtp, x),
            field_name="identifierTypes",
        ),
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
    contact_preference: Optional[Union[CustomerContactPreferenceMtp, TaegisEnum]] = (
        field(
            default=None,
            metadata=config(
                encoder=encode_enum,
                decoder=lambda x: decode_enum(CustomerContactPreferenceMtp, x),
                field_name="contactPreference",
            ),
        )
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
    service: Optional[Union[SecurityControlServiceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(SecurityControlServiceMtp, x),
            field_name="service",
        ),
    )
    source: Optional[Union[SecurityControlSourceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(SecurityControlSourceMtp, x),
            field_name="source",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SecurityControlCreateMtpInput:
    """SecurityControlCreateMtpInput."""

    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    details: Optional[str] = field(default=None, metadata=config(field_name="details"))
    service: Optional[Union[SecurityControlServiceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(SecurityControlServiceMtp, x),
            field_name="service",
        ),
    )
    source: Optional[Union[SecurityControlSourceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(SecurityControlSourceMtp, x),
            field_name="source",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SecurityControlUpdateMtpInput:
    """SecurityControlUpdateMtpInput."""

    ip: Optional[str] = field(default=None, metadata=config(field_name="ip"))
    details: Optional[str] = field(default=None, metadata=config(field_name="details"))
    service: Optional[Union[SecurityControlServiceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(SecurityControlServiceMtp, x),
            field_name="service",
        ),
    )
    source: Optional[Union[SecurityControlSourceMtp, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(SecurityControlSourceMtp, x),
            field_name="source",
        ),
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
