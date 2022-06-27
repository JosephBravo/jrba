'''Account Models'''

from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr

# Models
from models.dbmodel import DateTimeModel

class StatusAccount(Enum):
    active = "active"
    pending = "pending"
    disabled = "disabled"
    deleted = "deleted"

class Account(DateTimeModel, BaseModel):
    id: Optional[str]
    user: EmailStr
    name: Optional[str]
    description: Optional[str]
    country: str
    balances: Optional[str] # Here joint with Balances Model
    status: Union[str, StatusAccount] = 'pending'
    
class AccountUpdate(DateTimeModel, BaseModel):
    status: Union[str, StatusAccount]
