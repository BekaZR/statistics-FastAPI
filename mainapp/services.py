from datetime import datetime
from pydantic import ValidationError

from mainapp.models import Statistic

from mainapp.schemas import Range

from core.database import database


async def average_cost_per_click(cost, clicks):
    if not clicks is None:
        return cost / clicks
    return 0

async def average_cost_per_thousand_impressions(cost, clicks):
    if not clicks is None:
        return cost / clicks * 1000
    return 0


async def get_statistic_analitic(start_date, end_date):
    if start_date > end_date:
        raise ValidationError({"Wrong data": "start date cannot be greater than end date"})
    
    query = Statistic.select().where(start_date < Statistic.c.date, end_date > Statistic.c.date)
    return await database.fetch_all(query)


async def to_representation(data: list):
    representation = []
    for x in data:
        representation.append(
            {
                "id": x.id,
                "date": x.date,
                "views": x.views,
                "cliscks": x.clicks,
                "cost": x.cost,
                "cpc": await average_cost_per_click(x.cost, x.clicks),
                "cpm": await average_cost_per_thousand_impressions(x.cost, x.clicks)
            }
        )
    return representation