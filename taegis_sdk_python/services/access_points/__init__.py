"""AccessPoints Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.access_points.mutations import (
    TaegisSDKAccessPointsMutation,
)
from taegis_sdk_python.services.access_points.queries import TaegisSDKAccessPointsQuery
from taegis_sdk_python.services.access_points.subscriptions import (
    TaegisSDKAccessPointsSubscription,
)


class AccessPointsService(ServiceCore):
    """Taegis AccessPoints Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKAccessPointsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKAccessPointsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKAccessPointsSubscription(self)
        return self._subscriptions
