"""Preferences Types and Enums."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code

# Autogenerated
# DO NOT MODIFY

from dataclasses import dataclass, field

from enum import Enum

from typing import Any, Dict, List, Optional, Tuple, Union

from dataclasses_json import config, dataclass_json


from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.utils import encode_enum, decode_enum


class PreferencesAuthzObject(str, Enum):
    """PreferencesAuthzObject."""

    TENANT_PREFERENCE = "TenantPreference"
    USER_PREFERENCE = "UserPreference"


class PreferencesAuthzAction(str, Enum):
    """PreferencesAuthzAction."""

    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    LIST_ALL = "listAll"
    READ_ADMIN = "readAdmin"
    UPDATE_ADMIN = "updateAdmin"


class TicketingType(str, Enum):
    """TicketingType."""

    DISABLED = "Disabled"
    ZENDESK = "Zendesk"
    SERVICE_NOW = "ServiceNow"


class OptionType(str, Enum):
    """OptionType."""

    DEFAULT = "Default"
    PARTNER = "Partner"


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserPreferenceItem:
    """UserPreferenceItem."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))
    is_disabled_by_entitlement_channel: Optional[str] = field(
        default=None, metadata=config(field_name="is_disabled_by_entitlement_channel")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserPreferenceItemInput:
    """UserPreferenceItemInput."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserNotificationPreferencesArguments:
    """UserNotificationPreferencesArguments."""

    user_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="userIds")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantPreferenceItem:
    """TenantPreferenceItem."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantPreferenceItemInput:
    """TenantPreferenceItemInput."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    value: Optional[str] = field(default=None, metadata=config(field_name="value"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PartnerPreferenceInput:
    """PartnerPreferenceInput."""

    display_name: Optional[str] = field(
        default=None, metadata=config(field_name="displayName")
    )
    support_phone_number: Optional[str] = field(
        default=None, metadata=config(field_name="supportPhoneNumber")
    )
    documentation_link: Optional[str] = field(
        default=None, metadata=config(field_name="documentationLink")
    )
    email_domain: Optional[str] = field(
        default=None, metadata=config(field_name="emailDomain")
    )
    mention: Optional[str] = field(default=None, metadata=config(field_name="mention"))
    faq_link: Optional[str] = field(default=None, metadata=config(field_name="faqLink"))
    mention_email_inbox: Optional[str] = field(
        default=None, metadata=config(field_name="mentionEmailInbox")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ServiceNowConfigurationInput:
    """ServiceNowConfigurationInput."""

    user_name: Optional[str] = field(
        default=None, metadata=config(field_name="userName")
    )
    user_password: Optional[str] = field(
        default=None, metadata=config(field_name="userPassword")
    )
    client_id: Optional[str] = field(
        default=None, metadata=config(field_name="clientID")
    )
    client_secret: Optional[str] = field(
        default=None, metadata=config(field_name="clientSecret")
    )
    custom_user_path: Optional[str] = field(
        default=None, metadata=config(field_name="customUserPath")
    )
    instance_url: Optional[str] = field(
        default=None, metadata=config(field_name="instanceUrl")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class ZendeskConfigurationInput:
    """ZendeskConfigurationInput."""

    signing_key: Optional[str] = field(
        default=None, metadata=config(field_name="signingKey")
    )
    chat_signing_key: Optional[str] = field(
        default=None, metadata=config(field_name="chatSigningKey")
    )
    token_placeholder: Optional[str] = field(
        default=None, metadata=config(field_name="tokenPlaceholder")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class listAllTenantPreferencesInput:
    """listAllTenantPreferencesInput."""

    keys: Optional[List[str]] = field(default=None, metadata=config(field_name="keys"))
    tenant_ids: Optional[List[str]] = field(
        default=None, metadata=config(field_name="tenant_IDs")
    )
    environment: Optional[List[str]] = field(
        default=None, metadata=config(field_name="environment")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserPreferenceInput:
    """UserPreferenceInput."""

    category: Optional[str] = field(
        default=None, metadata=config(field_name="category")
    )
    sub_key: Optional[str] = field(default=None, metadata=config(field_name="subKey"))
    preference_items: Optional[dict] = field(
        default=None, metadata=config(field_name="preferenceItems")
    )
    is_global: Optional[bool] = field(
        default=None, metadata=config(field_name="isGlobal")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class PartnerPreference:
    """PartnerPreference."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    partner_id: Optional[str] = field(
        default=None, metadata=config(field_name="partnerID")
    )
    requested_tenant_partner_id: Optional[str] = field(
        default=None, metadata=config(field_name="requestedTenantPartnerID")
    )
    display_name: Optional[str] = field(
        default=None, metadata=config(field_name="displayName")
    )
    support_phone_number: Optional[str] = field(
        default=None, metadata=config(field_name="supportPhoneNumber")
    )
    documentation_link: Optional[str] = field(
        default=None, metadata=config(field_name="documentationLink")
    )
    email_domain: Optional[str] = field(
        default=None, metadata=config(field_name="emailDomain")
    )
    mention: Optional[str] = field(default=None, metadata=config(field_name="mention"))
    faq_link: Optional[str] = field(default=None, metadata=config(field_name="faqLink"))
    mention_email_inbox: Optional[str] = field(
        default=None, metadata=config(field_name="mentionEmailInbox")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserPreferenceDictionary:
    """UserPreferenceDictionary."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    user_id: Optional[str] = field(
        default=None,
        metadata=config(
            metadata={"deprecated": True, "deprecation_reason": "Use `taegisUserId`"},
            field_name="userID",
        ),
    )
    taegis_user_id: Optional[str] = field(
        default=None, metadata=config(field_name="taegisUserID")
    )
    category: Optional[str] = field(
        default=None, metadata=config(field_name="category")
    )
    sub_key: Optional[str] = field(default=None, metadata=config(field_name="subKey"))
    preferences: Optional[dict] = field(
        default=None, metadata=config(field_name="preferences")
    )
    environment: Optional[str] = field(
        default=None, metadata=config(field_name="environment")
    )
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="createdAt")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updatedAt")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UnsetPreferenceSelector:
    """UnsetPreferenceSelector."""

    category: Optional[str] = field(
        default=None, metadata=config(field_name="category")
    )
    sub_key: Optional[str] = field(default=None, metadata=config(field_name="subKey"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class GetPreferenceSelector:
    """GetPreferenceSelector."""

    category: Optional[str] = field(
        default=None, metadata=config(field_name="category")
    )
    sub_key: Optional[str] = field(default=None, metadata=config(field_name="subKey"))


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateUserNotificationPreferenceInput:
    """UpdateUserNotificationPreferenceInput."""

    user_email: Optional[str] = field(
        default=None, metadata=config(field_name="userEmail")
    )
    global_: Optional[bool] = field(default=None, metadata=config(field_name="global"))
    preferences: Optional[List[UserPreferenceItemInput]] = field(
        default=None, metadata=config(field_name="preferences")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserPreference:
    """UserPreference."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    user_id: Optional[str] = field(
        default=None,
        metadata=config(
            metadata={"deprecated": True, "deprecation_reason": "Use `taegis_user_id`"},
            field_name="user_id",
        ),
    )
    taegis_user_id: Optional[str] = field(
        default=None, metadata=config(field_name="taegis_user_id")
    )
    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    environment: Optional[str] = field(
        default=None, metadata=config(field_name="environment")
    )
    preference_items: Optional[List[UserPreferenceItem]] = field(
        default=None, metadata=config(field_name="preference_items")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserNotificationPreferencesResponse:
    """UserNotificationPreferencesResponse."""

    user_id: Optional[str] = field(
        default=None,
        metadata=config(
            metadata={"deprecated": True, "deprecation_reason": "Use `taegis_user_id`"},
            field_name="user_id",
        ),
    )
    taegis_user_id: Optional[str] = field(
        default=None, metadata=config(field_name="taegis_user_id")
    )
    error: Optional[str] = field(default=None, metadata=config(field_name="error"))
    user_notification_preference: Optional[UserPreference] = field(
        default=None, metadata=config(field_name="user_notification_preference")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NewUserPreferenceInput:
    """NewUserPreferenceInput."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    global_: Optional[bool] = field(default=None, metadata=config(field_name="global"))
    preference_items: Optional[List[UserPreferenceItemInput]] = field(
        default=None, metadata=config(field_name="preference_items")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateUserPreferenceInput:
    """UpdateUserPreferenceInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    global_: Optional[bool] = field(default=None, metadata=config(field_name="global"))
    preference_items: Optional[List[UserPreferenceItemInput]] = field(
        default=None, metadata=config(field_name="preference_items")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TenantPreference:
    """TenantPreference."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    created_at: Optional[str] = field(
        default=None, metadata=config(field_name="created_at")
    )
    updated_at: Optional[str] = field(
        default=None, metadata=config(field_name="updated_at")
    )
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenant_id")
    )
    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    environment: Optional[str] = field(
        default=None, metadata=config(field_name="environment")
    )
    preference_items: Optional[List[TenantPreferenceItem]] = field(
        default=None, metadata=config(field_name="preference_items")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class NewTenantPreferenceInput:
    """NewTenantPreferenceInput."""

    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    global_: Optional[bool] = field(default=None, metadata=config(field_name="global"))
    preference_items: Optional[List[TenantPreferenceItemInput]] = field(
        default=None, metadata=config(field_name="preference_items")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UpdateTenantPreferenceInput:
    """UpdateTenantPreferenceInput."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    key: Optional[str] = field(default=None, metadata=config(field_name="key"))
    global_: Optional[bool] = field(default=None, metadata=config(field_name="global"))
    preference_items: Optional[List[TenantPreferenceItemInput]] = field(
        default=None, metadata=config(field_name="preference_items")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TicketingSettingsConfigurationInput:
    """TicketingSettingsConfigurationInput."""

    service_now_configuration: Optional[ServiceNowConfigurationInput] = field(
        default=None, metadata=config(field_name="serviceNowConfiguration")
    )
    zendesk_configuration: Optional[ZendeskConfigurationInput] = field(
        default=None, metadata=config(field_name="zendeskConfiguration")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TicketingSettings:
    """TicketingSettings."""

    id: Optional[str] = field(default=None, metadata=config(field_name="id"))
    tenant_id: Optional[str] = field(
        default=None, metadata=config(field_name="tenantID")
    )
    lang: Optional[str] = field(default=None, metadata=config(field_name="lang"))
    display_name: Optional[str] = field(
        default=None, metadata=config(field_name="displayName")
    )
    view_ticket_url: Optional[str] = field(
        default=None, metadata=config(field_name="viewTicketURL")
    )
    partner_view_ticket_url: Optional[str] = field(
        default=None, metadata=config(field_name="partnerViewTicketURL")
    )
    create_ticket_url: Optional[str] = field(
        default=None, metadata=config(field_name="createTicketURL")
    )
    partner_create_ticket_url: Optional[str] = field(
        default=None, metadata=config(field_name="partnerCreateTicketURL")
    )
    chat_url: Optional[str] = field(default=None, metadata=config(field_name="chatURL"))
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    ticketing_type: Optional[Union[TicketingType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(TicketingType, x),
            field_name="ticketingType",
        ),
    )
    option_type: Optional[Union[OptionType, TaegisEnum]] = field(
        default=None,
        metadata=config(
            encoder=encode_enum,
            decoder=lambda x: decode_enum(OptionType, x),
            field_name="optionType",
        ),
    )
    configuration: Optional[List[TenantPreferenceItem]] = field(
        default=None, metadata=config(field_name="configuration")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class UserNotificationPreferences:
    """UserNotificationPreferences."""

    total_count: Optional[int] = field(
        default=None, metadata=config(field_name="totalCount")
    )
    user_preferences: Optional[List[UserNotificationPreferencesResponse]] = field(
        default=None, metadata=config(field_name="userPreferences")
    )


@dataclass_json
@dataclass(order=True, eq=True, frozen=True)
class TicketingSettingsInput:
    """TicketingSettingsInput."""

    lang: Optional[str] = field(default=None, metadata=config(field_name="lang"))
    display_name: Optional[str] = field(
        default=None, metadata=config(field_name="displayName")
    )
    view_ticket_url: Optional[str] = field(
        default=None, metadata=config(field_name="viewTicketURL")
    )
    partner_view_ticket_url: Optional[str] = field(
        default=None, metadata=config(field_name="partnerViewTicketURL")
    )
    create_ticket_url: Optional[str] = field(
        default=None, metadata=config(field_name="createTicketURL")
    )
    partner_create_ticket_url: Optional[str] = field(
        default=None, metadata=config(field_name="partnerCreateTicketURL")
    )
    chat_url: Optional[str] = field(default=None, metadata=config(field_name="chatURL"))
    enabled: Optional[bool] = field(default=None, metadata=config(field_name="enabled"))
    configuration: Optional[TicketingSettingsConfigurationInput] = field(
        default=None, metadata=config(field_name="configuration")
    )
