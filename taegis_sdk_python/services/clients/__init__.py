""""Clients Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.clients.mutations import TaegisSDKClientsMutation
from taegis_sdk_python.services.clients.queries import TaegisSDKClientsQuery
from taegis_sdk_python.services.clients.subscriptions import (
    TaegisSDKClientsSubscription,
)


class ClientsService(ServiceCore):
    """Taegis Clients Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKClientsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKClientsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKClientsSubscription(self)
        return self._subscriptions
