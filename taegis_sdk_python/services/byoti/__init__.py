""""Byoti Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.byoti.mutations import TaegisSDKByotiMutation
from taegis_sdk_python.services.byoti.queries import TaegisSDKByotiQuery
from taegis_sdk_python.services.byoti.subscriptions import (
    TaegisSDKByotiSubscription,
)


class ByotiService(ServiceCore):
    """Taegis Byoti Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKByotiQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKByotiMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKByotiSubscription(self)
        return self._subscriptions
