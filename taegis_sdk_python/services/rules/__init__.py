""""Rules Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.rules.mutations import TaegisSDKRulesMutation
from taegis_sdk_python.services.rules.queries import TaegisSDKRulesQuery
from taegis_sdk_python.services.rules.subscriptions import (
    TaegisSDKRulesSubscription,
)


class RulesService(ServiceCore):
    """Taegis Rules Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKRulesQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKRulesMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKRulesSubscription(self)
        return self._subscriptions
