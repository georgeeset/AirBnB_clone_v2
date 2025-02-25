#!/usr/bin/python3
"""
Minimal module for  flask web application
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ Home Page """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
