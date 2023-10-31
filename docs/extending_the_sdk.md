# Taegis SDK for Python

## Extending the SDK

One of the benefits that GraphQL can provide is federated services, where a single
GraphQL call can correlate results from another service.  The Taegis SDK for Python
does not provide this functionality out of the box, but can be easily extended.

In this example, we are looking to add event data side by side with our alert data.
Since this adds data from another service we will need to extend some dataclasses
from the original types.

Exploring the schema, we can see that `event_data` is a Map field (or a Python dictionary),
but it is not included by default in the AlertsResponse output string.  The SDK can be extended
to support this class, by inhereting from the base object and adding the field to the dataclass.

```python
from taegis_sdk_python import GraphQLService, build_output_string
from taegis_sdk_python.services.alerts.types import AlertsResponse

service = GraphQLService()
schema = service.core.get_sync_schema()
print(schema.query_type.fields["alertsServiceSearch"])
print(schema.type_map["AlertsResponse"].fields)
print(schema.type_map["AlertsList"].fields)
print(schema.type_map["Alert2"].fields)
print(schema.type_map['AuxiliaryEvent'].fields)
```

```
# alertsServiceSearch
<GraphQLField <GraphQLObjectType 'AlertsResponse'>>
# AlertsResponse
{'status': <GraphQLField <GraphQLEnumType 'RPCResponseStatus'>>,
 'reason': <GraphQLField <GraphQLScalarType 'String'>>,
 'alerts': <GraphQLField <GraphQLObjectType 'AlertsList'>>,
 'search_id': <GraphQLField <GraphQLScalarType 'String'>>}
# AlertsList
{'list': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'Alert2'>>>>,
 'total_results': <GraphQLField <GraphQLScalarType 'Int'>>,
 'next_offset': <GraphQLField <GraphQLScalarType 'Int'>>,
 'previous_offset': <GraphQLField <GraphQLScalarType 'Int'>>,
 'last_offset': <GraphQLField <GraphQLScalarType 'Int'>>,
 'first_offset': <GraphQLField <GraphQLScalarType 'Int'>>,
 'total_parts': <GraphQLField <GraphQLScalarType 'Int'>>,
 'part': <GraphQLField <GraphQLScalarType 'Int'>>,
 'group_by': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'AggregationResponse'>>>>}
# Alert2
{'id': <GraphQLField <GraphQLNonNull <GraphQLScalarType 'ID'>>>,
 'group_key': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLScalarType 'String'>>>>,
 'metadata': <GraphQLField <GraphQLObjectType 'AlertsMetadata'>>,
 'visibility': <GraphQLField <GraphQLEnumType 'Visibility'>>,
 'attack_technique_ids': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLScalarType 'String'>>>>,
 'tenant_id': <GraphQLField <GraphQLScalarType 'String'>>,
 'parent_tenant_id': <GraphQLField <GraphQLScalarType 'String'>>,
 'suppressed': <GraphQLField <GraphQLScalarType 'Boolean'>>,
 'suppression_rules': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'AlertRuleReference'>>>>,
 'alerting_rules': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'AlertRuleReference'>>>>,
 'status': <GraphQLField <GraphQLEnumType 'ResolutionStatus'>>,
 'resolution_reason': <GraphQLField <GraphQLScalarType 'String'>>,
 'resolution_history': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'ResolutionMetadata'>>>>,
 'severity_history': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'SeverityUpdate'>>>>,
 'tags': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLScalarType 'String'>>>>,
 'sensor_types': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLScalarType 'String'>>>>,
 'entities': <GraphQLField <GraphQLObjectType 'EntityRelationships'>>,
 'key_entities': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'EntityMetadata'>>>>,
 'event_ids': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'AuxiliaryEvent'>>>>,
 'observation_ids': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'Observation'>>>>,
 'investigation_ids': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'Investigation'>>>>,
 'collection_ids': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'Collection'>>>>,
 'enrichment_details': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'EnrichmentDetail'>>>>,
 'third_party_details': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'ThirdPartyDetail'>>>>,
 'reference_details': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'ReferenceDetail'>>>>,
 'priority': <GraphQLField <GraphQLObjectType 'AlertPriority'>>,
 'events_metadata': <GraphQLField <GraphQLObjectType 'AlertEventMetadata'>>}
# AuxiliaryEvent
{'id': <GraphQLField <GraphQLNonNull <GraphQLScalarType 'ID'>>>,
 'event_data': <GraphQLField <GraphQLScalarType 'Map'>>,
 'observation_ids': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'Observation'>>>>,
 'investigations_resource_id': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'Investigation'>>>>,
 'alerts_resource_id': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'Alerts2'>>>>}
```

```python
build_output_string(AlertsResponse)
```

```
...
event_ids { id }
...
```

*Note: Output has been truncated for verbosity.*

Any object tree that will utilize this custom dataclass will also need to be updated, but
only the fields that are modified need to be referenced.  In this example tree:
`AlertsResponse -> AlertsList -> Alert2 -> AuxiliaryEvent`.

```python
from taegis_sdk_python import GraphQLService, prepare_input, build_output_string
from taegis_sdk_python.services.alerts.types import *
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config

@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CustomAuxiliaryEvent(AuxiliaryEvent):
    """My Custom Auxiliary Event - Extends Auxiliary Event with event_data
    to take advantage of GQL federated services.
    """

    event_data: Optional[Dict[str, Any]] = field(
        default=None, metadata=config(field_name="event_data")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CustomAlert2(Alert2):
    """My Custom Alert2."""

    event_ids: Optional[List[CustomAuxiliaryEvent]] = field(
        default=None, metadata=config(field_name="event_ids")
    )



@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CustomAlertsList(AlertsList):
    """My Custom AlertsList."""

    list: Optional[List[CustomAlert2]] = field(
        default=None, metadata=config(field_name="list")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CustomAlertsResponse(AlertsResponse):
    """My Custom AlertsResponse."""

    alerts: Optional[CustomAlertsList] = field(
        default=None, metadata=config(field_name="alerts")
    )


def alerts_service_search_with_events(service: GraphQLService, in_: SearchRequestInput) -> CustomAlertsResponse:
    """Query Taegis Alerts with corresponding Events attached."""
    endpoint = "alertsServiceSearch"
    result = service.alerts.execute_query(
        endpoint=endpoint,
        variables={
            "in": prepare_input(in_),
        },
        output=build_output_string(CustomAlertsResponse),
    )
    if result is not None:
        return CustomAlertsResponse.from_dict(result.get(endpoint))
    raise GraphQLNoRowsInResultSetError("for query alertsServiceSearch")
```
