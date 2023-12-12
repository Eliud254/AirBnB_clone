#!/usr/bin/python3
"""The module that creates  User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """The class that manages user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
