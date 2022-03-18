from typing import TYPE_CHECKING

from daemon.stores.pods import PodStore

if TYPE_CHECKING:
    pass


class DeploymentStore(PodStore):
    """A Store of Deployments spawned as Containers by Daemon"""

    _kind = 'deployment'
