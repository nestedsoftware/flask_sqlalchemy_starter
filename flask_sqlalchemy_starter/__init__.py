from flask import Flask

from .db import Session

from .hello import hello_blueprint

app = Flask(__name__)
app.register_blueprint(hello_blueprint)

@app.teardown_appcontext
def teardown_db(resp_or_exc):
    Session.remove()

