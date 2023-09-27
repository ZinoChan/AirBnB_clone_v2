#!/usr/bin/python3
"""This script starts a Flask web app"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def show_states():
    """renders a html page with states from storage"""
    states = storage.all(State)
    formatted_states = []
    for state in states.values():
        formatted_states.append({'id': state.id, 'name': state.name})
    return render_template('7-states_list.html', states=formatted_states)


@app.teardown_appcontext
def teardown(exception):
    """removes the current SQL Alchemy session
        Args:
            exception: holds information about any exception that occurs
            during request processing"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
