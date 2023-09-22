#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table, MetaData
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from os import getenv

metadata = Base.metadata

place_amenity = Table(
    "place_amenity",
    metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary="place_amenity", viewonly=False)

    else:

        @property
        def reviews(self):
            """Returns the list of Review instances with place_id
            equals to the current Place.id"""
            from models import storage

            all_reviews = storage.all(Review)
            related_reviews = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    related_reviews.append(review)
            return related_reviews

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on amenity_ids."""
            from models import storage

            return [storage.get(Amenity, amenity_id) for amenity_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Handles append method for adding an Amenity.id
            to amenity_ids."""

            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
