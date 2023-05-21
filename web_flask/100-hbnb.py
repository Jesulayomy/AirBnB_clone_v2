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


@app.route('/hbnb', strict_slashes=False)
def hbnb_end():
    """ States list of all dump, all_states is a dictionary containing """

    amenity_dict = storage.all("Amenity")
    place_dict = storage.all("Place")
    state_dict = storage.all("State")
    """
    city_dict = storage.all("City")
    review_dict = storage.all("Review")
    user_dict = storage.all("User")
            reviews_dict=review_dict,
            users_dict=user_dict,
            cities_dict=city_dict,
    """

    return render_template(
            '100-hbnb.html',
            states_dict=state_dict,
            places_dict=place_dict,
            amenities_dict=amenity_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
