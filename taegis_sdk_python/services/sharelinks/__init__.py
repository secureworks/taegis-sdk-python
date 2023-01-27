""""Sharelinks Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.sharelinks.mutations import TaegisSDKSharelinksMutation
from taegis_sdk_python.services.sharelinks.queries import TaegisSDKSharelinksQuery
from taegis_sdk_python.services.sharelinks.subscriptions import (
    TaegisSDKSharelinksSubscription,
)


class SharelinksService(ServiceCore):
    """Taegis Sharelinks Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKSharelinksQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKSharelinksMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKSharelinksSubscription(self)
        return self._subscriptions
