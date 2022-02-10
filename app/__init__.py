from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers.open import router as open_router
from .routers.weather import router as weather_router


def create_app() -> FastAPI:
    _app = FastAPI()

    configure(_app)
    register_routers(_app)

    return _app


def configure(_app: FastAPI) -> None:
    _app.mount("/static", StaticFiles(directory="static"), name="static")


def register_routers(_app: FastAPI) -> None:
    _app.include_router(open_router)
    _app.include_router(weather_router, prefix="/api/1.0", tags=["weather"])
