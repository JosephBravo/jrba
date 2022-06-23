# User Routes

from bson import ObjectId
from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from bson import ObjectId
from passlib.context import CryptContext
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from utils.verify_token import VerifyTokenRoute

# Database
from config.db import conn

# Models
from models.user import User

# Serializer
from serializers.user import userObject, usersEntity


user = APIRouter(route_class=VerifyTokenRoute)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@user.get('/users', response_model=list[User], tags=["users"])
async def list_users():
    return usersEntity(conn.local.user.find())

@user.get('/users/{id}', response_model=User, tags=["users"])
async def retrieve_user(id: str):
    return userObject(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.post('/users', response_model=User, tags=["users"])
async def create_user(user: User):
    new_user = dict(user)
    if conn.local.user.find_one({"user": user.user}) != None:
        return JSONResponse(
            content={"message": f"user {new_user['user']} already registered in database"}, 
            status_code=400)
    else:
        new_user["password"] = get_password_hash(new_user["password"])
        del new_user["id"]
        id = conn.local.user.insert_one(new_user).inserted_id
        return userObject(conn.local.user.find_one({"_id": id}))
        

@user.put("/users/{id}", response_model=User, tags=["users"])
async def update_user(id: str, user: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, 
                                        {"$set": dict(user)})
    return userObject(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_user(id: str):
    conn.local.user.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.get('/users/{email}', response_model=User, tags=["users"])
def get_user_by_email(email: str):
    return userObject(conn.local.user.find_one({"user": email}))

def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)

def get_password_hash(password):
    return pwd_context.hash(password) 
 