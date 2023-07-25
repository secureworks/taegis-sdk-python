"""FastIoc Mutation."""
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
from taegis_sdk_python.services.fast_ioc.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.fast_ioc import FastIocService

log = logging.getLogger(__name__)


class TaegisSDKFastIocMutation:
    """Teagis Fast_ioc Mutation operations."""

    def __init__(self, service: FastIocService):
        self.service = service
