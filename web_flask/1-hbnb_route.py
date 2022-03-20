#!/usr/bin/python3
"""Module 1-hbnb_route.py with app route '/' and '/hbnb'"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """returns hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbhn_route():
    """returns HBNB"""
    return 'HBNB'


if __name__ == "__main__":
    """app.debug = True"""
    app.run(host='0.0.0.0', port=5000)
