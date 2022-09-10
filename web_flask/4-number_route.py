#!/usr/bin/python3
"""using flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hellob():
    """display hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def helloc(text):
    txt = text.replace('_', ' ')
    return 'C {}'.format(txt)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hellod(text='is cool'):
    txt = text.replace('_', ' ')
    return 'Python {}'.format(txt)


@app.route('/number/<n>', strict_slashes=False)
def hellon(n):
    if type(n) is int:
        return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
