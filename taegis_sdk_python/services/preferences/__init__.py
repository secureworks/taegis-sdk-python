""""Preferences Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.preferences.mutations import (
    TaegisSDKPreferencesMutation,
)
from taegis_sdk_python.services.preferences.queries import TaegisSDKPreferencesQuery
from taegis_sdk_python.services.preferences.subscriptions import (
    TaegisSDKPreferencesSubscription,
)


class PreferencesService(ServiceCore):
    """Taegis Preferences Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKPreferencesQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKPreferencesMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKPreferencesSubscription(self)
        return self._subscriptions
