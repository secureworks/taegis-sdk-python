"""Rules Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum, parse_union_result


class RuleEventType(str, Enum):
    """RuleEventType."""

    ANTIVIRUS = "antivirus"
    APICALL = "apicall"
    AUTH = "auth"
    CLOUDAUDIT = "cloudaudit"
    DHCP = "dhcp"
    DNSQUERY = "dnsquery"
    EMAIL = "email"
    ENCRYPT = "encrypt"
    FILEMOD = "filemod"
    GENERIC = "generic"
    HTTP = "http"
    MANAGEMENT_EVENT = "management_event"
    NETFLOW = "netflow"
    NIDS = "nids"
    OBSERVATION_V2 = "observation_v2"
    PERSISTENCE = "persistence"
    PROCESS = "process"
    REGISTRY = "registry"
    SCRIPT_BLOCK = "script_block"
    THIRDPARTYALERT = "thirdpartyalert"
    THREAD_INJECTION = "thread_injection"
    PROCESS_MODULE = "process_module"
    TAEGIS_AGENT_DETECTION = "taegis_agent_detection"


class RuleEndpointPlatform(str, Enum):
    """RuleEndpointPlatform."""

    PLATFORM_WINDOWS = "PLATFORM_WINDOWS"
    PLATFORM_LINUX = "PLATFORM_LINUX"
    PLATFORM_MAC = "PLATFORM_MAC"
    PLATFORM_UNKNOWN = "PLATFORM_UNKNOWN"


class RuleCountComparison(str, Enum):
    """RuleCountComparison."""

    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    EQUAL_TO = "equal_to"


class RuleType(str, Enum):
    """RuleType."""

    REGEX = "REGEX"
    REDQL = "REDQL"
    QL = "QL"


class RuleAction(str, Enum):
    """RuleAction."""

    ALERT = "ALERT"
    SUPPRESS = "SUPPRESS"
    TUNE = "TUNE"
    TAG_EVENT = "TAG_EVENT"
    NONE = "NONE"


class RuleScope(str, Enum):
    """RuleScope."""

    TENANT = "TENANT"
    GLOBAL = "GLOBAL"


class RuleSource(str, Enum):
    """RuleSource."""

    WATCHLIST = "WATCHLIST"
    DETECTOR = "DETECTOR"
    CUSTOM = "CUSTOM"


class AlertOrigin(str, Enum):
    """AlertOrigin."""

    INTERNAL = "INTERNAL"
    CUSTOMER = "CUSTOMER"
    EXTERNAL = "EXTERNAL"
    PARTNER = "PARTNER"


class AlertSeverity(str, Enum):
    """AlertSeverity."""

    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class RuleVisibility(str, Enum):
    """RuleVisibility."""

    VISIBLE = "visible"
    HIDDEN = "hidden"


class RuleDay(str, Enum):
    """RuleDay."""

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class RuleResolutionStatus(str, Enum):
    """RuleResolutionStatus."""

    OPEN = "OPEN"
    TRUE_POSITIVE_BENIGN = "TRUE_POSITIVE_BENIGN"
    TRUE_POSITIVE_MALICIOUS = "TRUE_POSITIVE_MALICIOUS"
    FALSE_POSITIVE = "FALSE_POSITIVE"
    NOT_ACTIONABLE = "NOT_ACTIONABLE"
    OTHER = "OTHER"
    SUPPRESSED = "SUPPRESSED"


class RuleQueryKind(str, Enum):
    """RuleQueryKind."""

    ALL = "all"
    GLOBAL = "global"
    TENANT = "tenant"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AttackCategoryDetail:
    """AttackCategoryDetail."""

    technique_id: Optional[str] = field(
        default=None, metadata=config(field_name="techniqueID")
    )
    technique: Optional[str] = field(
        default=None, metadata=config(field_name="technique")
    )
    tactics: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tactics")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleCount:
    """RuleCount."""

    enabled: Optional[int] = field(default=None, metadata=config(field_name="enabled"))
    disabled: Optional[int] = field(
        default=None, metadata=config(field_name="disabled")
    )
    deleted: Optional[int] = field(default=None, metadata=config(field_name="deleted"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleReference:
    """RuleReference."""

    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleQLFilterTest:
    """RuleQLFilterTest."""

    field_name: Optional[str] = field(
        default=None, metadata=config(field_name="fieldName")
    )
    field_value: Optional[str] = field(
        default=None, metadata=config(field_name="fieldValue")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleQLFilterTestInput:
    """RuleQLFilterTestInput."""

    field_name: Optional[str] = field(
        default=None, metadata=config(field_name="fieldName")
    )
    field_value: Optional[str] = field(
        default=None, metadata=config(field_name="fieldValue")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleRedQLFilterTest:
    """RuleRedQLFilterTest."""

    field_name: Optional[str] = field(
        default=None, metadata=config(field_name="fieldName")
    )
    field_value: Optional[str] = field(
        default=None, metadata=config(field_name="fieldValue")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleRedQLFilterTestInput:
    """RuleRedQLFilterTestInput."""

    field_name: Optional[str] = field(
        default=None, metadata=config(field_name="fieldName")
    )
    field_value: Optional[str] = field(
        default=None, metadata=config(field_name="fieldValue")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleReferenceInput:
    """RuleReferenceInput."""

    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    url: Optional[str] = field(default=None, metadata=config(field_name="url"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleEventData:
    """RuleEventData."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleDailyCount:
    """RuleDailyCount."""

    count: Optional[int] = field(default=None, metadata=config(field_name="count"))
    date: Optional[str] = field(default=None, metadata=config(field_name="date"))
    timestamp: Optional[int] = field(
        default=None, metadata=config(field_name="timestamp")
    )


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
class SearchRulesInput:
    """SearchRulesInput."""

    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    global_: Optional[bool] = field(default=None, metadata=config(field_name="global"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class WatchlistRuleQueryInput:
    """WatchlistRuleQueryInput."""

    exclude_prefixes: Optional[List[str]] = field(
        default=None, metadata=config(field_name="excludePrefixes")
    )
    updated_since_days: Optional[int] = field(
        default=None, metadata=config(field_name="updatedSinceDays")
    )
    updated_since: Optional[str] = field(
        default=None, metadata=config(field_name="updatedSince")
    )
    updated_prior_to: Optional[str] = field(
        default=None, metadata=config(field_name="updatedPriorTo")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PageInfoOffset:
    """PageInfoOffset."""

    page: Optional[int] = field(default=None, metadata=config(field_name="page"))
    per_page: Optional[int] = field(default=None, metadata=config(field_name="perPage"))
    offset: Optional[int] = field(default=None, metadata=config(field_name="offset"))
    total_entries_size: Optional[int] = field(
        default=None, metadata=config(field_name="totalEntriesSize")
    )
    current_entries_size: Optional[int] = field(
        default=None, metadata=config(field_name="currentEntriesSize")
    )
    total_pages: Optional[int] = field(
        default=None, metadata=config(field_name="totalPages")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleFacetAggregationsInput:
    """RuleFacetAggregationsInput."""

    filter_query: Optional[str] = field(
        default=None, metadata=config(field_name="filterQuery")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class AggregationPair:
    """AggregationPair."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[int] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TDRUser:
    """TDRUser."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleTermCount:
    """RuleTermCount."""

    value: Optional[int] = field(default=None, metadata=config(field_name="value"))
    comparison: Optional[Union[RuleCountComparison, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleCountComparison, x),
            field_name="comparison",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleFilter:
    """RuleFilter."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    rule_id: Optional[str] = field(default=None, metadata=config(field_name="ruleID"))
    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    pattern: Optional[str] = field(default=None, metadata=config(field_name="pattern"))
    inverted: Optional[bool] = field(
        default=None, metadata=config(field_name="inverted")
    )
    case_sensitive: Optional[bool] = field(
        default=None, metadata=config(field_name="caseSensitive")
    )
    test_should: Optional[List[str]] = field(
        default=None, metadata=config(field_name="testShould")
    )
    test_should_not: Optional[List[str]] = field(
        default=None, metadata=config(field_name="testShouldNot")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    count: Optional[RuleTermCount] = field(
        default=None, metadata=config(field_name="count")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleTermCountInput:
    """RuleTermCountInput."""

    value: Optional[int] = field(default=None, metadata=config(field_name="value"))
    comparison: Optional[Union[RuleCountComparison, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleCountComparison, x),
            field_name="comparison",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleFilterInput:
    """RuleFilterInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    pattern: Optional[str] = field(default=None, metadata=config(field_name="pattern"))
    inverted: Optional[bool] = field(
        default=None, metadata=config(field_name="inverted")
    )
    case_sensitive: Optional[bool] = field(
        default=None, metadata=config(field_name="caseSensitive")
    )
    clear_count: Optional[bool] = field(
        default=None, metadata=config(field_name="clearCount")
    )
    test_should: Optional[List[str]] = field(
        default=None, metadata=config(field_name="testShould")
    )
    test_should_not: Optional[List[str]] = field(
        default=None, metadata=config(field_name="testShouldNot")
    )
    count: Optional[RuleTermCountInput] = field(
        default=None, metadata=config(field_name="count")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleSampleEvent:
    """RuleSampleEvent."""

    data: Optional[List[RuleEventData]] = field(
        default=None, metadata=config(field_name="data")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleMetrics:
    """RuleMetrics."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    last_hit_date: Optional[str] = field(
        default=None, metadata=config(field_name="lastHitDate")
    )
    last30_days_count: Optional[int] = field(
        default=None, metadata=config(field_name="last30DaysCount")
    )
    daily_counts: Optional[List[RuleDailyCount]] = field(
        default=None, metadata=config(field_name="dailyCounts")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleCountResponse:
    """RuleCountResponse."""

    suppression: Optional[RuleCount] = field(
        default=None, metadata=config(field_name="suppression")
    )
    custom: Optional[RuleCount] = field(
        default=None, metadata=config(field_name="custom")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleQLFilter:
    """RuleQLFilter."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    rule_id: Optional[str] = field(default=None, metadata=config(field_name="ruleID"))
    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    test_should: Optional[List[RuleQLFilterTest]] = field(
        default=None, metadata=config(field_name="testShould")
    )
    test_should_not: Optional[List[RuleQLFilterTest]] = field(
        default=None, metadata=config(field_name="testShouldNot")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleQLFilterInput:
    """RuleQLFilterInput."""

    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    test_should: Optional[List[RuleQLFilterTestInput]] = field(
        default=None, metadata=config(field_name="testShould")
    )
    test_should_not: Optional[List[RuleQLFilterTestInput]] = field(
        default=None, metadata=config(field_name="testShouldNot")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleRedQLFilter:
    """RuleRedQLFilter."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    rule_id: Optional[str] = field(default=None, metadata=config(field_name="ruleID"))
    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    test_should: Optional[List[RuleRedQLFilterTest]] = field(
        default=None, metadata=config(field_name="testShould")
    )
    test_should_not: Optional[List[RuleRedQLFilterTest]] = field(
        default=None, metadata=config(field_name="testShouldNot")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleRedQLFilterInput:
    """RuleRedQLFilterInput."""

    query: Optional[str] = field(default=None, metadata=config(field_name="query"))
    test_should: Optional[List[RuleRedQLFilterTestInput]] = field(
        default=None, metadata=config(field_name="testShould")
    )
    test_should_not: Optional[List[RuleRedQLFilterTestInput]] = field(
        default=None, metadata=config(field_name="testShouldNot")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleTestMatchStep:
    """RuleTestMatchStep."""

    total: Optional[int] = field(default=None, metadata=config(field_name="total"))
    matches: Optional[int] = field(default=None, metadata=config(field_name="matches"))
    duration: Optional[str] = field(
        default=None, metadata=config(field_name="duration")
    )
    filter: Optional[RuleFilter] = field(
        default=None, metadata=config(field_name="filter")
    )
    samples: Optional[List[RuleSampleEvent]] = field(
        default=None, metadata=config(field_name="samples")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ValidateQLFilter:
    """ValidateQLFilter."""

    original_query: Optional[str] = field(
        default=None, metadata=config(field_name="originalQuery")
    )
    expanded_query: Optional[str] = field(
        default=None, metadata=config(field_name="expandedQuery")
    )
    event_type: Optional[Union[RuleEventType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleEventType, x),
            field_name="eventType",
        ),
    )
    errors: Optional[List[ParseError]] = field(
        default=None, metadata=config(field_name="errors")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class EventTaggingRulesInput:
    """EventTaggingRulesInput."""

    page: Optional[int] = field(default=None, metadata=config(field_name="page"))
    count: Optional[int] = field(default=None, metadata=config(field_name="count"))
    since: Optional[str] = field(default=None, metadata=config(field_name="since"))
    event_type: Optional[Union[RuleEventType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleEventType, x),
            field_name="eventType",
        ),
    )
    kind: Optional[Union[RuleQueryKind, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleQueryKind, x),
            field_name="kind",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SearchRulesByFieldInput:
    """SearchRulesByFieldInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    attack_categories: Optional[List[str]] = field(
        default=None, metadata=config(field_name="attackCategories")
    )
    cve: Optional[str] = field(default=None, metadata=config(field_name="cve"))
    vid: Optional[int] = field(default=None, metadata=config(field_name="vid"))
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    deleted: Optional[bool] = field(default=None, metadata=config(field_name="deleted"))
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    rule_source: Optional[Union[RuleSource, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleSource, x),
            field_name="ruleSource",
        ),
    )
    rule_action: Optional[Union[RuleAction, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleAction, x),
            field_name="ruleAction",
        ),
    )
    scope: Optional[Union[RuleScope, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleScope, x),
            field_name="scope",
        ),
    )
    rule_type: Optional[Union[RuleType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleType, x),
            field_name="ruleType",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleFacetAggregationsOutput:
    """RuleFacetAggregationsOutput."""

    vid: Optional[List[AggregationPair]] = field(
        default=None, metadata=config(field_name="vid")
    )
    cve: Optional[List[AggregationPair]] = field(
        default=None, metadata=config(field_name="cve")
    )
    severity: Optional[List[AggregationPair]] = field(
        default=None, metadata=config(field_name="severity")
    )
    mitre_technique: Optional[List[AggregationPair]] = field(
        default=None, metadata=config(field_name="mitreTechnique")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class RuleInput:
    """RuleInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    group_key_template: Optional[str] = field(
        default=None, metadata=config(field_name="groupKeyTemplate")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    severity: Optional[float] = field(
        default=None, metadata=config(field_name="severity")
    )
    confidence: Optional[float] = field(
        default=None, metadata=config(field_name="confidence")
    )
    create_alert: Optional[bool] = field(
        default=None, metadata=config(field_name="createAlert")
    )
    tags: Optional[List[str]] = field(default=None, metadata=config(field_name="tags"))
    cve: Optional[str] = field(default=None, metadata=config(field_name="cve"))
    vid: Optional[int] = field(default=None, metadata=config(field_name="vid"))
    destination_topic: Optional[str] = field(
        default=None, metadata=config(field_name="destinationTopic")
    )
    attack_categories: Optional[List[str]] = field(
        default=None, metadata=config(field_name="attackCategories")
    )
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    event_type: Optional[Union[RuleEventType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleEventType, x),
            field_name="eventType",
        ),
    )
    visibility: Optional[Union[RuleVisibility, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleVisibility, x),
            field_name="visibility",
        ),
    )
    result_visibility: Optional[Union[RuleVisibility, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleVisibility, x),
            field_name="resultVisibility",
        ),
    )
    status: Optional[Union[RuleResolutionStatus, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleResolutionStatus, x),
            field_name="status",
        ),
    )
    origin: Optional[Union[AlertOrigin, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(AlertOrigin, x),
            field_name="origin",
        ),
    )
    alert_severity: Optional[Union[AlertSeverity, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(AlertSeverity, x),
            field_name="alertSeverity",
        ),
    )
    rule_source: Optional[Union[RuleSource, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleSource, x),
            field_name="ruleSource",
        ),
    )
    rule_action: Optional[Union[RuleAction, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleAction, x),
            field_name="ruleAction",
        ),
    )
    endpoint_platform: Optional[List[Union[RuleEndpointPlatform, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleEndpointPlatform, x),
            field_name="endpointPlatform",
        ),
    )
    references: Optional[List[RuleReferenceInput]] = field(
        default=None, metadata=config(field_name="references")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Rule:
    """Rule."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    user_id: Optional[str] = field(
        default=None,
        metadata=config(
            metadata={"deprecated": True, "deprecation_reason": "Use user.ID"},
            field_name="userID",
        ),
    )
    group_key_template: Optional[str] = field(
        default=None, metadata=config(field_name="groupKeyTemplate")
    )
    name: Optional[str] = field(default=None, metadata=config(field_name="name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    generative_ai_rule_explain: Optional[str] = field(
        default=None, metadata=config(field_name="generativeAIRuleExplain")
    )
    severity: Optional[float] = field(
        default=None, metadata=config(field_name="severity")
    )
    confidence: Optional[float] = field(
        default=None, metadata=config(field_name="confidence")
    )
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    create_alert: Optional[bool] = field(
        default=None, metadata=config(field_name="createAlert")
    )
    tags: Optional[List[str]] = field(default=None, metadata=config(field_name="tags"))
    cve: Optional[str] = field(default=None, metadata=config(field_name="cve"))
    vid: Optional[int] = field(default=None, metadata=config(field_name="vid"))
    destination_topic: Optional[str] = field(
        default=None, metadata=config(field_name="destinationTopic")
    )
    attack_categories: Optional[List[str]] = field(
        default=None, metadata=config(field_name="attackCategories")
    )
    deleted: Optional[bool] = field(default=None, metadata=config(field_name="deleted"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )
    scope_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="scopeIDs")
    )
    user: Optional[TDRUser] = field(default=None, metadata=config(field_name="user"))
    event_type: Optional[Union[RuleEventType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleEventType, x),
            field_name="eventType",
        ),
    )
    seven_day_group_key_rollover_day: Optional[Union[RuleDay, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleDay, x),
            field_name="sevenDayGroupKeyRolloverDay",
        ),
    )
    visibility: Optional[Union[RuleVisibility, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleVisibility, x),
            field_name="visibility",
        ),
    )
    result_visibility: Optional[Union[RuleVisibility, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleVisibility, x),
            field_name="resultVisibility",
        ),
    )
    status: Optional[Union[RuleResolutionStatus, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleResolutionStatus, x),
            field_name="status",
        ),
    )
    origin: Optional[Union[AlertOrigin, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(AlertOrigin, x),
            field_name="origin",
        ),
    )
    alert_severity: Optional[Union[AlertSeverity, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(AlertSeverity, x),
            field_name="alertSeverity",
        ),
    )
    attack_categories_details: Optional[List[AttackCategoryDetail]] = field(
        default=None, metadata=config(field_name="attackCategoriesDetails")
    )
    endpoint_platform: Optional[List[Union[RuleEndpointPlatform, TaegisEnum]]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleEndpointPlatform, x),
            field_name="endpointPlatform",
        ),
    )
    references: Optional[List[RuleReference]] = field(
        default=None, metadata=config(field_name="references")
    )
    filters: Optional[List[RuleFilter]] = field(
        default=None, metadata=config(field_name="filters")
    )
    ql_filter: Optional[RuleQLFilter] = field(
        default=None, metadata=config(field_name="qlFilter")
    )
    rule_action: Optional[Union[RuleAction, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleAction, x),
            field_name="ruleAction",
        ),
    )
    rule_source: Optional[Union[RuleSource, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleSource, x),
            field_name="ruleSource",
        ),
    )
    rule_type: Optional[Union[RuleType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleType, x),
            field_name="ruleType",
        ),
    )
    scope: Optional[Union[RuleScope, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(RuleScope, x),
            field_name="scope",
        ),
    )
    red_ql_filter: Optional[RuleRedQLFilter] = field(
        default=None, metadata=config(field_name="redQLFilter")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class SearchRulesOutput:
    """SearchRulesOutput."""

    rules: Optional[List[Rule]] = field(
        default=None, metadata=config(field_name="rules")
    )
    page_info: Optional[PageInfoOffset] = field(
        default=None, metadata=config(field_name="pageInfo")
    )
