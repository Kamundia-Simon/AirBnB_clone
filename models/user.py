#!/bin/bash/python3
"""Write all those classes that inherit from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class representation of User

    Attributes:
        email : the email of the user.
        password : the password of the user.
        first_name : the first name of the user.
        last_name : the last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
