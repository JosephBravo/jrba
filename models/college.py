from enum import Enum
from typing import List

from pydantic import BaseModel
from os import getenv


class CollegeEnum(Enum):
    college_a = "college_name_a"
    college_b = "college_name_b"
    college_c = "college_name_c"


class Colleges(BaseModel):
    colleges: List[CollegeEnum]