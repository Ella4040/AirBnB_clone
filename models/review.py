#!/usr/bin/python3
"""This contains the review information for the class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ The Review class from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
