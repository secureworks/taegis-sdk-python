""""TenantProfiles Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.tenant_profiles.mutations import (
    TaegisSDKTenantProfilesMutation,
)
from taegis_sdk_python.services.tenant_profiles.queries import (
    TaegisSDKTenantProfilesQuery,
)
from taegis_sdk_python.services.tenant_profiles.subscriptions import (
    TaegisSDKTenantProfilesSubscription,
)


class TenantProfilesService(ServiceCore):
    """Taegis TenantProfiles Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKTenantProfilesQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKTenantProfilesMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKTenantProfilesSubscription(self)
        return self._subscriptions
