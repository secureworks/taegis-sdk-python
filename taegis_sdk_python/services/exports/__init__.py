""""Exports Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.exports.mutations import TaegisSDKExportsMutation
from taegis_sdk_python.services.exports.queries import TaegisSDKExportsQuery
from taegis_sdk_python.services.exports.subscriptions import (
    TaegisSDKExportsSubscription,
)


class ExportsService(ServiceCore):
    """Taegis Exports Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKExportsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKExportsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKExportsSubscription(self)
        return self._subscriptions
