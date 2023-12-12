#!/usr/bin/python3
"""The module that creates  User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """The class that manages city objects"""

    state_id = ""
    name = ""
