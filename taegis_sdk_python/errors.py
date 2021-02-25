from dataclasses import MISSING
from typing import List


class ServiceCoreException(Exception):
    """
    base class for all tool errors
    """

    def __init__(
            self, message,
            comments: List[str] = None,
            nested_exception: BaseException = None
    ):
        # Call the base class constructor with the parameters it needs
        super().__init__(message, comments, nested_exception)
        self.message = message
        self.comments = comments or []
        self.nested_exception = nested_exception

    def __str__(self):
        message = self.message
        if self.nested_exception:
            exc = self.nested_exception.__class__.__name__
            message += f'{message}\nnested exception: [{exc} -> {str(self.nested_exception)}]'
        if self.comments:
            joined = "\n".join(self.comments)
            return f'{message}\ncomments:\n{joined}'
        return message


class AccessTokenException(ServiceCoreException):
    """
    base class for access token issues
    """
    pass


class MissingAccessTokenError(AccessTokenException):
    """
    error raises if the access token was not found ( when testing endpoint )
    """
    pass


class InvalidAccessTokenError(ServiceCoreException):
    """
    error raises if the access token is invalid
    """
    pass


class GraphQLNoRowsInResultSetError(ServiceCoreException):
    """
    Exception raised when the provided GraphQL return no rows.
    """
