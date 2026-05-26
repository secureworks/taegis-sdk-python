"""EventStats Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.event_stats.mutations import TaegisSDKEventStatsMutation
from taegis_sdk_python.services.event_stats.queries import TaegisSDKEventStatsQuery
from taegis_sdk_python.services.event_stats.subscriptions import (
    TaegisSDKEventStatsSubscription,
)


class EventStatsService(ServiceCore):
    """Taegis EventStats Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKEventStatsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKEventStatsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKEventStatsSubscription(self)
        return self._subscriptions
