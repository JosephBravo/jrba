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

    
auth_routes = APIRouter()

@auth_routes.post("/sign_up")
def sign_up(user: User):
    user = json.dumps(create_user(user),
                sort_keys=True,
                indent=1,
                default=default)
    if user == 'null':
        return JSONResponse(content={"message": "user already registered in database"}, status_code=400)
    return JSONResponse(content=json.loads(user), status_code=201)

@auth_routes.post("/login")
def login(user: UserInLogin):
    userdb = get_user_by_email(user.user) # When user is bad handle error

    if user.user == userdb['user']:
        passvery = verify_password(user.password, userdb['password'])
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)

@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)