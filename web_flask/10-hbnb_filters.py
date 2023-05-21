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


@app.teardown_appcontext
def teardown_session(exception):
    """ Closes the storage session """

    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_display():
    """ States list of all dump, all_states is a dictionary containing """

    states_dict = storage.all(State)
    cities_dict = storage.all(Cities)
    amenities_dict = storage.all(Amenities)
    models = [states_dict, cities_dict, amenities_dict]

    return render_template('10-hbnb_filters.html', models=models)
