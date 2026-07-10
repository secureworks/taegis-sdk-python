"""Results Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.results.mutations import TaegisSDKResultsMutation
from taegis_sdk_python.services.results.queries import TaegisSDKResultsQuery
from taegis_sdk_python.services.results.subscriptions import (
    TaegisSDKResultsSubscription,
)


class ResultsService(ServiceCore):
    """Taegis Results Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKResultsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKResultsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKResultsSubscription(self)
        return self._subscriptions
