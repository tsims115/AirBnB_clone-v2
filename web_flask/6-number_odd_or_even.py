#!/usr/bin/python3
"""Module 1-hbnb_route.py with app route '/' and '/hbnb'"""
from flask import Flask
from flask import escape
from flask import render_template
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

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns Python is and <text>"""
    num = escape(n)
    if num.isdigit():
        return '%s is a number' % num

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Displays only if n is an int and renders template #5"""
    return render_template('5-number.html', num=escape(n))

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays only if n is an int and renders template #6"""
    return render_template('6-number_odd_or_even.html', num=int(escape(n)))

if __name__ == "__main__":
    """app.debug = True"""
    app.run(host = '0.0.0.0', port = 5000)