'''Withdraw Models'''

from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr, AnyUrl

# Models
from models.dbmodel import DateTimeModel
from models.user import User


class Withdraw(DateTimeModel, BaseModel):
    id: Optional[str]
    account_id: str
    currency: str
    amount: int
    bank_data: Optional[str]
    redirect_uri: Optional[AnyUrl]
    in_review: bool = False
    
class WithdrawUpdate(DateTimeModel, BaseModel):
    in_review: bool
    