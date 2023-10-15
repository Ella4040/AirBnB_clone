#!/usr/bin/python3
"""This contains the user information for the class"""
from models.base_model import BaseModel


class User(BaseModel):
     """ The User class from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
