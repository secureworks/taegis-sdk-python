"""Search Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.search.mutations import TaegisSDKSearchMutation
from taegis_sdk_python.services.search.queries import TaegisSDKSearchQuery
from taegis_sdk_python.services.search.subscriptions import TaegisSDKSearchSubscription


class SearchService(ServiceCore):
    """Taegis Search Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKSearchQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKSearchMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKSearchSubscription(self)
        return self._subscriptions
