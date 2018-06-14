import os 

import json

import pytest

import app

from .db import engine
from .db import Session

from .models import Base
from .models import Message

@pytest.fixture
def client():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    client = app.app.test_client()

    return client

def test_hello(client):
    response = client.get('/')
    data = json.loads(response.data.decode('utf-8'))
    assert data == { 'message': "Hello friend!" }

def test_messages(client):
    message = Message(message='Hello there!')

    Session.add(message)

    Session.commit()

    # This makes sure the test won't pass withoiut a Session.commit()
    Session.remove()

    response = client.get('/messages')

    data = json.loads(response.data.decode('utf-8'))
    assert data == [{'message': 'Hello there!'}]
