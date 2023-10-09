"""MultiTenantIoc Service."""
from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.multi_tenant_ioc.mutations import (
    TaegisSDKMultiTenantIocMutation,
)
from taegis_sdk_python.services.multi_tenant_ioc.queries import (
    TaegisSDKMultiTenantIocQuery,
)
from taegis_sdk_python.services.multi_tenant_ioc.subscriptions import (
    TaegisSDKMultiTenantIocSubscription,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services import GraphQLService


class MultiTenantIocService(ServiceCore):
    """Taegis MultiTenantIoc Service."""

    def __init__(self, service: GraphQLService):
        super().__init__(service)
        self._gateway = "/multi-tenant-ioc/query"

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKMultiTenantIocQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKMultiTenantIocMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKMultiTenantIocSubscription(self)
        return self._subscriptions
