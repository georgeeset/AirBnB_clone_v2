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

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
