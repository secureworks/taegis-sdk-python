""""ContractedEndpoint Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.contracted_endpoint.mutations import (
    TaegisSDKContractedEndpointMutation,
)
from taegis_sdk_python.services.contracted_endpoint.queries import (
    TaegisSDKContractedEndpointQuery,
)
from taegis_sdk_python.services.contracted_endpoint.subscriptions import (
    TaegisSDKContractedEndpointSubscription,
)


class ContractedEndpointService(ServiceCore):
    """Taegis ContractedEndpoint Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKContractedEndpointQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKContractedEndpointMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKContractedEndpointSubscription(self)
        return self._subscriptions
