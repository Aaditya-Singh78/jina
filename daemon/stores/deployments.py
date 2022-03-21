from daemon.stores.pods import PodStore


class DeploymentStore(PodStore):
    """A Store of Deployments spawned as Containers by Daemon"""

    _kind = 'deployment'
