"""CqlMetadata Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ParseError:
    """ParseError."""

    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    start_line: Optional[int] = field(
        default=None, metadata=config(field_name="startLine")
    )
    stop_line: Optional[int] = field(
        default=None, metadata=config(field_name="stopLine")
    )
    start_column: Optional[int] = field(
        default=None, metadata=config(field_name="startColumn")
    )
    stop_column: Optional[int] = field(
        default=None, metadata=config(field_name="stopColumn")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Aggregation:
    """Aggregation."""

    type: Optional[str] = field(default=None, metadata=config(field_name="type"))
    field_: Optional[str] = field(default=None, metadata=config(field_name="field"))
    alias: Optional[str] = field(default=None, metadata=config(field_name="alias"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class By:
    """By."""

    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    is_interval: Optional[bool] = field(
        default=None, metadata=config(field_name="isInterval")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SortField:
    """SortField."""

    ident: Optional[str] = field(default=None, metadata=config(field_name="ident"))
    ascending: Optional[bool] = field(
        default=None, metadata=config(field_name="ascending")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventQueryOptions:
    """EventQueryOptions."""

    aggregation_off: Optional[bool] = field(
        default=None, metadata=config(field_name="aggregationOff")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Aggregate:
    """Aggregate."""

    aggregations: Optional[List[Aggregation]] = field(
        default=None, metadata=config(field_name="aggregations")
    )
    by: Optional[List[By]] = field(default=None, metadata=config(field_name="by"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PipelineFunc:
    """PipelineFunc."""

    head: Optional[int] = field(default=None, metadata=config(field_name="head"))
    tail: Optional[int] = field(default=None, metadata=config(field_name="tail"))
    fields: Optional[List[str]] = field(
        default=None, metadata=config(field_name="fields")
    )
    aggregate: Optional[Aggregate] = field(
        default=None, metadata=config(field_name="aggregate")
    )
    sort: Optional[List[SortField]] = field(
        default=None, metadata=config(field_name="sort")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ValidatorResults:
    """ValidatorResults."""

    types: Optional[List[str]] = field(
        default=None, metadata=config(field_name="types")
    )
    errors: Optional[List[ParseError]] = field(
        default=None, metadata=config(field_name="errors")
    )
    warnings: Optional[List[ParseError]] = field(
        default=None, metadata=config(field_name="warnings")
    )
    pipeline: Optional[List[PipelineFunc]] = field(
        default=None, metadata=config(field_name="pipeline")
    )
