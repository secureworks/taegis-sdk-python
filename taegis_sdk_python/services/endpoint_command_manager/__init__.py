""""EndpointCommandManager Service."""
from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.endpoint_command_manager.mutations import (
    TaegisSDKEndpointCommandManagerMutation,
)
from taegis_sdk_python.services.endpoint_command_manager.queries import (
    TaegisSDKEndpointCommandManagerQuery,
)
from taegis_sdk_python.services.endpoint_command_manager.subscriptions import (
    TaegisSDKEndpointCommandManagerSubscription,
)

if TYPE_CHECKING:
    from taegis_sdk_python.services import GraphQLService


class EndpointCommandManagerService(ServiceCore):
    """Taegis EndpointCommandManager Service."""

    def __init__(self, service: GraphQLService):
        super().__init__(service)
        self._gateway = "/agent-graphql"

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKEndpointCommandManagerQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKEndpointCommandManagerMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKEndpointCommandManagerSubscription(self)
        return self._subscriptions
