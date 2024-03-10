from fastapi import FastAPI

from model import Order, OrderResponse
from orders import post_order, get_orders, cancel_order

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


@app.delete("/orders")
async def cancel_current_order(detail: OrderResponse):
    return cancel_order(detail)
