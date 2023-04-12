""""Investigations2 Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.investigations2.mutations import (
    TaegisSDKInvestigations2Mutation,
)
from taegis_sdk_python.services.investigations2.queries import (
    TaegisSDKInvestigations2Query,
)
from taegis_sdk_python.services.investigations2.subscriptions import (
    TaegisSDKInvestigations2Subscription,
)


class Investigations2Service(ServiceCore):
    """Taegis Investigations2 Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKInvestigations2Query(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKInvestigations2Mutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKInvestigations2Subscription(self)
        return self._subscriptions
