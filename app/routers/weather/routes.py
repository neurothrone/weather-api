from fastapi import Depends

from . import router
from app.controllers.weather import WeatherController, WeatherOut


@router.get("/weather/city/",
            response_model=WeatherOut,
            response_model_exclude_none=True)
async def read_weather_by_city(
        weather: WeatherOut = Depends(WeatherController.get_by_city)
):
    return weather


@router.get("/weather/coords/",
            response_model=WeatherOut)
async def read_weather_by_coords(
        weather: WeatherOut = Depends(WeatherController.get_by_coords)
):
    return weather
