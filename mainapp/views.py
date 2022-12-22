from fastapi import APIRouter
from mainapp.models import Statistic

from mainapp.schemas import Range, StaticticAdd, StatisticBase

from core.database import database

from mainapp.services import get_statistic_analitic, to_representation


router = APIRouter(tags=["statistic"])


@router.post("/statistic/add/", response_model=StatisticBase)
async def create_statistic(statistic: StaticticAdd):
    query = Statistic.insert().values(date=statistic.date, views=statistic.views, clicks=statistic.clicks, cost=statistic.cost)
    last_record_id = await database.execute(query)
    
    return {**statistic.dict(), 'id': last_record_id}


@router.post("/statistic/get/")
async def get_statistic_(range: Range):
    statisctic_db = await get_statistic_analitic(range.get("start_date"), range.get("end_date"))
    return await to_representation(statisctic_db)


@router.delete("/statistic/")
async def delete_statistic():
    query = Statistic.delete()
    await database.execute(query)
    return {"messages": "Statistic deleted"}
