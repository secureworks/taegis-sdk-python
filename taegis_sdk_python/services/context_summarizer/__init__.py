"""ContextSummarizer Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.context_summarizer.mutations import (
    TaegisSDKContextSummarizerMutation,
)
from taegis_sdk_python.services.context_summarizer.queries import (
    TaegisSDKContextSummarizerQuery,
)
from taegis_sdk_python.services.context_summarizer.subscriptions import (
    TaegisSDKContextSummarizerSubscription,
)


class ContextSummarizerService(ServiceCore):
    """Taegis ContextSummarizer Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKContextSummarizerQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKContextSummarizerMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKContextSummarizerSubscription(self)
        return self._subscriptions
