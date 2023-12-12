#!/usr/bin/python3
"""The module for the FileStorage class.


 BaseModel recreation using dictionary representation
 Flow of serialization-deserialization explained using to_dict() and JSON conversion

 Python data structure, JSON string representation

 Implementation of FileStorage class to handle serialization and deserialization
 FileStorage attributes: __file_path (path to JSON file), __objects (dictionary to store instances)
 Public methods: all (returns __objects), new (sets obj in __objects), save (serializes __objects to JSON file),
                  reload (deserializes JSON file to __objects if it exists)

 Instructions to update models/__init__.py:
 Import file_storage.py, create a unique FileStorage instance 'storage', and call reload() method

 Instructions to update models/base_model.py:
 Import the variable 'storage'
 In save() method, call save() method of 'storage'
 In __init__() method, if it's a new instance, add a call to new() method on 'storage'

"""
import datetime
import json
import os


class FileStorage:

    """Class storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """The returns of the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """The returns of the dictionary of valid classes areferences"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Reloads stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """The returns of valid attributes and the types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
