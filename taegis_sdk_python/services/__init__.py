import os
from typing import Optional

from taegis_sdk_python.taegis_sdk import ServiceCore
from taegis_sdk_python.services.investigations.investigations import InvestigationsService
from taegis_sdk_python.utils import get_token


class GraphQLService:
    def __init__(self):
        token = get_token().get('access_token')
        os.environ["SERVICE_URL"] = 'https://api.ctpx.secureworks.com'
        self._service_core = ServiceCore(token)
        self._investigations: Optional[InvestigationsService] = None

    @property
    def core(self) -> ServiceCore:
        return self._service_core

    @property
    def investigations(self) -> InvestigationsService:
        if self._investigations is None:
            self._investigations = InvestigationsService(self._service_core)
        return self._investigations


__all__ = [
    "GraphQLService",
    "InvestigationsService"
]
