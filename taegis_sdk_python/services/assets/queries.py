"""Assets Query."""
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
from taegis_sdk_python.services.assets.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.assets import AssetsService


class TaegisSDKAssetsQuery:
    """Teagis Assets Query operations."""

    def __init__(self, service: AssetsService):
        self.service = service

    def tag(self, id_: str) -> Tag:
        """Gen an asset tag by id."""
        endpoint = "tag"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Tag),
        )
        if result.get(endpoint) is not None:
            return Tag.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query tag")

    def asset(self, id_: str) -> Asset:
        """Get an asset by id."""
        endpoint = "asset"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query asset")

    def assets_by_tag(self, tags: List[str]) -> List[Asset]:
        """Get a list of assets with tag."""
        endpoint = "assetsByTag"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "tags": prepare_input(tags),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query assetsByTag")

    def all_unique_tags(self) -> List[str]:
        """Get a list of all unique tags."""
        endpoint = "allUniqueTags"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query allUniqueTags")

    def asset_endpoint_info(self, id_: str) -> EndpointInfo:
        """Get RedCloak endpoint info by id."""
        endpoint = "assetEndpointInfo"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(EndpointInfo),
        )
        if result.get(endpoint) is not None:
            return EndpointInfo.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query assetEndpointInfo")

    def all_assets(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        order_by: Optional[AssetsOrderByInput] = None,
        order_direction: Optional[AssetsOrderDirectionInput] = None,
        filter_asset_state: Optional[AssetStateFilter] = None,
        only_most_recent: Optional[bool] = None,
    ) -> AssetsResult:
        """Get a list of assets."""
        endpoint = "allAssets"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "offset": prepare_input(offset),
                "limit": prepare_input(limit),
                "order_by": prepare_input(order_by),
                "order_direction": prepare_input(order_direction),
                "filter_asset_state": prepare_input(filter_asset_state),
                "only_most_recent": prepare_input(only_most_recent),
            },
            output=build_output_string(AssetsResult),
        )
        if result.get(endpoint) is not None:
            return AssetsResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query allAssets")

    def all_assets_export(
        self, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> AssetsResult:
        """Get a list of assets for export to CSV."""
        endpoint = "allAssetsExport"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "offset": prepare_input(offset),
                "limit": prepare_input(limit),
            },
            output=build_output_string(AssetsResult),
        )
        if result.get(endpoint) is not None:
            return AssetsResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query allAssetsExport")

    def asset_count(self, endpoint_type: Optional[AgentType] = None) -> AssetCounts:
        """Count of assets of a specific endpoint_type."""
        endpoint = "assetCount"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "endpoint_type": prepare_input(endpoint_type),
            },
            output=build_output_string(AssetCounts),
        )
        if result.get(endpoint) is not None:
            return AssetCounts.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query assetCount")

    def asset_count_group_by_endpoint_type(self) -> List[AssetCountsByEndpointType]:
        """Count of assets of grouped by endpoint_type."""
        endpoint = "assetCountGroupByEndpointType"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(AssetCountsByEndpointType),
        )
        if result.get(endpoint) is not None:
            return AssetCountsByEndpointType.schema().load(
                result.get(endpoint), many=True
            )
        raise GraphQLNoRowsInResultSetError("for query assetCountGroupByEndpointType")

    def all_assets_count(self) -> AssetCounts:
        """Count of all assets."""
        endpoint = "allAssetsCount"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AssetCounts)
        )
        if result.get(endpoint) is not None:
            return AssetCounts.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query allAssetsCount")

    def assets_by_ids(self, ids: List[str]) -> List[Asset]:
        """Bulk lookup by ids."""
        endpoint = "assetsByIds"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query assetsByIds")

    def assets_by_host_ids(self, host_ids: List[str]) -> List[Asset]:
        """Bulk lookup by hostIds."""
        endpoint = "assetsByHostIds"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "hostIds": prepare_input(host_ids),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query assetsByHostIds")

    def assets_by_ip_addresses(self, ip_addresses: List[str]) -> List[Asset]:
        """Bulk lookup by ipAddress."""
        endpoint = "assetsByIpAddresses"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ipAddresses": prepare_input(ip_addresses),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query assetsByIpAddresses")

    def all_asset_histories(
        self, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> List[AssetHistory]:
        """Get a list of asset histories for the tenant."""
        endpoint = "allAssetHistories"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "offset": prepare_input(offset),
                "limit": prepare_input(limit),
            },
            output=build_output_string(AssetHistory),
        )
        if result.get(endpoint) is not None:
            return AssetHistory.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query allAssetHistories")

    def asset_red_cloak_histories(
        self, id_: str, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> List[AssetRedCloakHistory]:
        """Get history of actions on an asset by id (includes RedCloack history)."""
        endpoint = "assetRedCloakHistories"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "offset": prepare_input(offset),
                "limit": prepare_input(limit),
            },
            output=build_output_string(AssetRedCloakHistory),
        )
        if result.get(endpoint) is not None:
            return AssetRedCloakHistory.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query assetRedCloakHistories")

    def search_assets(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        hostname: Optional[str] = None,
        host_id: Optional[str] = None,
        ip_address: Optional[str] = None,
        mac_address: Optional[str] = None,
        os_version: Optional[str] = None,
        os_family: Optional[str] = None,
        os_distributor: Optional[str] = None,
        sensor_version: Optional[str] = None,
        username: Optional[str] = None,
        endpoint_type: Optional[str] = None,
        tag: Optional[str] = None,
        host_id_partial_match: Optional[bool] = None,
        only_most_recent: Optional[bool] = None,
        order_by: Optional[AssetsOrderByInput] = None,
        order_direction: Optional[AssetsOrderDirectionInput] = None,
        or_search: Optional[bool] = None,
        filter_asset_state: Optional[AssetStateFilter] = None,
    ) -> AssetsResult:
        """search assets. Soon to be deprecated."""
        endpoint = "searchAssets"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "offset": prepare_input(offset),
                "limit": prepare_input(limit),
                "hostname": prepare_input(hostname),
                "host_id": prepare_input(host_id),
                "ip_address": prepare_input(ip_address),
                "mac_address": prepare_input(mac_address),
                "os_version": prepare_input(os_version),
                "os_family": prepare_input(os_family),
                "os_distributor": prepare_input(os_distributor),
                "sensor_version": prepare_input(sensor_version),
                "username": prepare_input(username),
                "endpoint_type": prepare_input(endpoint_type),
                "tag": prepare_input(tag),
                "host_id_partial_match": prepare_input(host_id_partial_match),
                "only_most_recent": prepare_input(only_most_recent),
                "order_by": prepare_input(order_by),
                "order_direction": prepare_input(order_direction),
                "or_search": prepare_input(or_search),
                "filter_asset_state": prepare_input(filter_asset_state),
            },
            output=build_output_string(AssetsResult),
        )
        if result.get(endpoint) is not None:
            return AssetsResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query searchAssets")

    def search_assets_v2(
        self,
        input_: SearchAssetsInput,
        pagination_input: Optional[SearchAssetsPaginationInput] = None,
    ) -> AssetsResult:
        """search assets v2."""
        endpoint = "searchAssetsV2"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
                "paginationInput": prepare_input(pagination_input),
            },
            output=build_output_string(AssetsResult),
        )
        if result.get(endpoint) is not None:
            return AssetsResult.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query searchAssetsV2")

    def export_search_assets(
        self,
        input_: SearchAssetsInput,
        pagination_input: Optional[SearchAssetsPaginationInput] = None,
        legacy: Optional[bool] = None,
    ) -> AssetsExportOutput:
        """export search assets results."""
        endpoint = "exportSearchAssets"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
                "paginationInput": prepare_input(pagination_input),
                "legacy": prepare_input(legacy),
            },
            output=build_output_string(AssetsExportOutput),
        )
        if result.get(endpoint) is not None:
            return AssetsExportOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query exportSearchAssets")

    def assets_by_session(self, arguments: AssetsBySessionArguments) -> List[Asset]:
        """Return a list of assets for multiple tenants."""
        endpoint = "assetsBySession"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "arguments": prepare_input(arguments),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query assetsBySession")
