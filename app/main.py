from typing import List
from fastapi import FastAPI

from app import services
from app.schema import UserIn, BaseResponse, UserListOut

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello from FastAPI ;)"}


@app.post("/users", response_model=BaseResponse)
async def user_create(user: UserIn):
    try:
        services.add_userdata(user.dict())
    except:
        return {"success": False}
    return {"success": True}


@app.get("/users", response_model=UserListOut)
async def get_users():
    return services.read_usersdata()
