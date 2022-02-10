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


""" 
response.json()
---------------
{'coord': {'lon': 11.9668, 'lat': 57.7072},
'weather': [{'id': 803,
          'main': 'Clouds',
          'description': 'broken clouds',
          'icon': '04n'}],
'base': 'stations',
'main': {'temp': 276.55,
      'feels_like': 272.42,
      'temp_min': 275.07,
      'temp_max': 278.15,
      'pressure': 1008,
      'humidity': 88},
'visibility': 10000,
'wind': {'speed': 5.14, 'deg': 220},
'clouds': {'all': 75},
'dt': 1644473934,
'sys': {'type': 2,
     'id': 2002867,
     'country': 'SE',
     'sunrise': 1644476109,
     'sunset': 1644508662},
'timezone': 3600,
'id': 2711537,
'name': 'Gothenburg',
'cod': 200}
"""
