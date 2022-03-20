#!/usr/bin/python3
"""Module 9-states with /states/<id> route and teardown"""


from flask import Flask
from flask import escape
from flask import render_template
from models import storage
from models.state import State
from os import getenv


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays HTML template of all City"""
    id = ""
    return render_template('9-states.html', state_obj=id)


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id=""):
    """Displays HTML template of all City with Given state"""
    if id:
        states = storage.all(State)
        if "State." + id in states.keys():
            state_obj = states[id]
        else:
            id = ""
    return render_template('9-states.html', state_obj=id, id=id)


@app.teardown_appcontext
def tdown(exception):
    """removes current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    """app.debug = True"""
    app.run(host='0.0.0.0', port=5000)
