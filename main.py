from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse


from routes import chambers_router

from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
app.mount("/kp", StaticFiles(directory="static", html=True), name="static")

app.include_router(chambers_router, prefix="/chambers")
# app.include_router(problems_router, prefix="/problems")


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient("127.0.0.1")
    app.mongodb = app.mongodb_client["known_problems"]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


@app.get("/")
async def read_root():
    return RedirectResponse("/kp")
