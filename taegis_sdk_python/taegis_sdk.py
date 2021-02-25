import collections
import os
import pprint
import re
from dataclasses import field, MISSING
from datetime import timedelta
from timeit import default_timer as timer
from typing import (
    Any, Callable, cast, Dict, List, Optional, Tuple, Type, Union
)

import gql
import graphql

from taegis_sdk_python.errors import ServiceCoreException
from taegis_sdk_python.history import ExecutionHistory
from taegis_sdk_python.loader import SchemaLoader
from taegis_sdk_python.utils import duration_string, get_token


def _get_args_query(schema: graphql.GraphQLSchema, field_name: str) -> dict:
    formatted_fields = []
    enums = []
    names = []

    graphql_field = schema.query_type.fields.get(field_name, None)
    if graphql_field is None:
        graphql_field = schema.mutation_type.fields.get(field_name, None)
    if not graphql_field:
        raise graphql.GraphQLError(f"Could not find a graphql definition for '{field_name}'")

    for key, value in graphql_field.args.items():
        value_named_type = graphql.get_named_type(value.type)
        if graphql.is_scalar_type(value_named_type):
            formatted_fields.append(f"{key}: ${key}")
            names.append(key)
        elif graphql.is_enum_type(value_named_type):
            formatted_fields.append(f"{key}: ${key}")
            enums.append(key)
            names.append(key)
        elif graphql.is_input_type(value_named_type):
            sub_formatted_fields = []
            object_type = graphql.assert_input_object_type(value_named_type)
            for k, v in object_type.fields.items():
                value_named_type = graphql.get_named_type(v.type)
                if graphql.is_scalar_type(value_named_type):
                    sub_formatted_fields.append(f"{k}: ${k}")
                    names.append(k)
                elif graphql.is_enum_type(value_named_type):
                    sub_formatted_fields.append(f"{k}: ${k}")
                    enums.append(k)
                    names.append(k)
                else:
                    NotImplementedError("for {0.name}".format(value_named_type))
            copy = sub_formatted_fields.copy()
            # formatted_fields.clear()
            formatted_fields.append(f"{key}: {{ {', '.join(copy)} }}")
        else:
            type_name = graphql.get_named_type(value.type).name
            raise ServiceCoreException("Unhandled type {}".format(type_name))
    return dict(formatted_fields=formatted_fields, names=names, enums=enums)


def _get_type_query(schema: graphql.GraphQLSchema, type_name: str) -> Optional[List[str]]:
    fields = []
    named_type = schema.get_type(type_name)
    if not named_type:
        raise graphql.GraphQLError(f"Could not find definition type for '{type_name}'")
    if graphql.is_scalar_type(named_type):
        return None
    if graphql.is_object_type(named_type):
        object_type = graphql.assert_object_type(named_type)
        for key, value in object_type.fields.items():
            # --- Determine type of field
            value_named_type = graphql.get_named_type(value.type)
            if graphql.is_scalar_type(value_named_type):
                fields.append(key)
            elif graphql.is_enum_type(value_named_type):
                fields.append(key)
            elif graphql.is_object_type(value_named_type):
                sub_fields = _get_type_query(schema, value_named_type.name)
                sub_fields_str = " ".join(sub_fields)
                fields.append(f"{key} {{ {sub_fields_str} }}")
            else:
                pass
    else:
        pass

    return fields


