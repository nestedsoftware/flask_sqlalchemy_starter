import pytest

import json

from flask_sqlalchemy_starter import create_app

@pytest.fixture
def client():
    client = create_app().test_client()
    yield client

def test_hello(client):
    response = client.get('/')
    data = json.loads(response.data.decode('utf-8'))
    assert data == { 'message': "Hello friend!" }
