"""MitreAttackInfo Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class MitreAttackInformation:
    """MitreAttackInformation."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    technique_id: Optional[str] = field(
        default=None, metadata=config(field_name="technique_id")
    )
    technique: Optional[str] = field(
        default=None, metadata=config(field_name="technique")
    )
    tactics: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tactics")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    platform: Optional[List[str]] = field(
        default=None, metadata=config(field_name="platform")
    )
    system_requirements: Optional[List[str]] = field(
        default=None, metadata=config(field_name="system_requirements")
    )
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))
    data_sources: Optional[List[str]] = field(
        default=None, metadata=config(field_name="data_sources")
    )
    defence_bypassed: Optional[List[str]] = field(
        default=None, metadata=config(field_name="defence_bypassed")
    )
    contributors: Optional[List[str]] = field(
        default=None, metadata=config(field_name="contributors")
    )
    version: Optional[str] = field(default=None, metadata=config(field_name="version"))
    deprecated: Optional[bool] = field(
        default=None, metadata=config(field_name="deprecated")
    )
    alternate_technique: Optional[str] = field(
        default=None, metadata=config(field_name="alternate_technique")
    )
    alternate_url: Optional[str] = field(
        default=None, metadata=config(field_name="alternate_url")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SearchMitreAttackInput:
    """SearchMitreAttackInput."""

    case_sensitive: Optional[bool] = field(
        default=None, metadata=config(field_name="CaseSensitive")
    )
    technique_id: Optional[str] = field(
        default=None, metadata=config(field_name="technique_id")
    )
    technique: Optional[str] = field(
        default=None, metadata=config(field_name="technique")
    )
    tactics: Optional[str] = field(default=None, metadata=config(field_name="tactics"))
    data_sources: Optional[str] = field(
        default=None, metadata=config(field_name="data_sources")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    contributors: Optional[str] = field(
        default=None, metadata=config(field_name="contributors")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Ids:
    """Ids."""

    values: Optional[List[str]] = field(
        default=None, metadata=config(field_name="values")
    )
