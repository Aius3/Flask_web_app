from datetime import datetime
from pydantic import BaseModel


class AutoSchema(BaseModel):
    id: int
    gamintojas: str
    modelis: str
    spalva: str
    metai: int
    variklis: str
    kaina: float
    sukurimo_data: datetime

    class Config:
        from_attributes = True