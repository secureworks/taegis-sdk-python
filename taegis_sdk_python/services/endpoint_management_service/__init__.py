""""EndpointManagementService Service."""
from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.endpoint_management_service.mutations import (
    TaegisSDKEndpointManagementServiceMutation,
)
from taegis_sdk_python.services.endpoint_management_service.queries import (
    TaegisSDKEndpointManagementServiceQuery,
)
from taegis_sdk_python.services.endpoint_management_service.subscriptions import (
    TaegisSDKEndpointManagementServiceSubscription,
)

if TYPE_CHECKING:
    from taegis_sdk_python.services import GraphQLService


class EndpointManagementServiceService(ServiceCore):
    """Taegis EndpointManagementService Service."""

    def __init__(self, service: GraphQLService):
        super().__init__(service)
        self._gateway = "/agent-graphql"

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKEndpointManagementServiceQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKEndpointManagementServiceMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKEndpointManagementServiceSubscription(self)
        return self._subscriptions
