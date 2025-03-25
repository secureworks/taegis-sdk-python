"""Tenants4 Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum, parse_union_result


class TenantRegion(str, Enum):
    """TenantRegion."""

    CHARLIE = "CHARLIE"
    DELTA = "DELTA"
    ECHO = "ECHO"
    FOXTROT = "FOXTROT"
    PILOT = "PILOT"
    PILOT_CHARLIE = "PILOT_CHARLIE"
    PILOT_DELTA = "PILOT_DELTA"
    PILOT_ECHO = "PILOT_ECHO"
    PILOT_FOXTROT = "PILOT_FOXTROT"


class TenantResultOrder(str, Enum):
    """TenantResultOrder."""

    ID = "ID"
    NAME = "NAME"
    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"
    PARTNER_TENANT_ID = "PARTNER_TENANT_ID"
    ORGANIZATION_TENANT_ID = "ORGANIZATION_TENANT_ID"
    HAS_SUPPORT_ENABLED = "HAS_SUPPORT_ENABLED"


class OrderDir(str, Enum):
    """OrderDir."""

    ASC = "ASC"
    DESC = "DESC"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantLabel:
    """TenantLabel."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    owner_partner_id: Optional[str] = field(
        default=None, metadata=config(field_name="ownerPartnerId")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantSubscription:
    """TenantSubscription."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    service_id: Optional[str] = field(
        default=None, metadata=config(field_name="serviceID")
    )
    service_name: Optional[str] = field(
        default=None, metadata=config(field_name="serviceName")
    )
    service_description: Optional[str] = field(
        default=None, metadata=config(field_name="serviceDescription")
    )
    owner_partner_id: Optional[str] = field(
        default=None, metadata=config(field_name="ownerPartnerId")
    )
    requested_at: Optional[str] = field(
        default=None, metadata=config(field_name="requestedAt")
    )
    requested_by: Optional[str] = field(
        default=None, metadata=config(field_name="requestedBy")
    )
    granted_at: Optional[str] = field(
        default=None, metadata=config(field_name="grantedAt")
    )
    revoked_at: Optional[str] = field(
        default=None, metadata=config(field_name="revokedAt")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantLabelMatcher:
    """TenantLabelMatcher."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SubscriptionMatcher:
    """SubscriptionMatcher."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    is_requested: Optional[bool] = field(
        default=None, metadata=config(field_name="isRequested")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantSubscriptions:
    """TenantSubscriptions."""

    granted: Optional[List[TenantSubscription]] = field(
        default=None, metadata=config(field_name="granted")
    )
    requested: Optional[List[TenantSubscription]] = field(
        default=None, metadata=config(field_name="requested")
    )
    revoked: Optional[List[TenantSubscription]] = field(
        default=None, metadata=config(field_name="revoked")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantsQuery:
    """TenantsQuery."""

    ids: Optional[List[str]] = field(default=None, metadata=config(field_name="ids"))
    names: Optional[List[str]] = field(
        default=None, metadata=config(field_name="names")
    )
    is_partner_root: Optional[bool] = field(
        default=None, metadata=config(field_name="isPartnerRoot")
    )
    is_organization: Optional[bool] = field(
        default=None, metadata=config(field_name="isOrganization")
    )
    hierarchy_paths: Optional[List[str]] = field(
        default=None, metadata=config(field_name="hierarchyPaths")
    )
    partners: Optional[List[str]] = field(
        default=None, metadata=config(field_name="partners")
    )
    organizations: Optional[List[str]] = field(
        default=None, metadata=config(field_name="organizations")
    )
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    support_enabled: Optional[bool] = field(
        default=None, metadata=config(field_name="supportEnabled")
    )
    cursor_pos: Optional[str] = field(
        default=None, metadata=config(field_name="cursorPos")
    )
    after_cursor: Optional[str] = field(
        default=None, metadata=config(field_name="afterCursor")
    )
    before_cursor: Optional[str] = field(
        default=None, metadata=config(field_name="beforeCursor")
    )
    count: Optional[int] = field(default=None, metadata=config(field_name="count"))
    cql: Optional[str] = field(default=None, metadata=config(field_name="cql"))
    read_partner_roots: Optional[bool] = field(
        default=None, metadata=config(field_name="readPartnerRoots")
    )
    enabled_in: Optional[List[Union[TenantRegion, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(TenantRegion, x),
            field_name="enabledIn",
        ),
    )
    labels_match: Optional[List[TenantLabelMatcher]] = field(
        default=None, metadata=config(field_name="labelsMatch")
    )
    subscriptions_match: Optional[List[SubscriptionMatcher]] = field(
        default=None, metadata=config(field_name="subscriptionsMatch")
    )
    order_by: Optional[Union[TenantResultOrder, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(TenantResultOrder, x),
            field_name="orderBy",
        ),
    )
    order_dir: Optional[Union[OrderDir, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(OrderDir, x),
            field_name="orderDir",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantV4:
    """TenantV4."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    parent_tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="parentTenantID")
    )
    partner_tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="partnerTenantID")
    )
    partner_name: Optional[str] = field(
        default=None, metadata=config(field_name="partnerName")
    )
    organization_tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="organizationTenantID")
    )
    organization_name: Optional[str] = field(
        default=None, metadata=config(field_name="organizationName")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    hierarchy_path: Optional[str] = field(
        default=None, metadata=config(field_name="hierarchyPath")
    )
    is_organization: Optional[bool] = field(
        default=None, metadata=config(field_name="isOrganization")
    )
    is_partner: Optional[bool] = field(
        default=None, metadata=config(field_name="isPartner")
    )
    has_support_enabled: Optional[bool] = field(
        default=None, metadata=config(field_name="hasSupportEnabled")
    )
    support_inherited: Optional[bool] = field(
        default=None, metadata=config(field_name="supportInherited")
    )
    expires_at: Optional[str] = field(
        default=None, metadata=config(field_name="expiresAt")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    enabled_at_regions: Optional[List[Union[TenantRegion, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(TenantRegion, x),
            field_name="enabledAtRegions",
        ),
    )
    labels: Optional[List[TenantLabel]] = field(
        default=None, metadata=config(field_name="labels")
    )
    subscriptions: Optional[TenantSubscriptions] = field(
        default=None, metadata=config(field_name="subscriptions")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantResults:
    """TenantResults."""

    cursor_pos: Optional[str] = field(
        default=None, metadata=config(field_name="cursorPos")
    )
    count: Optional[int] = field(default=None, metadata=config(field_name="count"))
    has_more: Optional[bool] = field(
        default=None, metadata=config(field_name="hasMore")
    )
    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    first_index: Optional[int] = field(
        default=None, metadata=config(field_name="firstIndex")
    )
    last_index: Optional[int] = field(
        default=None, metadata=config(field_name="lastIndex")
    )
    tenants: Optional[List[TenantV4]] = field(
        default=None, metadata=config(field_name="tenants")
    )
