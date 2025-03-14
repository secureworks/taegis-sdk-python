"""Tenants Mutation."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.tenants.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.tenants import TenantsService

log = logging.getLogger(__name__)


class TaegisSDKTenantsMutation:
    """Taegis Tenants Mutation operations."""

    def __init__(self, service: TenantsService):
        self.service = service

    def create_subscription(self, input_: NewSubscription) -> Service:
        """Create a new Subscription."""
        endpoint = "createSubscription"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Service),
        )
        if result.get(endpoint) is not None:
            return Service.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createSubscription")

    def update_subscription(self, input_: SubscriptionUpdate) -> Service:
        """Updates a new Subscription."""
        endpoint = "updateSubscription"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Service),
        )
        if result.get(endpoint) is not None:
            return Service.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateSubscription")

    def delete_subscription(self, id_: str) -> Service:
        """Delete a Subscription."""
        endpoint = "deleteSubscription"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Service),
        )
        if result.get(endpoint) is not None:
            return Service.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteSubscription")

    def assign_subscription(self, tenant_id: str, subscription_id: str) -> Tenant:
        """Assign a Subscription to a Tenant."""
        endpoint = "assignSubscription"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "tenant_id": prepare_input(tenant_id),
                "subscription_id": prepare_input(subscription_id),
            },
            output=build_output_string(Tenant),
        )
        if result.get(endpoint) is not None:
            return Tenant.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation assignSubscription")

    def unassign_subscription(self, tenant_id: str, subscription_id: str) -> Tenant:
        """Unassign a Subscription from a Tenant."""
        endpoint = "unassignSubscription"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "tenant_id": prepare_input(tenant_id),
                "subscription_id": prepare_input(subscription_id),
            },
            output=build_output_string(Tenant),
        )
        if result.get(endpoint) is not None:
            return Tenant.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation unassignSubscription")

    def create_tenant_label(
        self, tenant_id: str, label_input: InputTenantLabel
    ) -> TenantLabel:
        """Add Label to Tenant. If label is for partner parent/child and is owned by SCWX, subject must have access to SCWX also.."""
        endpoint = "createTenantLabel"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "tenant_id": prepare_input(tenant_id),
                "label_input": prepare_input(label_input),
            },
            output=build_output_string(TenantLabel),
        )
        if result.get(endpoint) is not None:
            return TenantLabel.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createTenantLabel")

    def update_tenant_label(
        self, label_id: str, tenant_id: str, label_input: InputTenantLabel
    ) -> TenantLabel:
        """Update Label for a Tenant. If label is for partner parent/child and is owned by SCWX, subject must have access to SCWX also.."""
        endpoint = "updateTenantLabel"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "label_id": prepare_input(label_id),
                "tenant_id": prepare_input(tenant_id),
                "label_input": prepare_input(label_input),
            },
            output=build_output_string(TenantLabel),
        )
        if result.get(endpoint) is not None:
            return TenantLabel.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateTenantLabel")

    def delete_tenant_label(self, label_id: str, tenant_id: str) -> TenantLabel:
        """Remove a Label from a Tenant. If label is for partner parent/child and is owned by SCWX, subject must have access to SCWX also.."""
        endpoint = "deleteTenantLabel"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "label_id": prepare_input(label_id),
                "tenant_id": prepare_input(tenant_id),
            },
            output=build_output_string(TenantLabel),
        )
        if result.get(endpoint) is not None:
            return TenantLabel.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteTenantLabel")

    def create_tenant(self, new_tenant: TenantCreateInput) -> Tenant:
        """Creates a tenant, user needs to have access to the partner tenant to create a new tenant."""
        endpoint = "createTenant"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "newTenant": prepare_input(new_tenant),
            },
            output=build_output_string(Tenant),
        )
        if result.get(endpoint) is not None:
            return Tenant.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createTenant")

    def update_tenant(self, tenant_id: str, tenant_update: TenantUpdateInput) -> Tenant:
        """Allows to update a tenant."""
        endpoint = "updateTenant"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "tenantID": prepare_input(tenant_id),
                "tenantUpdate": prepare_input(tenant_update),
            },
            output=build_output_string(Tenant),
        )
        if result.get(endpoint) is not None:
            return Tenant.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateTenant")

    def create_sso_connection(
        self, new_connection: NewSSOConnectionInput
    ) -> SSOConnection:
        """Creates a SSO connection on a tenant."""
        endpoint = "createSSOConnection"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "newConnection": prepare_input(new_connection),
            },
            output=build_output_string(SSOConnection),
        )
        if result.get(endpoint) is not None:
            return SSOConnection.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createSSOConnection")

    def update_sso_connection(
        self, updated_connection: UpdateSSOConnectionInput
    ) -> SSOConnection:
        """Updates a SSO connection on a tenant."""
        endpoint = "updateSSOConnection"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "updatedConnection": prepare_input(updated_connection),
            },
            output=build_output_string(SSOConnection),
        )
        if result.get(endpoint) is not None:
            return SSOConnection.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateSSOConnection")

    def delete_sso_connection(self, connection_id: str) -> SSOConnection:
        """Deletes a SSO connection from a tenant."""
        endpoint = "deleteSSOConnection"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "connectionID": prepare_input(connection_id),
            },
            output=build_output_string(SSOConnection),
        )
        if result.get(endpoint) is not None:
            return SSOConnection.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteSSOConnection")

    def update_allow_response_action(self, tenant_id: str, allowed: bool) -> Tenant:
        """updates allowedResponseAction for a tenant."""
        endpoint = "updateAllowResponseAction"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "tenant_id": prepare_input(tenant_id),
                "allowed": prepare_input(allowed),
            },
            output=build_output_string(Tenant),
        )
        if result.get(endpoint) is not None:
            return Tenant.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateAllowResponseAction")

    def enable_tenant_support(self, tenant_id: str) -> Tenant:
        """Allows users with the appropriate Secureworks Support role to access this tenant under a Partner."""
        endpoint = "enableTenantSupport"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "tenantID": prepare_input(tenant_id),
            },
            output=build_output_string(Tenant),
        )
        if result.get(endpoint) is not None:
            return Tenant.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation enableTenantSupport")

    def disable_tenant_support(self, tenant_id: str) -> Tenant:
        """Disable support access for tenant."""
        endpoint = "disableTenantSupport"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "tenantID": prepare_input(tenant_id),
            },
            output=build_output_string(Tenant),
        )
        if result.get(endpoint) is not None:
            return Tenant.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation disableTenantSupport")

    def change_tenant_hierarchy(
        self, tenant_id: str, new_partner_tenant_id: str
    ) -> Tenant:
        """Allows changing the tenant's parent (tenant partner hierarchy)."""
        endpoint = "changeTenantHierarchy"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "tenantID": prepare_input(tenant_id),
                "newPartnerTenantID": prepare_input(new_partner_tenant_id),
            },
            output=build_output_string(Tenant),
        )
        if result.get(endpoint) is not None:
            return Tenant.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation changeTenantHierarchy")

    def request_service(
        self, tenant_service_input: TenantServiceInput
    ) -> TenantService:
        """Requests a service for the tenant, the subject should have tenant.update on TenantServiceInput.tenantID, only internal services can be requested."""
        endpoint = "requestService"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "tenantServiceInput": prepare_input(tenant_service_input),
            },
            output=build_output_string(TenantService),
        )
        if result.get(endpoint) is not None:
            return TenantService.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation requestService")

    def create_tenant_decommission_request(
        self, input_: TenantDecommissionCreateRequestInput
    ) -> TenantDecommissionRequest:
        """Creates a new TenantDecommissionRequest for a tenant."""
        endpoint = "createTenantDecommissionRequest"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(TenantDecommissionRequest),
        )
        if result.get(endpoint) is not None:
            return TenantDecommissionRequest.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation createTenantDecommissionRequest"
        )

    def update_tenant_decommission_request(
        self, update_request: TenantDecommissionUpdateRequestInput
    ) -> TenantDecommissionRequest:
        """Updates an existing TenantDecommissionRequest."""
        endpoint = "updateTenantDecommissionRequest"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "updateRequest": prepare_input(update_request),
            },
            output=build_output_string(TenantDecommissionRequest),
        )
        if result.get(endpoint) is not None:
            return TenantDecommissionRequest.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation updateTenantDecommissionRequest"
        )

    def defer_tenant_decommission_task(
        self, task_id: TenantDecommissionTaskDeferInput
    ) -> TenantDecommissionRequest:
        """Sets defer time for a given TenantDecommissionTask."""
        endpoint = "deferTenantDecommissionTask"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "taskID": prepare_input(task_id),
            },
            output=build_output_string(TenantDecommissionRequest),
        )
        if result.get(endpoint) is not None:
            return TenantDecommissionRequest.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deferTenantDecommissionTask")

    def submit_tenant_decommission_request(
        self, request_id: str
    ) -> TenantDecommissionRequest:
        """Set the TenantDecommissionRequest ready for review."""
        endpoint = "submitTenantDecommissionRequest"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "requestID": prepare_input(request_id),
            },
            output=build_output_string(TenantDecommissionRequest),
        )
        if result.get(endpoint) is not None:
            return TenantDecommissionRequest.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation submitTenantDecommissionRequest"
        )

    def approve_tenant_decommission_request(
        self, request_id: str
    ) -> TenantDecommissionRequest:
        """Mark the TenantDecommissionRequest as approved."""
        endpoint = "approveTenantDecommissionRequest"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "requestID": prepare_input(request_id),
            },
            output=build_output_string(TenantDecommissionRequest),
        )
        if result.get(endpoint) is not None:
            return TenantDecommissionRequest.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation approveTenantDecommissionRequest"
        )

    def execute_tenant_decommission_request(
        self, request_id: str
    ) -> TenantDecommissionRequest:
        """Start the execution of the Tenant Decommission tasks, needs to be in approved status in order to start these tasks."""
        endpoint = "executeTenantDecommissionRequest"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "requestID": prepare_input(request_id),
            },
            output=build_output_string(TenantDecommissionRequest),
        )
        if result.get(endpoint) is not None:
            return TenantDecommissionRequest.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation executeTenantDecommissionRequest"
        )

    def cancel_tenant_decommission_request(
        self, request_id: str, reason: str
    ) -> TenantDecommissionRequest:
        """Cancels a Tenant Decommission Request."""
        endpoint = "cancelTenantDecommissionRequest"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "requestID": prepare_input(request_id),
                "reason": prepare_input(reason),
            },
            output=build_output_string(TenantDecommissionRequest),
        )
        if result.get(endpoint) is not None:
            return TenantDecommissionRequest.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation cancelTenantDecommissionRequest"
        )

    def register_domain(self, input_: RegisterDomainInput) -> RegisteredDomain:
        """Register a domain to the tenant."""
        endpoint = "registerDomain"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(RegisteredDomain),
        )
        if result.get(endpoint) is not None:
            return RegisteredDomain.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation registerDomain")
