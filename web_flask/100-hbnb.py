#!/usr/bin/python3
"""Starts a Flask web application.
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State
from models.place import Place
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display the HTML page for hbnb home page."""
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    states = storage.all(State)
    return render_template("100-hbnb.html",
                           amenities=amenities,
                           places=places,
                           states=states)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
