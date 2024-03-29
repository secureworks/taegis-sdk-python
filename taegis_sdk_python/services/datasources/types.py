"""Datasources Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from typing import Optional, List, Dict, Union, Any, Tuple


from enum import Enum


from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


class AuthzObject(str, Enum):
    """AuthzObject."""

    COLLECTOR = "COLLECTOR"


class AuthzAction(str, Enum):
    """AuthzAction."""

    READ = "READ"
    DELETE = "DELETE"


class HealthState(str, Enum):
    """HealthState."""

    HEALTHY = "HEALTHY"
    NO_DATA = "NO_DATA"
    WARNING = "WARNING"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DeletedAsset:
    """DeletedAsset."""

    source_id: Optional[str] = field(
        default=None, metadata=config(field_name="sourceId")
    )
    collector_id: Optional[str] = field(
        default=None, metadata=config(field_name="collectorID")
    )
    successful: Optional[bool] = field(
        default=None, metadata=config(field_name="successful")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class DeleteAssetInput:
    """DeleteAssetInput."""

    source_id: Optional[str] = field(
        default=None, metadata=config(field_name="sourceId")
    )
    collector_id: Optional[str] = field(
        default=None, metadata=config(field_name="collectorId")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class GetDataSourceInput:
    """GetDataSourceInput."""

    collector_id: Optional[str] = field(
        default=None, metadata=config(field_name="collectorId")
    )
    source_id: Optional[str] = field(
        default=None, metadata=config(field_name="sourceId")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ClusterIdentity:
    """ClusterIdentity."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class LastSeenAsset:
    """LastSeenAsset."""

    source_id: Optional[str] = field(
        default=None, metadata=config(field_name="sourceId")
    )
    service: Optional[str] = field(default=None, metadata=config(field_name="service"))
    sensor_type: Optional[str] = field(
        default=None, metadata=config(field_name="sensorType")
    )
    collector_id: Optional[str] = field(
        default=None, metadata=config(field_name="collectorID")
    )
    last_seen: Optional[int] = field(
        default=None, metadata=config(field_name="lastSeen")
    )
    health: Optional[HealthState] = field(
        default=None, metadata=config(field_name="health")
    )
    collector: Optional[ClusterIdentity] = field(
        default=None, metadata=config(field_name="collector")
    )
