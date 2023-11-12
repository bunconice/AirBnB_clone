#!/usr/bin/python3
"""This module creates the User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing the city objects"""

    state_id = ""
    name = ""
