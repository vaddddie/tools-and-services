from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.requests import Request

from app.models.controller import *
from app.api import get_random_users
from app.routers.users import users_router

INITIAL_COUNT = 1000 # Начальное количество загружаемых пользователей

users = get_random_users(INITIAL_COUNT) # Получение данных из API

create_tables() # Пересоздание всех таблиц в базе данных
add_new_users(users) # Добавление данных в базу 

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(users_router)

@app.get("/", response_class= RedirectResponse, status_code=302)
async def root(requests: Request):
    return '/users'

