'''Withdraw Routes'''

from bson import ObjectId
from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from bson import ObjectId

from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from utils.verify_token import VerifyTokenRoute

# Database
from config.db import conn

# Models
from models.withdraw import Withdraw, WithdrawUpdate

# Serializer
from serializers.withdraw import withdrawObject, withdrawsEntity


withdraw_routes = APIRouter(route_class=VerifyTokenRoute)


@withdraw_routes.get('/withdraw', response_model=list[Withdraw], tags=["withdraw"])
async def list_withdraws():
    return withdrawsEntity(conn.local.withdraw.find())

@withdraw_routes.get('/withdraw/{id}', response_model=Withdraw, tags=["withdraw"])
async def retrieve_withdraw(id: str):
     return withdrawObject(conn.local.withdraw.find_one({"_id": ObjectId(id)}))

@withdraw_routes.post('/withdraw', response_model=Withdraw, tags=["withdraw"])
async def create_withdraw(withdraw: Withdraw):
    new_withdraw = dict(withdraw)
    del new_withdraw["id"]
    id = conn.local.withdraw.insert_one(new_withdraw).inserted_id
    return withdrawObject(conn.local.withdraw.find_one({"_id": id}))
        
@withdraw_routes.patch("/withdraw/{id}", response_model=WithdrawUpdate, tags=["withdraw"])
async def update_withdraw(id: str, withdraw: WithdrawUpdate):
    conn.local.withdraw.find_one_and_update({"_id": ObjectId(id)}, 
                                        {"$set": dict(withdraw)})
    return withdrawObject(conn.local.withdraw.find_one({"_id": ObjectId(id)}))

@withdraw_routes.delete("/withdraw/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["withdraw"])
async def delete_withdraw(id: str):
    conn.local.withdraw.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
