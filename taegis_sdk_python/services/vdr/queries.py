"""Vdr Query."""

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
from taegis_sdk_python.services.vdr.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.vdr import VdrService

log = logging.getLogger(__name__)


class TaegisSDKVdrQuery:
    """Taegis Vdr Query operations."""

    def __init__(self, service: VdrService):
        self.service = service

    def vdr_asset(self, arguments: VdrAssetInputArgs) -> VdrAsset:
        """Get a VDR asset."""
        endpoint = "vdrAsset"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(VdrAsset),
        )
        if result.get(endpoint) is not None:
            return VdrAsset.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrAsset")

    def vdr_assets(self, arguments: VdrAssetsInputArgs) -> VdrAssets:
        """Get VDR assets."""
        endpoint = "vdrAssets"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(VdrAssets),
        )
        if result.get(endpoint) is not None:
            return VdrAssets.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrAssets")

    def vdr_vulnerabilities(
        self, arguments: VdrVulnerabilitiesInputArgs
    ) -> VdrVulnerabilities:
        """Get VDR asset vulnerabilities."""
        endpoint = "vdrVulnerabilities"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(VdrVulnerabilities),
        )
        if result.get(endpoint) is not None:
            return VdrVulnerabilities.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrVulnerabilities")

    def vdr_vulnerability_details(
        self, arguments: VdrVulnerabilityDetailsInputArgs
    ) -> VdrVulnerabilityDetails:
        """Get VDR asset vulnerability details."""
        endpoint = "vdrVulnerabilityDetails"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(VdrVulnerabilityDetails),
        )
        if result.get(endpoint) is not None:
            return VdrVulnerabilityDetails.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrVulnerabilityDetails")

    def vdr_tenant(self) -> VdrTenant:
        """Get VDR organization information."""
        endpoint = "vdrTenant"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(VdrTenant)
        )
        if result.get(endpoint) is not None:
            return VdrTenant.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrTenant")

    def vdr_inspect_host(self, arguments: VdrInspectHostArgs) -> VdrInspectHost:
        """Get Inspect Hosts information."""
        endpoint = "vdrInspectHost"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(VdrInspectHost),
        )
        if result.get(endpoint) is not None:
            return VdrInspectHost.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrInspectHost")

    def vdr_edge_services(self) -> VdrEdgeServices:
        """Get VDR edge services."""
        endpoint = "vdrEdgeServices"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(VdrEdgeServices)
        )
        if result.get(endpoint) is not None:
            return VdrEdgeServices.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrEdgeServices")

    def vdr_vulnerability_metrics(
        self, arguments: Optional[VdrVulnerabilityMetricsInputArgs] = None
    ) -> VdrVulnerabilityMetrics:
        """Get vulnerability metrics for first discovered or last seen."""
        endpoint = "vdrVulnerabilityMetrics"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(VdrVulnerabilityMetrics),
        )
        if result.get(endpoint) is not None:
            return VdrVulnerabilityMetrics.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrVulnerabilityMetrics")

    def vdr_scans(self, arguments: Optional[VdrScanInputArgs] = None) -> VdrScans:
        """Get VDR scans."""
        endpoint = "vdrScans"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(VdrScans),
        )
        if result.get(endpoint) is not None:
            return VdrScans.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrScans")

    def vdr_vulnerability_definition(
        self, definition_hash: str
    ) -> VdrVulnerabilityDefinition:
        """Get Vulnerability info and reference urls."""
        endpoint = "vdrVulnerabilityDefinition"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "definitionHash": prepare_input(definition_hash),
            },
            output=build_output_string(VdrVulnerabilityDefinition),
        )
        if result.get(endpoint) is not None:
            return VdrVulnerabilityDefinition.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query vdrVulnerabilityDefinition")

    def vdr_threat_intel(self, threat_intel_ids: List[str]) -> List[VdrThreatIntel]:
        """Get Counter Threat Unit intel."""
        endpoint = "vdrThreatIntel"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "threatIntelIds": prepare_input(threat_intel_ids),
            },
            output=build_output_string(VdrThreatIntel),
        )
        if result.get(endpoint) is not None:
            return VdrThreatIntel.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query vdrThreatIntel")
