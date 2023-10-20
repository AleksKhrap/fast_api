from fastapi import FastAPI, HTTPException
from .models import Order, OrderItem
from .database import create_order, read_order

app = FastAPI()


@app.post("/orders")
async def create_order(order: Order):
    order_id = create_order(order)
    if order_id:
        return order_id
    else:
        raise HTTPException(status_code=500, detail="Ошибка при создании заказа")


@app.get("/orders/{order_id}")
async def read_order(order_id: str):
    order = read_order(order_id)
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="Заказ не найден")
