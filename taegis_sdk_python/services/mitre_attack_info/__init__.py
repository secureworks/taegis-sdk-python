""""MitreAttackInfo Service."""

from taegis_sdk_python.service_core import ServiceCore
from taegis_sdk_python.services.mitre_attack_info.mutations import (
    TaegisSDKMitreAttackInfoMutation,
)
from taegis_sdk_python.services.mitre_attack_info.queries import (
    TaegisSDKMitreAttackInfoQuery,
)
from taegis_sdk_python.services.mitre_attack_info.subscriptions import (
    TaegisSDKMitreAttackInfoSubscription,
)


class MitreAttackInfoService(ServiceCore):
    """Taegis MitreAttackInfo Service."""

    @property
    def query(self):
        if not self._queries:
            self._queries = TaegisSDKMitreAttackInfoQuery(self)
        return self._queries

    @property
    def mutation(self):
        if not self._mutations:
            self._mutations = TaegisSDKMitreAttackInfoMutation(self)
        return self._mutations

    @property
    def subscription(self):
        if not self._subscriptions:
            self._subscriptions = TaegisSDKMitreAttackInfoSubscription(self)
        return self._subscriptions
