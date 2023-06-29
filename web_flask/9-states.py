#!/usr/bin/python3
"""A python script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models import *


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Display a HTML page: (inside the tag BODY)"""
    # H1 tag: "States" inside the tag BODY
    # UL tag: with the list of all State objects present in DBStorage
    # LI tag: description of one State: <state.id>: <B><state.name></B>
    # LI tag: description of one City: <city.id>: <B><city.name></B>
    # sorted by name (A->Z)
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
