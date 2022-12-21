from sqlalchemy import (
    create_engine, MetaData
)

from databases import Database

from core.settings import (
    POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD, 
    POSTGRES_PORT, POSTGRES_USER
)

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)

metadat = MetaData()

database = Database(DATABASE_URL)
