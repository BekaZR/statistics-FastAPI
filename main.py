from fastapi import FastAPI

from core.database import database

from mainapp.views import router

app = FastAPI()

@app.on_event('startup')
async def startapp():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(router)