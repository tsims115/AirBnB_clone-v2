#!/usr/bin/python3
"""Module 7-states_list with /states_list route and teardown"""


from flask import Flask
from flask import escape
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays HTML template of all State objects present"""
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def tdown(exception):
    """removes current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    """app.debug = True"""
    app.run(host='0.0.0.0', port=5000)
