"""Assets2 Mutation."""
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
from taegis_sdk_python.services.assets2.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.assets2 import Assets2Service

log = logging.getLogger(__name__)


class TaegisSDKAssets2Mutation:
    """Taegis Assets2 Mutation operations."""

    def __init__(self, service: Assets2Service):
        self.service = service

    def update_tags_for_endpoint_v2(
        self, input_: UpdateTagsForEndpointInputV2
    ) -> BulkOpPayloadV2:
        """Start a job to update the tags for a given endpoint. Use the task ID
        in the response to poll the updateTagsForEndpointStatusV2 query to
        determine if the job succeeded.

        Note: any tags passed in the input will completely replace the current
        tags for the endpoint. If the intention is to change/remove a single
        tag, query the asset first to get the current set of tags for the
        endpoint, then pass the complete set of tags desired with the changes
        included.."""
        endpoint = "updateTagsForEndpointV2"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateTagsForEndpointV2")

    def bulk_update_tags_for_endpoints_v2(
        self, input_: BulkUpdateTagsForEndpointsInputV2
    ) -> BulkOpPayloadV2:
        """Start a job to update the tags for multiple endpoints: it does not
        overwrite tags, it adds the tags in the input to the endpoints. If any
        endpoints have tags with the same key, but a different value, the value
        will be updated with the value in the input. Use the task ID in the
        response to poll the bulkUpdateTagsForEndpointsStatusV2 query to
        determine if the job succeeded.."""
        endpoint = "bulkUpdateTagsForEndpointsV2"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation bulkUpdateTagsForEndpointsV2")

    def delete_assets_v2(self, input_: DeleteAssetsInputV2) -> BulkOpPayloadV2:
        """Start a job to "soft" delete the assets matching the filter criteria.
        Use the task ID in the response to poll the deleteAssetsStatusV2
        query to determine if the job succeeded.."""
        endpoint = "deleteAssetsV2"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteAssetsV2")

    def restore_assets_v2(self, input_: RestoreAssetsInputV2) -> BulkOpPayloadV2:
        """Start a job to restore assets that were previously deleted and that
        match the filter criteria. Use the task ID in the response to poll the
        restoreAssetsStatusV2 query to determine if the job succeeded.."""
        endpoint = "restoreAssetsV2"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation restoreAssetsV2")

    def assign_bulk_assets_to_group(
        self, input_: AssignBulkAssetsToGroupInput
    ) -> BulkOpPayloadV2:
        """Start a job to assign the endpoints matching the filter criteria to the
        endpoint group in the input. Use the task ID in the response to poll the
        assignBulkAssetsToGroupStatus query to determine if the job succeeded.."""
        endpoint = "assignBulkAssetsToGroup"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation assignBulkAssetsToGroup")

    def bulk_delete_tags_for_endpoints_v2(
        self, input_: BulkDeleteTagsForEndpointsInputV2
    ) -> BulkOpPayloadV2:
        """Start a job to delete the provided tags from the endpoints matching the
        filter criteria in the input. Use the task ID in the response to poll
        the bulkDeleteTagsForEndpointsStatusV2 query to determine if the job
        succeeded.."""
        endpoint = "bulkDeleteTagsForEndpointsV2"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation bulkDeleteTagsForEndpointsV2")

    def assign_bulk_assets_to_investigation(
        self, input_: AssignBulkAssetsToInvestigationInput
    ) -> BulkOpPayloadV2:
        """Start a job to assign the endpoints matching the filter criteria to the
        investigation in the input. Use the task ID in the response to poll the
        assignBulkAssetsToInvestigationStatus query to determine if the job succeeded..
        """
        endpoint = "assignBulkAssetsToInvestigation"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation assignBulkAssetsToInvestigation"
        )

    def bulk_delete_investigation_for_endpoints(
        self, input_: BulkDeleteInvestigationForEndpointsInput
    ) -> BulkOpPayloadV2:
        """Start a job to delete the provided investigation from the endpoints matching
        the filter criteria in the input. Use the task ID in the response to poll the
        bulkDeleteInvestigationForEndpointsStatus query to determine if the job succeeded..
        """
        endpoint = "bulkDeleteInvestigationForEndpoints"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation bulkDeleteInvestigationForEndpoints"
        )

    def bulk_reconnect_native_assets(
        self, input_: BulkReconnectNativeAssetsInput
    ) -> BulkOpPayloadV2:
        """None."""
        endpoint = "bulkReconnectNativeAssets"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation bulkReconnectNativeAssets")

    def bulk_uninstall_native_assets(
        self, input_: BulkUninstallNativeAssetsInput
    ) -> BulkOpPayloadV2:
        """None."""
        endpoint = "bulkUninstallNativeAssets"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(BulkOpPayloadV2),
        )
        if result.get(endpoint) is not None:
            return BulkOpPayloadV2.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation bulkUninstallNativeAssets")
