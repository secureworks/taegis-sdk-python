""""TriggerAction Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.trigger_action.mutations import (
    TaegisSDKTriggerActionMutation,
)
from taegis_sdk_python.services.trigger_action.queries import (
    TaegisSDKTriggerActionQuery,
)
from taegis_sdk_python.services.trigger_action.subscriptions import (
    TaegisSDKTriggerActionSubscription,
)


class TriggerActionService(ServiceCore):
    """Taegis TriggerAction Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKTriggerActionQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKTriggerActionMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKTriggerActionSubscription(self)
        return self._subscriptions
