"""Rules Query."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import build_output_string, prepare_input
from taegis_sdk_python.services.rules.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.rules import RulesService


class TaegisSDKRulesQuery:
    """Teagis Rules Query operations."""

    def __init__(self, service: RulesService):
        self.service = service

    def rules(
        self,
        page: Optional[int] = None,
        count: Optional[int] = None,
        rule_type: Optional[RuleType] = None,
    ) -> List[Rule]:
        """Return pages of all rules, sorted by descending updated at date."""
        endpoint = "rules"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "page": prepare_input(page),
                "count": prepare_input(count),
                "ruleType": prepare_input(rule_type),
            },
            output=build_output_string(Rule),
        )
        if result.get(endpoint) is not None:
            return Rule.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query rules")

    def all_rules(
        self, page: Optional[int] = None, count: Optional[int] = None
    ) -> List[Rule]:
        """Return pages of all the rules regardless of rule type, sorted by descending updated at date."""
        endpoint = "allRules"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "page": prepare_input(page),
                "count": prepare_input(count),
            },
            output=build_output_string(Rule),
        )
        if result.get(endpoint) is not None:
            return Rule.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query allRules")

    def suppression_rules(
        self,
        page: Optional[int] = None,
        count: Optional[int] = None,
        kind: Optional[RuleQueryKind] = None,
    ) -> List[Rule]:
        """Return pages of alert suppression rules, sorted by descending updated at date.

        Providing a kind allows for choosing global-only rules, tenant-only rules, or
        all rules. If not provided the default kinds of rules are returned, which
        depends on who is making the request: Secureworks users will get all rules
        (global and all tenant rules), but tenant users will only get their rules.."""
        endpoint = "suppressionRules"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "page": prepare_input(page),
                "count": prepare_input(count),
                "kind": prepare_input(kind),
            },
            output=build_output_string(Rule),
        )
        if result.get(endpoint) is not None:
            return Rule.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query suppressionRules")

    def event_tagging_rules(
        self, input_: Optional[EventTaggingRulesInput] = None
    ) -> List[Rule]:
        """Return pages of event tagging rules, sorted by descending updated at date.

        Providing an eventType is not specified, rules for all eventTypes are provided.
        Providing a kind allows for choosing global-only rules, tenant-only rules, or
        all rules. If not provided the default kinds of rules are returned, which
        depends on who is making the request: Secureworks users will get all rules
        (global and all tenant rules), but tenant users will only get their rules.."""
        endpoint = "eventTaggingRules"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Rule),
        )
        if result.get(endpoint) is not None:
            return Rule.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query eventTaggingRules")

    def deleted_rules(
        self,
        page: Optional[int] = None,
        count: Optional[int] = None,
        rule_type: Optional[RuleType] = None,
    ) -> List[Rule]:
        """Return deleted rules."""
        endpoint = "deletedRules"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "page": prepare_input(page),
                "count": prepare_input(count),
                "ruleType": prepare_input(rule_type),
            },
            output=build_output_string(Rule),
        )
        if result.get(endpoint) is not None:
            return Rule.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query deletedRules")

    def rules_count(self, rule_type: Optional[RuleType] = None) -> int:
        """Return a count of all rules."""
        endpoint = "rulesCount"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "ruleType": prepare_input(rule_type),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query rulesCount")

    def suppression_rules_count(self, kind: Optional[RuleQueryKind] = None) -> int:
        """Return a count of suppression rules. The kind works like in the suppressionRules query."""
        endpoint = "suppressionRulesCount"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "kind": prepare_input(kind),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query suppressionRulesCount")

    def event_tagging_rules_count(self, kind: Optional[RuleQueryKind] = None) -> int:
        """Return a count of event tagging rules. The kind works like in the eventTaggingRules query."""
        endpoint = "eventTaggingRulesCount"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "kind": prepare_input(kind),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query eventTaggingRulesCount")

    def detailed_rules_count(self) -> RuleCountResponse:
        """Return enabled, disabled, deleted counts for suppression and custom rules."""
        endpoint = "detailedRulesCount"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={},
            output=build_output_string(RuleCountResponse),
        )
        if result.get(endpoint) is not None:
            return RuleCountResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query detailedRulesCount")

    def rules_for_event(
        self,
        event_type: RuleEventType,
        page: Optional[int] = None,
        count: Optional[int] = None,
        rule_type: Optional[RuleType] = None,
    ) -> List[Rule]:
        """Return pages of rules for the given event type, sorted by descending updated at date."""
        endpoint = "rulesForEvent"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "eventType": prepare_input(event_type),
                "page": prepare_input(page),
                "count": prepare_input(count),
                "ruleType": prepare_input(rule_type),
            },
            output=build_output_string(Rule),
        )
        if result.get(endpoint) is not None:
            return Rule.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query rulesForEvent")

    def rules_for_event_count(
        self, event_type: RuleEventType, rule_type: Optional[RuleType] = None
    ) -> int:
        """Return a count of all rules for the given event type."""
        endpoint = "rulesForEventCount"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "eventType": prepare_input(event_type),
                "ruleType": prepare_input(rule_type),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query rulesForEventCount")

    def rule(self, id_: str) -> Rule:
        """Get the rule with this ID."""
        endpoint = "rule"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(Rule),
        )
        if result.get(endpoint) is not None:
            return Rule.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query rule")

    def filter_keys(self, event_type: RuleEventType) -> List[str]:
        """Return a list of all valid filter keys for the given event type."""
        endpoint = "filterKeys"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "eventType": prepare_input(event_type),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query filterKeys")

    def changes_since(
        self,
        timestamp: str,
        event_type: Optional[RuleEventType] = None,
        rule_type: Optional[RuleType] = None,
    ) -> List[Rule]:
        """Return rules that changed since the given time rounded down to the nearest whole minute.

        The provided time will be compared to the updated at time of the rules and
        if any of those are greater than the provided time, that rule (and its
        filters) will be returned.

        The event type, if provided, will limit the returned rules to those for that
        event type.

        The rule type may be nil. If it is nil, the returned rules will be of
        both types: regex and QL.

        If no rules or filters have changed since that time, nothing will be returned.

        This can be used by clients to easily see when rules have been edited by
        polling this endpoint periodically, passing in the last time they checked.."""
        endpoint = "changesSince"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "timestamp": prepare_input(timestamp),
                "eventType": prepare_input(event_type),
                "ruleType": prepare_input(rule_type),
            },
            output=build_output_string(Rule),
        )
        if result.get(endpoint) is not None:
            return Rule.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query changesSince")

    def test_filters(
        self,
        event_type: RuleEventType,
        filters: List[RuleFilterInput],
        sample_count: Optional[int] = None,
    ) -> List[RuleTestMatchStep]:
        """None."""
        endpoint = "testFilters"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "eventType": prepare_input(event_type),
                "filters": prepare_input(filters),
                "sampleCount": prepare_input(sample_count),
            },
            output=build_output_string(RuleTestMatchStep),
        )
        if result.get(endpoint) is not None:
            return RuleTestMatchStep.schema().load(result.get(endpoint), many=True)
        raise GraphQLNoRowsInResultSetError("for query testFilters")

    def rule_metrics(self, id_: str) -> RuleMetrics:
        """Get hit metrics for the rule with this ID."""
        endpoint = "ruleMetrics"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(RuleMetrics),
        )
        if result.get(endpoint) is not None:
            return RuleMetrics.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query ruleMetrics")

    def entity_prefixes(self) -> Dict[str, Any]:
        """Get entity prefixes for rules against observation event type."""
        endpoint = "entityPrefixes"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query entityPrefixes")

    def validate_ql_filter(
        self,
        ql_filter: RuleQLFilterInput,
        optional_event_type: Optional[RuleEventType] = None,
    ) -> ValidateQLFilter:
        """Validate and test this proposed QL filter."""
        endpoint = "validateQLFilter"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "qlFilter": prepare_input(ql_filter),
                "optionalEventType": prepare_input(optional_event_type),
            },
            output=build_output_string(ValidateQLFilter),
        )
        if result.get(endpoint) is not None:
            return ValidateQLFilter.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query validateQLFilter")

    def search_rules(
        self,
        query: SearchRulesInput,
        page: Optional[int] = None,
        count: Optional[int] = None,
    ) -> SearchRulesOutput:
        """Search Rules by CQL Filter."""
        endpoint = "searchRules"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "query": prepare_input(query),
                "page": prepare_input(page),
                "count": prepare_input(count),
            },
            output=build_output_string(SearchRulesOutput),
        )
        if result.get(endpoint) is not None:
            return SearchRulesOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query searchRules")

    def updated_watchlist_rules(
        self,
        query: WatchlistRuleQueryInput,
        page: Optional[int] = None,
        count: Optional[int] = None,
    ) -> SearchRulesOutput:
        """Gets a list of global non-deleted and enabled watchlist rules that were recently updated."""
        endpoint = "updatedWatchlistRules"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "query": prepare_input(query),
                "page": prepare_input(page),
                "count": prepare_input(count),
            },
            output=build_output_string(SearchRulesOutput),
        )
        if result.get(endpoint) is not None:
            return SearchRulesOutput.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query updatedWatchlistRules")
