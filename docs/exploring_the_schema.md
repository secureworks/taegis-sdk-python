# Taegis SDK for Python

## Exploring the Schema

### Getting Started

```python
from taegis_sdk_python import GraphQLService

service = GraphQLService()
schema = service.core.get_sync_schema()
```

### Main Areas of Interest

* `query_types`
* `mutation_types`
* `subscription_types`
* `type_map`

To see the GraphQL Queries/Mutations/Subscriptions that are supported, use the appropriate `*_types.fields` accessor.  For these examples, `query_types` will be used, but `mutation_types` / `subscription_types` can be used as well.

```python
schema.query_type.fields
```

```python
{'getAccessPoint': <GraphQLField <GraphQLObjectType 'AccessPoint'>>,
 'getAccessPointTemplate': <GraphQLField <GraphQLObjectType 'AccessPointCloudFormation'>>,
 'aggregatedAlertsPerEndpoint': <GraphQLField <GraphQLNonNull <GraphQLObjectType 'AggregatedAlertsPerEndpointResult'>>>,
 'aggregatedLicensedEndpointDeploymentRatio': <GraphQLField <GraphQLNonNull <GraphQLObjectType 'AggregatedLicensedEndpointDeploymentRatioResult'>>>,
 'aggregatedMeanTimeToAcknowledgeMetrics': <GraphQLField <GraphQLNonNull <GraphQLObjectType 'AggregatedMeanTimeToAcknowledgeResult'>>>,
 'aggregatedMeanTimeToResolveMetrics': <GraphQLField <GraphQLNonNull <GraphQLObjectType 'AggregatedMeanTimeToResolveResult'>>>,
...
<truncationed for readability>
```

### Return Field Name

Accessing the field is the same as a dictionary in Python (direct access via brackets `[]` or using `.get()`).

```python
schema.query_type.fields['alertsServiceSearch']
```

\- or -

```python
schema.query_type.fields.get('alertsServiceSearch')
```

```python
<GraphQLField <GraphQLObjectType 'AlertsResponse'>>
```

Here we can see that the `alertsServiceSearch` will return an `AlertsResponse` object.

### Endpoint Arguments

Lising the argument names.

```python
schema.query_type.fields['alertsServiceSearch'].args
```

```python
{'in': <graphql.type.definition.GraphQLArgument at 0x7f8ee52bf2e0>}
```

We can get the argument type name.

```python
schema.query_type.fields['alertsServiceSearch'].args["in"].type
```

This is a `SearchRequestInput` object.

```
<GraphQLInputObjectType 'SearchRequestInput'>
```

This endpoint takes 1 argument called `in`, but we do not know the fields this argument will accept.

```python
schema.query_type.fields['alertsServiceSearch'].args["in"].type.fields
```

```python
{'cql_query': <graphql.type.definition.GraphQLInputField at 0x7f8ee49f9490>,
 'offset': <graphql.type.definition.GraphQLInputField at 0x7f8ee49f94c0>,
 'limit': <graphql.type.definition.GraphQLInputField at 0x7f8ee49f94f0>,
 'search_id': <graphql.type.definition.GraphQLInputField at 0x7f8ee49f9520>}
```

This will continue until all the field types are of a GraphQLScalarType.  Some items may be a list or non-nullable, these can be unpacked using the `of_type` accessor.

### Return Fields

We can use `.type.fields` to get a dictionary of return fields.  Using a combination of `.type` or `.of_type` on each field until we reach a scalar or enum to determine what is available for request.

```python
schema.query_type.fields['alertsServiceSearch'].type.fields
```

```python
{'status': <GraphQLField <GraphQLEnumType 'RPCResponseStatus'>>,
 'reason': <GraphQLField <GraphQLScalarType 'String'>>,
 'alerts': <GraphQLField <GraphQLObjectType 'AlertsList'>>,
 'search_id': <GraphQLField <GraphQLScalarType 'String'>>}
```

```python
schema.query_type.fields['alertsServiceSearch'].type.fields["alerts"].type.fields
```

