"""Tenants4 Mutation."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.tenants4.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.tenants4 import Tenants4Service

log = logging.getLogger(__name__)


class TaegisSDKTenants4Mutation:
    """Taegis Tenants4 Mutation operations."""

    def __init__(self, service: Tenants4Service):
        self.service = service

    def delete_cached_entries(
        self, input_: DeleteCachedEntriesInput
    ) -> DeleteCachedEntriesOutput:
        """Delete entries from cache. Non-atomic transaction."""
        endpoint = "deleteCachedEntries"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(DeleteCachedEntriesOutput),
        )
        if result.get(endpoint) is not None:
            return DeleteCachedEntriesOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteCachedEntries")
