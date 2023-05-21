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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_display(id=None):
    """ States list of all dump, all_states is a dictionary containing """

    states_dict = storage.all(State)

    new_dict = {value.id: value.name for value in states_dict.values()}
    if not id:
        return render_template('7-states_list.html', all_states=new_dict)

    state_id = str(id)
    if id in new_dict.keys():
        return render_template(
                '9-states.html',
                all_states=states_dict["State.{}".format(state_id)])
    else:
        return render_template(
                '9-states.html',
                all_states=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
