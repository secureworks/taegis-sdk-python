""""Authz Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.authz.mutations import TaegisSDKAuthzMutation
from taegis_sdk_python.services.authz.queries import TaegisSDKAuthzQuery
from taegis_sdk_python.services.authz.subscriptions import (
    TaegisSDKAuthzSubscription,
)


class AuthzService(ServiceCore):
    """Taegis Authz Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKAuthzQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKAuthzMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKAuthzSubscription(self)
        return self._subscriptions
