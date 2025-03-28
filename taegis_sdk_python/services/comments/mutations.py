"""Comments Mutation."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.comments.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.comments import CommentsService

log = logging.getLogger(__name__)


class TaegisSDKCommentsMutation:
    """Taegis Comments Mutation operations."""

    def __init__(self, service: CommentsService):
        self.service = service

    def mark_comment_read(self, comment_id: str) -> Comment:
        """None."""
        endpoint = "markCommentRead"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'use investigation-v2 comments queries'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "comment_id": prepare_input(comment_id),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation markCommentRead")

    def mark_parent_comments_read(self, parents: List[Parent]) -> List[Comment]:
        """None."""
        endpoint = "markParentCommentsRead"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'use investigation-v2 comments queries'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "parents": prepare_input(parents),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation markParentCommentsRead")

    def create_comment(self, comment: CommentInput) -> Comment:
        """None."""
        endpoint = "createComment"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'use investigation-v2 comments queries'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "comment": prepare_input(comment),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createComment")

    def update_comment(self, comment_id: str, comment: CommentUpdate) -> Comment:
        """None."""
        endpoint = "updateComment"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'use investigation-v2 comments queries'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "comment_id": prepare_input(comment_id),
                "comment": prepare_input(comment),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateComment")

    def delete_comment(self, comment_id: str) -> Comment:
        """None."""
        endpoint = "deleteComment"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'use investigation-v2 comments queries'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "comment_id": prepare_input(comment_id),
            },
            output=build_output_string(Comment),
        )
        if result.get(endpoint) is not None:
            return Comment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteComment")

    def bulk_restore_comments(self, ids: List[str]) -> List[str]:
        """None."""
        endpoint = "bulkRestoreComments"

        log.warning(
            f"GraphQL Mutation `{endpoint}` is deprecated: 'use investigation-v2 comments queries'"
        )

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation bulkRestoreComments")
