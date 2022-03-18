from typing import TYPE_CHECKING, Dict, Optional

from daemon.stores.base import BaseStore
from daemon.stores.containers import ContainerStore
from daemon.stores.mixin import AiohttpMixin
from jina.helper import colored

if TYPE_CHECKING:
    from daemon.models import DaemonID


class FlowStore(ContainerStore, AiohttpMixin):
    """A Store of Flows spawned as Containers by Daemon"""

    _kind = 'flow'

    async def add_in_partial(
        self, uri: str, params: Dict, envs: Optional[Dict] = {}, **kwargs
    ) -> Dict:
        """Sends `POST` request to `partial-daemon` to create a Flow.

        :param uri: uri of partial-daemon
        :param params: Flow params
        :param envs: environment variables to be passed into partial flow
        :param kwargs: keyword args
        :return: response from POST request
        """
        ports = kwargs.get('ports', [])
        return await self.POST(
            url=f'{uri}/{self._kind}',
            params=None,
            json={'flow': params, 'ports': ports, 'envs': envs},
        )

    async def delete_in_partial(self, uri: str, **kwargs) -> Dict:
        """Sends a `DELETE` request to `partial-daemon` to terminate the Flow
        and, remove the container.

        :param uri: uri of partial-daemon
        :param kwargs: keyword args
        :return: response from DELETE request
        """
        return await self.DELETE(url=f'{uri}/{self._kind}')
