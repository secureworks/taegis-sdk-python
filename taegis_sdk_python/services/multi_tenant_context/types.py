"""MultiTenantContext Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MTTenantService:
    """MTTenantService."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class History:
    """History."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    tenant_name: Optional[str] = field(
        default=None, metadata=config(field_name="tenantName")
    )
    visited: Optional[str] = field(default=None, metadata=config(field_name="visited"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantClaim:
    """TenantClaim."""

    subject: Optional[str] = field(default=None, metadata=config(field_name="subject"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    first_name: Optional[str] = field(
        default=None, metadata=config(field_name="firstName")
    )
    last_name: Optional[str] = field(
        default=None, metadata=config(field_name="lastName")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MTSubject:
    """MTSubject."""

    subject: Optional[str] = field(default=None, metadata=config(field_name="subject"))
    email: Optional[str] = field(default=None, metadata=config(field_name="email"))
    first_name: Optional[str] = field(
        default=None, metadata=config(field_name="firstName")
    )
    last_name: Optional[str] = field(
        default=None, metadata=config(field_name="lastName")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CreateSessionInput:
    """CreateSessionInput."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    tenant_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tenantIDs")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SessionInput:
    """SessionInput."""

    tenant_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tenantIDs")
    )
    key: Optional[str] = field(default=None, metadata=config(field_name="key"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantsClaim:
    """TenantsClaim."""

    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    subjects: Optional[List[MTSubject]] = field(
        default=None, metadata=config(field_name="subjects")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CachedTriage:
    """CachedTriage."""

    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    tenant_name: Optional[str] = field(
        default=None, metadata=config(field_name="tenantName")
    )
    partner: Optional[str] = field(default=None, metadata=config(field_name="partner"))
    oldest_alert: Optional[str] = field(
        default=None, metadata=config(field_name="oldestAlert")
    )
    critical: Optional[int] = field(
        default=None, metadata=config(field_name="critical")
    )
    high: Optional[int] = field(default=None, metadata=config(field_name="high"))
    medium: Optional[int] = field(default=None, metadata=config(field_name="medium"))
    low: Optional[int] = field(default=None, metadata=config(field_name="low"))
    info: Optional[int] = field(default=None, metadata=config(field_name="info"))
    endpoints_affected: Optional[int] = field(
        default=None, metadata=config(field_name="endpointsAffected")
    )
    endpoints_total: Optional[int] = field(
        default=None, metadata=config(field_name="endpointsTotal")
    )
    open_investigations: Optional[int] = field(
        default=None, metadata=config(field_name="openInvestigations")
    )
    services: Optional[List[str]] = field(
        default=None, metadata=config(field_name="services")
    )
    claimed_by: Optional[List[TenantClaim]] = field(
        default=None, metadata=config(field_name="claimedBy")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MTTenant:
    """MTTenant."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    claims: Optional[List[TenantClaim]] = field(
        default=None, metadata=config(field_name="claims")
    )
    services: Optional[List[MTTenantService]] = field(
        default=None, metadata=config(field_name="services")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Session:
    """Session."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    subject: Optional[str] = field(default=None, metadata=config(field_name="subject"))
    tenant_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tenantIDs")
    )
    tenants: Optional[List[MTTenant]] = field(
        default=None, metadata=config(field_name="tenants")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CachedTriageOutput:
    """CachedTriageOutput."""

    total_results: Optional[int] = field(
        default=None, metadata=config(field_name="totalResults")
    )
    next_page: Optional[int] = field(
        default=None, metadata=config(field_name="nextPage")
    )
    tenant_triage: Optional[List[CachedTriage]] = field(
        default=None, metadata=config(field_name="tenantTriage")
    )
