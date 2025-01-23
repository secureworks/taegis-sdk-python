"""AlertsHistory Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.alerts_history.mutations import (
    TaegisSDKAlertsHistoryMutation,
)
from taegis_sdk_python.services.alerts_history.queries import (
    TaegisSDKAlertsHistoryQuery,
)
from taegis_sdk_python.services.alerts_history.subscriptions import (
    TaegisSDKAlertsHistorySubscription,
)


class AlertsHistoryService(ServiceCore):
    """Taegis AlertsHistory Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKAlertsHistoryQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKAlertsHistoryMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKAlertsHistorySubscription(self)
        return self._subscriptions
