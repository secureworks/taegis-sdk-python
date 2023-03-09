"""Collector Query."""
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


class TaegisSDKCollectorQuery:
    """Teagis Collector Query operations."""

    def __init__(self, service: CollectorService):
        self.service = service

    def get_cluster(self, cluster_id: str) -> Cluster:
        """Get cluster by ID."""
        endpoint = "getCluster"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output=build_output_string(Cluster),
        )
        if result.get(endpoint) is not None:
            return Cluster.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getCluster")

    def get_clusters_by_ids(self, cluster_ids: List[str]) -> List[Cluster]:
        """Get clusters by IDs."""
        endpoint = "getClustersByIDs"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterIDs": prepare_input(cluster_ids),
            },
            output=build_output_string(Cluster),
        )
        if result.get(endpoint) is not None:
            return Cluster.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query getClustersByIDs")

    def get_cluster_node(
        self, cluster_id: str, cluster_node_input: Optional[ClusterNodeInput] = None
    ) -> ClusterNode:
        """None."""
        endpoint = "getClusterNode"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "clusterNodeInput": prepare_input(cluster_node_input),
            },
            output=build_output_string(ClusterNode),
        )
        if result.get(endpoint) is not None:
            return ClusterNode.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getClusterNode")

    def get_all_clusters(self, role: str) -> List[Cluster]:
        """Get all clusters provisioned on the tenant."""
        endpoint = "getAllClusters"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "role": prepare_input(role),
            },
            output=build_output_string(Cluster),
        )
        if result.get(endpoint) is not None:
            return Cluster.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query getAllClusters")

    def get_cluster_config(self, cluster_id: str) -> Any:
        """Get a cluster's config."""
        endpoint = "getClusterConfig"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query getClusterConfig")

    def get_cluster_image_v2(self, input_: ClusterImageInput) -> Image:
        """Get a cluster's image download link.."""
        endpoint = "getClusterImageV2"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "input": prepare_input(input_),
            },
            output=build_output_string(Image),
        )
        if result.get(endpoint) is not None:
            return Image.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getClusterImageV2")

    def get_cluster_image(
        self,
        cluster_id: str,
        image_type: ImageType,
        launch_console: Optional[bool] = None,
        aws_details: Optional[AWSDetails] = None,
        gcp_details: Optional[GCPDetails] = None,
    ) -> Image:
        """Deprecated, use `getClusterImageV2` instead for consolidated inputs.."""
        endpoint = "getClusterImage"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "imageType": prepare_input(image_type),
                "launchConsole": prepare_input(launch_console),
                "awsDetails": prepare_input(aws_details),
                "gcpDetails": prepare_input(gcp_details),
            },
            output=build_output_string(Image),
        )
        if result.get(endpoint) is not None:
            return Image.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getClusterImage")

    def get_cloud_zones(self, image_type: ImageType) -> List[CloudRegion]:
        """Get a cloud service region and zones."""
        endpoint = "getCloudZones"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "imageType": prepare_input(image_type),
            },
            output=build_output_string(CloudRegion),
        )
        if result.get(endpoint) is not None:
            return CloudRegion.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query getCloudZones")

    def get_cluster_credentials(self, cluster_id: str) -> Credentials:
        """Get a cluster's credentials."""
        endpoint = "getClusterCredentials"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output=build_output_string(Credentials),
        )
        if result.get(endpoint) is not None:
            return Credentials.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getClusterCredentials")

    def get_hosts(self, cluster_id: str) -> Any:
        """Get all of the host->address mappings associated with a given cluster."""
        endpoint = "getHosts"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query getHosts")

    def get_cluster_activation_details(self, cluster_id: str) -> Activation:
        """None."""
        endpoint = "getClusterActivationDetails"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output=build_output_string(Activation),
        )
        if result.get(endpoint) is not None:
            return Activation.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getClusterActivationDetails")

    def get_system_by_role(self, role: str) -> System:
        """None."""
        endpoint = "getSystemByRole"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "role": prepare_input(role),
            },
            output=build_output_string(System),
        )
        if result.get(endpoint) is not None:
            return System.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getSystemByRole")

    def get_os_config(
        self, cluster_id: str, node_name: Optional[str] = None
    ) -> OSConfig:
        """None."""
        endpoint = "getOSConfig"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "nodeName": prepare_input(node_name),
            },
            output=build_output_string(OSConfig),
        )
        if result.get(endpoint) is not None:
            return OSConfig.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getOSConfig")

    def get_all_os_configs(self, cluster_id: str) -> OSConfig:
        """None."""
        endpoint = "getAllOSConfigs"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output=build_output_string(OSConfig),
        )
        if result.get(endpoint) is not None:
            return OSConfig.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getAllOSConfigs")

    def get_cluster_statuses(self, cluster_id: str) -> List[Status]:
        """Get a cluster's statuses and helm resources deployed."""
        endpoint = "getClusterStatuses"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output=build_output_string(Status),
        )
        if result.get(endpoint) is not None:
            return Status.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query getClusterStatuses")

    def get_cluster_deployment_status(
        self, cluster_id: str, deployment_id: str
    ) -> Dict[str, Any]:
        """Get the status of a cluster deployment."""
        endpoint = "getClusterDeploymentStatus"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
            },
            output="",
        )
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query getClusterDeploymentStatus")

    def get_chart(self, chart_name: str) -> Chart:
        """Get a single Helm chart by name."""
        endpoint = "getChart"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "chartName": prepare_input(chart_name),
            },
            output=build_output_string(Chart),
        )
        if result.get(endpoint) is not None:
            return Chart.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getChart")

    def get_all_charts(self) -> List[ChartList]:
        """Get all of the Helm charts available for deployment to any cluster."""
        endpoint = "getAllCharts"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(ChartList)
        )
        if result.get(endpoint) is not None:
            return ChartList.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query getAllCharts")

    def get_bill_of_materials(self) -> BillOfMaterials:
        """None."""
        endpoint = "getBillOfMaterials"

        result = self.service.execute_query(
            endpoint=endpoint, variables={}, output=build_output_string(BillOfMaterials)
        )
        if result.get(endpoint) is not None:
            return BillOfMaterials.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getBillOfMaterials")

    def get_cluster_deployment(self, cluster_id: str, deployment_id: str) -> Deployment:
        """Get a single deployment under a collector."""
        endpoint = "getClusterDeployment"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
            },
            output=build_output_string(Deployment),
        )
        if result.get(endpoint) is not None:
            return Deployment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getClusterDeployment")

    def get_all_cluster_deployments(self, cluster_id: str) -> List[Deployment]:
        """Get all of the deployments under a collector."""
        endpoint = "getAllClusterDeployments"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output=build_output_string(Deployment),
        )
        if result.get(endpoint) is not None:
            return Deployment.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query getAllClusterDeployments")

    def get_deployment_endpoint(
        self, cluster_id: str, deployment_id: str, endpoint_id: str
    ) -> Endpoint:
        """Get an endpoint configured for a given deployment."""
        endpoint = "getDeploymentEndpoint"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
                "endpointID": prepare_input(endpoint_id),
            },
            output=build_output_string(Endpoint),
        )
        if result.get(endpoint) is not None:
            return Endpoint.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getDeploymentEndpoint")

    def get_all_deployment_endpoints(
        self, cluster_id: str, deployment_id: str
    ) -> List[Endpoint]:
        """Get all of the endpoints configured for a given deployment."""
        endpoint = "getAllDeploymentEndpoints"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
            },
            output=build_output_string(Endpoint),
        )
        if result.get(endpoint) is not None:
            return Endpoint.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query getAllDeploymentEndpoints")

    def get_deployment_endpoint_credentials_validity_period(
        self, cluster_id: str, deployment_id: str, endpoint_id: str
    ) -> ValidityPeriod:
        """Get EndpointCredential validity period."""
        endpoint = "getDeploymentEndpointCredentialsValidityPeriod"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "deploymentID": prepare_input(deployment_id),
                "endpointID": prepare_input(endpoint_id),
            },
            output=build_output_string(ValidityPeriod),
        )
        if result.get(endpoint) is not None:
            return ValidityPeriod.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError(
            "for query getDeploymentEndpointCredentialsValidityPeriod"
        )

    def get_aws_regions(self) -> List[str]:
        """Fetch list of AWS regions where we have images available."""
        endpoint = "getAWSRegions"

        result = self.service.execute_query(endpoint=endpoint, variables={}, output="")
        if result.get(endpoint) is not None:
            return result.get(endpoint)
        raise GraphQLNoRowsInResultSetError("for query getAWSRegions")

    def get_role_deployments(self, role: str) -> List[Deployment]:
        """Get deployments to be installed on every cluster of a given role.."""
        endpoint = "getRoleDeployments"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "role": prepare_input(role),
            },
            output=build_output_string(Deployment),
        )
        if result.get(endpoint) is not None:
            return Deployment.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query getRoleDeployments")

    def get_role_deployment(self, deployment_id: str) -> Deployment:
        """Get a role based deployment by ID.."""
        endpoint = "getRoleDeployment"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "deploymentID": prepare_input(deployment_id),
            },
            output=build_output_string(Deployment),
        )
        if result.get(endpoint) is not None:
            return Deployment.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getRoleDeployment")

    def get_all_collectors_overview(
        self, role: str, time_range: TimeRange
    ) -> List[CollectorOverview]:
        """Get all collector overview data for the given role and time range."""
        endpoint = "getAllCollectorsOverview"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "role": prepare_input(role),
                "timeRange": prepare_input(time_range),
            },
            output=build_output_string(CollectorOverview),
        )
        if result.get(endpoint) is not None:
            return CollectorOverview.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query getAllCollectorsOverview")

    def get_collector_metrics(self, time_range: TimeRange) -> CollectorMetrics:
        """Get collector data flow metrics over a given time range."""
        endpoint = "getCollectorMetrics"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "timeRange": prepare_input(time_range),
            },
            output=build_output_string(CollectorMetrics),
        )
        if result.get(endpoint) is not None:
            return CollectorMetrics.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getCollectorMetrics")

    def get_aggregate_rate_by_collector(
        self, cluster_id: str, time_range: TimeRange
    ) -> AggregateRateByCollector:
        """Get aggregated data flow rate metrics for a given collector over a given time range."""
        endpoint = "getAggregateRateByCollector"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "timeRange": prepare_input(time_range),
            },
            output=build_output_string(AggregateRateByCollector),
        )
        if result.get(endpoint) is not None:
            return AggregateRateByCollector.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getAggregateRateByCollector")

    def get_flow_rate(self, cluster_id: str, time_range: TimeRange) -> FlowRate:
        """Get flow rate metrics for a given collector over a given time range."""
        endpoint = "getFlowRate"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
                "timeRange": prepare_input(time_range),
            },
            output=build_output_string(FlowRate),
        )
        if result.get(endpoint) is not None:
            return FlowRate.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getFlowRate")

    def get_log_last_seen_metrics(
        self, cluster_id: Optional[str] = None
    ) -> LogLastSeenMetrics:
        """Get last seen metrics for all available log sources for a given cluster.
        If no clusterId is specified, this will return all log sources metrics for all existing clusters.
        """
        endpoint = "getLogLastSeenMetrics"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "clusterID": prepare_input(cluster_id),
            },
            output=build_output_string(LogLastSeenMetrics),
        )
        if result.get(endpoint) is not None:
            return LogLastSeenMetrics.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getLogLastSeenMetrics")

    def get_data_source_metrics(
        self, in_: GetDataSourceMetricsArguments
    ) -> DataSourceMetrics:
        """Get metrics for all available data sources for a given cluster."""
        endpoint = "getDataSourceMetrics"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(DataSourceMetrics),
        )
        if result.get(endpoint) is not None:
            return DataSourceMetrics.from_dict(result.get(endpoint))
        raise GraphQLNoRowsInResultSetError("for query getDataSourceMetrics")

    def syslog_message_count_v2(
        self, in_: SyslogMessageCountV2Arguments
    ) -> List[SyslogMessageCountV2]:
        """Get syslog message counts for a given cluster or data source."""
        endpoint = "syslogMessageCountV2"

        result = self.service.execute_query(
            endpoint=endpoint,
            variables={
                "in": prepare_input(in_),
            },
            output=build_output_string(SyslogMessageCountV2),
        )
        if result.get(endpoint) is not None:
            return SyslogMessageCountV2.schema().load(
                [r or {} for r in result.get(endpoint)], many=True
            )
        raise GraphQLNoRowsInResultSetError("for query syslogMessageCountV2")