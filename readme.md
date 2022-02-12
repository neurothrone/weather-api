# Weather API Service

[demo]: https://zn-weather-api.herokuapp.com/

[fastapi]: https://fastapi.tiangolo.com/

[openweather]: https://openweathermap.org/

## About

A simplistic asynchronous Weather API service powered by [FastAPI][fastapi] that employs the
[OpenWeather][openweather] API to allow retrieval of current weather by city or coordinates.

## Demo

A working demo can be found at [Heroku][demo].

## Setup

1. Install packages from requirements.txt
2. Add an environment file called `.env` in the projects root directory with the following content:

```sh
# Get a key by creating an account at OpenWeather
OPEN_WEATHER_API_KEY=...
```

3. Execute the script `run.py` or run the following command in a terminal from the root project directory:

```sh
uvicorn run:app
```