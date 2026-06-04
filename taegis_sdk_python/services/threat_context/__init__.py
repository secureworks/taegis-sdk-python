"""ThreatContext Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.threat_context.mutations import (
    TaegisSDKThreatContextMutation,
)
from taegis_sdk_python.services.threat_context.queries import (
    TaegisSDKThreatContextQuery,
)
from taegis_sdk_python.services.threat_context.subscriptions import (
    TaegisSDKThreatContextSubscription,
)


class ThreatContextService(ServiceCore):
    """Taegis ThreatContext Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKThreatContextQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKThreatContextMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKThreatContextSubscription(self)
        return self._subscriptions
