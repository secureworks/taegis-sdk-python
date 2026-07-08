"""QueryRelay Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.query_relay.mutations import TaegisSDKQueryRelayMutation
from taegis_sdk_python.services.query_relay.queries import TaegisSDKQueryRelayQuery
from taegis_sdk_python.services.query_relay.subscriptions import (
    TaegisSDKQueryRelaySubscription,
)


class QueryRelayService(ServiceCore):
    """Taegis QueryRelay Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKQueryRelayQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKQueryRelayMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKQueryRelaySubscription(self)
        return self._subscriptions
