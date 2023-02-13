"""Alerts Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.alerts.mutations import TaegisSDKAlertsMutation
from taegis_sdk_python.services.alerts.queries import TaegisSDKAlertsQuery
from taegis_sdk_python.services.alerts.subscriptions import (
    TaegisSDKAlertsSubscription,
)


class AlertsService(ServiceCore):
    """Taegis Alerts Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKAlertsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKAlertsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKAlertsSubscription(self)
        return self._subscriptions
