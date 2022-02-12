import asyncio

import httpx
import pytest
from asgi_lifespan import LifespanManager
from fastapi import Query

from app import create_app
from app.controllers.weather import GeoData, WeatherController
from app.routers.weather.models import WeatherOut
from app.shared.enums import Units

app = create_app()

mock_data = {
    "temperature": "2.3 C",
    "units": "metric",
    "city": "Gothenburg",
    "country": "SE",
    "weather": "Clouds",
    "lat": 50,
    "lon": 30
}


async def get_by_city_override(city: str = Query(..., title="Name of the city",
                                                 regex="^[A-Za-z]+$"),
                               state: str | None = Query(None, title="State code if the US"),
                               country: str | None = Query(None, title="Country code such as 'uk'"),
                               units: Units = Query(default=Units.METRIC,
                                                    description="The units in which you want the temperature in")
                               ) -> WeatherOut:
    return WeatherOut(**mock_data)


async def get_by_coords_override(lat: float = Query(...,
                                                    ge=GeoData.MIN_LAT,
                                                    le=GeoData.MAX_LAT,
                                                    title="Latitude"),
                                 lon: float = Query(...,
                                                    ge=GeoData.MIN_LON,
                                                    le=GeoData.MAX_LON,
                                                    title="Longitude"),
                                 units: Units = Query(default=Units.METRIC)
                                 ) -> WeatherOut:
    return WeatherOut(**mock_data)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(name="client")
async def client_fixture():
    app.dependency_overrides[WeatherController.get_by_city] = get_by_city_override
    app.dependency_overrides[WeatherController.get_by_coords] = get_by_coords_override
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://test") as client:
            yield client
            app.dependency_overrides.clear()
