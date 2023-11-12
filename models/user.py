#!/usr/bin/python3
"""This module creates the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing the user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
