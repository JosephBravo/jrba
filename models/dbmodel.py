from datetime import datetime
from typing import Optional

from pydantic import BaseModel
import datetime


class DateTimeModel(BaseModel):
    created_at: datetime.datetime = datetime.datetime.now()

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()