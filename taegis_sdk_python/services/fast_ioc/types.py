"""FastIoc Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum


class LogicalType(str, Enum):
    """LogicalType."""

    DOMAIN = "DOMAIN"
    HASH = "HASH"
    HOST = "HOST"
    IP = "IP"
    MAC = "MAC"
    USER = "USER"


class Operator(str, Enum):
    """Operator."""

    EQUALS = "EQUALS"
    MATCHES_REGEX = "MATCHES_REGEX"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventWindow:
    """EventWindow."""

    earliest_event: Optional[str] = field(
        default=None, metadata=config(field_name="earliestEvent")
    )
    latest_event: Optional[str] = field(
        default=None, metadata=config(field_name="latestEvent")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DataAvailabilityError:
    """DataAvailabilityError."""

    message: Optional[str] = field(default=None, metadata=config(field_name="message"))
    unavailable_dates: Optional[List[str]] = field(
        default=None, metadata=config(field_name="unavailableDates")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantCount:
    """TenantCount."""

    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantId")
    )
    count: Optional[int] = field(default=None, metadata=config(field_name="count"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantsInput:
    """TenantsInput."""

    tenant_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tenantIds")
    )
    session_key: Optional[str] = field(
        default=None,
        metadata=config(
            metadata={"deprecated": True, "deprecation_reason": "no longer supported"},
            field_name="sessionKey",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventCountByLogicalType:
    """EventCountByLogicalType."""

    matching_value: Optional[str] = field(
        default=None, metadata=config(field_name="matchingValue")
    )
    event_type: Optional[str] = field(
        default=None, metadata=config(field_name="eventType")
    )
    date: Optional[str] = field(default=None, metadata=config(field_name="date"))
    count: Optional[int] = field(default=None, metadata=config(field_name="count"))
    counts_by_tenant: Optional[List[TenantCount]] = field(
        default=None, metadata=config(field_name="countsByTenant")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventCountResult:
    """EventCountResult."""

    next: Optional[str] = field(default=None, metadata=config(field_name="next"))
    results: Optional[List[EventCountByLogicalType]] = field(
        default=None, metadata=config(field_name="results")
    )
    error: Optional[DataAvailabilityError] = field(
        default=None, metadata=config(field_name="error")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class LogicalTypeFilter:
    """LogicalTypeFilter."""

    values: Optional[List[str]] = field(
        default=None, metadata=config(field_name="values")
    )
    logical_type: Optional[Union[LogicalType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(LogicalType, x),
            field_name="logicalType",
        ),
    )
    operator: Optional[Union[Operator, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(Operator, x),
            field_name="operator",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventAggregationArguments:
    """EventAggregationArguments."""

    event_type_filter: Optional[List[str]] = field(
        default=None, metadata=config(field_name="eventTypeFilter")
    )
    earliest: Optional[str] = field(
        default=None, metadata=config(field_name="earliest")
    )
    latest: Optional[str] = field(default=None, metadata=config(field_name="latest"))
    limit: Optional[int] = field(default=None, metadata=config(field_name="limit"))
    logical_type_filter: Optional[LogicalTypeFilter] = field(
        default=None, metadata=config(field_name="logicalTypeFilter")
    )
    tenants_context: Optional[TenantsInput] = field(
        default=None, metadata=config(field_name="tenantsContext")
    )
