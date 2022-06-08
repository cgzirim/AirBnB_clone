#!/usr/bin/python3
"""Define a class Amenity that inherits from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.
    Attributes:
        name (str): Name of amenity.
    """

    name = ""
