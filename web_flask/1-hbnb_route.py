#!/usr/bin/python3
"""
    This module starts a simple flask application
    and sets the / route and /hbnb route
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def web_root():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
