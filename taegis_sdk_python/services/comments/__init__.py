""""Comments Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.comments.mutations import TaegisSDKCommentsMutation
from taegis_sdk_python.services.comments.queries import TaegisSDKCommentsQuery
from taegis_sdk_python.services.comments.subscriptions import (
    TaegisSDKCommentsSubscription,
)


class CommentsService(ServiceCore):
    """Taegis Comments Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKCommentsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKCommentsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKCommentsSubscription(self)
        return self._subscriptions
