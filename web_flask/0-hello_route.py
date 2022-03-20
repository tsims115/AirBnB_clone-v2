#!/usr/bin/python3
"""Module 0-hello_route with'/'"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    """app.debug = True"""
    app.run(host='0.0.0.0', port=5000)
