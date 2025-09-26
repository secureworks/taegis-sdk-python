"""Taegis Commons Federated Alerts Search implementation."""

import logging
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

from dataclasses_json import config, dataclass_json

from taegis_sdk_python import (
    GraphQLNoRowsInResultSetError,
    GraphQLService,
    build_output_string,
    prepare_input,
)
from taegis_sdk_python.services.alerts.types import (
    Alert2,
    AlertsList,
    AlertsResponse,
    AuxiliaryEvent,
    PollRequestInput,
    SearchRequestInput,
)

log = logging.getLogger(__name__)


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TaegisCommonsAuxiliaryEvent(AuxiliaryEvent):
    """My TaegisCommons Auxiliary Event - Extends Auxiliary Event with event_data
    to take advantage of GQL federated services.
    """

    event_data: Optional[Dict[str, Any]] = field(
        default=None, metadata=config(field_name="event_data")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TaegisCommonsAlert2(Alert2):
    """My TaegisCommons Alert2."""

    event_ids: Optional[List[TaegisCommonsAuxiliaryEvent]] = field(
        default=None, metadata=config(field_name="event_ids")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TaegisCommonsAlertsList(AlertsList):
    """My TaegisCommons AlertsList."""

    list: Optional[List[TaegisCommonsAlert2]] = field(
        default=None, metadata=config(field_name="list")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TaegisCommonsAlertsResponse(AlertsResponse):
    """My TaegisCommons AlertsResponse."""

    alerts: Optional[TaegisCommonsAlertsList] = field(
        default=None, metadata=config(field_name="alerts")
    )


def alerts_service_search_with_events(
    service: GraphQLService, in_: SearchRequestInput
) -> TaegisCommonsAlertsResponse:
    """Query Taegis Alerts with corresponding Events attached."""
    endpoint = "alertsServiceSearch"
    result = service.alerts.execute_query(
        endpoint=endpoint,
        variables={
            "in": prepare_input(in_),
        },
        output=build_output_string(TaegisCommonsAlertsResponse),
    )
    if result is not None:
        return TaegisCommonsAlertsResponse.from_dict(  # pylint: disable=no-member
            result.get(endpoint)
        )
    raise GraphQLNoRowsInResultSetError("for query alertsServiceSearch")


def alerts_service_poll_with_events(
    service: GraphQLService, in_: PollRequestInput
) -> TaegisCommonsAlertsResponse:
    """Federated alerts_service_poll with event_data."""
    endpoint = "alertsServicePoll"
    result = service.alerts.execute_query(
        endpoint=endpoint,
        variables={
            "in": prepare_input(in_),
        },
        output=build_output_string(TaegisCommonsAlertsResponse),
    )
    if result is not None:
        return TaegisCommonsAlertsResponse.from_dict(  # pylint: disable=no-member
            result.get(endpoint)
        )
    raise GraphQLNoRowsInResultSetError("for query alertsServicePoll")


def alerts_federated_search(
    service: GraphQLService,
    query: str,
    *,
    limit: int = 10000,
    caller_name: str = "Taegis SDK Commons",
    federated_call: Callable,
    federated_poll_call: Callable,
) -> List[TaegisCommonsAlertsResponse]:
    """
    Search Taegis Alerts service.
    """
    if "aggregate" in query:
        limit = 1

    result = federated_call(
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
                response = federated_poll_call(
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