class ServiceCore:
    _FILTER_KEYS: Dict[str, Tuple[str, ...]] = {
        "document": ("definitions",),
        "operation_definition": (
            "selection_set",
        ),
        "selection_set": ("selections",),
        "field": ("name", "selection_set"),
    }

    def __init__(self, access_token: str):
        """
        Initializes the service.
        1. get the access token based on CLIENT_ID and CLIENT_SECRET
        2. sets the base environment variable SERVICE_URL endpoint
        3. initialized the history queue
        """
        self._access_token = access_token
        self._history = collections.deque(maxlen=20)
        self._schema: graphql.GraphQLSchema = MISSING
        self._localstorage = None
        self._contextstorage = None
        self._transport = None
        self._query_type = "query"
        self._required_query_output: Optional[str] = None
        self._service_endpoint: Optional[str] = None
        self._caller: Optional[str] = None

    def __update(self, kwargs: dict):
        self._contextstorage = self._LocalStorage({})
        if "output" in kwargs:
            self._required_query_output = kwargs.get("output")

    def __clear(self):
        self._contextstorage.clear()
        self._required_query_output = None

    def __enter__(self):
        self._contextstorage = self._LocalStorage({})
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__clear()

    def __call__(self, *args, **kwargs):
        self.__update(kwargs)
        return self

    def print_schema(self, to_file: Optional[str] = None):
        output = graphql.print_schema(self._schema)

        def get_indexed_graphql_file(file_path: str):
            if not os.path.exists(file_path):
                return file_path

            filename, file_extension = os.path.splitext(file_path)
            counter = 1
            new_filename = "{}_{}{}".format(filename, counter, file_extension)
            while os.path.exists(new_filename):
                counter += 1
                new_filename = "{}_{}{}".format(filename, counter, file_extension)
            return new_filename

            while os.path.exists(file_path):
                file_path = file_path.replace("")

        if to_file:
            file = get_indexed_graphql_file(to_file)
            with open(file, 'w') as f:
                f.write(output)
                f.close()

    def execute_gql_query(
            self, gql_name: str, **kwargs
    ) -> Union[dict, list, int]:
        """
        Executing query with a query name
        :param gql_name: the query name to execute
        :param kwargs: additional query arguments
        """
        self._query_type = "query"
        data = self._exec(gql_name, kwargs)
        return data

    def execute_gql_mutation(
            self, gql_name: str, **kwargs
    ) -> Union[dict, list, int]:
        """
        Executing mutation with a query name
        :param gql_name: the mutation name to execute
        :param kwargs: additional mutation arguments
        """
        self._query_type = "mutation"
        data = self._exec(gql_name, kwargs)
        return data

    def execute_gql_string(
            self, gql_string: str
    ) -> dict:
        """
        Executes a custom query string
        :param gql_string: the valid custom graphql query
        """
        try:
            document_node = graphql.parse(gql_string)
            if self._schema is MISSING:
                self._service_endpoint = os.getenv("SERVICE_URL") + "/graphql"
                self._load_schema()
            returned_errors = graphql.validation.validate(
                schema=self._schema,
                document_ast=document_node
            )
            if returned_errors:
                formatted_error_list = list(map(lambda x: str(x.formatted), returned_errors))
                print("ERROR: failed to validate query string against schema.")
                for error in formatted_error_list:
                    print(pprint.pformat(error, indent=4, compact=True).replace("\\", ""))
                e = ServiceCoreException(
                    f"failed to validate query string against schema"
                )
                print(str(e))
                raise e

            return self._send_gql_query(gql_string)

        except graphql.GraphQLSyntaxError as e:
            raise ServiceCoreException(
                "Failed to parse provided string",
                nested_exception=e
            )

        except BaseException as e:
            raise ServiceCoreException(
                "Failed to parse provided string",
                nested_exception=e
            )

    class _FilterVisitor(graphql.language.printer.PrintAstVisitor):
        """
        This class uses the PrintAstVisitor to determine the response
        structure and able to filter it
        """

        def __init__(self, filter_keys: dict):
            self.filter_keys = filter_keys

        def leave_field(self, node: graphql.language.printer.PrintedNode, *_args: Any) -> str:
            j = graphql.language.printer.join(
                (
                    graphql.language.printer.wrap("", node.alias, ": ")
                    + node.name
                    + graphql.language.printer.wrap(
                        "(", graphql.language.printer.join(node.arguments, ", "), ")"
                    ),
                    node.selection_set,
                ),
                " ",
            )
            if node.name in self.filter_keys and node.selection_set:
                return f"{node.name} {{ {self.filter_keys.get(node.name)} }}"
            else:
                return (
                    graphql.language.printer.join(
                        (
                            graphql.language.printer.wrap("", node.alias, ": ")
                            + node.name
                            + graphql.language.printer.wrap(
                                "(", graphql.language.printer.join(node.arguments, ", "), ")"
                            ),
                            node.selection_set,
                        ),
                        " ",
                    )
                )

    class _LocalStorage(dict):
        def get_as(
                self, convert: Callable, name: str, default: Any = None, value_type: Type = None
        ) -> Any:
            if value_type is None:
                value_type = convert

            value = self.get(name, MISSING)
            if value is MISSING:
                return default
            elif isinstance(value, value_type):
                return value
            else:
                assert callable(convert)
                return convert(value)

        def get_int(self, name, default=0):
            return self.get_as(int, name, default)

        def get_float(self, name, default=0.0):
            return self.get_as(float, name, default)

        def get_bool(self, name, default=False):
            """
            return s bool type from a storage value
            :param name: the argument name
            :param default: the argument default value, in case is missing
            """
            return self.get_as(self.parse_bool, name, default, value_type=bool)

        @staticmethod
        def parse_bool(text: str):
            from distutils.util import strtobool
            return bool(strtobool(text))

    @property
    def schema(self) -> graphql.GraphQLSchema:
        """
        The current schema the framework is working with
        """
        return self._schema

    @property
    def history(self) -> collections.deque:
        return self._history

    @property
    def last_history_item(self) -> ExecutionHistory:
        """
        :return: The last history item on the execution history queue
        """
        return self._history[-1]

    @property
    def localstorage(self) -> _LocalStorage:
        """
        :return: the local storage object for cross test/query execution
        """
        if self._localstorage is None:
            self._localstorage = self._LocalStorage({})
        return self._localstorage

    @property
    def service_endpoint(self) -> str:
        return self._service_endpoint

    @service_endpoint.setter
    def service_endpoint(self, endpoint: str):
        self._service_endpoint = os.getenv("SERVICE_URL") + endpoint

    @property
    def caller(self):
        return self._caller

    @caller.setter
    def caller(self, caller: str):
        self._caller = caller

    def _exec(self, gql_name: str, query_arguments: dict):
        start = timer()
        try:
            # -- STEP: validates that the query or mutation name does exists in the schema
            if self._query_type == "query":
                graphql_field = self._validate_query_name(gql_name)
            else:
                graphql_field = self._validate_mutation_name(gql_name)
        except ServiceCoreException as e:
            raise e

        # --- STEP: read the schema and creates a query string
        query_string = self._get_query_string(
            graphql_field, gql_name, query_arguments
        )

        pretty_query = (
            graphql.visit(
                graphql.parse(query_string),
                graphql.language.printer.PrintAstVisitor()
            )
        )
        history_item = self._append_history(gql_name, query_arguments, pretty_query)
        if self._caller:
            history_item.function_name = self._caller
        # --- STEP: finally, sending the query to graphql endpoint
        response = self._send_gql_query(query_string)
        # --- STEP: if no errors sending the query, collecting info for execution history
        # -- takes the response data part
        data = response.get(gql_name)
        end = timer()
        t_delta = timedelta(seconds=end - start)
        history_item.duration = duration_string(t_delta)
        return data

    def _validate_query_name(
            self, gql_name: str
    ) -> graphql.GraphQLField:
        if self.schema is MISSING:
            self._load_schema()

        # -- schema should be loaded at this point, otherwise raise exception
        if self.schema is None:
            raise ServiceCoreException("Schema was not loaded!")

        # -- searching the query name on the schema
        schema_field = self.schema.query_type.fields.get(gql_name, None)
        if schema_field:
            return schema_field
        print("ERROR: No such query with name: '%s'", gql_name)
        raise ServiceCoreException("No such query with name: '{}'".format(gql_name))

    def _validate_mutation_name(
            self, gql_name: str
    ) -> graphql.GraphQLField:
        if self.schema is MISSING:
            self._load_schema()

        # -- schema should be loaded at this point, otherwise raise exception
        if self.schema is MISSING:
            raise ServiceCoreException("Schema was not loaded!")

        schema_field = self.schema.mutation_type.fields.get(gql_name, None)
        if schema_field:
            return schema_field
        print("ERROR: No such mutation with name: '%s'", gql_name)
        raise ServiceCoreException("No such mutation with name: '{}'".format(gql_name))

    def _load_schema(self) -> None:
        assert self._service_endpoint is not None, "No service enpoint url was defined"
        self._schema = SchemaLoader.from_endpoint(self._service_endpoint, self._access_token)

    def _append_history(
            self, gql_name: str, args: dict, last_query: str
    ) -> ExecutionHistory:
        history_item = ExecutionHistory(
            query_name=gql_name,
            query_type=self._query_type,
            endpoint=self._service_endpoint,
            query_arguments=args,
            pretty_query=last_query,
        )
        self._history.append(history_item)
        return history_item

    def _get_query_string(
            self, graphql_field: graphql.GraphQLField,
            field_name: str,
            query_arguments: dict
    ) -> str:
        if self.schema and graphql_field:
            out_type = cast(graphql.GraphQLOutputType, graphql_field.type)
            out_type_name = graphql.get_named_type(out_type)
            if self.schema:
                return self._build_query_string(
                    graphql_field=graphql_field,
                    gql_field_name=field_name,
                    query_arguments=query_arguments
                )
            else:
                raise ServiceCoreException("missing schema")

    def _build_query_string(
            self, graphql_field: graphql.GraphQLField,
            gql_field_name: str,
            query_arguments: dict
    ) -> str:
        if self.schema and field:
            mutation_str = "mutation" if self._query_type == "mutation" else ""
            query_output_str = self._build_output_type_string(graphql_field, gql_field_name)
            if self._required_query_output:
                query_output_str = self._required_query_output
            try:
                query_arguments_map = _get_args_query(self._schema, gql_field_name)
                query_enums = query_arguments_map.get("enums")
                formatted_query_arguments = ", ".join(query_arguments_map.get("formatted_fields"))
                all_query_arguments_names = query_arguments_map.get("names")

                args = f'( {formatted_query_arguments} )' if formatted_query_arguments else ''
                if query_output_str is None:
                    resp = ''
                elif query_output_str.startswith("{") and query_output_str.endswith("}"):
                    resp = f'{query_output_str}' if query_output_str else ''
                else:
                    resp = f'{{ {query_output_str} }}' if query_output_str else ''
                query_template = f'{mutation_str}{{ {gql_field_name}{args} {resp} }}'
                # -- STEP: Correlating arguments with template
                query_arguments = (
                    self._transform_query_arguments(
                        query_arguments, all_query_arguments_names
                    )
                )
                query_string = self._correlate_arguments(
                    query_template,
                    enums=query_enums,
                    all_names=all_query_arguments_names,
                    query_arguments=query_arguments
                )
                return query_string

            except graphql.GraphQLError as e:
                raise ServiceCoreException(
                    f"Error while parsing field arguments for {gql_field_name} -> {e!s}"
                )
            except TypeError as e:
                raise ServiceCoreException(
                    f"Error while validating field {gql_field_name} -> {e!s}"
                )

    def _filter_output_fields(self, output_string: str, filter_fields: dict):

        output_string = f"{{ {output_string} }}"
        output = graphql.visit(
            graphql.parse(output_string),
            self._FilterVisitor(filter_fields),
            visitor_keys=self._FILTER_KEYS
        )
        filtered = (
            output.replace("\n", " ").replace("   ", " ").replace("   ", " ").replace("  ", " ")
        )[2:-3]
        return filtered

    def _build_output_type_string(
            self, graphql_field: graphql.GraphQLField, field_name: str
    ) -> Optional[str]:
        if self.schema and graphql_field:
            named_type = graphql.get_named_type(graphql_field.type).name
            try:
                query_response = _get_type_query(self.schema, named_type)
                if query_response is not None:
                    return ", ".join(query_response)
                else:
                    return None
            except graphql.GraphQLError as e:
                raise ServiceCoreException(
                    f"Error while parsing field for {field_name} -> {e!s}"
                )
            except TypeError as e:
                raise ServiceCoreException(
                    f"Error while validating field {field_name} -> {e!s}"
                )

    def _send_gql_query(self, query: str) -> dict:
        if self.schema and query:
            headers = self._get_tenant_header()
            if not self._transport:
                from gql.transport.requests import RequestsHTTPTransport
                self._transport = RequestsHTTPTransport(
                    url=self._service_endpoint,
                    headers=headers,
                    timeout=60,
                    retries=2
                )
            else:
                self._transport.headers = headers
            client = gql.Client(
                transport=self._transport,
                schema=self._schema
            )
            source = graphql.Source(body=query)
            document_node = graphql.parse(source)
            return client.execute(document_node)

    def _get_tenant_header(self) -> dict:
        return {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self._access_token}"
        }

    def _correlate_arguments(
            self, template: str,
            enums: List[str],
            all_names: List[str],
            query_arguments: dict
    ):
        if not self.schema:
            return
        query = template
        for key, value in query_arguments.items():
            if key in enums:
                temp = value
            elif type(value) == list:
                temp = str(value).replace("'", '"')
            elif type(value) == bool:
                temp = f"{str(value).lower()}"
            elif type(value) == str:
                temp = f'"{value}"'
            elif type(value) == int or type(value) == float or type(value) == bool:
                temp = value
            else:
                temp = None

            pattern = rf'\${key}'
            query = re.sub(pattern, str(temp), query, 1)
        for qa in all_names:
            pattern = rf'{qa}: \${qa},.|{qa}: \${qa}'
            query = re.sub(pattern, "", query, 1)
        query = query.replace(",  )", " )").replace(",  } )", " } )").replace("(  )", "")
        return query

    @staticmethod
    def _transform_query_arguments(q_args: dict, q_all: dict):
        import stringcase
        transformed = {}
        for key, value in q_args.items():
            if key in q_all:
                transformed[key] = value
            else:
                sc = stringcase.snakecase(key)
                if sc in q_all:
                    transformed[sc] = value
        return transformed
