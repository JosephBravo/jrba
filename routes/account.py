'''Account Routes'''

from bson import ObjectId
from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from bson import ObjectId

from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from utils.verify_token import VerifyTokenRoute

# Database
from config.db import conn

# Models
from models.account import Account, AccountUpdate

# Serializer
from serializers.account import accountObject, accountsEntity


account_routes = APIRouter(route_class=VerifyTokenRoute)


@account_routes.get('/account', response_model=list[Account], tags=["account"])
async def list_accounts():
    return accountsEntity(conn.local.account.find())

@account_routes.get('/account/{id}', response_model=Account, tags=["account"])
async def retrieve_account(id: str):
     return accountObject(conn.local.account.find_one({"_id": ObjectId(id)}))

@account_routes.post('/account', response_model=Account, tags=["account"])
async def create_account(account: Account):
    new_account = dict(account)
    del new_account["id"]
    id = conn.local.account.insert_one(new_account).inserted_id
    return accountObject(conn.local.account.find_one({"_id": id}))
        
@account_routes.patch("/account/{id}", response_model=AccountUpdate, tags=["account"])
async def update_account(id: str, account: AccountUpdate):
    conn.local.account.find_one_and_update({"_id": ObjectId(id)}, 
                                        {"$set": dict(account)})
    return accountObject(conn.local.account.find_one({"_id": ObjectId(id)}))

@account_routes.delete("/account/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["account"])
async def delete_account(id: str):
    conn.local.account.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
