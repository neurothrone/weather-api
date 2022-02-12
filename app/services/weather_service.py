import httpx

from app.config import settings
from app.shared.enums import Units

__API_KEY = settings.OPEN_WEATHER_API_KEY
__BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"


async def _get_weather(params: dict) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        return await client.get(__BASE_URL, params=params)


async def get_weather_by_coords(lat: float,
                                lon: float,
                                units: Units = Units.METRIC
                                ) -> httpx.Response:
    params = dict(
        appid=__API_KEY,
        lat=lat,
        lon=lon,
        units=units.value
    )
    return await _get_weather(params)


async def get_weather_by_city(city: str,
                              state: str | None,
                              country: str | None,
                              units: Units = Units.METRIC
                              ) -> httpx.Response:
    query = city
    if country:
        query += f",{country}"
        if state and country.lower() == "us":
            query += f",{state}"

    params = dict(
        appid=__API_KEY,
        q=query,
        units=units.value
    )
    return await _get_weather(params)
