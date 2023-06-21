#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ

from models.engine.db_storage import DBStorage

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

dummy_classes = {"BaseModel": BaseModel, "User": User,
                 "Review": Review, "City": City,
                 "State": State, "Place": Place,
                 "Amenity": Amenity}

dummy_tables = {"states": State, "cities": City,
                "users": User, "places": Place,
                "reviews": Review, "amenities": Amenity
                }

storage_engine = environ.get("HBNB_TYPE_STORAGE")

if storage_engine == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
