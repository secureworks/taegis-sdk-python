""""Datasources Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.datasources.mutations import (
    TaegisSDKDatasourcesMutation,
)
from taegis_sdk_python.services.datasources.queries import TaegisSDKDatasourcesQuery
from taegis_sdk_python.services.datasources.subscriptions import (
    TaegisSDKDatasourcesSubscription,
)


class DatasourcesService(ServiceCore):
    """Taegis Datasources Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKDatasourcesQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKDatasourcesMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKDatasourcesSubscription(self)
        return self._subscriptions
