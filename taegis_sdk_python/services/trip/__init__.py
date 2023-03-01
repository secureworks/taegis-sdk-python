""""Trip Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.trip.mutations import TaegisSDKTripMutation
from taegis_sdk_python.services.trip.queries import TaegisSDKTripQuery
from taegis_sdk_python.services.trip.subscriptions import (
    TaegisSDKTripSubscription,
)


class TripService(ServiceCore):
    """Taegis Trip Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKTripQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKTripMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKTripSubscription(self)
        return self._subscriptions
