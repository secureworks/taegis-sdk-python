"""Taegis Sharelinks Unfurler."""

from typing import Any
from urllib.parse import urlparse

from taegis_sdk_python import GraphQLNoRowsInResultSetError, GraphQLService
from taegis_sdk_python.services.alerts.types import GetByIDRequestInput
from taegis_sdk_python.services.investigations2.types import InvestigationV2Arguments
from taegis_sdk_python.services.rules.types import Rule


def unfurl_sharelink(
    service: GraphQLService,
    id_: str,
) -> Any:
    """Unpack sharelink urls and uuids.  Returns underlying datastructure results."""
    if "/share/" in id_:
        parse_result = urlparse(id_)
        id_ = parse_result.path.replace("/share/", "")

    results = service.sharelinks.query.share_link_by_id(id_=id_)

    if results.link_type in ("alertId", "alertV2Id"):
        with service(tenant_id=results.tenant_id):
            unfurl_results = service.alerts.query.alerts_service_retrieve_alerts_by_id(
                GetByIDRequestInput(i_ds=[results.link_ref])
            )
    elif results.link_type == "eventId":
        with service(tenant_id=results.tenant_id):
            unfurl_results = service.events.query.events(ids=[results.link_ref])
    elif results.link_type == "investigationId":
        with service(tenant_id=results.tenant_id):
            unfurl_results = service.investigations2.query.investigation_v2(
                InvestigationV2Arguments(id=results.link_ref)
            )
    elif results.link_type == "rules":
        with service(tenant_id=results.tenant_id):
            try:
                unfurl_results = service.rules.query.rule(id_=results.link_ref)
            except GraphQLNoRowsInResultSetError:  # pragma: no cover
                unfurl_results = Rule()

    else:
        raise ValueError(f"Unable to process sharelink results: {results}")

    return unfurl_results
