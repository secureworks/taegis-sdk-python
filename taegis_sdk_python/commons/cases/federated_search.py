"""Taegis Commons Cases implementations."""

import logging
import re
from dataclasses import dataclass, field
from typing import Callable, List, Optional

from dataclasses_json import config, dataclass_json
from taegis_magic.core.utils import remove_output_node

from taegis_sdk_python import (
    GraphQLNoRowsInResultSetError,
    GraphQLService,
    build_output_string,
    prepare_input,
)
from taegis_sdk_python.services.investigations2.types import (
    CreateInvestigationInput,
    InvestigationsV2,
    InvestigationsV2Arguments,
    InvestigationV2,
)
from taegis_sdk_python.services.subjects.types import Subject as FederatedSubject

log = logging.getLogger(__name__)


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TaegisCommonsInvestigationV2(InvestigationV2):
    """TaegisCommonsInvestigationV2"""

    contributor_subjects: Optional[List[FederatedSubject]] = field(
        default=None, metadata=config(field_name="contributorSubjects")
    )
    assignee_subject: Optional[FederatedSubject] = field(
        default=None, metadata=config(field_name="assigneeSubject")
    )
    created_by_subject: Optional[FederatedSubject] = field(
        default=None, metadata=config(field_name="createdBySubject")
    )
    updated_by_subject: Optional[FederatedSubject] = field(
        default=None, metadata=config(field_name="updatedBySubject")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TaegisCommonsInvestigationsV2(InvestigationsV2):
    """TaegisCommonsInvestigationsV2"""

    investigations: List[TaegisCommonsInvestigationV2] = field(
        default_factory=list, metadata=config(field_name="investigations")
    )


def investigations_create_with_subjects(
    service: GraphQLService, input_: CreateInvestigationInput
) -> TaegisCommonsInvestigationV2:
    """createInvestigationV2 creates new investigation with the provided arguments."""
    endpoint = "createInvestigationV2"

    result = service.investigations2.execute_mutation(
        endpoint=endpoint,
        variables={
            "input": prepare_input(input_),
        },
        output=build_output_string(TaegisCommonsInvestigationV2),
    )
    if result.get(endpoint) is not None:
        return TaegisCommonsInvestigationV2.from_dict(  # pylint: disable=no-member
            result.get(endpoint)
        )
    raise GraphQLNoRowsInResultSetError("for mutation createInvestigationV2")


def investigations_search_with_subjects(
    service, arguments: InvestigationsV2Arguments
) -> TaegisCommonsInvestigationsV2:
    """investigationsV2 returns a list of investigations matching the provided arguments."""
    endpoint = "investigationsV2"

    result = service.investigations2.execute_query(
        endpoint=endpoint,
        variables={
            "arguments": prepare_input(arguments),
        },
        output=build_output_string(TaegisCommonsInvestigationsV2),
    )
    if result.get(endpoint) is not None:
        return TaegisCommonsInvestigationsV2.from_dict(  # pylint: disable=no-member
            result.get(endpoint)
        )
    raise GraphQLNoRowsInResultSetError("for query investigationsV2")


def cases_federated_search(
    service: GraphQLService,
    query: str,
    *,
    limit: int = 10000,
    federated_call: Callable,
) -> List[InvestigationsV2]:
    """Taegis Cases search with Subject federation."""

    page = 1
    per_page = 100

    results = []

    # fix for CX-99036
    pattern = r"\|\s*(head|tail)\s*([0-9]+)"
    match = re.search(pattern, query)

    if not limit:
        if match and match.group(1) == "tail":  # pragma: no cover
            log.warning(
                "tail is not currently supported, it will be used as the limit..."
            )

        if match:
            limit = int(match.group(2))
    elif match:  # pragma: no cover
        log.warning(
            f"limit and {match.group(1)} both provided, only limit will be honored..."
        )

    query = re.sub(pattern, "", query)

    if limit and limit < per_page:
        per_page = limit
    # endfix

    # fix for CX-103490
    output = build_output_string(TaegisCommonsInvestigationsV2)

    output = remove_output_node(output, "metric")
    output = remove_output_node(output, "metrics")
    # endfix

    with service(output=output):
        investigations_results = federated_call(
            service=service,
            arguments=InvestigationsV2Arguments(
                page=page,
                per_page=per_page,
                cql=query,
            ),
        )

    results.append(investigations_results)

    # fix for CX-99036
    if not limit or investigations_results.total_count < limit:
        limit = investigations_results.total_count
    # endfix

    while (
        sum_results := sum(len(result.investigations) for result in results)
    ) < limit:
        page += 1

        # fix for CX-99036
        if (per_page * page) > limit:
            per_page = limit - sum_results
        # endfix

        with service(output=output):
            investigations_results = federated_call(
                service=service,
                arguments=InvestigationsV2Arguments(
                    page=page,
                    per_page=per_page,
                    cql=query,
                ),
            )
        results.append(investigations_results)

    return results
