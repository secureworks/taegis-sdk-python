""""Roadrunner Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.roadrunner.mutations import TaegisSDKRoadrunnerMutation
from taegis_sdk_python.services.roadrunner.queries import TaegisSDKRoadrunnerQuery
from taegis_sdk_python.services.roadrunner.subscriptions import (
    TaegisSDKRoadrunnerSubscription,
)


class RoadrunnerService(ServiceCore):
    """Taegis Roadrunner Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKRoadrunnerQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKRoadrunnerMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKRoadrunnerSubscription(self)
        return self._subscriptions
