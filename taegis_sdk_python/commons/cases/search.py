"""Taegis Commons Cases implementations."""

import logging
import re
from typing import List

from taegis_sdk_python import GraphQLService, build_output_string
from taegis_sdk_python.services.investigations2.types import (
    InvestigationsV2,
    InvestigationsV2Arguments,
)
from taegis_sdk_python.utils import remove_output_node

log = logging.getLogger(__name__)


def cases_search(
    service: GraphQLService,
    query: str,
    *,
    limit: int = 10000,
) -> List[InvestigationsV2]:
    """Taegis Cases search."""

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
    output = build_output_string(InvestigationsV2)

    output = remove_output_node(output, "metric")
    output = remove_output_node(output, "metrics")
    # endfix

    with service(output=output):
        investigations_results = service.investigations2.query.investigations_v2(
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
            investigations_results = service.investigations2.query.investigations_v2(
                service=service,
                arguments=InvestigationsV2Arguments(
                    page=page,
                    per_page=per_page,
                    cql=query,
                ),
            )
        results.append(investigations_results)

    return results
