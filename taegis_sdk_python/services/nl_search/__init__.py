"""NlSearch Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.nl_search.mutations import TaegisSDKNlSearchMutation
from taegis_sdk_python.services.nl_search.queries import TaegisSDKNlSearchQuery
from taegis_sdk_python.services.nl_search.subscriptions import (
    TaegisSDKNlSearchSubscription,
)


class NlSearchService(ServiceCore):
    """Taegis NlSearch Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKNlSearchQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKNlSearchMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKNlSearchSubscription(self)
        return self._subscriptions
