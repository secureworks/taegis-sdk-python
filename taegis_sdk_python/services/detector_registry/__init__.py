""""DetectorRegistry Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.detector_registry.mutations import (
    TaegisSDKDetectorRegistryMutation,
)
from taegis_sdk_python.services.detector_registry.queries import (
    TaegisSDKDetectorRegistryQuery,
)
from taegis_sdk_python.services.detector_registry.subscriptions import (
    TaegisSDKDetectorRegistrySubscription,
)


class DetectorRegistryService(ServiceCore):
    """Taegis DetectorRegistry Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKDetectorRegistryQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKDetectorRegistryMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKDetectorRegistrySubscription(self)
        return self._subscriptions
