import json

from flask import Blueprint

from .db import Session

from .models import Message

hello_blueprint = Blueprint('hello', __name__)

@hello_blueprint.route('/')
def hello():
    return (json.dumps({ 'message': "Hello friend!" }), 
        200, { 'content_type': 'application/json'})

@hello_blueprint.route('/messages')
def messages():
    values = Session.query(Message).all()

    results = [{ 'message': value.message } for value in values]

    return (json.dumps(results), 200, { 'content_type': 'application/json' })

