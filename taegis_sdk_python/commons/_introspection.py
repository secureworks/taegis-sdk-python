"""Taegis Commons - Introspection GraphQL operations."""

from typing import Any, Optional

from graphql import GraphQLSchema

from taegis_sdk_python import (
    GraphQLService,
    build_output_string_from_introspection,
    prepare_input,
)


def introspection_query(
    service: GraphQLService,
    endpoint: str,
    schema: Optional[GraphQLSchema] = None,
    **kwargs
) -> Any:
    """Generate a GraphQL Query operation with output based on server-side introspection.

    Parameters
    ----------
    service : GraphQLService
    endpoint : str
    schema : Optional[GraphQLSchema], optional
        If not provided, the latest schema will be retrieved from the GQL endpoint. By default, None.
        Useful when the schmea is not on the core service, but is on a child service (e.g. EventService) that shares the same GQL endpoint.
    Returns
    -------
    Any
        Usually a dict or list of dicts, depending on the query.
    """
    # retreive the latest schema from the GQL endpoint
    if schema is None:
        schema = service.core.schema
    # parse the correct output fields for the desired query from the schema
    field = schema.query_type.fields.get(endpoint)

    output = build_output_string_from_introspection(field)

    results = service.core.execute_query(
        endpoint=endpoint,
        variables={key: prepare_input(value) for key, value in kwargs.items()},
        output=output,
    )

    return results.get(endpoint)


def introspection_mutation(
    service: GraphQLService,
    endpoint: str,
    schema: Optional[GraphQLSchema] = None,
    **kwargs
) -> Any:
    """Generate a GraphQL Mutation operation with output based on server-side introspection.

    Parameters
    ----------
    service : GraphQLService
    endpoint : str
    schema : Optional[GraphQLSchema], optional
        If not provided, the latest schema will be retrieved from the GQL endpoint. By default, None.
        Useful when the schmea is not on the core service, but is on a child service (e.g. EventService) that shares the same GQL endpoint.
    Returns
    -------
    Any
        Usually a dict or list of dicts, depending on the query.
    """
    # retreive the latest schema from the GQL endpoint
    if schema is None:
        schema = service.core.schema
    # parse the correct output fields for the desired query from the schema
    field = schema.mutation_type.fields.get(endpoint)

    output = build_output_string_from_introspection(field)

    results = service.core.execute_query(
        endpoint=endpoint,
        variables={key: prepare_input(value) for key, value in kwargs.items()},
        output=output,
    )

    return results.get(endpoint)


def introspection_subscription(
    service: GraphQLService,
    endpoint: str,
    schema: Optional[GraphQLSchema] = None,
    **kwargs
) -> Any:
    """Generate a GraphQL Subscription operation with output based on server-side introspection.

    Parameters
    ----------
    service : GraphQLService
    endpoint : str
    schema : Optional[GraphQLSchema], optional
        If not provided, the latest schema will be retrieved from the GQL endpoint. By default, None.
        Useful when the schmea is not on the core service, but is on a child service (e.g. EventService) that shares the same GQL endpoint.
    Returns
    -------
    Any
        Usually a dict or list of dicts, depending on the query.
    """
    # retreive the latest schema from the GQL endpoint
    if schema is None:
        schema = service.core.schema
    # parse the correct output fields for the desired query from the schema
    field = schema.subscription_type.fields.get(endpoint)

    output = build_output_string_from_introspection(field)

    results = service.core.execute_query(
        endpoint=endpoint,
        variables={key: prepare_input(value) for key, value in kwargs.items()},
        output=output,
    )

    return results.get(endpoint)
