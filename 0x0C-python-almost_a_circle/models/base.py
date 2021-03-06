#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project
"""
import json
import os
from fileinput import filename
from logging import exception


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        ...
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        ...
        """
        if list_objs is None or len(list_objs) == 0:
            json_s = "[]"
        else:
            json_s = cls.to_json_string(
                [element.to_dictionary() for element in list_objs])
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(json_s)

    @staticmethod
    def from_json_string(json_string):
        """
        ...
        """
        if type(json_string) is not str or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        ...
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        ...
        """
        filename = f"{cls.__name__}.json"
        new_l = []
        new_dict = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                j = file.read()
                new_dict = cls.from_json_string(j)
                for i in new_dict:
                    new_l.append(cls.create(**i))
        return new_l
