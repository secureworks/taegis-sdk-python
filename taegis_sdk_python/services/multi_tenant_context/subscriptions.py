"""MultiTenantContext Subscription."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.multi_tenant_context.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.multi_tenant_context import (
        MultiTenantContextService,
    )

log = logging.getLogger(__name__)


class TaegisSDKMultiTenantContextSubscription:
    """Taegis Multi_tenant_context Subscription operations."""

    def __init__(self, service: MultiTenantContextService):
        self.service = service
