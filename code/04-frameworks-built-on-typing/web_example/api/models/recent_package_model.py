import datetime

import pydantic


class RecentPackage(pydantic.BaseModel):
    name: str
    updated: datetime.datetime


class RecentPackagesModel(pydantic.BaseModel):
    count: int
    packages: list[RecentPackage]
