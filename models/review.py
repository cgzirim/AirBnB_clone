#!/usr/bin/python3
"""Define a class Review that inherits from BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a user's review.
    Attributes:
        place_id (str): Place id.
        user_id (str): User's id.
        text (str): Users review.
    """

    place_id = ""
    user_id = ""
    text = ""
