from pydantic import BaseModel


class Weather(BaseModel):
    description: str
    category: str


class Wind(BaseModel):
    speed: float
    deg: int


class Forecast(BaseModel):
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    low: int
    high: int


class Location(BaseModel):
    city: str
    state: str
    country: str


class RateLimiting(BaseModel):
    unique_lookups_remaining: int
    lookup_reset_window: str


class WeatherForecast(BaseModel):
    weather: Weather
    wind: Wind
    units: str
    forecast: Forecast
    location: Location
    rate_limiting: RateLimiting
