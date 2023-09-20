""""Subjects Service."""
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.subjects.mutations import TaegisSDKSubjectsMutation
from taegis_sdk_python.services.subjects.queries import TaegisSDKSubjectsQuery
from taegis_sdk_python.services.subjects.subscriptions import (
    TaegisSDKSubjectsSubscription,
)


class SubjectsService(ServiceCore):
    """Taegis Subjects Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKSubjectsQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKSubjectsMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKSubjectsSubscription(self)
        return self._subscriptions
