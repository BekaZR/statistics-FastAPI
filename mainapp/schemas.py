from pydantic import BaseModel, condecimal

from datetime import datetime


class StaticticAdd(BaseModel):
    date: datetime
    views: int
    clicks: int
    cost: condecimal(max_digits=6, decimal_places=2)

    class Config:
        schema_extra = {
            "example": {
                "date": "2008-09-15T15:53:00+05:00",
                "views": 1,
                "clicks": 1,
                "cost": 2.3
            }
    }


class StatisticBase(StaticticAdd):
    id: int
    
    class Config:
        orm_mode = True