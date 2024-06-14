""""FastIoc Service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.fast_ioc.mutations import TaegisSDKFastIocMutation
from taegis_sdk_python.services.fast_ioc.queries import TaegisSDKFastIocQuery
from taegis_sdk_python.services.fast_ioc.subscriptions import (
    TaegisSDKFastIocSubscription,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services import GraphQLService


class FastIocService(ServiceCore):
    """Taegis FastIoc Service."""

    def __init__(self, service: GraphQLService):
        super().__init__(service)
        self._gateway = "/fast-ioc/query"

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKFastIocQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKFastIocMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKFastIocSubscription(self)
        return self._subscriptions
