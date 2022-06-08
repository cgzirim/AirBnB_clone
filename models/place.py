#!/usr/bin/python3
"""Define a class Place that inherits from BaseModel."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.
    Attributes:
        city_id (str): City id of the place.
        user_id (str): User id
        name (str): Place name
        description (str): Place description.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum amount of guests.
        price_by_night (int): Price by night
        latitude (float): Latitude of the place.
        longitude (float): Longitude of the place.
        amenity_ids (list of strings): List of amenity id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
