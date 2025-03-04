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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
