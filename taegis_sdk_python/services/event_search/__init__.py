""""EventSearch Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.event_search.mutations import (
    TaegisSDKEventSearchMutation,
)
from taegis_sdk_python.services.event_search.queries import TaegisSDKEventSearchQuery
from taegis_sdk_python.services.event_search.subscriptions import (
    TaegisSDKEventSearchSubscription,
)


class EventSearchService(ServiceCore):
    """Taegis EventSearch Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKEventSearchQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKEventSearchMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKEventSearchSubscription(self)
        return self._subscriptions
