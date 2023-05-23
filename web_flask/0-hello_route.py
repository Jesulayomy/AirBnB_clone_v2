#!/usr/bin/python3
"""
    This module starts a simple flask application
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def web_flask():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
