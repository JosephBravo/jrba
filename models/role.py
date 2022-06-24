# Role Models

from enum import Enum
from typing import List
from pydantic import BaseModel
from os import getenv


class RoleEnum(Enum):
    superuser = "superuser"
    standard = "standard"

class Roles(BaseModel):
    roles: List[RoleEnum]
    