import datetime
from typing import Optional

import beanie
import pydantic
import pymongo


class Location(pydantic.BaseModel):
    state: Optional[str] = None
    country: Optional[str] = None


class User(beanie.Document):
    name: str
    email: str
    hash_password: Optional[str] = None
    created_date: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)
    last_login: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)
    profile_image_url: Optional[str] = None
    location: Location

    class Settings:
        name = 'users'
        indexes = [
            pymongo.IndexModel(keys=[("created_date", pymongo.DESCENDING)], name="created_date_descend"),
            pymongo.IndexModel(keys=[("last_login", pymongo.DESCENDING)], name="last_login_descend"),

            pymongo.IndexModel(keys=[("email", pymongo.ASCENDING)], name="email_ascend", unique=True),
        ]