```python
{'list': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'Alert2'>>>>,
 'total_results': <GraphQLField <GraphQLScalarType 'Int'>>,
 'next_offset': <GraphQLField <GraphQLScalarType 'Int'>>,
 'previous_offset': <GraphQLField <GraphQLScalarType 'Int'>>,
 'last_offset': <GraphQLField <GraphQLScalarType 'Int'>>,
 'first_offset': <GraphQLField <GraphQLScalarType 'Int'>>,
 'total_parts': <GraphQLField <GraphQLScalarType 'Int'>>,
 'part': <GraphQLField <GraphQLScalarType 'Int'>>,
 'group_by': <GraphQLField <GraphQLList <GraphQLNonNull <GraphQLObjectType 'AggregationResponse'>>>>}
```

For a field like `list`, we can see that there are multiple defintions to unpack: `GraphQLField (type) -> GraphQLList (of_type) -> GraphQLNonNull (of_type)`.

```python
schema.query_type.fields['alertsServiceSearch'].type.fields["alerts"].type.fields["list"].type.of_type.of_type.fields
```

```python
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
 'threat_score': <GraphQLField <GraphQLScalarType 'Float32'>>,
 'events_metadata': <GraphQLField <GraphQLObjectType 'AlertEventMetadata'>>,
 'alertPrioritization': <GraphQLField <GraphQLObjectType 'AlertPrioritization'>>}
```

### Building an arbitrary query

We can now start building out a valid GraphQL query.  We will use the `alertsServiceSearch` for this example.  The variables will come from our argument exploration.  We will use the `in` top argument with field `cql_query`.  Our return fields will get the query `status` and a list of alert ids.

Arbitrary methods include:

* `execute_query` 
* `execute_mutation` 
* `execute_subscription`

```python
service.core.execute_query(
    endpoint="alertsServiceSearch",
    variables={
        "in": {
            "cql_query": "FROM alert EARLIEST=-1d | head 10"
        }
    },
    output="""
    status
    alerts {
        list {
            id
        }
    }
    """
)
```

```python
{'alertsServiceSearch': {'status': 'OK',
  'alerts': {'list': [{'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:email:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:email:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter-ql:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'}]}}}
```

### Building an raw query

We can now start building out a valid GraphQL query.  We will use the `alertsServiceSearch` for this example.  The variables will come from our argument exploration.  We will use the `in` top argument with field `cql_query`.  Our return fields will get the query `status` and a list of alert ids.  For more information on GraphQL query strings, see [GraphQL Learn](https://graphql.org/learn/queries/).

`execute()` works with queries and mutations.  `subscribe()` is used for subscriptions.

```python
service.core.execute(
    query_string="""
    query MyAlertsServiceSearch($in: SearchRequestInput) {
        alertsServiceSearch(in: $in) {
            status
            alerts {
                list {
                    id
                }
            }
        }
    }
    """
    variables={
        "in": {
            "cql_query": "FROM alert EARLIEST=-1d | head 10"
        }
    },
)
```

```python
{'alertsServiceSearch': {'status': 'OK',
  'alerts': {'list': [{'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:email:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:email:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter-ql:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'},
    {'id': 'alert://priv:event-filter:00000:0000000000000:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'}]}}}
```


### Schema File

We can parse the schema object to a `schema.graphql` format.  This will generate a GraphQL schema definition document per https://graphql.org/learn/schema/.

```python
from taegis_sdk_python import GraphQLService
from graphql.utilities import print_schema

service = GraphQLService()
schema = service.core.get_sync_schema()

print(print_schema(schema))
```

```
input AbsoluteTimeRedQLQueryInput {
  query: String!
  referenceTime: Time!
  currentTime: Time!
}

type AccessPoint {
  tenantID: String!
  arn: String!
  alias: String!
  principal: [String!]!
}
...
<truncated for readability>
```

### Special Cases

Not all APIs reside behind the same configuration.  APIs like `tenants` or `events` may be specially configured.  It is best to use those services instead of `core` for exploration and execution.  Special configuration cases can be found in the `__init__.py` file under the `__init__` class method per service.  Configuration is subject to change in any update.  For robust code, please use the appropriate service to execute your queries, mutations or subscriptions.
