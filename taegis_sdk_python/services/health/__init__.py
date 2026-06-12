"""Health Service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.health.mutations import TaegisSDKHealthMutation
from taegis_sdk_python.services.health.queries import TaegisSDKHealthQuery
from taegis_sdk_python.services.health.subscriptions import TaegisSDKHealthSubscription

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services import GraphQLService


class HealthService(ServiceCore):
    """Taegis Health Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKHealthQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKHealthMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKHealthSubscription(self)
        return self._subscriptions
