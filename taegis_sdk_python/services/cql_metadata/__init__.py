""""CqlMetadata Service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.cql_metadata.mutations import (
    TaegisSDKCqlMetadataMutation,
)
from taegis_sdk_python.services.cql_metadata.queries import TaegisSDKCqlMetadataQuery
from taegis_sdk_python.services.cql_metadata.subscriptions import (
    TaegisSDKCqlMetadataSubscription,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services import GraphQLService


class CqlMetadataService(ServiceCore):
    """Taegis CqlMetadata Service."""

    def __init__(self, service: GraphQLService):
        """Initialize the CqlMetadata Service."""
        super().__init__(service)
        self._gateway = "/cql-metadata/query"
        self._input_value_deprecation = False

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
