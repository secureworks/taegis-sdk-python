"""EndpointManagementService Query."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.endpoint_management_service.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.endpoint_management_service import (
        EndpointManagementServiceService,
    )


log = logging.getLogger(__name__)


class TaegisSDKEndpointManagementServiceQuery:
    """Taegis Endpoint_management_service Query operations."""

    def __init__(self, service: EndpointManagementServiceService):
        self.service = service

    def all_endpoint_groups(self) -> List[EndpointGroup]:
        """Get list of all endpoint groups for a tenant."""
        endpoint = "allEndpointGroups"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(EndpointGroup)
        )
        if result.get(endpoint) is not None:
            return EndpointGroup.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query allEndpointGroups")

    def all_endpoint_groups_paged(
        self, first: Optional[int] = None, after: Optional[str] = None
    ) -> EndpointGroupsPagedOutput:
        """Get list of all endpoint groups for a tenant, paged."""
        endpoint = "allEndpointGroupsPaged"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "first": prepare_input(first),
                "after": prepare_input(after),
            },
            output=build_output_string(EndpointGroupsPagedOutput),
        )
        if result.get(endpoint) is not None:
            return EndpointGroupsPagedOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query allEndpointGroupsPaged")

    def endpoint_group_by_id(self, arguments: EndpointGroupArguments) -> EndpointGroup:
        """Get a endpoint group filtered by id."""
        endpoint = "endpointGroupByID"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(EndpointGroup),
        )
        if result.get(endpoint) is not None:
            return EndpointGroup.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query endpointGroupByID")

    def endpoint_group_by_registration_key(
        self, registration_key: str
    ) -> EndpointGroup:
        """Get a endpoint group by registration_key."""
        endpoint = "endpointGroupByRegistrationKey"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "registrationKey": prepare_input(registration_key),
            },
            output=build_output_string(EndpointGroup),
        )
        if result.get(endpoint) is not None:
            return EndpointGroup.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query endpointGroupByRegistrationKey")

    def policy_by_name(self, arguments: PolicyArguments) -> List[Policy]:
        """Get a policy by name and filtered by registration_key."""
        endpoint = "policyByName"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(Policy),
        )
        if result.get(endpoint) is not None:
            return Policy.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query policyByName")

    def bulk_assignment_status_by_request_id(
        self, request_id: str
    ) -> BulkAssignRequestOutput:
        """Get a asset bulk action status  by request Id."""
        endpoint = "bulkAssignmentStatusByRequestID"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "requestId": prepare_input(request_id),
            },
            output=build_output_string(BulkAssignRequestOutput),
        )
        if result.get(endpoint) is not None:
            return BulkAssignRequestOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query bulkAssignmentStatusByRequestID")

    def bulk_assignment_status_by_id(self, id_: str) -> BulkAssignRequestOutput:
        """Get a asset bulk action status  by request Id."""
        endpoint = "bulkAssignmentStatusByID"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(BulkAssignRequestOutput),
        )
        if result.get(endpoint) is not None:
            return BulkAssignRequestOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query bulkAssignmentStatusByID")

    def default_agent_setting(self) -> AgentSetting:
        """fetch the default agent settings item."""
        endpoint = "defaultAgentSetting"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AgentSetting)
        )
        if result.get(endpoint) is not None:
            return AgentSetting.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query defaultAgentSetting")

    def agent_setting(self, id_: str) -> AgentSetting:
        """fetch a single agent settings item by id."""
        endpoint = "agentSetting"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(AgentSetting),
        )
        if result.get(endpoint) is not None:
            return AgentSetting.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query agentSetting")

    def agent_settings(
        self, first: Optional[int] = None, after: Optional[str] = None
    ) -> AgentSettings:
        """fetch paginated list of agent settings items."""
        endpoint = "agentSettings"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "first": prepare_input(first),
                "after": prepare_input(after),
            },
            output=build_output_string(AgentSettings),
        )
        if result.get(endpoint) is not None:
            return AgentSettings.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query agentSettings")

    def get_settings_for_profile(
        self, profile_name: Optional[Union[AgentSettingsProfile, TaegisEnum]] = None
    ) -> AgentSettingsDefaults:
        """fetch the setting defaults for a given profile."""
        endpoint = "getSettingsForProfile"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "profileName": prepare_input(profile_name),
            },
            output=build_output_string(AgentSettingsDefaults),
        )
        if result.get(endpoint) is not None:
            return AgentSettingsDefaults.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getSettingsForProfile")
