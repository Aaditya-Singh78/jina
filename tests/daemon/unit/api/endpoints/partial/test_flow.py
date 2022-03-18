from pathlib import Path

import pytest

from daemon.models import FlowModel
from jina import Client, Document

cur_dir = Path(__file__).parent
api = '/flow'


def test_flow_api(monkeypatch, partial_flow_client):
    flow_model = FlowModel()
    flow_model.uses = f'{cur_dir}/good_flow_dummy.yml'
    create_response = partial_flow_client.post(
        api, json={'flow': flow_model.dict(exclude={'log_config'})}
    )

    get_response = partial_flow_client.get(api)

    endpoint_responses = Client(port=56789, return_responses=True).post(
        on='/any_endpoint', inputs=Document()
    )

    delete_response = partial_flow_client.delete(api)

    assert create_response
    assert get_response
    assert get_response.json()['arguments']['port'] == 56789
    assert endpoint_responses[0].docs[0].content == 'https://jina.ai'
    assert delete_response
