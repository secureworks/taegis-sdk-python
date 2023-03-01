"""Agent Query."""
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
from taegis_sdk_python.services.agent.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.agent import AgentService


class TaegisSDKAgentQuery:
    """Teagis Agent Query operations."""

    def __init__(self, service: AgentService):
        self.service = service

    def agent_packages(
        self, args: Optional[PackageSearchInput] = None
    ) -> List[Package]:
        """None."""
        endpoint = "agentPackages"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "args": prepare_input(args),
            },
            output=build_output_string(Package),
        )
        if result.get(endpoint) is not None:
            return Package.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query agentPackages")

    def agent_package_signed_url(
        self, args: Optional[PackageDownloadInput] = None
    ) -> PackageSignedUrl:
        """None."""
        endpoint = "agentPackageSignedUrl"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "args": prepare_input(args),
            },
            output=build_output_string(PackageSignedUrl),
        )
        if result.get(endpoint) is not None:
            return PackageSignedUrl.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query agentPackageSignedUrl")

    def agent_package_signed_url_by_id(self, id_: str) -> PackageSignedUrl:
        """None."""
        endpoint = "agentPackageSignedUrlByID"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(PackageSignedUrl),
        )
        if result.get(endpoint) is not None:
            return PackageSignedUrl.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query agentPackageSignedUrlByID")
