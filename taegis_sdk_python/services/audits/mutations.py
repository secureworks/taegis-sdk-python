"""Audits Mutation."""
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
from taegis_sdk_python.services.audits.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.audits import AuditsService

log = logging.getLogger(__name__)


class TaegisSDKAuditsMutation:
    """Taegis Audits Mutation operations."""

    def __init__(self, service: AuditsService):
        self.service = service

    def create_audit(self, audit: AuditInput) -> Audit:
        """Create a new audit log."""
        endpoint = "createAudit"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "audit": prepare_input(audit),
            },
            output=build_output_string(Audit),
        )
        if result.get(endpoint) is not None:
            return Audit.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createAudit")
