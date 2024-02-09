""""ThreatScore Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.threat_score.mutations import (
    TaegisSDKThreatScoreMutation,
)
from taegis_sdk_python.services.threat_score.queries import TaegisSDKThreatScoreQuery
from taegis_sdk_python.services.threat_score.subscriptions import (
    TaegisSDKThreatScoreSubscription,
)


class ThreatScoreService(ServiceCore):
    """Taegis ThreatScore Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKThreatScoreQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKThreatScoreMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKThreatScoreSubscription(self)
        return self._subscriptions
