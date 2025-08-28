from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from app.data import get_experiences
from app.dependencies import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home_section(request: Request):
    experiences = get_experiences()
    return templates.TemplateResponse(
        "pages/home.jinja",
        {"request": request, "experiences": experiences},
    )


@router.get("/projects", response_class=HTMLResponse)
async def projects_section(request: Request):
    return templates.TemplateResponse(
        "pages/projects.jinja",
        {"request": request},
    )


@router.get("/photos", response_class=HTMLResponse)
async def photos_section(request: Request):
    return templates.TemplateResponse(
        "pages/photos.jinja",
        {"request": request},
    )
