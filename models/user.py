# User Models

from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr

# Models
from models.dbmodel import DateTimeModel
#from sqlmodel import sqlmodel
from models.role import RoleEnum
from models.college import CollegeEnum


class User(DateTimeModel, BaseModel):
    id: Optional[str]
    user: EmailStr
    name: Optional[str]
    surname: Optional[str]
    second_surname: Optional[str]
    password: str
    active: bool = True
    role: Union[str, RoleEnum] = 'standard'
    college: Union[str, CollegeEnum] = None
    
class UserInLogin(BaseModel):
    user: EmailStr
    password: str
