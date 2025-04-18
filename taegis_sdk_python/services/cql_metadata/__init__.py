""""CqlMetadata Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.cql_metadata.mutations import (
    TaegisSDKCqlMetadataMutation,
)
from taegis_sdk_python.services.cql_metadata.queries import TaegisSDKCqlMetadataQuery
from taegis_sdk_python.services.cql_metadata.subscriptions import (
    TaegisSDKCqlMetadataSubscription,
)


class CqlMetadataService(ServiceCore):
    """Taegis CqlMetadata Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKCqlMetadataQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKCqlMetadataMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKCqlMetadataSubscription(self)
        return self._subscriptions
