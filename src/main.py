from importlib.metadata import version
from fastapi import FastAPI

from Products.products import route

v = "v1"

app = FastAPI(
    title = "FastAPI & MySQL",
    description="A REST API for web service",
    version = v
)
app.include_router(route, prefix='/Products', tags=['Products'])

@app.get("/")
async def root():
    return {"Message" : "Welcome to FastAPI"}