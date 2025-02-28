#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """ index """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ hbnb route """
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """ /c route """
    return "C %s" % text.replace("_", " ")


@app.route('/python', defaults={"text": "is cool"})
@app.route('/python/<text>')
def python(text):
    """ python route """
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    """ number route """
    return "%d is a number" % n


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
