#!/usr/bin/python3
"""Module 1-hbnb_route.py with app route '/' and '/hbnb'"""
from flask import Flask
from flask import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """returns hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbhn_route():
    """returns HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays c <text>"""
    ntext = escape(text).replace("_", " ")
    return 'c %s' % ntext

@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """returns Python is and <text>"""
    ntext = escape(text).replace("_", " ")
    return 'Python %s' % ntext

if __name__ == "__main__":
    """app.debug = True"""
    app.run(host = '0.0.0.0', port = 5000)
