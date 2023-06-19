"""Notifications Subscription."""
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
from taegis_sdk_python.services.notifications.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.notifications import NotificationsService

log = logging.getLogger(__name__)


class TaegisSDKNotificationsSubscription:
    """Teagis Notifications Subscription operations."""

    def __init__(self, service: NotificationsService):
        self.service = service
