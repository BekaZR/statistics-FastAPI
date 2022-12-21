from fastapi import APIRouter
from mainapp.models import Statistic

from mainapp.schemas import StaticticAdd, StatisticBase

from core.database import database

router = APIRouter(tags=["statistic"])


@router.post("/statistic/", )
async def create_statistic(statistic: StaticticAdd):
    query = Statistic.insert().values(date=statistic.date, views=statistic.views, clicks=statistic.clicks, cost=statistic.cost)
    last_record_id = await database.execute(query)
    
    return {**statistic.dict(), 'id': last_record_id}


