#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a HTML page with a list
    of states and their cities sorted by name"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
