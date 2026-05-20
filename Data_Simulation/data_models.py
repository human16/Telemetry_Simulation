from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class DataModel(BaseModel):
    timestamp: datetime
    sensor_id: str
    run_id: str
    data_type: Literal["temp", "pressure", "vibration"]
    value: float