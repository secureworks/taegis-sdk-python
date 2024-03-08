""""Queries Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.queries.mutations import (
    TaegisSDKQueriesMutation,
)
from taegis_sdk_python.services.queries.queries import TaegisSDKQueriesQuery
from taegis_sdk_python.services.queries.subscriptions import (
    TaegisSDKQueriesSubscription,
)


class QueriesService(ServiceCore):
    """Taegis Queries Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKQueriesQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKQueriesMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKQueriesSubscription(self)
        return self._subscriptions
