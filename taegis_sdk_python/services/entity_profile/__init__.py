""""EntityProfile Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.entity_profile.mutations import (
    TaegisSDKEntityProfileMutation,
)
from taegis_sdk_python.services.entity_profile.queries import (
    TaegisSDKEntityProfileQuery,
)
from taegis_sdk_python.services.entity_profile.subscriptions import (
    TaegisSDKEntityProfileSubscription,
)


class EntityProfileService(ServiceCore):
    """Taegis EntityProfile Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKEntityProfileQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKEntityProfileMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKEntityProfileSubscription(self)
        return self._subscriptions
