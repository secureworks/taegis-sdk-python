"""AccessPoints Query."""

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
from taegis_sdk_python.services.access_points.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.access_points import AccessPointsService

log = logging.getLogger(__name__)


class TaegisSDKAccessPointsQuery:
    """Taegis Access_points Query operations."""

    def __init__(self, service: AccessPointsService):
        self.service = service

    def get_access_point(self) -> AccessPoint:
        """None."""
        endpoint = "getAccessPoint"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(AccessPoint)
        )
        if result.get(endpoint) is not None:
            return AccessPoint.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getAccessPoint")

    def get_access_point_template(self) -> AccessPointCloudFormation:
        """None."""
        endpoint = "getAccessPointTemplate"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(AccessPointCloudFormation),
        )
        if result.get(endpoint) is not None:
            return AccessPointCloudFormation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getAccessPointTemplate")

    def get_access_point_prefixes(self) -> AccessPointPrefixes:
        """None."""
        endpoint = "getAccessPointPrefixes"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(AccessPointPrefixes),
        )
        if result.get(endpoint) is not None:
            return AccessPointPrefixes.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getAccessPointPrefixes")
