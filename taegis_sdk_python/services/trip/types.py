"""Trip Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum


class ApiProductGroup(str, Enum):
    """ApiProductGroup."""

    TRIP = "Trip"
    CROWDSTRIKE = "Crowdstrike"


class ApiProductStatus(str, Enum):
    """ApiProductStatus."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    LEGACY = "Legacy"
    API_ONLY = "ApiOnly"


class ApiIntegrationStatus(str, Enum):
    """ApiIntegrationStatus."""

    PROVISIONING = "Provisioning"
    ACTIVE = "Active"
    DISABLED = "Disabled"
    PAUSED = "Paused"


class ApiIntegrationHealthStatus(str, Enum):
    """ApiIntegrationHealthStatus."""

    PENDING = "Pending"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    PROVISIONING_FAILED = "ProvisioningFailed"


class ApiIntegrationHistoryStatus(str, Enum):
    """ApiIntegrationHistoryStatus."""

    RUNNING = "Running"
    SUCCESS = "Success"
    FAILURE = "Failure"
    RETRYING = "Retrying"


class ApiFormItemType(str, Enum):
    """ApiFormItemType."""

    TEXT = "Text"
    TEXT_INPUT = "TextInput"
    OPTION = "Option"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ApiIntegrationParameterInput:
    """ApiIntegrationParameterInput."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ApiIntegrationUpdateResponse:
    """ApiIntegrationUpdateResponse."""

    success: Optional[bool] = field(default=None, metadata=config(field_name="success"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ApiIntegrationParameter:
    """ApiIntegrationParameter."""

    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    caption: Optional[str] = field(default=None, metadata=config(field_name="caption"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TripEnvConfig:
    """TripEnvConfig."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ApiIntegrationHistory:
    """ApiIntegrationHistory."""

    id: Optional[int] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    start_time: Optional[str] = field(
        default=None, metadata=config(field_name="startTime")
    )
    heartbeat_time: Optional[str] = field(
        default=None, metadata=config(field_name="heartbeatTime")
    )
    end_time: Optional[str] = field(default=None, metadata=config(field_name="endTime"))
    start_checkpoint: Optional[str] = field(
        default=None, metadata=config(field_name="startCheckpoint")
    )
    end_checkpoint: Optional[str] = field(
        default=None, metadata=config(field_name="endCheckpoint")
    )
    summary: Optional[str] = field(default=None, metadata=config(field_name="summary"))
    status: Optional[Union[ApiIntegrationHistoryStatus, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(ApiIntegrationHistoryStatus, x),
            field_name="status",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ApiProduct:
    """ApiProduct."""

    id: Optional[int] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    product_group: Optional[Union[ApiProductGroup, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(ApiProductGroup, x),
            field_name="productGroup",
        ),
    )
    status: Optional[Union[ApiProductStatus, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(ApiProductStatus, x),
            field_name="status",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ApiIntegrationSummary:
    """ApiIntegrationSummary."""

    id: Optional[int] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    product: Optional[ApiProduct] = field(
        default=None, metadata=config(field_name="product")
    )
    status: Optional[Union[ApiIntegrationHealthStatus, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(ApiIntegrationHealthStatus, x),
            field_name="status",
        ),
    )
    child_summaries: Optional[List["ApiIntegrationSummary"]] = field(
        default=None, metadata=config(field_name="childSummaries")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ApiIntegration:
    """ApiIntegration."""

    id: Optional[int] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    integration_uuid: Optional[str] = field(
        default=None, metadata=config(field_name="integrationUuid")
    )
    start_date_time: Optional[str] = field(
        default=None, metadata=config(field_name="startDateTime")
    )
    start_checkpoint: Optional[str] = field(
        default=None, metadata=config(field_name="startCheckpoint")
    )
    product: Optional[ApiProduct] = field(
        default=None, metadata=config(field_name="product")
    )
    parent_integration: Optional["ApiIntegration"] = field(
        default=None, metadata=config(field_name="parentIntegration")
    )
    child_integrations: Optional[List["ApiIntegration"]] = field(
        default=None, metadata=config(field_name="childIntegrations")
    )
    status: Optional[Union[ApiIntegrationStatus, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(ApiIntegrationStatus, x),
            field_name="status",
        ),
    )
    parameters: Optional[List[ApiIntegrationParameter]] = field(
        default=None, metadata=config(field_name="parameters")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ApiIntegrationHistoryPage:
    """ApiIntegrationHistoryPage."""

    start_time: Optional[str] = field(
        default=None, metadata=config(field_name="startTime")
    )
    end_time: Optional[str] = field(default=None, metadata=config(field_name="endTime"))
    page_number: Optional[int] = field(
        default=None, metadata=config(field_name="pageNumber")
    )
    page_size: Optional[int] = field(
        default=None, metadata=config(field_name="pageSize")
    )
    total_pages: Optional[int] = field(
        default=None, metadata=config(field_name="totalPages")
    )
    total_rows: Optional[int] = field(
        default=None, metadata=config(field_name="totalRows")
    )
    results: Optional[List[ApiIntegrationHistory]] = field(
        default=None, metadata=config(field_name="results")
    )
