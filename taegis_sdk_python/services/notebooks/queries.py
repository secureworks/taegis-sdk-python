"""Notebooks Query."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import build_output_string, prepare_input
from taegis_sdk_python.services.notebooks.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.notebooks import NotebooksService


class TaegisSDKNotebooksQuery:
    """Teagis Notebooks Query operations."""

    def __init__(self, service: NotebooksService):
        self.service = service

    def notebook(self) -> Notebook:
        """returns a Notebook object for the current user."""
        endpoint = "notebook"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(Notebook)
        )
        if result.get(endpoint) is not None:
            return Notebook.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query notebook")