from pydantic import BaseModel, condecimal, Field, root_validator, ValidationError

from datetime import datetime


class StaticticAdd(BaseModel):
    date: datetime
    views: int
    clicks: int
    cost: condecimal(max_digits=6, decimal_places=2)


class StatisticBase(StaticticAdd):
    id: int
    
    class Config:
        orm_mode = True


class Range(BaseModel):
    start_date: datetime = Field(alias="from")
    end_date: datetime = Field(alias="to")
    
    
    class Config:
        orm_mode = True