""""Threat Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.threat.mutations import TaegisSDKThreatMutation
from taegis_sdk_python.services.threat.queries import TaegisSDKThreatQuery
from taegis_sdk_python.services.threat.subscriptions import (
    TaegisSDKThreatSubscription,
)


class ThreatService(ServiceCore):
    """Taegis Threat Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKThreatQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKThreatMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKThreatSubscription(self)
        return self._subscriptions
