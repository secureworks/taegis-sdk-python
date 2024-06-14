""""VDR Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.vdr.mutations import TaegisSDKVdrMutation
from taegis_sdk_python.services.vdr.queries import TaegisSDKVdrQuery
from taegis_sdk_python.services.vdr.subscriptions import (
    TaegisSDKVdrSubscription,
)


class VDRService(ServiceCore):
    """Taegis VDR Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKVdrQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKVdrMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKVdrSubscription(self)
        return self._subscriptions
