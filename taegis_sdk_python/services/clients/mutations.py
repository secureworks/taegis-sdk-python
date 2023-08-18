"""Clients Mutation."""
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
from taegis_sdk_python.services.clients.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.clients import ClientsService

log = logging.getLogger(__name__)


class TaegisSDKClientsMutation:
    """Taegis Clients Mutation operations."""

    def __init__(self, service: ClientsService):
        self.service = service

    def create_client(self, name: str, roles: List[str]) -> NewClient:
        """Create a new client (SCWX (tenant 5000) clients are disallowed)."""
        endpoint = "createClient"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "name": prepare_input(name),
                "roles": prepare_input(roles),
            },
            output=build_output_string(NewClient),
        )
        if result.get(endpoint) is not None:
            return NewClient.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createClient")

    def rotate_client_secret(self, id_: str) -> NewClient:
        """Generate a new secret for an existing client."""
        endpoint = "rotateClientSecret"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(NewClient),
        )
        if result.get(endpoint) is not None:
            return NewClient.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation rotateClientSecret")

    def append_client_roles(
        self, id_: str, roles: List[ClientRoleAssignmentInput]
    ) -> Client:
        """Append roles to a clients role assignments (internal roles are forbidden)."""
        endpoint = "appendClientRoles"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "roles": prepare_input(roles),
            },
            output=build_output_string(Client),
        )
        if result.get(endpoint) is not None:
            return Client.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation appendClientRoles")

    def remove_client_roles(self, id_: str, roles: List[str]) -> Client:
        """Remove roles from a clients role assignments (internal roles are forbidden)."""
        endpoint = "removeClientRoles"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "roles": prepare_input(roles),
            },
            output=build_output_string(Client),
        )
        if result.get(endpoint) is not None:
            return Client.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation removeClientRoles")

    def delete_client(self, id_: str) -> Client:
        """Delete a client."""
        endpoint = "deleteClient"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Client),
        )
        if result.get(endpoint) is not None:
            return Client.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteClient")
