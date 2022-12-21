from sqlalchemy import (
    Column, Integer, String, MetaData, Table, DateTime, Numeric
)

from core.database import MetaData

metadata = MetaData()


Statistic = Table(
    "statistic",
    metadata,
    Column("id", Integer, primary_key=True,),
    Column("date", DateTime(100), ),
    Column("views", Integer, ),
    Column("clicks", Integer, ),
    Column("cost", Numeric(6, 2), ),
)

