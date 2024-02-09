"""Authz Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class Effect(str, Enum):
    """Effect."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class AuthzRequestPermissionObject(str, Enum):
    """AuthzRequestPermissionObject."""

    AUTHZ_CUSTOM_ROLES = "AuthzCustomRoles"
    SUPPORTED_FEATURES = "SupportedFeatures"


class AuthzRequestPermissionAction(str, Enum):
    """AuthzRequestPermissionAction."""

    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"


class AuthzSupportedFeatureTarget(str, Enum):
    """AuthzSupportedFeatureTarget."""

    TENANT = "TENANT"
    CHILD_TENANTS = "CHILD_TENANTS"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzObjectAction:
    """AuthzObjectAction."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    object: Optional[str] = field(default=None, metadata=config(field_name="object"))
    action: Optional[str] = field(default=None, metadata=config(field_name="action"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzObjectActionInput:
    """AuthzObjectActionInput."""

    object: Optional[str] = field(default=None, metadata=config(field_name="object"))
    action: Optional[str] = field(default=None, metadata=config(field_name="action"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzActionTuple:
    """AuthzActionTuple."""

    action: Optional[str] = field(default=None, metadata=config(field_name="action"))
    effect: Optional[bool] = field(default=None, metadata=config(field_name="effect"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantHierarchy:
    """TenantHierarchy."""

    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    organization_id: Optional[str] = field(
        default=None, metadata=config(field_name="organizationID")
    )
    partner_id: Optional[str] = field(
        default=None, metadata=config(field_name="partnerID")
    )
    is_organization: Optional[bool] = field(
        default=None, metadata=config(field_name="isOrganization")
    )
    is_partner: Optional[bool] = field(
        default=None, metadata=config(field_name="isPartner")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzObjectActionStatusResponse:
    """AuthzObjectActionStatusResponse."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    object: Optional[str] = field(default=None, metadata=config(field_name="object"))
    action: Optional[str] = field(default=None, metadata=config(field_name="action"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    managed_only: Optional[bool] = field(
        default=None, metadata=config(field_name="managed_only")
    )
    subject_permitted: Optional[bool] = field(
        default=None, metadata=config(field_name="subject_permitted")
    )
    required_for_ui_login: Optional[bool] = field(
        default=None, metadata=config(field_name="required_for_ui_login")
    )
    feature_enabled: Optional[bool] = field(
        default=None, metadata=config(field_name="feature_enabled")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzCustomRoleDeleteResponse:
    """AuthzCustomRoleDeleteResponse."""

    deleted: Optional[bool] = field(default=None, metadata=config(field_name="deleted"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzSupportedFeatureState:
    """AuthzSupportedFeatureState."""

    enabled_in_tenant: Optional[bool] = field(
        default=None, metadata=config(field_name="enabledInTenant")
    )
    enabled_in_child_tenants: Optional[bool] = field(
        default=None, metadata=config(field_name="enabledInChildTenants")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Subject:
    """Subject."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzPermission:
    """AuthzPermission."""

    object: Optional[str] = field(default=None, metadata=config(field_name="object"))
    actions: Optional[List[AuthzActionTuple]] = field(
        default=None, metadata=config(field_name="actions")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzCanSubjectAssumeTenantDetailedResponse:
    """AuthzCanSubjectAssumeTenantDetailedResponse."""

    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    parent_tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="parentTenantID")
    )
    subject_can_assume_tenant: Optional[bool] = field(
        default=None, metadata=config(field_name="subjectCanAssumeTenant")
    )
    subject_is_scwx: Optional[bool] = field(
        default=None, metadata=config(field_name="subjectIsScwx")
    )
    tenant_hierarchy: Optional[TenantHierarchy] = field(
        default=None, metadata=config(field_name="tenantHierarchy")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzCustomRoleCreateInput:
    """AuthzCustomRoleCreateInput."""

    display_name: Optional[str] = field(
        default=None, metadata=config(field_name="displayName")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    object_actions: Optional[List[AuthzObjectActionInput]] = field(
        default=None, metadata=config(field_name="objectActions")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzUpdateSupportedFeatureStateInput:
    """AuthzUpdateSupportedFeatureStateInput."""

    object: Optional[str] = field(default=None, metadata=config(field_name="object"))
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    target: Optional[AuthzSupportedFeatureTarget] = field(
        default=None, metadata=config(field_name="target")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzPolicy:
    """AuthzPolicy."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant: Optional[str] = field(default=None, metadata=config(field_name="tenant"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    managed: Optional[bool] = field(default=None, metadata=config(field_name="managed"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    deleted: Optional[bool] = field(default=None, metadata=config(field_name="deleted"))
    object_actions: Optional[List[AuthzObjectAction]] = field(
        default=None, metadata=config(field_name="objectActions")
    )
    effect: Optional[Effect] = field(default=None, metadata=config(field_name="effect"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzCustomRoleUpdateInput:
    """AuthzCustomRoleUpdateInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    display_name: Optional[str] = field(
        default=None, metadata=config(field_name="displayName")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    remove_object_actions: Optional[List[AuthzObjectActionInput]] = field(
        default=None, metadata=config(field_name="removeObjectActions")
    )
    add_object_actions: Optional[List[AuthzObjectActionInput]] = field(
        default=None, metadata=config(field_name="addObjectActions")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzSupportedFeatureResponse:
    """AuthzSupportedFeatureResponse."""

    object: Optional[str] = field(default=None, metadata=config(field_name="object"))
    feature_display_name: Optional[str] = field(
        default=None, metadata=config(field_name="featureDisplayName")
    )
    feature_description: Optional[str] = field(
        default=None, metadata=config(field_name="featureDescription")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    updated_by: Optional[str] = field(
        default=None, metadata=config(field_name="updatedBy")
    )
    feature_state: Optional[AuthzSupportedFeatureState] = field(
        default=None, metadata=config(field_name="featureState")
    )
    updated_by_subject: Optional[Subject] = field(
        default=None, metadata=config(field_name="updatedBySubject")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzRole:
    """AuthzRole."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    display_name: Optional[str] = field(
        default=None, metadata=config(field_name="displayName")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    tenant: Optional[str] = field(default=None, metadata=config(field_name="tenant"))
    trusted_roles: Optional[List[str]] = field(
        default=None,
        metadata=config(
            metadata={"deprecated": True, "deprecation_reason": "No longer supported"},
            field_name="trustedRoles",
        ),
    )
    managed: Optional[bool] = field(default=None, metadata=config(field_name="managed"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    created_by: Optional[str] = field(
        default=None, metadata=config(field_name="createdBy")
    )
    updated_by: Optional[str] = field(
        default=None, metadata=config(field_name="updatedBy")
    )
    deleted: Optional[bool] = field(default=None, metadata=config(field_name="deleted"))
    policies: Optional[List[AuthzPolicy]] = field(
        default=None, metadata=config(field_name="policies")
    )
    created_by_subject: Optional[Subject] = field(
        default=None, metadata=config(field_name="createdBySubject")
    )
    updated_by_subject: Optional[Subject] = field(
        default=None, metadata=config(field_name="updatedBySubject")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzCheckPermissionsResponse:
    """AuthzCheckPermissionsResponse."""

    object: Optional[str] = field(default=None, metadata=config(field_name="object"))
    action: Optional[str] = field(default=None, metadata=config(field_name="action"))
    policy: Optional[AuthzPolicy] = field(
        default=None, metadata=config(field_name="policy")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AuthzCanSubjectAssignRoleResponse:
    """AuthzCanSubjectAssignRoleResponse."""

    subject_can_assign: Optional[bool] = field(
        default=None, metadata=config(field_name="subjectCanAssign")
    )
    role: Optional[AuthzRole] = field(default=None, metadata=config(field_name="role"))
    absent_permissions: Optional[List[AuthzPermission]] = field(
        default=None, metadata=config(field_name="absentPermissions")
    )
