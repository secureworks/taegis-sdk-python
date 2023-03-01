"""Sharelinks Mutation."""
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
from taegis_sdk_python.services.sharelinks.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.sharelinks import SharelinksService


class TaegisSDKSharelinksMutation:
    """Teagis Sharelinks Mutation operations."""

    def __init__(self, service: SharelinksService):
        self.service = service

    def create_share_link(self, input_: ShareLinkCreateInput) -> ShareLink:
        """Create a new ShareLink."""
        endpoint = "createShareLink"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(ShareLink),
        )
        if result.get(endpoint) is not None:
            return ShareLink.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createShareLink")
