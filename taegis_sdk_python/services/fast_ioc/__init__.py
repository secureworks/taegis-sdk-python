""""FastIoc Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.fast_ioc.mutations import TaegisSDKFastIocMutation
from taegis_sdk_python.services.fast_ioc.queries import TaegisSDKFastIocQuery
from taegis_sdk_python.services.fast_ioc.subscriptions import (
    TaegisSDKFastIocSubscription,
)


class FastIocService(ServiceCore):
    """Taegis FastIoc Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKFastIocQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKFastIocMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKFastIocSubscription(self)
        return self._subscriptions
