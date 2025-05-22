from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request

from app.models.controller import *
from app.api import get_random_users

users_router = APIRouter(prefix="/users", tags=["users"])

templates = Jinja2Templates(directory="app/templates")

@users_router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    all_users = get_all_users()
    context = {
        "users": [user.to_dict() for user in all_users],
        "count": len(all_users)
    }
    return templates.TemplateResponse(request, "index.html", context)

@users_router.post("/add", response_class= RedirectResponse, status_code=302)
async def load_users_handle(request: Request, number: int = Form()):
    new_users = get_random_users(number)
    add_new_users(new_users)
    return "/users"

@users_router.get("/random", response_class=HTMLResponse)
async def read_user_page(request: Request):
    context = {
        "user": get_random_user()
    }
    return templates.TemplateResponse(request, "user_page.html", context)

@users_router.get("/{user_id}", response_class=HTMLResponse)
async def read_user_page(request: Request, user_id: int):
    context = {
        "user": get_user_by_id(user_id)
    }
    return templates.TemplateResponse(request, "user_page.html", context)