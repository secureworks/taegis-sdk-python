"""EscalationPolicies Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.escalation_policies.mutations import (
    TaegisSDKEscalationPoliciesMutation,
)
from taegis_sdk_python.services.escalation_policies.queries import (
    TaegisSDKEscalationPoliciesQuery,
)
from taegis_sdk_python.services.escalation_policies.subscriptions import (
    TaegisSDKEscalationPoliciesSubscription,
)


class EscalationPoliciesService(ServiceCore):
    """Taegis EscalationPolicies Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKEscalationPoliciesQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKEscalationPoliciesMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKEscalationPoliciesSubscription(self)
        return self._subscriptions
