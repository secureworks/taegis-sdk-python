"""EndpointCommandManager Types and Enums."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum, parse_union_result


class HashType(str, Enum):
    """HashType."""

    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SHA512 = "SHA512"


class FetchRequestPathTypeEnum(str, Enum):
    """FetchRequestPathTypeEnum."""

    FILE = "FILE"
    DIAGNOSTICS = "DIAGNOSTICS"


class FetchRequestReasonCodeEnum(str, Enum):
    """FetchRequestReasonCodeEnum."""

    REASONCODE_UNSPECIFIED = "REASONCODE_UNSPECIFIED"
    POSSIBLY_MALICIOUS = "POSSIBLY_MALICIOUS"
    TROUBLESHOOTING = "TROUBLESHOOTING"


class StatusEnum(str, Enum):
    """StatusEnum."""

    ISSUED = "ISSUED"
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    FAILED = "FAILED"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class Result:
    """Result."""

    success: Optional[bool] = field(default=None, metadata=config(field_name="Success"))
    reason: Optional[str] = field(default=None, metadata=config(field_name="Reason"))
    request_id: Optional[str] = field(
        default=None, metadata=config(field_name="requestID")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CommandRequestInput:
    """CommandRequestInput."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )
    reason: Optional[str] = field(default=None, metadata=config(field_name="reason"))
    request_id: Optional[str] = field(
        default=None, metadata=config(field_name="requestID")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class BlockUserCommandInput:
    """BlockUserCommandInput."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )
    reason: Optional[str] = field(default=None, metadata=config(field_name="reason"))
    user_principal_name: Optional[str] = field(
        default=None, metadata=config(field_name="userPrincipalName")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UninstallStateArguments:
    """UninstallStateArguments."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserInfo:
    """UserInfo."""

    family_name: Optional[str] = field(
        default=None, metadata=config(field_name="FamilyName")
    )
    given_name: Optional[str] = field(
        default=None, metadata=config(field_name="GivenName")
    )
    email: Optional[str] = field(default=None, metadata=config(field_name="Email"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class HistoryPartialPageInfo:
    """HistoryPartialPageInfo."""

    has_next_page: Optional[bool] = field(
        default=None, metadata=config(field_name="hasNextPage")
    )
    end_cursor: Optional[str] = field(
        default=None, metadata=config(field_name="endCursor")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CommandHistoryArguments:
    """CommandHistoryArguments."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CommandHistoryPagedArguments:
    """CommandHistoryPagedArguments."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )
    first: Optional[int] = field(default=None, metadata=config(field_name="first"))
    after: Optional[str] = field(default=None, metadata=config(field_name="after"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CreateIsolationExclusionRuleArguments:
    """CreateIsolationExclusionRuleArguments."""

    name: Optional[str] = field(default=None, metadata=config(field_name="Name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="Description")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="Type"))
    values: Optional[List[str]] = field(
        default=None, metadata=config(field_name="Values")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateIsolationExclusionRuleArguments:
    """UpdateIsolationExclusionRuleArguments."""

    rule_id: Optional[str] = field(default=None, metadata=config(field_name="RuleID"))
    name: Optional[str] = field(default=None, metadata=config(field_name="Name"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="Description")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="Type"))
    values: Optional[List[str]] = field(
        default=None, metadata=config(field_name="Values")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsolationExclusionRuleResult:
    """IsolationExclusionRuleResult."""

    rule_id: Optional[str] = field(default=None, metadata=config(field_name="RuleID"))
    success: Optional[bool] = field(default=None, metadata=config(field_name="Success"))
    reason: Optional[str] = field(default=None, metadata=config(field_name="Reason"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class QuarantinedFileCommandInput:
    """QuarantinedFileCommandInput."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="EndpointID")
    )
    file_id: Optional[str] = field(default=None, metadata=config(field_name="FileID"))
    file_path: Optional[str] = field(
        default=None, metadata=config(field_name="FilePath")
    )
    reason: Optional[str] = field(default=None, metadata=config(field_name="Reason"))
    request_id: Optional[str] = field(
        default=None, metadata=config(field_name="RequestID")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class HashAndType:
    """HashAndType."""

    value: Optional[str] = field(default=None, metadata=config(field_name="Value"))
    type: Optional[Union[HashType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(HashType, x),
            field_name="Type",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class IsolationExclusionRule:
    """IsolationExclusionRule."""

    name: Optional[str] = field(default=None, metadata=config(field_name="Name"))
    rule_id: Optional[str] = field(default=None, metadata=config(field_name="RuleID"))
    create_time: Optional[str] = field(
        default=None, metadata=config(field_name="CreateTime")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="Description")
    )
    type: Optional[str] = field(default=None, metadata=config(field_name="Type"))
    values: Optional[List[str]] = field(
        default=None, metadata=config(field_name="Values")
    )
    user_id: Optional[str] = field(default=None, metadata=config(field_name="UserID"))
    user: Optional[UserInfo] = field(default=None, metadata=config(field_name="User"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class CommandHistoryInput:
    """CommandHistoryInput."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="EndpointID")
    )
    request_id: Optional[str] = field(
        default=None, metadata=config(field_name="RequestID")
    )
    command: Optional[str] = field(default=None, metadata=config(field_name="Command"))
    issued_at: Optional[str] = field(
        default=None, metadata=config(field_name="IssuedAt")
    )
    response_at: Optional[str] = field(
        default=None, metadata=config(field_name="ResponseAt")
    )
    success: Optional[bool] = field(default=None, metadata=config(field_name="Success"))
    request_reason: Optional[str] = field(
        default=None, metadata=config(field_name="RequestReason")
    )
    failure_reason: Optional[str] = field(
        default=None, metadata=config(field_name="FailureReason")
    )
    status: Optional[Union[StatusEnum, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(StatusEnum, x),
            field_name="Status",
        ),
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class HistoryEntry:
    """HistoryEntry."""

    command: Optional[str] = field(default=None, metadata=config(field_name="Command"))
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="UpdatedAt")
    )
    issued_at: Optional[str] = field(
        default=None, metadata=config(field_name="IssuedAt")
    )
    response_at: Optional[str] = field(
        default=None, metadata=config(field_name="ResponseAt")
    )
    success: Optional[bool] = field(default=None, metadata=config(field_name="Success"))
    user_id: Optional[str] = field(default=None, metadata=config(field_name="UserID"))
    request_reason: Optional[str] = field(
        default=None, metadata=config(field_name="RequestReason")
    )
    failure_reason: Optional[str] = field(
        default=None, metadata=config(field_name="FailureReason")
    )
    status: Optional[Union[StatusEnum, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(StatusEnum, x),
            field_name="Status",
        ),
    )
    user: Optional[UserInfo] = field(default=None, metadata=config(field_name="User"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class HistoryPagedOutput:
    """HistoryPagedOutput."""

    history: Optional[List[HistoryEntry]] = field(
        default=None, metadata=config(field_name="history")
    )
    partial_page_info: Optional[HistoryPartialPageInfo] = field(
        default=None, metadata=config(field_name="partialPageInfo")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class FetchRequestInput:
    """FetchRequestInput."""

    endpoint_id: Optional[str] = field(
        default=None, metadata=config(field_name="endpointID")
    )
    reason: Optional[str] = field(default=None, metadata=config(field_name="reason"))
    path: Optional[str] = field(default=None, metadata=config(field_name="path"))
    path_type: Optional[Union[FetchRequestPathTypeEnum, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(FetchRequestPathTypeEnum, x),
            field_name="pathType",
        ),
    )
    reason_code: Optional[Union[FetchRequestReasonCodeEnum, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(FetchRequestReasonCodeEnum, x),
            field_name="reasonCode",
        ),
    )
    hash_and_type: Optional[HashAndType] = field(
        default=None, metadata=config(field_name="hashAndType")
    )
