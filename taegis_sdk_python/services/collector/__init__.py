""""Collector Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.collector.mutations import TaegisSDKCollectorMutation
from taegis_sdk_python.services.collector.queries import TaegisSDKCollectorQuery
from taegis_sdk_python.services.collector.subscriptions import (
    TaegisSDKCollectorSubscription,
)


class CollectorService(ServiceCore):
    """Taegis Collector Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKCollectorQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKCollectorMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKCollectorSubscription(self)
        return self._subscriptions
