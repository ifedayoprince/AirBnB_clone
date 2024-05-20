#!/usr/bin/python3
"""
BaseModel module
Defines a base class for other models with common attributes and methods.
"""

from datetime import datetime
from models import storage
import uuid

class BaseModel:
    """
    A base class for all models.
    
    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments that may contain instance attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
        if kwargs:
            del kwargs["__class__"]
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
            self.__dict__.update(kwargs)
        else:
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        
        Returns:
            str: String representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        Converts instance attributes to a dictionary format.

        Returns:
            dict: Dictionary containing all instance attributes including the class name.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = datetime.isoformat(self.created_at)
        dict_copy["updated_at"] = datetime.isoformat(self.updated_at)
        return dict_copy

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.today()
        storage.save()
