from fastapi import FastAPI

from Products.products import route

app = FastAPI()
app.include_router(route, prefix='/Products', tags=['Products'])

@app.get("/")
async def root():
    return {"Message" : "Welcome to FastAPI"}