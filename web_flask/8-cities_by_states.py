#!/usr/bin/python3
"""Module 8-cities_by_states with /cities_by_states route and teardown"""


from flask import Flask
from flask import escape
from flask import render_template
from models import storage
from models.state import State
from os import getenv


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays HTML template of all State objects present"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def tdown(exception):
    """removes current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    """app.debug = True"""
    app.run(host='0.0.0.0', port=5000)
