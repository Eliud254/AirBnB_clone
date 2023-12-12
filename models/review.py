#!/usr/bin/python3
"""The module that creates review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ The class manages the review objects"""

    place_id = ""
    user_id = ""
    text = ""
