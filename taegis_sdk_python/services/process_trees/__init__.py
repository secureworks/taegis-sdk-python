""""ProcessTrees Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.process_trees.mutations import (
    TaegisSDKProcessTreesMutation,
)
from taegis_sdk_python.services.process_trees.queries import TaegisSDKProcessTreesQuery
from taegis_sdk_python.services.process_trees.subscriptions import (
    TaegisSDKProcessTreesSubscription,
)


class ProcessTreesService(ServiceCore):
    """Taegis ProcessTrees Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKProcessTreesQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKProcessTreesMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKProcessTreesSubscription(self)
        return self._subscriptions
