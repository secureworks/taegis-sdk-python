"""EntityContext Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.entity_context.mutations import (
    TaegisSDKEntityContextMutation,
)
from taegis_sdk_python.services.entity_context.queries import (
    TaegisSDKEntityContextQuery,
)
from taegis_sdk_python.services.entity_context.subscriptions import (
    TaegisSDKEntityContextSubscription,
)


class EntityContextService(ServiceCore):
    """Taegis EntityContext Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKEntityContextQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKEntityContextMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKEntityContextSubscription(self)
        return self._subscriptions
