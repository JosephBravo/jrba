# Auth Routes

from fastapi import APIRouter, Header
from pydantic import BaseModel, EmailStr
from utils.jwt_token import validate_token, write_token
from fastapi.responses import JSONResponse

# Models
from models.user import User, UserInLogin
from models.dbmodel import default
from routes.user import create_user

import datetime
import json

    
auth_routes = APIRouter()

@auth_routes.post("/sign_up")
def sign_up(user: User):
    user = json.dumps(create_user(user),
                sort_keys=True,
                indent=1,
                default=default)
    return JSONResponse(content=json.loads(user), status_code=201)
    

@auth_routes.post("/login")
def login(user: UserInLogin):
    if user.user == "nelson@gmail.com":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)