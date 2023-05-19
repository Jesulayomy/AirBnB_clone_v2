#!/usr/bin/python3
"""
    This module starts a simple flask application and sets the
    /states_list route to display a list of all states in the db
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list_route():
    """ States list of all dump """

    states_list = storage.all(State)
    return render_template('7-states_list.html', all_states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
