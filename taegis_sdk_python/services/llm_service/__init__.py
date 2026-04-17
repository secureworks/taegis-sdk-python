"""LlmService Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.llm_service.mutations import TaegisSDKLlmServiceMutation
from taegis_sdk_python.services.llm_service.queries import TaegisSDKLlmServiceQuery
from taegis_sdk_python.services.llm_service.subscriptions import (
    TaegisSDKLlmServiceSubscription,
)


class LlmServiceService(ServiceCore):
    """Taegis LlmService Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKLlmServiceQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKLlmServiceMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKLlmServiceSubscription(self)
        return self._subscriptions
