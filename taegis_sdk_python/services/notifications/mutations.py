"""Notifications Mutation."""
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


class TaegisSDKNotificationsMutation:
    """Teagis Notifications Mutation operations."""

    def __init__(self, service: NotificationsService):
        self.service = service

    def create_notification(self, notification: NotificationInput) -> Notification:
        """Create new notification by passing in a text message and HTML message."""
        endpoint = "createNotification"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "notification": prepare_input(notification),
            },
            output=build_output_string(Notification),
        )
        if result.get(endpoint) is not None:
            return Notification.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createNotification")

    def create_notification_via_template(
        self, notification: NotificationTemplateInput
    ) -> Notification:
        """Create new notification via a template stored in the API by passing in the template type and template variables."""
        endpoint = "createNotificationViaTemplate"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "notification": prepare_input(notification),
            },
            output=build_output_string(Notification),
        )
        if result.get(endpoint) is not None:
            return Notification.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation createNotificationViaTemplate"
        )

    def create_notification_with_existing_html(
        self, notification: NotificationInput
    ) -> Notification:
        """Create notification using an existing HTML header/footer/CSS template."""
        endpoint = "createNotificationWithExistingHTML"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "notification": prepare_input(notification),
            },
            output=build_output_string(Notification),
        )
        if result.get(endpoint) is not None:
            return Notification.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation createNotificationWithExistingHTML"
        )

    def update_notification(
        self, notification_id: str, notification: UpdateNotificationInput
    ) -> Notification:
        """Update notification."""
        endpoint = "updateNotification"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "notification_id": prepare_input(notification_id),
                "notification": prepare_input(notification),
            },
            output=build_output_string(Notification),
        )
        if result.get(endpoint) is not None:
            return Notification.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateNotification")

    def delete_notification(self, notification_id: str) -> Notification:
        """Delete notification."""
        endpoint = "deleteNotification"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "notification_id": prepare_input(notification_id),
            },
            output=build_output_string(Notification),
        )
        if result.get(endpoint) is not None:
            return Notification.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteNotification")

    def bulk_delete_notification(self, ids: List[str]) -> List[Notification]:
        """Deletes a list of notificaitons."""
        endpoint = "bulkDeleteNotification"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output=build_output_string(Notification),
        )
        if result.get(endpoint) is not None:
            return Notification.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation bulkDeleteNotification")

    def read_notification(self, notification_id: str) -> Notification:
        """Marks a notification as read."""
        endpoint = "readNotification"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "notification_id": prepare_input(notification_id),
            },
            output=build_output_string(Notification),
        )
        if result.get(endpoint) is not None:
            return Notification.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation readNotification")

    def bulk_read_notification(
        self, ids: List[str], mark_all_as_read: Optional[bool] = None
    ) -> List[Notification]:
        """Marks a list of notifications as read."""
        endpoint = "bulkReadNotification"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
                "mark_all_as_read": prepare_input(mark_all_as_read),
            },
            output=build_output_string(Notification),
        )
        if result.get(endpoint) is not None:
            return Notification.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation bulkReadNotification")

    def bulk_restore_notifications(self, ids: List[str]) -> List[str]:
        """Bulk restore deleted notifications."""
        endpoint = "bulkRestoreNotifications"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation bulkRestoreNotifications")
