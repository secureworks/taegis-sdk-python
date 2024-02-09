""""FileInfo Service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.file_info.mutations import TaegisSDKFileInfoMutation
from taegis_sdk_python.services.file_info.queries import TaegisSDKFileInfoQuery
from taegis_sdk_python.services.file_info.subscriptions import (
    TaegisSDKFileInfoSubscription,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services import GraphQLService


class FileInfoService(ServiceCore):
    """Taegis FileInfo Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKFileInfoQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKFileInfoMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKFileInfoSubscription(self)
        return self._subscriptions
