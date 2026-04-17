"""QlSchemas Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.ql_schemas.mutations import TaegisSDKQlSchemasMutation
from taegis_sdk_python.services.ql_schemas.queries import TaegisSDKQlSchemasQuery
from taegis_sdk_python.services.ql_schemas.subscriptions import (
    TaegisSDKQlSchemasSubscription,
)


class QlSchemasService(ServiceCore):
    """Taegis QlSchemas Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKQlSchemasQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKQlSchemasMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKQlSchemasSubscription(self)
        return self._subscriptions
