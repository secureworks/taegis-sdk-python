"""Taegis Sharelinks create implementations."""

from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.sharelinks.types import (
    ExtraParamCreateInput,
    ShareLinkCreateInput,
)


def create_sharelink(service: GraphQLService, input_: ShareLinkCreateInput):
    """Create a Taegis Sharelink."""
    result = service.sharelinks.mutation.create_share_link(input_=input_)

    shareable_url = f'{service.core.sync_url.replace("api.", "")}/share/{result.id}'
    return shareable_url


def create_alerts_query_sharelink(service: GraphQLService, query_identifier: str):
    """Create a Taegis Sharelink for alert_service_search results."""
    input_ = ShareLinkCreateInput(
        link_ref=query_identifier,
        link_target="cql",
        link_type="queryId",
        tenant_id=service.tenant_id,
        extra_parameters=[
            ExtraParamCreateInput(key="sourceType", value="alert"),
        ],
    )

    return create_sharelink(service, input_)


def create_events_query_sharelink(service: GraphQLService, query_identifier: str):
    """Create a Taegis Sharelink events_query results."""
    input_ = ShareLinkCreateInput(
        link_ref=query_identifier,
        link_target="cql",
        link_type="queryId",
        tenant_id=service.tenant_id,
        extra_parameters=[
            ExtraParamCreateInput(key="sourceType", value="event"),
        ],
    )

    return create_sharelink(service, input_)


def create_investigations_sharelink(service: GraphQLService, investigation_id: str):
    """Create a Taegis Sharelink from InvestigationV2 results."""
    input_ = ShareLinkCreateInput(
        link_ref=investigation_id,
        link_type="investigationId",
        tenant_id=service.tenant_id,
    )

    return create_sharelink(service, input_)


def create_cases_sharelink(service: GraphQLService, case_id: str):
    """Create a Taegis Sharelink from InvestigationV2 results."""
    input_ = ShareLinkCreateInput(
        link_ref=case_id,
        link_type="investigationId",
        tenant_id=service.tenant_id,
    )

    return create_sharelink(service, input_)
