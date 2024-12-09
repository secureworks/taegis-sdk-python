"""Users Mutation."""

# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python._consts import TaegisEnum
from taegis_sdk_python.services.users.types import *
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.users import UsersService

log = logging.getLogger(__name__)


class TaegisSDKUsersMutation:
    """Taegis Users Mutation operations."""

    def __init__(self, service: UsersService):
        self.service = service

    def invite_tdruser(self, invite: TDRUserInviteInput) -> TDRUser:
        """Invite a TDRUser. The tenant to use for the request will be extracted from the X-Tenant-Context header."""
        endpoint = "inviteTDRUser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "invite": prepare_input(invite),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation inviteTDRUser")

    def invite_tdrusers(
        self, invites: List[TDRUserInviteInput]
    ) -> List[InviteUsersResponse]:
        """Invite multiple TDRUsers. The tenant to use for the request will be extracted from the X-Tenant-Context header."""
        endpoint = "inviteTDRUsers"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "invites": prepare_input(invites),
            },
            output=build_output_string(InviteUsersResponse),
        )
        if result.get(endpoint) is not None:
            return InviteUsersResponse.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation inviteTDRUsers")

    def invite_trial_tdruser(self, invite: TDRUserTrialInviteInput) -> TDRUser:
        """Invite a trial TDRUser. The first or trial tenant ID will be extracted from the X-Tenant-Context header. The second or demo tenant ID will be in the input. Trial users in this invite get assigned the tenant admin role to the two tenants."""
        endpoint = "inviteTrialTDRUser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "invite": prepare_input(invite),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation inviteTrialTDRUser")

    def update_tdruser(self, id_: str, patch: TDRUserUpdateInput) -> TDRUser:
        """Update user."""
        endpoint = "updateTDRUser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "patch": prepare_input(patch),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateTDRUser")

    def change_tdruser_email(self, id_: str, new_email_address: str) -> TDRUser:
        """Change user email address."""
        endpoint = "changeTDRUserEmail"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "newEmailAddress": prepare_input(new_email_address),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation changeTDRUserEmail")

    def remove_tdruser_roles(self, id_: str, roles: List[str]) -> TDRUser:
        """Remove roles from a user. Roles can either contain the role ID or role assignment ID."""
        endpoint = "removeTDRUserRoles"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "roles": prepare_input(roles),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation removeTDRUserRoles")

    def append_tdruser_internal_roles(
        self, id_: str, roles: List[str], expires_at: Optional[str] = None
    ) -> TDRUser:
        """Append internal roles to a users role assignments."""
        endpoint = "appendTDRUserInternalRoles"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "roles": prepare_input(roles),
                "expires_at": prepare_input(expires_at),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation appendTDRUserInternalRoles")

    def remove_tdruser_internal_roles(self, id_: str, roles: List[str]) -> TDRUser:
        """Remove internal roles from a users role assignments."""
        endpoint = "removeTDRUserInternalRoles"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "roles": prepare_input(roles),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation removeTDRUserInternalRoles")

    def validate_support_pin(self, email: str, support_pin: str) -> PinValidation:
        """Validate that the given support pin matches the pin associated with the given user id. Upon validation, a new token will generated for the user.."""
        endpoint = "validateSupportPin"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "email": prepare_input(email),
                "supportPin": prepare_input(support_pin),
            },
            output=build_output_string(PinValidation),
        )
        if result.get(endpoint) is not None:
            return PinValidation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation validateSupportPin")

    def update_tdruser_info(self, user_info: TDRUserInfoInput) -> TDRUser:
        """Self-update user information. Permissions are user:read since all users have read permission. The user to update is determined by the sub claim in the access token.."""
        endpoint = "updateTDRUserInfo"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "userInfo": prepare_input(user_info),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateTDRUserInfo")

    def current_user_reset_mfa(self) -> MFAResetResponse:
        """Reset MFA while logged in. This will read the access token from the authorization header to get the target user."""
        endpoint = "currentUserResetMFA"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={},
            output=build_output_string(MFAResetResponse),
        )
        if result.get(endpoint) is not None:
            return MFAResetResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation currentUserResetMFA")

    def register_partner_user(
        self, registration_input: PartnerRegistrationInput
    ) -> TDRUser:
        """Creates a pre-verified Partner User. Requires active SSO connection for the user's email domain."""
        endpoint = "registerPartnerUser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "registrationInput": prepare_input(registration_input),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation registerPartnerUser")

    def resend_migration_email(self, id_: str) -> TDRUser:
        """Resends the Cognito migration email to non-SSO users, with a new temporary password. This should be short-lived until the migration is complete."""
        endpoint = "resendMigrationEmail"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(TDRUser),
        )
        if result.get(endpoint) is not None:
            return TDRUser.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation resendMigrationEmail")

    def forgot_password(
        self, email: str, app: Optional[str] = None
    ) -> ForgotPasswordResponse:
        """Initiate the password reset workflow requested by a user."""
        endpoint = "forgotPassword"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "email": prepare_input(email),
                "app": prepare_input(app),
            },
            output=build_output_string(ForgotPasswordResponse),
        )
        if result.get(endpoint) is not None:
            return ForgotPasswordResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation forgotPassword")

    def reset_password(self, reset_input: PasswordResetInput) -> ForgotPasswordResponse:
        """Set/reset the password for the specified user."""
        endpoint = "resetPassword"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "resetInput": prepare_input(reset_input),
            },
            output=build_output_string(ForgotPasswordResponse),
        )
        if result.get(endpoint) is not None:
            return ForgotPasswordResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation resetPassword")

    def need_mfa_reset(self, email: str) -> ForgotPasswordResponse:
        """Initiate the MFA reset workflow requested by a user."""
        endpoint = "needMFAReset"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "email": prepare_input(email),
            },
            output=build_output_string(ForgotPasswordResponse),
        )
        if result.get(endpoint) is not None:
            return ForgotPasswordResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation needMFAReset")

    def reset_mfa(self, mfa_input: MFAResetInput) -> MFAResetResponse:
        """Set/reset the password for the specified user."""
        endpoint = "resetMFA"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "mfaInput": prepare_input(mfa_input),
            },
            output=build_output_string(MFAResetResponse),
        )
        if result.get(endpoint) is not None:
            return MFAResetResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation resetMFA")

    def register_tdruser(
        self, registration_input: UserRegistrationInput
    ) -> MFAResetResponse:
        """Process user registration from invites."""
        endpoint = "registerTDRUser"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "registrationInput": prepare_input(registration_input),
            },
            output=build_output_string(MFAResetResponse),
        )
        if result.get(endpoint) is not None:
            return MFAResetResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation registerTDRUser")

    def verify_mfa_registration(
        self, verify_mfa_input: VerifyMFARegistrationInput
    ) -> VerifyMFARegistrationResponse:
        """Verify MFA registration."""
        endpoint = "verifyMFARegistration"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "verifyMFAInput": prepare_input(verify_mfa_input),
            },
            output=build_output_string(VerifyMFARegistrationResponse),
        )
        if result.get(endpoint) is not None:
            return VerifyMFARegistrationResponse.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation verifyMFARegistration")
