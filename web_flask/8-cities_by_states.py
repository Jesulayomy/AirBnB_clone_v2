#!/usr/bin/python3
"""
    This module starts a simple flask application and sets the
    /states_list route to display a list of all states in the db
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Closes the storage session """

    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def city_states_route():
    """
        States and city list of all dump, all_states is a
        dictionary containing all state objects
    """

    states_dict = storage.all(State)
    return render_template('8-cities_by_states.html', all_states=states_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
