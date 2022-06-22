# User Routes

from bson import ObjectId
from fastapi import APIRouter, status, Response
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT
from utils.verify_token import VerifyTokenRoute

# Database
from config.db import conn

# Models
from models.user import User

# Serializer
from serializers.user import userObject, usersEntity


user = APIRouter(route_class=VerifyTokenRoute)

@user.get('/users', response_model=list[User], tags=["users"])
async def list_users():
    # print(list(conn.local.user.find()))
    return usersEntity(conn.local.user.find())

@user.get('/users/{id}', response_model=User, tags=["users"])
async def retrieve_user(id: str):
    return userObject(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.post('/users', response_model=User, tags=["users"])
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
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
