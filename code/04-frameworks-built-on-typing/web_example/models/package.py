import datetime
from typing import Optional

import beanie as beanie
import pydantic
import pymongo


class Release(pydantic.BaseModel):
    major_ver: int
    minor_ver: int
    build_ver: int
    created_date: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)
    comment: Optional[str] = None
    url: Optional[str] = None
    size: int


class Package(beanie.Document):
    id: str
    created_date: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)
    last_updated: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)
    summary: str
    description: str
    home_page: Optional[str] = None
    docs_url: Optional[str] = None
    package_url: Optional[str] = None
    author_name: Optional[str] = None
    author_email: Optional[str] = None
    license: Optional[str] = None
    releases: list[Release]
    maintainer_ids: list[beanie.PydanticObjectId]

    class Settings:
        name = 'packages'
        indexes = [
            pymongo.IndexModel(keys=[('last_updated', pymongo.DESCENDING)], name='last_updated_descending'),
            pymongo.IndexModel(keys=[("created_date", pymongo.ASCENDING)], name="created_date_ascend"),
            pymongo.IndexModel(keys=[("releases.created_date", pymongo.ASCENDING)],
                               name="releases_created_date_ascend"),
            pymongo.IndexModel(keys=[("author_email", pymongo.ASCENDING)], name="author_email_ascend"),

            pymongo.IndexModel(keys=[("releases.major_ver", pymongo.ASCENDING)], name="releases_major"),
            pymongo.IndexModel(keys=[("releases.minor_ver", pymongo.ASCENDING)], name="releases_minor"),
            pymongo.IndexModel(keys=[("releases.build_ver", pymongo.ASCENDING)], name="releases_build"),

            pymongo.IndexModel(keys=[
                ("releases.major_ver", pymongo.ASCENDING),
                ("releases.minor_ver", pymongo.ASCENDING),
                ("releases.build_ver", pymongo.ASCENDING)
            ],
                name="releases_version_ascending"),
        ]


class PackageTopLevelOnly(pydantic.BaseModel):
    id: str
    last_updated: datetime.datetime
    summary: str

    class Settings:
        projection = {
            "id": "$_id",
            "summary": "$summary",
            "last_updated": "$last_updated",
        }
