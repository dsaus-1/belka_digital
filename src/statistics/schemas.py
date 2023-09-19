from pydantic import BaseModel, Field
from datetime import datetime


class GeneralSchemas(BaseModel):
    time: datetime
    value: float
