from fastapi import FastAPI

from model import Order
from orders import post_order, get_orders

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/orders")
async def order(detail: Order):
    return post_order(detail)


@app.get("/orders")
async def get_wait_order_uuid():
    return get_orders()
