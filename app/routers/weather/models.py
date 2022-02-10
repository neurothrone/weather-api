from pydantic import BaseModel, Field

from app.shared.enums import Units


class LocationBase(BaseModel):
    units: Units = Units.METRIC


class CityLocation(BaseModel):
    city: str
    state: str | None = Field(default=None, max_length=3)
    country: str | None = None

    class Config:
        schema_extra = {
            "example": {
                "city": "gothenburg"
            }
        }


class CoordsLocation(LocationBase):
    lat: float
    lon: float

    class Config:
        schema_extra = {
            "example": {
                "lat": "50",
                "lon": "30"
            }
        }


class WeatherOut(BaseModel):
    temperature: str
    city: str | None = None
    country: str | None = None
    lat: float | None = None
    lon: float | None = None
