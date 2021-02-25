from datetime import datetime

from taegis_sdk_python import ServiceCore
from taegis_sdk_python.services.investigations.mutations import InvestigationMutation
from taegis_sdk_python.services.investigations.queries import InvestigationQuery


class InvestigationsService:
    def __init__(self, query_builder: ServiceCore):
        # --- Setting investigation endpoint
        query_builder.service_endpoint = "/investigations/query"
        self._queries = InvestigationQuery(query_builder)
        self._mutations = InvestigationMutation(query_builder)

    @staticmethod
    def get_default_time_based_name(
            prefix: str = "service-investigation",
            date_pattern: str = '%Y-%m-%d %H:%M:%S.%f'
    ) -> str:
        """
        Service method to create an item name based on time
        :param prefix: a string that specifies the start of the name e.g. "taegis_auto"
        :param date_pattern: optional desired date pattern
        :return: the name of the item
        """
        dt = datetime.utcnow().strftime(date_pattern)[:-3]
        return f"{prefix} {dt}"

    @property
    def query(self) -> InvestigationQuery:
        return self._queries

    @property
    def mutation(self) -> InvestigationMutation:
        return self._mutations
