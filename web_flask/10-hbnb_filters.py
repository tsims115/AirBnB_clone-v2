#!/usr/bin/python3
"""Module 10-hbnb_filters with /hbnb_filters route and teardown"""


from flask import Flask
from flask import escape
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from os import getenv


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters(id=""):
    """Displays HTML template of all Amenity State, and city filters"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(
        '10-hbnb_filters.html', states=states, amenities=amenities
        )


@app.teardown_appcontext
def tdown(exception):
    """removes current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    """app.debug = True"""
    app.run(host='0.0.0.0', port=5000)
