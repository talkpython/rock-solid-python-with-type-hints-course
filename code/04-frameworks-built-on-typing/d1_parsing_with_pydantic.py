from typing import Optional

import pydantic


class Weather(pydantic.BaseModel):
    temp: float
    location: Optional[str] = None
    pressure: int
    humidity: int
    temp_range: list[int]


def main():
    data = {
        "temp": 60.44,
        # "location": "Portland, OR",
        # "location": ("Portland", "OR"), # <-- Error!
        "pressure": 1019.0,
        "humidity": 86,
        "temp_range": [56, "64"]
    }

    w = Weather(**data)
    print(w)


if __name__ == '__main__':
    main()
