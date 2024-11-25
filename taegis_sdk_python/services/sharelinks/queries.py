"""Sharelinks Query."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.sharelinks.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.sharelinks import SharelinksService


log = logging.getLogger(__name__)


class TaegisSDKSharelinksQuery:
    """Taegis Sharelinks Query operations."""

    def __init__(self, service: SharelinksService):
        self.service = service

    def share_link_by_id(self, id_: str) -> ShareLink:
        """Fetch a ShareLink by ID."""
        endpoint = "shareLinkById"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(ShareLink),
        )
        if result.get(endpoint) is not None:
            return ShareLink.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query shareLinkById")
