#!/usr/bin/python3
"""
    This module starts a simple flask application and sets the
    /states_list route to display a list of all states in the db
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Closes the storage session """

    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_display():
    """ States list of all dump, all_states is a dictionary containing """

    states_dict = storage.all(State)
    cities_dict = storage.all(City)
    amenities_dict = storage.all(Amenity)
    model_list = [states_dict, cities_dict, amenities_dict]

    return render_template('10-hbnb_filters.html', model_list=model_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
