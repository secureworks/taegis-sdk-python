""""Audits Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.audits.mutations import TaegisSDKAuditsMutation
from taegis_sdk_python.services.audits.queries import TaegisSDKAuditsQuery
from taegis_sdk_python.services.audits.subscriptions import (
    TaegisSDKAuditsSubscription,
)


class AuditsService(ServiceCore):
    """Taegis Audits Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKAuditsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKAuditsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKAuditsSubscription(self)
        return self._subscriptions
