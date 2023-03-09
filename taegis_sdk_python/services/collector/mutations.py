"""Collector Mutation."""
# pylint: disable=no-member, unused-argument, too-many-locals, duplicate-code, wildcard-import, unused-wildcard-import, cyclic-import


# Autogenerated
# DO NOT MODIFY

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Dict, Optional, Tuple, Union

from taegis_sdk_python.utils import (
    build_output_string,
    prepare_input,
    parse_union_result,
)
from taegis_sdk_python.services.collector.types import *

from taegis_sdk_python import GraphQLNoRowsInResultSetError

if TYPE_CHECKING:  # pragma: no cover
    from taegis_sdk_python.services.collector import CollectorService


class TaegisSDKCollectorMutation:
    """Teagis Collector Mutation operations."""

    def __init__(self, service: CollectorService):
        self.service = service

    def create_cluster(self, cluster_input: ClusterInput) -> Cluster:
        """Create a new cluster of a given role."""
        endpoint = "createCluster"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterInput": prepare_input(cluster_input),
            },
            output=build_output_string(Cluster),
        )
        if result.get(endpoint) is not None:
            return Cluster.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createCluster")

    def create_ha_cluster_static_config(
        self, cluster_input: HAStaticClusterInput
    ) -> Cluster:
        """Create a cluster with clusterNodes containing static ips."""
        endpoint = "createHAClusterStaticConfig"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterInput": prepare_input(cluster_input),
            },
            output=build_output_string(Cluster),
        )
        if result.get(endpoint) is not None:
            return Cluster.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createHAClusterStaticConfig")

    def update_cluster(self, cluster_id: str, cluster_input: ClusterInput) -> Cluster:
        """Update a cluster."""
        endpoint = "updateCluster"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "clusterInput": prepare_input(cluster_input),
            },
            output=build_output_string(Cluster),
        )
        if result.get(endpoint) is not None:
            return Cluster.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateCluster")

    def delete_cluster(self, cluster_id: str) -> Deleted:
        """Delete a cluster."""
        endpoint = "deleteCluster"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output=build_output_string(Deleted),
        )
        if result.get(endpoint) is not None:
            return Deleted.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteCluster")

    def create_os_config(self, input_: OSConfigInput) -> OSConfig:
        """None."""
        endpoint = "createOSConfig"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(OSConfig),
        )
        if result.get(endpoint) is not None:
            return OSConfig.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createOSConfig")

    def update_os_config(self, input_: OSConfigInput) -> OSConfig:
        """None."""
        endpoint = "updateOSConfig"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(OSConfig),
        )
        if result.get(endpoint) is not None:
            return OSConfig.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateOSConfig")

    def delete_os_config(self, cluster_id: str, node_name: Optional[str] = None) -> str:
        """None."""
        endpoint = "deleteOSConfig"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "nodeName": prepare_input(node_name),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation deleteOSConfig")

    def add_host(self, cluster_id: str, host_input: HostsInput) -> Any:
        """Add a address:hostname mapping to a given cluster."""
        endpoint = "addHost"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "hostInput": prepare_input(host_input),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for mutation addHost")

    def delete_host(self, cluster_id: str, address: str) -> Deleted:
        """Remove an address:hostname mapping from a given cluster by providing the IP address and associated host name."""
        endpoint = "deleteHost"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "address": prepare_input(address),
            },
            output=build_output_string(Deleted),
        )
        if result.get(endpoint) is not None:
            return Deleted.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteHost")

    def create_cluster_status(
        self, cluster_id: str, status_input: StatusInput
    ) -> Status:
        """Create the initial deployment status of a given cluster."""
        endpoint = "createClusterStatus"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "statusInput": prepare_input(status_input),
            },
            output=build_output_string(Status),
        )
        if result.get(endpoint) is not None:
            return Status.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createClusterStatus")

    def update_cluster_status(
        self, cluster_id: str, status_input: StatusInput
    ) -> Status:
        """Update the deployment status of a given cluster."""
        endpoint = "updateClusterStatus"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "statusInput": prepare_input(status_input),
            },
            output=build_output_string(Status),
        )
        if result.get(endpoint) is not None:
            return Status.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateClusterStatus")

    def delete_cluster_status(self, cluster_id: str, deployment_id: str) -> Deleted:
        """Delete the deployment status of a given cluster."""
        endpoint = "deleteClusterStatus"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
            },
            output=build_output_string(Deleted),
        )
        if result.get(endpoint) is not None:
            return Deleted.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteClusterStatus")

    def create_cluster_deployment(
        self, cluster_id: str, deployment_input: DeploymentInput
    ) -> Deployment:
        """Create a deployment local to a given cluster."""
        endpoint = "createClusterDeployment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentInput": prepare_input(deployment_input),
            },
            output=build_output_string(Deployment),
        )
        if result.get(endpoint) is not None:
            return Deployment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createClusterDeployment")

    def update_cluster_deployment(
        self, cluster_id: str, deployment_id: str, deployment_input: DeploymentInput
    ) -> Deployment:
        """Deprecated, use `updateClusterDeploymentV2` instead."""
        endpoint = "updateClusterDeployment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
                "deploymentInput": prepare_input(deployment_input),
            },
            output=build_output_string(Deployment),
        )
        if result.get(endpoint) is not None:
            return Deployment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateClusterDeployment")

    def update_cluster_deployment_v2(
        self,
        cluster_id: str,
        deployment_id: str,
        update_deployment_input: UpdateDeploymentInput,
    ) -> Deployment:
        """Update a deployment on a given cluster version2."""
        endpoint = "updateClusterDeploymentV2"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
                "updateDeploymentInput": prepare_input(update_deployment_input),
            },
            output=build_output_string(Deployment),
        )
        if result.get(endpoint) is not None:
            return Deployment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateClusterDeploymentV2")

    def delete_cluster_deployment(self, cluster_id: str, deployment_id: str) -> Deleted:
        """Delete a deployment on a given cluster."""
        endpoint = "deleteClusterDeployment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
            },
            output=build_output_string(Deleted),
        )
        if result.get(endpoint) is not None:
            return Deleted.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteClusterDeployment")

    def create_endpoint(
        self, cluster_id: str, deployment_id: str, endpoint_input: EndpointInput
    ) -> Endpoint:
        """Create an endpoint for a given cluster."""
        endpoint = "createEndpoint"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
                "endpointInput": prepare_input(endpoint_input),
            },
            output=build_output_string(Endpoint),
        )
        if result.get(endpoint) is not None:
            return Endpoint.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createEndpoint")

    def update_endpoint(
        self,
        cluster_id: str,
        deployment_id: str,
        endpoint_id: str,
        endpoint_input: EndpointInput,
    ) -> Endpoint:
        """Update an endpoint for a given cluster."""
        endpoint = "updateEndpoint"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
                "endpointID": prepare_input(endpoint_id),
                "endpointInput": prepare_input(endpoint_input),
            },
            output=build_output_string(Endpoint),
        )
        if result.get(endpoint) is not None:
            return Endpoint.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateEndpoint")

    def delete_endpoint(
        self, cluster_id: str, deployment_id: str, endpoint_id: str
    ) -> Deleted:
        """Delete an endpoint for a given cluster."""
        endpoint = "deleteEndpoint"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
                "endpointID": prepare_input(endpoint_id),
            },
            output=build_output_string(Deleted),
        )
        if result.get(endpoint) is not None:
            return Deleted.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteEndpoint")

    def create_role_deployment(
        self, role: str, deployment_input: DeploymentInput
    ) -> Deployment:
        """Create a deployment to be installed on every cluster of a given role. Only Secureworks admins can reach this endpoint.."""
        endpoint = "createRoleDeployment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "role": prepare_input(role),
                "deploymentInput": prepare_input(deployment_input),
            },
            output=build_output_string(Deployment),
        )
        if result.get(endpoint) is not None:
            return Deployment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation createRoleDeployment")

    def update_role_deployment(
        self, deployment_id: str, deployment_input: DeploymentInput
    ) -> Deployment:
        """Update a system deployment by ID. Only Secureworks admins can reach this endpoint.."""
        endpoint = "updateRoleDeployment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "deploymentID": prepare_input(deployment_id),
                "deploymentInput": prepare_input(deployment_input),
            },
            output=build_output_string(Deployment),
        )
        if result.get(endpoint) is not None:
            return Deployment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation updateRoleDeployment")

    def delete_role_deployment(self, deployment_id: str) -> Deleted:
        """Delete a system deployment by ID. Only Secureworks admins can reach this endpoint.."""
        endpoint = "deleteRoleDeployment"

        result = self.service.execute_mutation(
            endpoint=endpoint,
            variables={
                "deploymentID": prepare_input(deployment_id),
            },
            output=build_output_string(Deleted),
        )
        if result.get(endpoint) is not None:
            return Deleted.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for mutation deleteRoleDeployment")