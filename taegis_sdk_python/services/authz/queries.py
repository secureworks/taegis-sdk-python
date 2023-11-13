"""Authz Query."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)
from taegis_sdk_python.services.authz.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.authz import AuthzService

log = logging.getLogger(__name__)


class TaegisSDKAuthzQuery:
    """Taegis Authz Query operations."""

    def __init__(self, service: AuthzService):
        self.service = service

    def authz_role(self, id_: str) -> AuthzRole:
        """Retrieve a Role by its unique ID."""
        endpoint = "authzRole"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(AuthzRole),
        )
        if result.get(endpoint) is not None:
            return AuthzRole.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query authzRole")

    def authz_assignable_roles(self) -> List[AuthzRole]:
        """Retrieve roles that can be assigned to users within the requesting tenant."""
        endpoint = "authzAssignableRoles"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AuthzRole)
        )
        if result.get(endpoint) is not None:
            return AuthzRole.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzAssignableRoles")

    def authz_subject_assignable_roles(self) -> List[AuthzRole]:
        """Retrieve roles that the requesting subject can assign within the requesting tenant."""
        endpoint = "authzSubjectAssignableRoles"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AuthzRole)
        )
        if result.get(endpoint) is not None:
            return AuthzRole.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzSubjectAssignableRoles")

    def authz_assignable_internal_roles(self) -> List[AuthzRole]:
        """Retrieve internal roles that can be assigned to users within the requesting tenant."""
        endpoint = "authzAssignableInternalRoles"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AuthzRole)
        )
        if result.get(endpoint) is not None:
            return AuthzRole.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzAssignableInternalRoles")

    def authz_object_actions(self) -> List[AuthzObjectAction]:
        """Retrieve all authorization ObjectActions."""
        endpoint = "authzObjectActions"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(AuthzObjectAction),
        )
        if result.get(endpoint) is not None:
            return AuthzObjectAction.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzObjectActions")

    def authz_policy(self, id_: str) -> AuthzPolicy:
        """Retrieve authorization policy by its ID."""
        endpoint = "authzPolicy"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(AuthzPolicy),
        )
        if result.get(endpoint) is not None:
            return AuthzPolicy.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query authzPolicy")

    def authz_policies(self) -> List[AuthzPolicy]:
        """Retrieve all policies within the requesting tenant."""
        endpoint = "authzPolicies"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AuthzPolicy)
        )
        if result.get(endpoint) is not None:
            return AuthzPolicy.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzPolicies")

    def authz_check_permission(self, input_: AuthzObjectActionInput) -> AuthzPolicy:
        """Perform a permission check against the input ObjectAction, returning the applicable policy and authorization effect for the given subject & tenant context."""
        endpoint = "authzCheckPermission"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(AuthzPolicy),
        )
        if result.get(endpoint) is not None:
            return AuthzPolicy.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query authzCheckPermission")

    def authz_check_permissions(
        self, input_: List[AuthzObjectActionInput]
    ) -> List[AuthzCheckPermissionsResponse]:
        """Perform a permission check against multiple input ObjectActions, returning the applicable policies and authorization effects for the given subject & tenant context."""
        endpoint = "authzCheckPermissions"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(AuthzCheckPermissionsResponse),
        )
        if result.get(endpoint) is not None:
            return AuthzCheckPermissionsResponse.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzCheckPermissions")

    def authz_check_tenants(
        self, input_: AuthzObjectActionInput, tenants: List[str]
    ) -> List[str]:
        """Given a list of tenants and a permission, returns the IDs of tenants where the subject posesses the given permission."""
        endpoint = "authzCheckTenants"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
                "tenants": prepare_input(tenants),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query authzCheckTenants")

    def authz_permissions(self) -> List[AuthzPermission]:
        """Retrieve the full list of subjects permissions for the tenant context."""
        endpoint = "authzPermissions"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AuthzPermission)
        )
        if result.get(endpoint) is not None:
            return AuthzPermission.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzPermissions")

    def authz_can_subject_assume_tenant(self) -> bool:
        """Determine if the subject can assume the target tenant."""
        endpoint = "authzCanSubjectAssumeTenant"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query authzCanSubjectAssumeTenant")

    def authz_can_subject_assume_tenant_detailed(
        self,
    ) -> AuthzCanSubjectAssumeTenantDetailedResponse:
        """Returns the authzCanSubjectAssumeTenant result along with subject and partner detail."""
        endpoint = "authzCanSubjectAssumeTenantDetailed"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(AuthzCanSubjectAssumeTenantDetailedResponse),
        )
        if result.get(endpoint) is not None:
            return AuthzCanSubjectAssumeTenantDetailedResponse.from_dict(
                result.get(endpoint)
            )
        raise GraphQLNoRowsInResultSetError(
            "for query authzCanSubjectAssumeTenantDetailed"
        )

    def authz_can_subject_idassume_tenant(self, subject_id: str) -> bool:
        """Indicates if the input subject can assume the target tenant."""
        endpoint = "authzCanSubjectIDAssumeTenant"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "subjectID": prepare_input(subject_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query authzCanSubjectIDAssumeTenant")

    def authz_can_subject_assume_tenants(self, tenants: List[str]) -> List[str]:
        """Identify which tenants the subject can assume with an input list of Tenant IDs, returning the IDs where the tenant can be assumed."""
        endpoint = "authzCanSubjectAssumeTenants"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "tenants": prepare_input(tenants),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query authzCanSubjectAssumeTenants")

    def authz_can_subject_assume_all_tenants(self) -> bool:
        """Determine if the subject can assume *all* tenants."""
        endpoint = "authzCanSubjectAssumeAllTenants"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query authzCanSubjectAssumeAllTenants")

    def authz_can_subject_assign_role(
        self, id_: str
    ) -> AuthzCanSubjectAssignRoleResponse:
        """Check if the subject can assign the input role."""
        endpoint = "authzCanSubjectAssignRole"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(AuthzCanSubjectAssignRoleResponse),
        )
        if result.get(endpoint) is not None:
            return AuthzCanSubjectAssignRoleResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query authzCanSubjectAssignRole")

    def authz_internal_permissions(self) -> List[AuthzPermission]:
        """Retrieve the full list of subjects internal permissions for the tenant context."""
        endpoint = "authzInternalPermissions"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AuthzPermission)
        )
        if result.get(endpoint) is not None:
            return AuthzPermission.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzInternalPermissions")

    def authz_object_action_status(self) -> List[AuthzObjectActionStatusResponse]:
        """Retrieve all object actions with their statuses for the current tenant context."""
        endpoint = "authzObjectActionStatus"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(AuthzObjectActionStatusResponse),
        )
        if result.get(endpoint) is not None:
            return AuthzObjectActionStatusResponse.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzObjectActionStatus")

    def authz_supported_features(self) -> List[AuthzSupportedFeatureResponse]:
        """Retrieve all supported features and their states for the current tenant context."""
        endpoint = "authzSupportedFeatures"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(AuthzSupportedFeatureResponse),
        )
        if result.get(endpoint) is not None:
            return AuthzSupportedFeatureResponse.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzSupportedFeatures")

    def authz_can_user_assume_tenant(self) -> bool:
        """DEPRECATED: Please use authzCanSubjectAssumeTenant."""
        endpoint = "authzCanUserAssumeTenant"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query authzCanUserAssumeTenant")

    def authz_trusted_roles(self, role_ids: List[str]) -> List[AuthzRole]:
        """DEPRECATED: Trusted roles functionality has been removed."""
        endpoint = "authzTrustedRoles"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "roleIDs": prepare_input(role_ids),
            },
            output=build_output_string(AuthzRole),
        )
        if result.get(endpoint) is not None:
            return AuthzRole.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query authzTrustedRoles")
