from datetime import datetime

import fastapi_jinja
from fastapi import Request
from fastapi.responses import HTMLResponse

from . import router


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
@fastapi_jinja.template("open/index.html")
async def root(request: Request):
    return dict(now=datetime.utcnow())
