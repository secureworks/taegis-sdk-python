"""service_core.py

Taegis ServiceCore manager.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.websockets import WebsocketsTransport
from graphql import GraphQLError, GraphQLField, GraphQLSchema
from taegis_sdk_python._version import __version__
from taegis_sdk_python.errors import InvalidGraphQLEndpoint
from taegis_sdk_python.utils import async_block, prepare_variables, remove_node

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services import GraphQLService


log = logging.getLogger(__name__)


class SchemaCache:
    """GraphQL Schema Cache."""

    def __init__(self, schema: Optional[GraphQLSchema] = None, expires: int = 5):
        """Initialize SchemaCache.

        Parameters
        ----------
        schema : Optional[GraphQLSchema], optional
            GraphQL schema object, by default None
        expires : int, optional
            Schema expires in minutes, by default 5
        """
        self._schema = schema
        self._inserted_at = datetime.now()
        self.expires = expires

    @property
    def schema(self) -> Union[GraphQLSchema, None]:
        """Return GraphQLSchema if it exists and is not expired.

        Returns
        -------
        Union[GraphQLSchema, None]
            GraphQL Schema
        """
        if self._inserted_at + timedelta(minutes=self.expires) < datetime.now():
            self.schema = None
        return self._schema

    @schema.setter
    def schema(self, schema: Optional[GraphQLSchema]):
        """Set schema and update inserted_at.

        Parameters
        ----------
        schema :
            _description_
        """
        if self._schema is not schema:
            self._schema = schema
            self._inserted_at = datetime.now()

    def should_fetch_schema(self) -> bool:
        """Return True if schema is should be fetched in transport.

        Returns
        -------
        bool
            True if schema is should be fetched in transport.
        """
        return not self.schema


class ServiceCore:
    """Taegis GraphQL Service core functionality."""

    def __init__(self, service: GraphQLService):
        self.service = service

        self._urls = self.service._environments
        self._gateway = self.service._gateway
        self._input_value_deprecation = True

        self._schema = SchemaCache(schema=None, expires=self.service.schema_expiry)

        self._queries = None
        self._mutations = None
        self._subscriptions = None

    @property
    def sync_url(self) -> str:
        """Syncronous URL."""
        return self.service.url or self._urls.get(self.service.environment)

    @property
    def wss_url(self) -> str:
        """WebSockets URL."""
        return self.sync_url.replace("https", "wss")

    @property
    def gateway(self) -> str:
        """GraphQL Gateway"""
        return self.service.gateway or self._gateway

    @property
    def query(self):  # pragma: no cover
        """Service Query calls."""
        raise NotImplementedError

    @property
    def mutation(self):  # pragma: no cover
        """Service Mutation calls."""
        raise NotImplementedError

    @property
    def subscription(self):  # pragma: no cover
        """Service Subscription calls."""
        raise NotImplementedError

    @property
    def sync_client(self) -> Client:
        """GraphQL Synchronous Transport with Client."""
        transport = RequestsHTTPTransport(
            f"{self.sync_url}{self.gateway}",
            headers=self.service.headers,
        )

        client = Client(
            transport=transport,
            schema=self._schema.schema,
            fetch_schema_from_transport=self._schema.should_fetch_schema(),
            introspection_args={
                "input_value_deprecation": (
                    bool(self.service.input_value_deprecation)
                    if self.service.input_value_deprecation is not None
                    else self._input_value_deprecation
                )
            },
        )

        with client:
            self._schema.schema = client.schema

        return client

    @property
    def ws_client(self) -> Client:
        """GraphQL WebSockets Transport with Client."""
        subprotocols = [
            "graphql-ws",
            f"access-token-{self.service.access_token}",
        ]

        # we cannot build the async client and use it to fetch the schema
        # due to async issues with the transport.  This will grab the schema
        # from a sync client and use it to build the async client.
        if not self._schema.schema:
            self.sync_client  # pylint: disable=pointless-statement

        if self.service.tenant_id:
            subprotocols.append(f"x-tenant-context-{self.service.tenant_id}")

        transport = WebsocketsTransport(
            f"{self.wss_url}{self.gateway}",
            headers=self.service.headers,
            subprotocols=subprotocols,
            connect_args={"max_size": None},
        )

        client = Client(
            transport=transport,
            schema=self._schema.schema,
            fetch_schema_from_transport=self._schema.should_fetch_schema(),
            introspection_args={
                "input_value_deprecation": (
                    bool(self.service.input_value_deprecation)
                    if self.service.input_value_deprecation is not None
                    else self._input_value_deprecation
                )
            },
        )

        return client

    @property
    def schema(self) -> GraphQLSchema:
        """Retrieves introspection schema from Synchronous endpoint.

        Returns
        -------
        GraphQLSchema
        """
        if not self._schema.schema:
            self.sync_client  # pylint: disable=pointless-statement
        return self._schema.schema

    def clear_schema(self):
        """Clears the introspection schema."""
        self._schema.schema = None

    def get_sync_schema(self) -> Union[GraphQLSchema, None]:
        """Retrieves introspection schema from Synchronous endpoint.

        Returns
        -------
        GraphQLSchema
        """
        client = self.sync_client
        with client:
            schema = client.schema
        return schema

    @async_block
    async def get_ws_schema(self) -> Union[GraphQLSchema, None]:
        """Retrieves introspection schema from WebSockets endpoint.

        Returns
        -------
        GraphQLSchema
        """
        client = self.ws_client
        async with client:
            schema = client.schema
        return schema

    def execute_query(
        self, endpoint: str, output: str, variables: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Execute a GraphQL Query."""
        operation_type = "query"
        graphql_field = self.get_sync_schema().query_type.fields.get(endpoint)
        if not graphql_field:
            raise InvalidGraphQLEndpoint(message=f"{endpoint} not found in schema")

        if self.service.output:
            query_string = self._build_output_query(
                operation_type=operation_type,
                endpoint=endpoint,
                graphql_field=graphql_field,
                output=self.service.output,
            )
        else:
            query_string = self._build_validated_query(
                operation_type=operation_type,
                endpoint=endpoint,
                graphql_field=graphql_field,
                output=output,
            )

        return self.execute(query_string, variables)

    def execute_mutation(
        self, endpoint: str, output: str, variables: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Execute a GraphQL Mutation."""
        operation_type = "mutation"
        graphql_field = self.get_sync_schema().mutation_type.fields.get(endpoint)
        if not graphql_field:
            raise InvalidGraphQLEndpoint(message=f"{endpoint} not found in schema")

        if self.service.output:
            query_string = self._build_output_query(
                operation_type=operation_type,
                endpoint=endpoint,
                graphql_field=graphql_field,
                output=self.service.output,
            )
        else:
            query_string = self._build_validated_query(
                operation_type=operation_type,
                endpoint=endpoint,
                graphql_field=graphql_field,
                output=output,
            )

        return self.execute(query_string, variables)

    def execute_subscription(
        self, endpoint: str, output: str, variables: Optional[Dict[str, Any]] = None
    ) -> List[Any]:
        """Execute a GraphQL Subscription."""
        operation_type = "subscription"
        graphql_field = self.get_ws_schema().subscription_type.fields.get(endpoint)
        if not graphql_field:
            raise InvalidGraphQLEndpoint(message=f"{endpoint} not found in schema")

        if self.service.output:
            query_string = self._build_output_query(
                operation_type=operation_type,
                endpoint=endpoint,
                graphql_field=graphql_field,
                output=self.service.output,
            )
        else:
            query_string = self._build_validated_query(
                operation_type=operation_type,
                endpoint=endpoint,
                graphql_field=graphql_field,
                output=output,
            )

        return self.subscribe(query_string, variables)

    def execute(
        self, query_string: str, variables: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Execute a syncronous GraphQL string."""
        query = gql(query_string)
        return self.sync_client.execute(
            query,
            variable_values=prepare_variables(variables),
        )

    @async_block
    async def subscribe(
        self, query_string: str, variables: Optional[Dict[str, Any]] = None
    ) -> List[Any]:
        """Execute a subsciption GraphQL string."""
        query = gql(query_string)
        results = []
        async with self.ws_client as session:
            async for result in session.subscribe(
                query,
                variable_values=prepare_variables(variables),
            ):
                results.append(result)

        return results[:-1]

    def _build_validated_query(
        self,
        operation_type: str,
        endpoint: str,
        graphql_field: GraphQLField,
        output: str,
    ) -> str:
        """Build a validated output string.  This method is to be used only for default
        generated output strings.  It's purpose is to validate the output string against
        the introspected schema.  The primary purpose of this is remove invalid fields from
        generated graphql output strings where they may differ from the intended release.

        Parameters
        ----------
        operation_type : str
            query/mutation/subscription
        endpoint : str
            GraphQL Endpoint
        graphql_field : GraphQLField
            GraphQL Field (from endpoint in schema)
        output : str
            Output string

        Returns
        -------
        str
            GraphQL string
        """
        query_string = self._build_output_query(
            operation_type=operation_type,
            endpoint=endpoint,
            graphql_field=graphql_field,
            output=output,
        )
        query_string = " ".join(query_string.split())

        # open a connection for introspection and download schema
        with self.sync_client as session:
            # if multiple fields are invalid, we want to iterate until the
            # output string is valid
            for _ in range(10000):
                try:
                    session.client.validate(gql(query_string))
                    break

                except GraphQLError as exc:
                    if "Cannot query field" in exc.message:
                        log.warning(
                            f"{self.service.environment} - field {exc.nodes[0].name.value} not found.  Removing from query string..."
                        )
                        query_string = remove_node(
                            query_string, exc.nodes[0], exc.locations[0]
                        )
                    else:
                        raise exc

        return query_string

    @staticmethod
    def _build_output_query(
        operation_type: str,
        endpoint: str,
        graphql_field: GraphQLField,
        output: str,
    ) -> str:
        """Build out a GraphQL string.

        Parameters
        ----------
        operation_type : str
            query/mutation/subscription
        endpoint : str
            GraphQL Endpoint
        graphql_field : GraphQLField
            GraphQL Field (from endpoint in schema)
        output : str
            Output string

        Returns
        -------
        str
            GraphQL string
        """
        if graphql_field.args:
            directives = f"""({
                ', '.join(
                    f'${arg_name}: {arg_def.type}'
                    for arg_name, arg_def in graphql_field.args.items()
                )
            })"""
            definitions = f"""({
                ', '.join(
                    f'{arg_name}: ${arg_name}'
                    for arg_name in graphql_field.args
                )
            })"""
        else:
            directives = ""
            definitions = ""

        if output:
            output = f"""{{
                {output.strip()}
            }}"""

        query_string = f"""{operation_type} {endpoint}{directives}
        {{
            {endpoint}{definitions}
            {output}
        }}"""

        return query_string
