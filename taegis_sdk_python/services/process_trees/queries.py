"""ProcessTrees Query."""

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
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.process_trees.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.process_trees import ProcessTreesService

log = logging.getLogger(__name__)


class TaegisSDKProcessTreesQuery:
    """Taegis Process_trees Query operations."""

    def __init__(self, service: ProcessTreesService):
        self.service = service

    def get_process_children(
        self,
        tenant_id: str,
        host_id: str,
        process_correlation_id: str,
        resource_id: Optional[str] = None,
    ) -> Children:
        """None."""
        endpoint = "GetProcessChildren"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "tenantID": prepare_input(tenant_id),
                "hostID": prepare_input(host_id),
                "processCorrelationID": prepare_input(process_correlation_id),
                "resourceID": prepare_input(resource_id),
            },
            output=build_output_string(Children),
        )
        if result.get(endpoint) is not None:
            return Children.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query GetProcessChildren")

    def get_process_parent(
        self,
        tenant_id: str,
        host_id: str,
        parent_process_correlation_id: str,
        resource_id: Optional[str] = None,
    ) -> ProcessEvent:
        """None."""
        endpoint = "GetProcessParent"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "tenantID": prepare_input(tenant_id),
                "hostID": prepare_input(host_id),
                "parentProcessCorrelationID": prepare_input(
                    parent_process_correlation_id
                ),
                "resourceID": prepare_input(resource_id),
            },
            output=build_output_string(ProcessEvent),
        )
        if result.get(endpoint) is not None:
            return ProcessEvent.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query GetProcessParent")
