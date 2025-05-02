"""
Taegis SDK Python GraphQL Service manager.
"""

import logging
import threading
from ssl import SSLContext
from typing import Any, Dict, Literal, Optional, Union

import aiohttp
from aiohttp.client_reqrep import Fingerprint
from aiohttp.typedefs import LooseHeaders

from taegis_sdk_python._consts import (
    TAEGIS_ENVIRONMENT_URLS,
    UNIVERSAL_AUTHENTICATION_URL,
    UNIVERSAL_ENVIRONMENT,
)
from taegis_sdk_python._version import __version__
from taegis_sdk_python.authentication import get_token
from taegis_sdk_python.config import write_to_config
from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.access_points import AccessPointsService
from taegis_sdk_python.services.agent import AgentService
from taegis_sdk_python.services.alerts import AlertsService
from taegis_sdk_python.services.alerts_history import AlertsHistoryService
from taegis_sdk_python.services.assets import AssetsService
from taegis_sdk_python.services.assets2 import Assets2Service
from taegis_sdk_python.services.audits import AuditsService
from taegis_sdk_python.services.authz import AuthzService
from taegis_sdk_python.services.byoti import ByotiService
from taegis_sdk_python.services.clients import ClientsService
from taegis_sdk_python.services.collector import CollectorService
from taegis_sdk_python.services.comments import CommentsService
from taegis_sdk_python.services.contracted_endpoint import ContractedEndpointService
from taegis_sdk_python.services.cql_metadata import CqlMetadataService
from taegis_sdk_python.services.datasources import DatasourcesService
from taegis_sdk_python.services.detector_registry import DetectorRegistryService
from taegis_sdk_python.services.endpoint_command_manager import (
    EndpointCommandManagerService,
)
from taegis_sdk_python.services.endpoint_management_service import (
    EndpointManagementServiceService,
)
from taegis_sdk_python.services.event_search import EventSearchService
from taegis_sdk_python.services.events import EventsService
from taegis_sdk_python.services.exports import ExportsService
from taegis_sdk_python.services.fast_ioc import FastIocService
from taegis_sdk_python.services.file_info import FileInfoService
from taegis_sdk_python.services.ingest_stats import IngestStatsService
from taegis_sdk_python.services.investigations import InvestigationsService
from taegis_sdk_python.services.investigations2 import Investigations2Service
from taegis_sdk_python.services.isensor import IsensorService
from taegis_sdk_python.services.mitre_attack_info import MitreAttackInfoService
from taegis_sdk_python.services.multi_tenant_context import MultiTenantContextService
from taegis_sdk_python.services.multi_tenant_ioc import MultiTenantIocService
from taegis_sdk_python.services.nl_search import NlSearchService
from taegis_sdk_python.services.notebooks import NotebooksService
from taegis_sdk_python.services.notifications import NotificationsService
from taegis_sdk_python.services.preferences import PreferencesService
from taegis_sdk_python.services.process_trees import ProcessTreesService
from taegis_sdk_python.services.queries import QueriesService
from taegis_sdk_python.services.roadrunner import RoadrunnerService
from taegis_sdk_python.services.rules import RulesService
from taegis_sdk_python.services.sharelinks import SharelinksService
from taegis_sdk_python.services.subjects import SubjectsService
from taegis_sdk_python.services.tenant_profiles import TenantProfilesService
from taegis_sdk_python.services.tenants import TenantsService
from taegis_sdk_python.services.tenants4 import Tenants4Service
from taegis_sdk_python.services.threat import ThreatService
from taegis_sdk_python.services.threat_score import ThreatScoreService
from taegis_sdk_python.services.trigger_action import TriggerActionService
from taegis_sdk_python.services.trip import TripService
from taegis_sdk_python.services.users import UsersService
from taegis_sdk_python.services.vdr import VDRService

__all__ = ["GraphQLService"]

log = logging.getLogger(__name__)


