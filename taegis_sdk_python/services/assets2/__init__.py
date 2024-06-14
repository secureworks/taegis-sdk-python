""""Assets2 Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.assets2.mutations import TaegisSDKAssets2Mutation
from taegis_sdk_python.services.assets2.queries import TaegisSDKAssets2Query
from taegis_sdk_python.services.assets2.subscriptions import (
    TaegisSDKAssets2Subscription,
)


class Assets2Service(ServiceCore):
    """Taegis Assets2 Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKAssets2Query(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKAssets2Mutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKAssets2Subscription(self)
        return self._subscriptions
