from weather_models import WeatherForecast


def main():
    data = {
        "weather":
            {
                "description": "broken clouds",
                "category": "Clouds"
            },
        "wind":
            {
                "speed": "7.0",
                "deg": 0
            },
        "units": "imperial",
        "forecast":
            {
                "temp": 59.95,
                "feels_like": 59.79,
                "pressure": 1019,
                "humidity": 88,
                "low": 56,
                "high": 63
            },
        "location":
            {
                "city": "Portland",
                "state": "OR",
                "country": "US"
            },
        "rate_limiting":
            {
                "unique_lookups_remaining": 49,
                "lookup_reset_window": "1 hour"
            }
    }

    w = WeatherForecast(**data)
    print(w)

    print(f"Right now it's {w.forecast.temp:,.0f} F and {w.weather.description}.")


if __name__ == '__main__':
    main()
