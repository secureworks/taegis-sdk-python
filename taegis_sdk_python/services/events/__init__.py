""""Events Service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.events.mutations import TaegisSDKEventsMutation
from taegis_sdk_python.services.events.queries import TaegisSDKEventsQuery
from taegis_sdk_python.services.events.subscriptions import TaegisSDKEventsSubscription

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services import GraphQLService


class EventsService(ServiceCore):
    """Events Service."""

    def __init__(self, service: GraphQLService):
        super().__init__(service)
        self._gateway = "/events/query"

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKEventsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKEventsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKEventsSubscription(self)
        return self._subscriptions
