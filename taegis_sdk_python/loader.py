import logging

import gql
import graphql
from requests.adapters import ConnectTimeout

from taegis_sdk_python.errors import ServiceCoreException


class SchemaLoader:
    """
    Represents a GraphQL Schema loaded from a string, file or endpoint
    """

    @classmethod
    def from_endpoint(
            cls, url: str, access_token: str
    ) -> graphql.GraphQLSchema:
        """
        get the graphql schema from endpoint
        :param url: the endpoint url
        :param access_token: the access token
        :return: a graphqk schema or exception
        """
        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        logging.getLogger("chardet").setLevel(logging.WARNING)
        from gql.transport.requests import RequestsHTTPTransport
        transport = RequestsHTTPTransport(
            url=url,
            headers=headers,
            timeout=1,
            retries=2
        )
        try:
            client = gql.Client(
                execute_timeout=1,
                fetch_schema_from_transport=True,
                transport=transport
            )
            return client.schema
        except graphql.GraphQLError as e:
            raise ServiceCoreException(
                "GraphQLError: Could not get introspection_query",
                nested_exception=e
            )
        except TypeError as e:
            raise ServiceCoreException(
                "Could not get introspection_query for graphql schema",
                nested_exception=e
            )
        except ServiceCoreException:
            raise
        except ConnectTimeout as e:
            raise ServiceCoreException(
                "Could not get GraphQL schema",
                nested_exception=e,
                comments=["1. Check your connection"]
            )
        except BaseException as e:
            raise ServiceCoreException(
                "BaseException: Unknow error while getting introspection_query",
                nested_exception=e
            )
