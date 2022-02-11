from pathlib import Path

import fastapi_jinja
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .config import settings
from .routers.open import router as open_router
from .routers.weather import router as weather_router

BASE_PATH = Path(__file__).resolve().parent
template_folder = str(BASE_PATH / "templates")
templates = Jinja2Templates(directory=template_folder)


def create_app() -> FastAPI:
    _app = FastAPI(title=settings.PROJECT_TITLE,
                   version=settings.PROJECT_VERSION)

    configure(_app)
    register_routers(_app)

    return _app


def configure(_app: FastAPI) -> None:
    fastapi_jinja.global_init(template_folder, auto_reload=True)
    _app.mount("/static", StaticFiles(directory=str(BASE_PATH / "static")), name="static")


def register_routers(_app: FastAPI) -> None:
    _app.include_router(open_router)
    _app.include_router(weather_router, prefix="/api/1.0", tags=["weather"])
