import httpx
import pytest
from fastapi import status

from .conftest import mock_data


@pytest.mark.asyncio
async def test_get_weather_by_city(client: httpx.AsyncClient):
    params = dict(city="gothenburg")
    response = await client.get("/api/1.0/weather/city/", params=params)
    json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert json == mock_data


@pytest.mark.asyncio
async def test_get_weather_by_coords(client: httpx.AsyncClient):
    params = dict(lat=50, lon=30)
    response = await client.get("/api/1.0/weather/coords/", params=params)
    json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert json == mock_data
