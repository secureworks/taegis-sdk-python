"""Notebooks Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.notebooks.mutations import TaegisSDKNotebooksMutation
from taegis_sdk_python.services.notebooks.queries import TaegisSDKNotebooksQuery
from taegis_sdk_python.services.notebooks.subscriptions import (
    TaegisSDKNotebooksSubscription,
)


class NotebooksService(ServiceCore):
    """Taegis Notebooks Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKNotebooksQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKNotebooksMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKNotebooksSubscription(self)
        return self._subscriptions
