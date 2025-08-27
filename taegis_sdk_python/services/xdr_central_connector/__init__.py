"""XdrCentralConnector Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.xdr_central_connector.mutations import (
    TaegisSDKXdrCentralConnectorMutation,
)
from taegis_sdk_python.services.xdr_central_connector.queries import (
    TaegisSDKXdrCentralConnectorQuery,
)
from taegis_sdk_python.services.xdr_central_connector.subscriptions import (
    TaegisSDKXdrCentralConnectorSubscription,
)


class XdrCentralConnectorService(ServiceCore):
    """Taegis XdrCentralConnector Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKXdrCentralConnectorQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKXdrCentralConnectorMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKXdrCentralConnectorSubscription(self)
        return self._subscriptions
