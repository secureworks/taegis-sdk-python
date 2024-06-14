""""Users Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.users.mutations import TaegisSDKUsersMutation
from taegis_sdk_python.services.users.queries import TaegisSDKUsersQuery
from taegis_sdk_python.services.users.subscriptions import (
    TaegisSDKUsersSubscription,
)


class UsersService(ServiceCore):
    """Taegis Users Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKUsersQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKUsersMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKUsersSubscription(self)
        return self._subscriptions
