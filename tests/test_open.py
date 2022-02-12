import httpx
import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_root(client: httpx.AsyncClient):
    response = await client.get("/")
    assert response.status_code == status.HTTP_200_OK
