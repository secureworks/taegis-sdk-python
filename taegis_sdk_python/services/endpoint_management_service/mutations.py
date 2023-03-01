"""EndpointManagementService Mutation."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import (
    build_output_string,
    prepare_input,
    parse_union_result,
)
from taegis_sdk_python.services.endpoint_management_service.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.endpoint_management_service import (
        EndpointManagementServiceService,
    )


class TaegisSDKEndpointManagementServiceMutation:
    """Teagis Endpoint_management_service Mutation operations."""

    def __init__(self, service: EndpointManagementServiceService):
        self.service = service

    def create_endpoint_group(self, input_: CreateEndpointGroupInput) -> EndpointGroup:
        """Create new endpoint group for a tenant.."""
        endpoint = "createEndpointGroup"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(EndpointGroup),
        )
        if result.get(endpoint) is not None:
            return EndpointGroup.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createEndpointGroup")

    def update_endpoint_group(self, input_: UpdateEndpointGroupInput) -> EndpointGroup:
        """Update policy type of endpoint group for a tenant.."""
        endpoint = "updateEndpointGroup"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(EndpointGroup),
        )
        if result.get(endpoint) is not None:
            return EndpointGroup.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateEndpointGroup")

    def delete_endpoint_group(self, input_: DeleteEndpointGrpInput) -> bool:
        """Delete endpoint group for a tenant.."""
        endpoint = "deleteEndpointGroup"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation deleteEndpointGroup")

    def create_policy(self, input_: CreatePolicyInput) -> Policy:
        """Create new policy. Used by administrator of the taegis."""
        endpoint = "createPolicy"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Policy),
        )
        if result.get(endpoint) is not None:
            return Policy.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createPolicy")

    def assign_bulk_assets_to_group(
        self, input_: Optional[BulkAssignRequestInput] = None
    ) -> BulkAssignRequestOutput:
        """Assign the assets to target group."""
        endpoint = "assignBulkAssetsToGroup"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkAssignRequestOutput),
        )
        if result.get(endpoint) is not None:
            return BulkAssignRequestOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation assignBulkAssetsToGroup")
