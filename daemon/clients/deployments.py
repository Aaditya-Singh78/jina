from http import HTTPStatus
from typing import Dict, Optional, Union

import aiohttp

from daemon.clients.mixin import AsyncToSyncMixin
from daemon.clients.pods import AsyncPodClient
from daemon.helper import error_msg_from, if_alive
from daemon.models.id import DaemonID, daemonize


class AsyncDeploymentClient(AsyncPodClient):
    """Async Client to create/update/delete Deployments on remote JinaD"""

    _kind = 'deployment'
    _endpoint = '/deployments'


class DeploymentClient(AsyncToSyncMixin, AsyncDeploymentClient):
    """Client to create/update/delete Deployments on remote JinaD"""
