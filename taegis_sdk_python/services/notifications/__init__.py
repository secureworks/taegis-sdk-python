""""Notifications Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.notifications.mutations import (
    TaegisSDKNotificationsMutation,
)
from taegis_sdk_python.services.notifications.queries import TaegisSDKNotificationsQuery
from taegis_sdk_python.services.notifications.subscriptions import (
    TaegisSDKNotificationsSubscription,
)


class NotificationsService(ServiceCore):
    """Taegis Notifications Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKNotificationsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKNotificationsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKNotificationsSubscription(self)
        return self._subscriptions
