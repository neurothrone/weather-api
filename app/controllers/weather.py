from typing import Callable

from fastapi import HTTPException, status, Query
from httpx import Response

from app.routers.weather.models import WeatherOut
from app.services import weather_service
from app.shared.enums import Units


class GeoData:
    MIN_LAT: float = -90
    MAX_LAT: float = 90
    MIN_LON: float = -180
    MAX_LON: float = 80


class WeatherController:
    @classmethod
    async def _get_weather_response_or_400(cls,
                                           weather_request_func: Callable,
                                           *args
                                           ) -> Response:
        response: Response = await weather_request_func(*args)

        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Invalid args.")

        return response

    @classmethod
    async def _get_parsed_data(cls, data: dict, units: Units) -> dict:
        city = data.get("name")
        country = data.get("sys").get("country")
        temperature = f"{data['main']['temp']} {Units.get_symbol(units)}"
        weather = data["weather"][0]["main"]
        lon = data["coord"]["lon"]
        lat = data["coord"]["lat"]

        return dict(
            city=city,
            country=country,
            temperature=temperature,
            weather=weather,
            units=units,
            lon=lon,
            lat=lat
        )

    @classmethod
    async def get_by_city(cls,
                          city: str = Query(..., title="Name of the city",
                                            regex="^[A-Za-z]+$"),
                          state: str | None = Query(None, title="State code if the US"),
                          country: str | None = Query(None, title="Country code such as 'uk'"),
                          units: Units = Query(default=Units.METRIC,
                                               description="The units in which you want the temperature in")
                          ) -> WeatherOut:
        response = await cls._get_weather_response_or_400(
            weather_service.get_weather_by_city, city, state, country, units
        )
        parsed_data = await cls._get_parsed_data(response.json(), units)
        return WeatherOut(**parsed_data)

    @classmethod
    async def get_by_coords(cls,
                            lat: float = Query(...,
                                               ge=GeoData.MIN_LAT,
                                               le=GeoData.MAX_LAT,
                                               title="Latitude"),
                            lon: float = Query(...,
                                               ge=GeoData.MIN_LON,
                                               le=GeoData.MAX_LON,
                                               title="Longitude"),
                            units: Units = Query(default=Units.METRIC)
                            ) -> WeatherOut:
        response = await cls._get_weather_response_or_400(
            weather_service.get_weather_by_coords, lat, lon, units
        )
        parsed_data = await cls._get_parsed_data(response.json(), units)
        return WeatherOut(**parsed_data)
