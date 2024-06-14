""""Investigations Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.investigations.mutations import (
    TaegisSDKInvestigationsMutation,
)
from taegis_sdk_python.services.investigations.queries import (
    TaegisSDKInvestigationsQuery,
)
from taegis_sdk_python.services.investigations.subscriptions import (
    TaegisSDKInvestigationsSubscription,
)


class InvestigationsService(ServiceCore):
    """Taegis Investigations Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKInvestigationsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKInvestigationsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKInvestigationsSubscription(self)
        return self._subscriptions
