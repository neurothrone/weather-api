from fastapi.responses import RedirectResponse

from . import router


@router.get("/")
async def root():
    return RedirectResponse("/docs")
