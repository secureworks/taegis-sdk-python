"""errors.py

Taegis Python SDK Exception class definitions.
"""
from typing import List, Optional


class ServiceCoreException(Exception):
    """Base class for all tool errors."""

    def __init__(
        self,
        message: str,
        comments: Optional[List[str]] = None,
        nested_exception: Optional[BaseException] = None,
    ):
        """ServiceCoreException initialization.

        Parameters
        ----------
        message : str
            Error message
        comments : List[str], optional
            Error comments, by default None
        nested_exception : BaseException, optional
            Exception thrown by Python or other library, by default None
        """
        # Call the base class constructor with the parameters it needs
        super().__init__(message, comments, nested_exception)
        self.message = message
        self.comments = comments or []
        self.nested_exception = nested_exception

    def __str__(self) -> str:
        """Display the string representation of the exception.

        Returns
        -------
        str
            Formatted error message.
        """
        message = self.message
        if self.nested_exception:
            exc = self.nested_exception.__class__.__name__
            message += f"\nnested exception: [{exc} -> {str(self.nested_exception)}]"
        if self.comments:
            joined = "\n".join(self.comments)
            message += f"\ncomments:\n{joined}"
        return message


class InvalidAuthenticationMethod(ServiceCoreException):
    """Error raises if no authenication mechanism can be determined."""


class AccessTokenException(ServiceCoreException):
    """Error raises if access token issues."""


class MissingAccessTokenError(AccessTokenException):
    """Error raises if the access token was not found (when testing endpoint)."""


class InvalidAccessTokenError(AccessTokenException):
    """Error raises if the access token is invalid."""


class GraphQLNoRowsInResultSetError(ServiceCoreException):
    """Error raises when the provided GraphQL return no rows."""


class InvalidAccessTokenClaims(ServiceCoreException):
    """Error raises when access token claims cannot be parsed."""


class InvalidGraphQLEndpoint(ServiceCoreException):
    """Error raises when a GraphQL endpoint is not found."""


__all__ = [  # pylint: disable=duplicate-code
    "ServiceCoreException",
    "InvalidAuthenticationMethod",
    "AccessTokenException",
    "MissingAccessTokenError",
    "InvalidAccessTokenError",
    "GraphQLNoRowsInResultSetError",
    "InvalidAccessTokenClaims",
    "InvalidGraphQLEndpoint",
]
