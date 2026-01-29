"""Notifications2 Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.notifications2.mutations import (
    TaegisSDKNotifications2Mutation,
)
from taegis_sdk_python.services.notifications2.queries import (
    TaegisSDKNotifications2Query,
)
from taegis_sdk_python.services.notifications2.subscriptions import (
    TaegisSDKNotifications2Subscription,
)


class Notifications2Service(ServiceCore):
    """Taegis Notifications Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKNotifications2Query(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKNotifications2Mutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKNotifications2Subscription(self)
        return self._subscriptions
