"""Taegis Commons Alerts Search implementations."""

import logging
from typing import List

from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.alerts.types import (
    AlertsResponse,
    PollRequestInput,
    SearchRequestInput,
)

log = logging.getLogger(__name__)


def alerts_search(
    service: GraphQLService,
    query: str,
    *,
    limit: int = 10000,
    caller_name: str = "Taegis SDK Commons",
) -> List[AlertsResponse]:
    """
    Search Taegis Alerts service.
    """
    if "aggregate" in query:
        limit = 1

    result = service.alerts.query.alerts_service_search(
        service,
        SearchRequestInput(
            cql_query=query,
            offset=0,
            limit=limit,
            metadata={"callerName": caller_name},
        ),
    )

    poll_responses = [result]
    search_id = result.search_id
    total_parts = result.alerts.total_parts

    if search_id:
        for part in range(2, total_parts + 1):
            response = None
            try:
                log.debug(f"Submitting page {part}...")
                response = service.alerts.query.alerts_service_poll(
                    service,
                    PollRequestInput(
                        search_id=search_id,
                        part_id=part,
                    ),
                )
            except Exception as exc:  # pylint: disable=broad-exception-caught
                log.error(
                    f"Cannot retrieve results for search_id:{search_id}:{part}::{exc}"
                )
                if "not found" in str(exc):
                    break

            if isinstance(response, AlertsResponse) and response.alerts is not None:
                poll_responses.append(response)
                # CX-92571 work around
                if sum(len(response.alerts.list) for response in poll_responses) >= int(
                    limit
                ):
                    break

    return poll_responses
