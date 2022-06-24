# Deposit Routes

from bson import ObjectId
from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from bson import ObjectId

from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from utils.verify_token import VerifyTokenRoute

# Database
from config.db import conn

# Models
from models.deposit import Deposit, DepositUpdate

# Serializer
from serializers.deposit import depositObject, depositsEntity


deposit_routes = APIRouter(route_class=VerifyTokenRoute)


@deposit_routes.get('/deposit', response_model=list[Deposit], tags=["deposit"])
async def list_deposits():
    return depositsEntity(conn.local.deposit.find())

@deposit_routes.get('/deposit/{id}', response_model=Deposit, tags=["deposit"])
async def retrieve_deposi(id: str):
     return depositObject(conn.local.deposit.find_one({"_id": ObjectId(id)}))

@deposit_routes.post('/deposit', response_model=Deposit, tags=["deposit"])
async def create_deposit(deposit: Deposit):
    new_deposit = dict(deposit)
    del new_deposit["id"]
    id = conn.local.deposit.insert_one(new_deposit).inserted_id
    return depositObject(conn.local.deposit.find_one({"_id": id}))
        
@deposit_routes.patch("/deposit/{id}", response_model=DepositUpdate, tags=["deposit"])
async def update_deposit(id: str, deposit: DepositUpdate):
    conn.local.deposit.find_one_and_update({"_id": ObjectId(id)}, 
                                        {"$set": dict(deposit)})
    return depositObject(conn.local.deposit.find_one({"_id": ObjectId(id)}))

@deposit_routes.delete("/deposit/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["deposit"])
async def delete_deposit(id: str):
    conn.local.deposit.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
