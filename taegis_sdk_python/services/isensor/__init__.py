""""Isensor Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.isensor.mutations import (
    TaegisSDKIsensorMutation,
)
from taegis_sdk_python.services.isensor.queries import TaegisSDKIsensorQuery
from taegis_sdk_python.services.isensor.subscriptions import (
    TaegisSDKIsensorSubscription,
)


class IsensorService(ServiceCore):
    """Taegis Isensor Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKIsensorQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKIsensorMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKIsensorSubscription(self)
        return self._subscriptions
