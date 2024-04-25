""""IngestStats Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.ingest_stats.mutations import (
    TaegisSDKIngestStatsMutation,
)
from taegis_sdk_python.services.ingest_stats.queries import TaegisSDKIngestStatsQuery
from taegis_sdk_python.services.ingest_stats.subscriptions import (
    TaegisSDKIngestStatsSubscription,
)


class IngestStatsService(ServiceCore):
    """Taegis IngestStats Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKIngestStatsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKIngestStatsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKIngestStatsSubscription(self)
        return self._subscriptions
