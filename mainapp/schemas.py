from pydantic import BaseModel, condecimal, Field, root_validator, ValidationError

from datetime import datetime


class StaticticAdd(BaseModel):
    date: datetime
    views: int
    clicks: int
    cost: condecimal(max_digits=6, decimal_places=2)

    class Config:
        schema_extra = {
            "example": {
                "date": "2022-12-31 01:00:00",
                "views": 1,
                "clicks": 1,
                "cost": 2.3
            }
    }


class StatisticBase(StaticticAdd):
    id: int
    
    class Config:
        orm_mode = True


class StatisticCrm(StatisticBase):
    cpc: float
    cpm: float
    
    class Config:
        orm_mode = True


class Range(BaseModel):
    start_date: datetime
    end_date: datetime
    
    
    class Config:
        
        schema_extra = {
            "example": {
                "start_date": "2022-12-31 00:00:00",
                "end_date": "2022-12-31 01:00:00",
                }
            }
    
    @root_validator
    def validate(cls, values):
        start_date = values.get("start_date")
        end_date = values.get("end_date")
        
        if end_date < start_date:
            raise ValidationError(
                {"Wrong data": "start date cannot be greater than end date"}
                )
        return values
    
    
