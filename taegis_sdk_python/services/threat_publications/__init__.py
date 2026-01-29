"""ThreatPublications Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.threat_publications.mutations import (
    TaegisSDKThreatPublicationsMutation,
)
from taegis_sdk_python.services.threat_publications.queries import (
    TaegisSDKThreatPublicationsQuery,
)
from taegis_sdk_python.services.threat_publications.subscriptions import (
    TaegisSDKThreatPublicationsSubscription,
)


class ThreatPublicationsService(ServiceCore):
    """Taegis ThreatPublications Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKThreatPublicationsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKThreatPublicationsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKThreatPublicationsSubscription(self)
        return self._subscriptions
