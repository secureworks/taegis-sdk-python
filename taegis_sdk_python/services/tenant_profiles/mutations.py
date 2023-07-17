"""TenantProfiles Mutation."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from taegis_sdk_python import GraphQLNoRowsInResultSetError
from taegis_sdk_python.utils import (
    build_output_string,
    parse_union_result,
    prepare_input,
)
from taegis_sdk_python.services.tenant_profiles.types import *

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.tenant_profiles import TenantProfilesService

log = logging.getLogger(__name__)


class TaegisSDKTenantProfilesMutation:
    """Teagis Tenant_profiles Mutation operations."""

    def __init__(self, service: TenantProfilesService):
        self.service = service

    def create_profile_mtp(self) -> ManagedTenantProfile:
        """None."""
        endpoint = "createProfileMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={},
            output=build_output_string(ManagedTenantProfile),
        )
        if result.get(endpoint) is not None:
            return ManagedTenantProfile.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createProfileMtp")

    def create_critical_contact_mtp(
        self, input_: CriticalContactMtpInput
    ) -> CustomerContactMtp:
        """adds a new cse contact. Note only one each CSE Preference type allowed in CSE contacts."""
        endpoint = "createCriticalContactMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(CustomerContactMtp),
        )
        if result.get(endpoint) is not None:
            return CustomerContactMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createCriticalContactMtp")

    def create_critical_external_contact_mtp(
        self, input_: CriticalExternalContactMtpInput
    ) -> CustomerContactMtp:
        """add a new cse contact that is a external (non XDR user)."""
        endpoint = "createCriticalExternalContactMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(CustomerContactMtp),
        )
        if result.get(endpoint) is not None:
            return CustomerContactMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation createCriticalExternalContactMtp"
        )

    def update_critical_contact_mtp(
        self, id_: str, input_: CriticalContactMtpInput
    ) -> CustomerContactMtp:
        """updates a cse contact that is a XDR user."""
        endpoint = "updateCriticalContactMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "input": prepare_input(input_),
            },
            output=build_output_string(CustomerContactMtp),
        )
        if result.get(endpoint) is not None:
            return CustomerContactMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateCriticalContactMtp")

    def update_critical_external_contact_mtp(
        self, id_: str, input_: CriticalExternalContactMtpInput
    ) -> CustomerContactMtp:
        """updates a cse contact that is a external."""
        endpoint = "updateCriticalExternalContactMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "input": prepare_input(input_),
            },
            output=build_output_string(CustomerContactMtp),
        )
        if result.get(endpoint) is not None:
            return CustomerContactMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation updateCriticalExternalContactMtp"
        )

    def delete_critical_contact_mtp(self, id_: str) -> CustomerContactMtp:
        """None."""
        endpoint = "deleteCriticalContactMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(CustomerContactMtp),
        )
        if result.get(endpoint) is not None:
            return CustomerContactMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteCriticalContactMtp")

    def bulk_delete_critical_contact_mtp(
        self, ids: List[str]
    ) -> List[CustomerContactMtp]:
        """Delete multiple CustomerContactMtps and return list of ones actually deleted."""
        endpoint = "bulkDeleteCriticalContactMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output=build_output_string(CustomerContactMtp),
        )
        if result.get(endpoint) is not None:
            return CustomerContactMtp.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation bulkDeleteCriticalContactMtp")

    def verify_critical_external_contact_mtp(
        self, id_: str, message: str
    ) -> CustomerContactMtp:
        """None."""
        endpoint = "verifyCriticalExternalContactMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "message": prepare_input(message),
            },
            output=build_output_string(CustomerContactMtp),
        )
        if result.get(endpoint) is not None:
            return CustomerContactMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for mutation verifyCriticalExternalContactMtp"
        )

    def create_network_range_mtp(
        self, input_: Optional[NetworkRangeCreateMtpInput] = None
    ) -> NetworkRangeMtp:
        """None."""
        endpoint = "createNetworkRangeMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(NetworkRangeMtp),
        )
        if result.get(endpoint) is not None:
            return NetworkRangeMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createNetworkRangeMtp")

    def update_network_range_mtp(
        self, id_: str, network: Optional[NetworkRangeUpdateMtpInput] = None
    ) -> NetworkRangeMtp:
        """None."""
        endpoint = "updateNetworkRangeMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "network": prepare_input(network),
            },
            output=build_output_string(NetworkRangeMtp),
        )
        if result.get(endpoint) is not None:
            return NetworkRangeMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateNetworkRangeMtp")

    def delete_network_range_mtp(self, id_: str) -> NetworkRangeMtp:
        """None."""
        endpoint = "deleteNetworkRangeMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(NetworkRangeMtp),
        )
        if result.get(endpoint) is not None:
            return NetworkRangeMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteNetworkRangeMtp")

    def bulk_delete_network_range_mtp(self, ids: List[str]) -> List[NetworkRangeMtp]:
        """Delete multiple NetworkRangeMtps and return list of ones actually deleted."""
        endpoint = "bulkDeleteNetworkRangeMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output=build_output_string(NetworkRangeMtp),
        )
        if result.get(endpoint) is not None:
            return NetworkRangeMtp.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation bulkDeleteNetworkRangeMtp")

    def update_note_mtp(self, contents: str) -> NoteMtp:
        """None."""
        endpoint = "updateNoteMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "contents": prepare_input(contents),
            },
            output=build_output_string(NoteMtp),
        )
        if result.get(endpoint) is not None:
            return NoteMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateNoteMtp")

    def create_security_control_mtp(
        self, input_: SecurityControlCreateMtpInput
    ) -> SecurityControlMtp:
        """None."""
        endpoint = "createSecurityControlMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(SecurityControlMtp),
        )
        if result.get(endpoint) is not None:
            return SecurityControlMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createSecurityControlMtp")

    def update_security_control_mtp(
        self, id_: str, input_: SecurityControlUpdateMtpInput
    ) -> SecurityControlMtp:
        """None."""
        endpoint = "updateSecurityControlMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "input": prepare_input(input_),
            },
            output=build_output_string(SecurityControlMtp),
        )
        if result.get(endpoint) is not None:
            return SecurityControlMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateSecurityControlMtp")

    def delete_security_control_mtp(self, id_: str) -> SecurityControlMtp:
        """None."""
        endpoint = "deleteSecurityControlMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(SecurityControlMtp),
        )
        if result.get(endpoint) is not None:
            return SecurityControlMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteSecurityControlMtp")

    def bulk_delete_security_control_mtp(
        self, ids: List[str]
    ) -> List[SecurityControlMtp]:
        """Delete multiple SecurityControlMtps and return list of ones actually deleted."""
        endpoint = "bulkDeleteSecurityControlMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output=build_output_string(SecurityControlMtp),
        )
        if result.get(endpoint) is not None:
            return SecurityControlMtp.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation bulkDeleteSecurityControlMtp")

    def create_mfa_access_mtp(self, input_: MfaAccessCreateMtpInput) -> MfaAccessMtp:
        """None."""
        endpoint = "createMfaAccessMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(MfaAccessMtp),
        )
        if result.get(endpoint) is not None:
            return MfaAccessMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createMfaAccessMtp")

    def update_mfa_access_mtp(
        self, id_: str, input_: MfaAccessUpdateMtpInput
    ) -> MfaAccessMtp:
        """None."""
        endpoint = "updateMfaAccessMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
                "input": prepare_input(input_),
            },
            output=build_output_string(MfaAccessMtp),
        )
        if result.get(endpoint) is not None:
            return MfaAccessMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateMfaAccessMtp")

    def delete_mfa_access_mtp(self, id_: str) -> MfaAccessMtp:
        """None."""
        endpoint = "deleteMfaAccessMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "id": prepare_input(id_),
            },
            output=build_output_string(MfaAccessMtp),
        )
        if result.get(endpoint) is not None:
            return MfaAccessMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteMfaAccessMtp")

    def bulk_delete_mfa_access_mtp(self, ids: List[str]) -> List[MfaAccessMtp]:
        """Delete multiple MfaAccessMtps and return list of ones actually deleted."""
        endpoint = "bulkDeleteMfaAccessMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output=build_output_string(MfaAccessMtp),
        )
        if result.get(endpoint) is not None:
            return MfaAccessMtp.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation bulkDeleteMfaAccessMtp")

    def upload_attachment_mtp(self, file: FileUploadInputMtp) -> FileAttachmentMtp:
        """Upload a file to the current tenant profile."""
        endpoint = "uploadAttachmentMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "file": prepare_input(file),
            },
            output=build_output_string(FileAttachmentMtp),
        )
        if result.get(endpoint) is not None:
            return FileAttachmentMtp.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation uploadAttachmentMtp")

    def delete_attachments_mtp(self, ids: List[str]) -> List[FileAttachmentMtp]:
        """Mark an attachment as deleted. Only works on the most recent file version.."""
        endpoint = "deleteAttachmentsMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output=build_output_string(FileAttachmentMtp),
        )
        if result.get(endpoint) is not None:
            return FileAttachmentMtp.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation deleteAttachmentsMtp")

    def restore_attachments_mtp(self, ids: List[str]) -> List[FileAttachmentMtp]:
        """Restore a previously deleted attachment. Only works on the most recent file version.."""
        endpoint = "restoreAttachmentsMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "ids": prepare_input(ids),
            },
            output=build_output_string(FileAttachmentMtp),
        )
        if result.get(endpoint) is not None:
            return FileAttachmentMtp.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation restoreAttachmentsMtp")

    def update_attachments_mtp(
        self, inputs: List[FileUpdateInputMtp]
    ) -> List[FileAttachmentMtp]:
        """Updates one or more file attachments. Currently only the clientVisible flag can be modified.."""
        endpoint = "updateAttachmentsMtp"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "inputs": prepare_input(inputs),
            },
            output=build_output_string(FileAttachmentMtp),
        )
        if result.get(endpoint) is not None:
            return FileAttachmentMtp.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for mutation updateAttachmentsMtp")
