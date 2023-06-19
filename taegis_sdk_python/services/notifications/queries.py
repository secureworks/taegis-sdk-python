"""Notifications Query."""
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


class TaegisSDKNotificationsQuery:
    """Teagis Notifications Query operations."""

    def __init__(self, service: NotificationsService):
        self.service = service

    def notifications(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        is_deleted: Optional[bool] = None,
        is_read: Optional[bool] = None,
        order_direction: Optional[NotificationsOrderDirection] = None,
    ) -> NotificationsOutput:
        """Get all Notifications.."""
        endpoint = "notifications"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "page": prepare_input(page),
                "per_page": prepare_input(per_page),
                "is_deleted": prepare_input(is_deleted),
                "is_read": prepare_input(is_read),
                "order_direction": prepare_input(order_direction),
            },
            output=build_output_string(NotificationsOutput),
        )
        if result.get(endpoint) is not None:
            return NotificationsOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query notifications")

    def notification(self, notification_id: str) -> Notification:
        """Get an notification by id."""
        endpoint = "notification"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "notification_id": prepare_input(notification_id),
            },
            output=build_output_string(Notification),
        )
        if result.get(endpoint) is not None:
            return Notification.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query notification")
