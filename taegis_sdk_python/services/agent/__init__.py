""""Agent Service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.agent.mutations import TaegisSDKAgentMutation
from taegis_sdk_python.services.agent.queries import TaegisSDKAgentQuery
from taegis_sdk_python.services.agent.subscriptions import (
    TaegisSDKAgentSubscription,
)

if TYPE_CHECKING:
    from taegis_sdk_python.services import GraphQLService


class AgentService(ServiceCore):
    """Taegis Agent Service."""

    def __init__(self, service: GraphQLService):
        super().__init__(service)
        self._gateway = "/agent-graphql"

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKAgentQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKAgentMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKAgentSubscription(self)
        return self._subscriptions
