#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask, render_template
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


@app.route('/number_template/<int:n>')
def number_template(n):
    """ number_template route """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