class GraphQLService:
    """Taegis GraphQL Service manager."""

    def __init__(
        self,
        *,
        environment: Optional[str] = None,
        tenant_id: Optional[str] = None,
        environments: Optional[Dict[str, str]] = None,
        gateway: Optional[str] = None,
        extra_headers: Optional[Dict[str, Any]] = None,
        schema_expiry: int = 5,
        proxy: Optional[str] = None,
        proxy_auth: Optional[aiohttp.BasicAuth] = None,
        proxy_headers: Optional[LooseHeaders] = None,
        trust_env: bool = False,
        ssl: Optional[Union[SSLContext, Literal[False], Fingerprint]] = None,
        execute_timeout: Optional[Union[int, float]] = 300,
        max_message_size: int = 0,
        use_universal_authentication: bool = False,
    ):  # pylint: disable=too-many-statements
        """
        GraphQLService

        Parameters
        ----------
        environment : Optional[str], optional
            Taegis Cluster environment identifier.
        tenant_id : Optional[str], optional
            Tenant ID, by default None
        environments : Optional[Dict[str, str]], optional
            Environments dictionary {"identifier": "url"}
        gateway : Optional[str], optional
            Default Taegis Gateway, can be overwritten by service
        extra_headers: Optional[Dict[str, Any]], optional
            Extra HTTP Headers to be included in API calls
        schema_expiry: int, optional
            Expire time for GraphQL Schema Caching in minutes, by default 1
        proxy: str, optional
            Proxy URL for API requests
            Examples:
                http://proxy.example.com:8080
                http://username:password@proxy.example.com:8080
        proxy_auth: aiohttp.BasicAuth, optional
            Examples:
                aiohttp.BasicAuth("username", "password")
        proxy_headers: Optional[LooseHeaders], optional
            Proxy Headers for API requests
        trust_env: bool, optional
            Trust Environment Variables for Proxy Authentication
        ssl: Optional[Union[SSLContext, Literal[False], Fingerprint]], optional
            SSL Context for API requests
        execute_timeout: Optional[Union[int, float]], optional
            Timeout for GraphQL Execute in seconds, by default 30
        max_message_size: int, optional
            Max Message Size for Subscriptions, by default 0

        Raises
        ------
        ValueError
            environment must be charlie, delta, echo, or foxtrot (or equivalent)
        """
        self._environments = environments or TAEGIS_ENVIRONMENT_URLS
        self._environment = environment or list(self._environments)[0]
        self._use_universal_authentication = use_universal_authentication

        if self._environment not in self._environments:
            raise ValueError(f"environment must be in {self._environments.keys()}")

        self._tenant_id = tenant_id
        self._gateway = gateway or "/graphql"
        self._thread_id = threading.get_ident()
        self._context_kwargs = {}
        if not extra_headers:
            self._extra_headers = {}
        else:
            self._extra_headers = extra_headers
        self._schema_expiry = schema_expiry
        self._input_value_deprecation = None

        if trust_env and proxy:
            raise ValueError("trust_env and proxy cannot be used together")

        if proxy_auth and not proxy:
            raise ValueError("proxy_auth requires proxy to be set")

        self._proxy = proxy
        self._proxy_auth = proxy_auth
        self._proxy_headers = proxy_headers
        self._ssl = ssl
        self._trust_env = trust_env

        self._execute_timeout = execute_timeout
        self._max_message_size = max_message_size

        self._access_points = None
        self._agent = None
        self._alerts = None
        self._alerts_history = None
        self._assets = None
        self._assets2 = None
        self._audits = None
        self._authz = None
        self._byoti = None
        self._clients = None
        self._collector = None
        self._comments = None
        self._contracted_endpoint = None
        self._cql_metadata = None
        self._datasources = None
        self._detector_registry = None
        self._endpoint_command_manager = None
        self._endpoint_management_service = None
        self._event_search = None
        self._events = None
        self._exports = None
        self._fast_ioc = None
        self._file_info = None
        self._ingest_stats = None
        self._investigations = None
        self._investigations2 = None
        self._isensor = None
        self._mitre_attack_info = None
        self._multi_tenant_context = None
        self._multi_tenant_ioc = None
        self._nl_search = None
        self._notebooks = None
        self._notifications = None
        self._preferences = None
        self._process_trees = None
        self._queries = None
        self._roadrunner = None
        self._rules = None
        self._core = None
        self._sharelinks = None
        self._subjects = None
        self._tenant_profiles = None
        self._tenants = None
        self._tenants4 = None
        self._threat = None
        self._threat_score = None
        self._trigger_action = None
        self._trip = None
        self._users = None
        self._vdr = None

    def __call__(self, **kwargs):
        if threading.get_ident() not in self._context_kwargs:
            self._context_kwargs[threading.get_ident()] = []

        self._context_kwargs[threading.get_ident()].append(kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if threading.get_ident() in self._context_kwargs:
            if self._context_kwargs[threading.get_ident()]:
                self._context_kwargs[threading.get_ident()].pop()

            else:
                del self._context_kwargs[threading.get_ident()]

    @property
    def _context_manager(self):
        """Internal Context Manager property."""
        temp_context = {}

        for kwarg in self._context_kwargs.get(self._thread_id, []):
            temp_context.update(kwarg)
        if self._thread_id != threading.get_ident():
            for kwarg in self._context_kwargs.get(threading.get_ident(), []):
                temp_context.update(kwarg)

        return temp_context

    @property
    def environment(self):
        """Taegis Environment."""
        return self._context_manager.get("environment", self._environment)

    @property
    def authentication_environment(self):
        """Taegis Authentication Environment."""
        return self._context_manager.get(
            "authentication_environment",
            (
                UNIVERSAL_ENVIRONMENT
                if self.use_universal_authentication
                else self.environment
            ),
        )

    @property
    def url(self):
        """Taegis Environment URL."""
        return self._context_manager.get("url")

    @property
    def authentication_url(self):
        """Taegis Authentication URL."""
        return self._context_manager.get(
            "authentication_url",
            (
                UNIVERSAL_AUTHENTICATION_URL
                if self.use_universal_authentication
                else self._environments[self.environment]
            ),
        )

    @property
    def use_universal_authentication(self):
        """Use Universal Authentication."""
        return self._context_manager.get(
            "use_universal_authentication", self._use_universal_authentication
        )

    @property
    def gateway(self):
        """Taegis GraphQL Gateway."""
        return self._context_manager.get("gateway")

    @property
    def tenant_id(self):
        """Taegis Tenant Context."""
        return self._context_manager.get("tenant_id", self._tenant_id)

    @property
    def access_token(self):
        """Taegis Access Token."""
        access_token = self._context_manager.get(
            "access_token",
        )
        if not access_token:
            access_token = get_token(
                environment=self.authentication_environment,
                request_url=self.authentication_url,
            )
        return access_token

    def clear_access_token(self):
        """Clear the current access token."""
        write_to_config(self.authentication_environment, "access_token", "")

    @property
    def output(self):
        """GraphQL Output."""
        return self._context_manager.get("output")

    @property
    def extra_headers(self):
        """Additional headers for API requests."""
        extra_headers = self._extra_headers.copy()
        extra_headers.update(self._context_manager.get("extra_headers", {}))
        return extra_headers

    @property
    def headers(self):
        """Taegis Headers."""
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": f"taegis_sdk_python/{__version__}",
            "apollographql-client-name": "taegis_sdk_python",
            "apollographql-client-version": __version__,
        }

        if self.tenant_id:
            headers["X-Tenant-Context"] = self.tenant_id

        headers.update(self.extra_headers)

        return headers

    @property
    def schema_expiry(self):
        """GraphQL Schema Timeout."""
        return self._context_manager.get("schema_expiry", self._schema_expiry)

    @property
    def max_message_size(self):
        """Max Message Size for Subscriptions."""
        return self._context_manager.get("max_message_size", self._max_message_size)

    @property
    def input_value_deprecation(self):
        """GraphQL Query Deprecated Input Fields in Schema."""
        return self._context_manager.get(
            "input_value_deprecation", self._input_value_deprecation
        )

    @property
    def proxy(self):
        """Proxy URL for API requests."""
        return self._context_manager.get("proxy", self._proxy)

    @property
    def proxy_auth(self):
        """Proxy Auth for API requests."""
        value = self._context_manager.get("proxy_auth", self._proxy_auth)

        if value and not self.proxy:
            log.warning("proxy_auth is ignored when proxy is not set")
            return None

        return value

    @property
    def proxy_headers(self):
        """Proxy Headers for API requests."""
        value = self._context_manager.get("proxy_headers", self._proxy_headers)

        if value and not self.proxy:
            log.warning("proxy_headers is ignored when proxy is not set")
            return None

        return value

    @property
    def ssl(self):
        """SSL Context for API requests."""
        return self._context_manager.get("ssl", self._ssl)

    @property
    def trust_env(self):
        """Trust Environment for Proxy Authentication."""
        value = self._context_manager.get("trust_env", self._trust_env)

        if value and self.proxy:
            log.warning("trust_env is ignored when proxy is set")
            return False

        return value

    @property
    def execute_timeout(self):
        """GraphQL Execute Timeout."""
        return self._context_manager.get("execute_timeout", self._execute_timeout)

    @property
    def access_points(self):
        """Access Points Service Endpoint."""
        if not self._access_points:
            self._access_points = AccessPointsService(self)
        return self._access_points

    @property
    def agent(self):
        """Agent Service Endpoint."""
        if not self._agent:
            self._agent = AgentService(self)
        return self._agent

    @property
    def alerts(self):
        """Alerts2 Service Endpoint."""
        if not self._alerts:
            self._alerts = AlertsService(self)
        return self._alerts

    @property
    def alerts_history(self):
        """AlertsHistory Service Endpoint."""
        if not self._alerts_history:
            self._alerts_history = AlertsHistoryService(self)
        return self._alerts_history

    @property
    def assets(self):
        """Assets Service Endpoint."""
        if not self._assets:
            self._assets = AssetsService(self)
        return self._assets

    @property
    def assets2(self):
        """Assets2 Service Endpoint."""
        if not self._assets2:
            self._assets2 = Assets2Service(self)
        return self._assets2

    @property
    def audits(self):
        """Audits Service Endpoint."""
        if not self._audits:
            self._audits = AuditsService(self)
        return self._audits

    @property
    def authz(self):
        """Authz Service Endpoint."""
        if not self._authz:
            self._authz = AuthzService(self)
        return self._authz

    @property
    def byoti(self):
        """BYOTI (Bring Your Own Threat Intelligence) Service Endpoint."""
        if not self._byoti:
            self._byoti = ByotiService(self)
        return self._byoti

    @property
    def clients(self):
        """Clients Service Endpoint."""
        if not self._clients:
            self._clients = ClientsService(self)
        return self._clients

    @property
    def collector(self):
        """Collector Service Endpoint."""
        if not self._collector:
            self._collector = CollectorService(self)
        return self._collector

    @property
    def comments(self):
        """Comments Service Endpoint."""
        if not self._comments:
            self._comments = CommentsService(self)
        return self._comments

    @property
    def contracted_endpoint(self):
        """ContractedEndpoint Service Endpoint."""
        if not self._contracted_endpoint:
            self._contracted_endpoint = ContractedEndpointService(self)
        return self._contracted_endpoint

    @property
    def cql_metadata(self):
        """CqlMetadata Service Endpoint."""
        if not self._cql_metadata:
            self._cql_metadata = CqlMetadataService(self)
        return self._cql_metadata

    @property
    def datasources(self):
        """Datasources Service Endpoint."""
        if not self._datasources:
            self._datasources = DatasourcesService(self)
        return self._datasources

    @property
    def detector_registry(self):
        """Detector Registry Service Endpoint."""
        if not self._detector_registry:
            self._detector_registry = DetectorRegistryService(self)
        return self._detector_registry

    @property
    def endpoint_command_manager(self):
        """Endpoint Command Manager Service Endpoint."""
        if not self._endpoint_command_manager:
            self._endpoint_command_manager = EndpointCommandManagerService(self)
        return self._endpoint_command_manager

    @property
    def endpoint_management_service(self):
        """Endpoint Management Service Endpoint."""
        if not self._endpoint_management_service:
            self._endpoint_management_service = EndpointManagementServiceService(self)
        return self._endpoint_management_service

    @property
    def event_search(self):
        """Events Search Service Endpoint."""
        if not self._event_search:
            self._event_search = EventSearchService(self)
        return self._event_search

    @property
    def events(self):
        """Events Service Endpoint."""
        if not self._events:
            self._events = EventsService(self)
        return self._events

    @property
    def exports(self):
        """Exports Service Endpoint."""
        if not self._exports:
            self._exports = ExportsService(self)
        return self._exports

    @property
    def fast_ioc(self):
        """Fast IOC (Indicator of Compromise) Service Endpoint. (Deprecated: Use MultiTenantIoc)"""
        if not self._fast_ioc:
            self._fast_ioc = FastIocService(self)
        return self._fast_ioc

    @property
    def file_info(self):
        """FileInfo Service Endpoint."""
        if not self._file_info:
            self._file_info = FileInfoService(self)
        return self._file_info

    @property
    def ingest_stats(self):
        """IngestStats Service Endpoint."""
        if not self._ingest_stats:
            self._ingest_stats = IngestStatsService(self)
        return self._ingest_stats

    @property
    def investigations(self):
        """Investigations Service Endpoint."""
        if not self._investigations:
            self._investigations = InvestigationsService(self)
        return self._investigations

    @property
    def investigations2(self):
        """Investigations2 Service Endpoint."""
        if not self._investigations2:
            self._investigations2 = Investigations2Service(self)
        return self._investigations2

    @property
    def isensor(self):
        """Isensor Service Endpoint."""
        if not self._isensor:
            self._isensor = IsensorService(self)
        return self._isensor

    @property
    def mitre_attack_info(self):
        """MitreAttackInfo Service Endpoint."""
        if not self._mitre_attack_info:
            self._mitre_attack_info = MitreAttackInfoService(self)
        return self._mitre_attack_info

    @property
    def multi_tenant_context(self):
        """MultiTenantContext Service Endpoint."""
        if not self._multi_tenant_context:
            self._multi_tenant_context = MultiTenantContextService(self)
        return self._multi_tenant_context

    @property
    def multi_tenant_ioc(self):
        """MultiTenantIoc (Indicator of Compromise) Service Endpoint."""
        if not self._multi_tenant_ioc:
            self._multi_tenant_ioc = MultiTenantIocService(self)
        return self._multi_tenant_ioc

    @property
    def nl_search(self):
        """NlSearch Service Endpoint."""
        if not self._nl_search:
            self._nl_search = NlSearchService(self)
        return self._nl_search

    @property
    def notebooks(self):
        """Notebooks Service Endpoint."""
        if not self._notebooks:
            self._notebooks = NotebooksService(self)
        return self._notebooks

    @property
    def notifications(self):
        """Notifications Service Endpoint."""
        if not self._notifications:
            self._notifications = NotificationsService(self)
        return self._notifications

    @property
    def preferences(self):
        """Preferences Service Endpoint."""
        if not self._preferences:
            self._preferences = PreferencesService(self)
        return self._preferences

    @property
    def process_tress(self):
        """Preferences Service Endpoint."""
        if not self._process_trees:
            self._process_trees = ProcessTreesService(self)
        return self._process_trees

    @property
    def queries(self):
        """Queries Service Endpoint."""
        if not self._queries:
            self._queries = QueriesService(self)
        return self._queries

    @property
    def roadrunner(self):
        """Roadrunner Service Endpoint."""
        if not self._roadrunner:
            self._roadrunner = RoadrunnerService(self)
        return self._roadrunner

    @property
    def rules(self):
        """Rules Service Endpoint."""
        if not self._rules:
            self._rules = RulesService(self)
        return self._rules

    @property
    def core(self):
        """Default Service Core"""
        if not self._core:
            self._core = ServiceCore(self)
        return self._core

    @property
    def sharelinks(self):
        """Sharelinks Service Endpoint."""
        if not self._sharelinks:
            self._sharelinks = SharelinksService(self)
        return self._sharelinks

    @property
    def subjects(self):
        """Subjects Service Endpoint."""
        if not self._subjects:
            self._subjects = SubjectsService(self)
        return self._subjects

    @property
    def tenant_profiles(self):
        """Tenant Profiles Service Endpoint."""
        if not self._tenant_profiles:
            self._tenant_profiles = TenantProfilesService(self)
        return self._tenant_profiles

    @property
    def tenants(self):
        """Tenants Service Endpoint."""
        if not self._tenants:
            self._tenants = TenantsService(self)
        return self._tenants

    @property
    def tenants4(self):
        """Tenants Service Endpoint."""
        if not self._tenants4:
            self._tenants4 = Tenants4Service(self)
        return self._tenants4

    @property
    def threat(self):
        """Threat Service Endpoint."""
        if not self._threat:
            self._threat = ThreatService(self)
        return self._threat

    @property
    def threat_score(self):
        """ThreatScore Service Endpoint."""
        if not self._threat_score:
            self._threat_score = ThreatScoreService(self)
        return self._threat_score

    @property
    def trigger_action(self):
        """Trigger Action Service Endpoint."""
        if not self._trigger_action:
            self._trigger_action = TriggerActionService(self)
        return self._trigger_action

    @property
    def trip(self):
        """Trip Service Endpoint."""
        if not self._trip:
            self._trip = TripService(self)
        return self._trip

    @property
    def users(self):
        """Users Service Endpoint."""
        if not self._users:
            self._users = UsersService(self)
        return self._users

    @property
    def vdr(self):
        """VDR Service Endpoint."""
        if not self._vdr:
            self._vdr = VDRService(self)
        return self._vdr
