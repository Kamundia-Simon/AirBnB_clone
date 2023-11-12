#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id : state id
        name : name of the city
    """

    state_id = ""
    name = ""
