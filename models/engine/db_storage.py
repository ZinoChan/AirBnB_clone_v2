#!/usr/bin/python3
""" DBStorage module """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
            pool_pre_ping=True,
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects"""
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            objs = []
            for cls in classes:
                objs.extend(self.__session.query(cls).all())

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Add object to current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload all tables and create session"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close sessions"""
        self.__session.close()
