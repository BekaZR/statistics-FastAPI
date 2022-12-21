from fastapi import APIRouter
from mainapp.models import Statistic

from mainapp.schemas import Range, StaticticAdd, StatisticBase, StatisticCrm

from core.database import database

from datetime import datetime

from mainapp.services import average_cost_per_click, to_representation


router = APIRouter(tags=["statistic"])


@router.post("/statistic/add/", response_model=StatisticBase)
async def create_statistic(statistic: StaticticAdd):
    query = Statistic.insert().values(date=statistic.date, views=statistic.views, clicks=statistic.clicks, cost=statistic.cost)
    last_record_id = await database.execute(query)
    
    return {**statistic.dict(), 'id': last_record_id}


@router.post("/statistic/get/")
async def get_statistic_(range: Range):
    start_date = datetime.strptime(range.get("start_date"), "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(range.get("end_date"), "%Y-%m-%d %H:%M:%S")
    query = Statistic.select().where(start_date < Statistic.c.date, end_date > Statistic.c.date)
    statisctic_db = await database.fetch_all(query)
    
    return await to_representation(statisctic_db)


@router.delete("/statistic/")
async def delete_statistic():
    query = Statistic.delete()
    await database.execute(query)
    return {"messages": "Statistic deleted"}
