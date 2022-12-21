async def average_cost_per_click(cost, clicks):
    return cost / clicks

async def average_cost_per_thousand_impressions(cost, clicks):
    return cost / clicks * 1000

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