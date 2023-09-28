import pydantic


class StatsModel(pydantic.BaseModel):
    user_count: int
    package_count: int
    release_count: int
