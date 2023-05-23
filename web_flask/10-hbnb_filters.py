#!/usr/bin/python3
"""
    This module starts a simple flask application and sets the
    /states_list route to display a list of all states in the db
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Closes the storage session """

    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_display():
    """ States list of all dump, all_states is a dictionary containing """

    stat_dict = storage.all("State")
    amenity_dict = storage.all("Amenity")

    return render_template(
            '10-hbnb_filters.html',
            states_dict=stat_dict,
            amenities_dict=amenity_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
