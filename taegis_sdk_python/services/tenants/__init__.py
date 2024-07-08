""""Tenants Service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python._consts import TAEGIS_TENANTS_URLS
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.tenants.mutations import TaegisSDKTenantsMutation
from taegis_sdk_python.services.tenants.queries import TaegisSDKTenantsQuery
from taegis_sdk_python.services.tenants.subscriptions import (
    TaegisSDKTenantsSubscription,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services import GraphQLService


class TenantsService(ServiceCore):
    """Taegis Tenants Service."""

    def __init__(self, service: GraphQLService):
        super().__init__(service)
        self._urls = TAEGIS_TENANTS_URLS
        self._gateway = "/public/query"
        self._input_value_deprecation = False

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKTenantsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKTenantsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKTenantsSubscription(self)
        return self._subscriptions
