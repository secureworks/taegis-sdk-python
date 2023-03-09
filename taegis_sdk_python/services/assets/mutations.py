"""Assets Mutation."""
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


class TaegisSDKAssetsMutation:
    """Teagis Assets Mutation operations."""

    def __init__(self, service: AssetsService):
        self.service = service

    def isolate_asset(self, id_: str, reason: str) -> Asset:
        """Isolate an asset by id."""
        endpoint = "isolateAsset"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "reason": prepare_input(reason),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation isolateAsset")

    def integrate_asset(self, id_: str, reason: str) -> Asset:
        """Integate an asset by id."""
        endpoint = "integrateAsset"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "reason": prepare_input(reason),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation integrateAsset")

    def delete_assets(self, ids: List[str], undelete: Optional[bool] = None) -> bool:
        """Delete or un-delete asset."""
        endpoint = "deleteAssets"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
                "undelete": prepare_input(undelete),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation deleteAssets")

    def create_asset_tag(self, host_id: str, tag: str) -> Tag:
        """Create a new tag for an asseti."""
        endpoint = "createAssetTag"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "hostId": prepare_input(host_id),
                "tag": prepare_input(tag),
            },
            output=build_output_string(Tag),
        )
        if result.get(endpoint) is not None:
            return Tag.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createAssetTag")

    def update_asset_tag(self, id_: str, tag: str) -> Tag:
        """Updates a tag for an asset."""
        endpoint = "updateAssetTag"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "tag": prepare_input(tag),
            },
            output=build_output_string(Tag),
        )
        if result.get(endpoint) is not None:
            return Tag.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateAssetTag")

    def delete_asset_tag(self, id_: str) -> Tag:
        """Deletes a tag for an asset."""
        endpoint = "deleteAssetTag"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Tag),
        )
        if result.get(endpoint) is not None:
            return Tag.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteAssetTag")

    def update_asset(self, asset_input: Optional[AssetInput] = None) -> Asset:
        """None."""
        endpoint = "updateAsset"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "assetInput": prepare_input(asset_input),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateAsset")

    def add_investigation_assets(
        self,
        investigation_id: str,
        host_ids: Optional[List[str]] = None,
        asset_ids: Optional[List[str]] = None,
    ) -> List[Asset]:
        """add investigation assets relation for the list of host_ids and return the asset ids."""
        endpoint = "addInvestigationAssets"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "hostIds": prepare_input(host_ids),
                "assetIds": prepare_input(asset_ids),
                "investigationId": prepare_input(investigation_id),
            },
            output=build_output_string(Asset),
        )
        if result.get(endpoint) is not None:
            return Asset.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation addInvestigationAssets")

    def remove_investigation_assets(
        self, asset_ids: List[str], investigation_id: str
    ) -> bool:
        """remove investigation assets relation."""
        endpoint = "removeInvestigationAssets"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "assetIds": prepare_input(asset_ids),
                "investigationId": prepare_input(investigation_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation removeInvestigationAssets")
