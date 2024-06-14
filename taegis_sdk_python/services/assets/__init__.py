""""Assets Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.assets.mutations import TaegisSDKAssetsMutation
from taegis_sdk_python.services.assets.queries import TaegisSDKAssetsQuery
from taegis_sdk_python.services.assets.subscriptions import (
    TaegisSDKAssetsSubscription,
)


class AssetsService(ServiceCore):
    """Taegis Assets Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKAssetsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKAssetsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKAssetsSubscription(self)
        return self._subscriptions
