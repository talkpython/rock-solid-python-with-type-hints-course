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
                "speed": 5.99,
                "deg": 0
            },
        "units": "imperial",
        "forecast":
            {
                "temp": 60.44,
                "feels_like": 60.22,
                "pressure": 1019,
                "humidity": 86,
                "low": 56,
                "high": "64"
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

    print(f"Right now it's {w.weather.description} and {w.forecast.temp:.0f} F degrees.")


if __name__ == '__main__':
    main()
