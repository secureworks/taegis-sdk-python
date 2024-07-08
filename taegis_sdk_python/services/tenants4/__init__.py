""""TenantsV4 Service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python._consts import TAEGIS_TENANTS_URLS
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.tenants4.mutations import TaegisSDKTenants4Mutation
from taegis_sdk_python.services.tenants4.queries import TaegisSDKTenants4Query
from taegis_sdk_python.services.tenants4.subscriptions import (
    TaegisSDKTenants4Subscription,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services import GraphQLService


class Tenants4Service(ServiceCore):
    """Taegis Tenants4 Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKTenants4Query(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKTenants4Mutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKTenants4Subscription(self)
        return self._subscriptions
