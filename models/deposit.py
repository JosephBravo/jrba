# Deposit Models

from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr

# Models
from models.dbmodel import DateTimeModel
from models.user import User


class StatusDeposit(Enum):
    created = "created"
    settled = "settled"
    cancelled = "cancelled"
    rejected = "rejected"

class Deposit(DateTimeModel, BaseModel):
    id: Optional[str]
    bank_id: str
    currency: str
    amount: int
    reference: str
    status: Union[str, StatusDeposit] = 'created'
    
class DepositUpdate(DateTimeModel, BaseModel):
    bank_id: Optional[str]
    currency: Optional[str]
    amount: Optional[str]
    reference: Optional[str]
    status: Optional[str]
    