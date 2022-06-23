# Auth Routes

from fastapi import APIRouter, Header
from pydantic import BaseModel, EmailStr
from utils.jwt_token import validate_token, write_token
from fastapi.responses import JSONResponse

# Models
from models.user import User, UserInLogin
from models.dbmodel import default
from routes.user import create_user, verify_password, get_user_by_email

# Utils
import datetime
import json

# Database
from config.db import conn

    
auth_routes = APIRouter()

@auth_routes.post("/sign_up")
async def sign_up(user: User):
    user_created = json.dumps(await create_user(user),
                sort_keys=True,
                indent=1,
                default=default)
    if user_created == 'null':
        return JSONResponse(
            content={"message": f"user {user.user} already exists in database. try another email"}, 
            status_code=400)
    return JSONResponse(content=json.loads(user_created), status_code=201)

@auth_routes.post("/login")
async def login(user: UserInLogin):
    userdb = conn.local.user.find_one({"user": user.user})
    if userdb == None:
        return JSONResponse(
            content={"message": f"user {user.user} is not registered in database"}, 
            status_code=400)
    elif user.user == userdb['user']:
        verify_password(user.password, userdb['password'])
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)

@auth_routes.post("/verify/token")
async def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)
