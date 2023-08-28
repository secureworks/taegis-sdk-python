"""Authz Mutation."""
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


class TaegisSDKAuthzMutation:
    """Taegis Authz Mutation operations."""

    def __init__(self, service: AuthzService):
        self.service = service

    def authz_custom_role_create(self, input_: AuthzCustomRoleCreateInput) -> AuthzRole:
        """AuthzCustomRoleCreate creates a new custom role."""
        endpoint = "AuthzCustomRoleCreate"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(AuthzRole),
        )
        if result.get(endpoint) is not None:
            return AuthzRole.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation AuthzCustomRoleCreate")

    def authz_custom_role_update(self, input_: AuthzCustomRoleUpdateInput) -> AuthzRole:
        """authzCustomRoleUpdate updates an existing custom role."""
        endpoint = "authzCustomRoleUpdate"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(AuthzRole),
        )
        if result.get(endpoint) is not None:
            return AuthzRole.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation authzCustomRoleUpdate")
