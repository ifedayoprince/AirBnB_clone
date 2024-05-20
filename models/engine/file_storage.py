#!/usr/bin/python3
"""
FileStorage module
Defines a class to handle serialization and deserialization of instances.
"""

import json

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects by <class name>.id.
    """
    
    __file_path = "file.json"
    __objects = dict()
    
    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        
        Args:
            obj: The object to add to __objects.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        with open(self.__file_path, "w") as file:
            current_objs = self.__objects.copy()
            for key in current_objs:
                current_objs[key] = current_objs[key].to_dict()

            json.dump(current_objs, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the file exists.
        """
        from models.classes import models
        
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    cls = models[class_name]
                    self.__objects[key] = cls(**value)
        except:
            return
