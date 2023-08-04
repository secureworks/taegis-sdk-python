""""MultiTenantContext Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.multi_tenant_context.mutations import (
    TaegisSDKMultiTenantContextMutation,
)
from taegis_sdk_python.services.multi_tenant_context.queries import (
    TaegisSDKMultiTenantContextQuery,
)
from taegis_sdk_python.services.multi_tenant_context.subscriptions import (
    TaegisSDKMultiTenantContextSubscription,
)


class MultiTenantContextService(ServiceCore):
    """Taegis MultiTenantContext Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKMultiTenantContextQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKMultiTenantContextMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKMultiTenantContextSubscription(self)
        return self._subscriptions
