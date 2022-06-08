#!/usr/bin/python3
"""Define a class City that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.
    Attributes:
        state_id (str): Id of the state of the city.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
