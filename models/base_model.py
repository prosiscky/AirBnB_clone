#!/usr/bin/python3
"""A file containing A parent class called 'BaseModel' """

import uuid
from datetime import datetime
import models

class BaseModel:
    """Definition of the 'BaseModel' class"""

    def __init__(self, *args, **kwargs):
        """This is the instance constructor"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)


    def __str__(self):
        """This method returns the user defined information
        about the instance created from this class"""

        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """The save() method creates a timestamp on changes
        made and saves it to the updated_at attribute"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """The to_dict() method adds the name of the instance
        created to the dictionary representation of the object
        created and ensures all the attributes as contained in
        __dict__ of the instance are in a format ready for
        serialization, hence
        It converts created_at and updated_at attributes from
        datetime class to str"""

        dict_cpy = self.__dict__.copy()
        dict_cpy["__class__"] = self.__class__.__name__
        dict_cpy["updated_at"] = self.created_at.isoformat()
        dict_cpy["created_at"] = self.created_at.isoformat()
        return dict_cpy
