from datetime import datetime
from fastapi import APIRouter, HTTPException
from OrderService.order_app.models import schemas
from OrderService.order_app.db.database import database
from OrderService.order_app.db import crud
from aiokafka import AIOKafkaProducer
import json

router = APIRouter()


# Отправка сообщения в kafka
async def send_to_kafka(kafka_order_data):
    # Инициализация KafkaProducer
    producer = AIOKafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    try:
        await producer.start()
        # Отправляем сообщение в тему Kafka
        await producer.send_and_wait('order_topic', value=kafka_order_data)
    finally:
        await producer.stop()


# Создание заказа
@router.post('/create_order', response_model=schemas.Order)
async def add_order(order: schemas.OrderCreate):
    order_products = []
    total_cost = 0.0

    async with database.start_session() as session:
        async with session.start_transaction():
            product = await crud.read_product_info(order.product_id)
            available_quantity = int(product.quantity_on_inventory) if product is not None else 0

            if product.quantity > available_quantity:
                raise HTTPException(
                    status_code=400,
                    detail=f"Недостаточное количество товара '{product.product_name}' на складе"
                )

            total_cost += product.current_price * product.quantity

            order_products.append({
                "product_id": product.product_id,
                "product_name": product.product_name,
                "quantity": product.quantity,
                "cost": product.current_price
            })

            await crud.update_inventory(product.product_id, available_quantity - product.quantity)

            new_order = {
                "order_date": order.order_date,
                "products": order_products,
                "total_cost": total_cost
            }

            # Сохранение заказа в MongoDB
            await database.orders.insert_one(new_order)

            # Отправка асинхронного сообщения в Kafka
            kafka_order_data = {
                "order_id": str(new_order["_id"]),
                "order_date": new_order["order_date"],
                "total_cost": new_order["total_cost"],
                "products": new_order["products"]
            }

            await send_to_kafka(kafka_order_data)

            return new_order


@router.delete("/cancel_order/{order_id}")
async def cancel_order(order_id: str):
    order = await database.orders.find_one({"_id": order_id})

    if order is None:
        raise HTTPException(status_code=404, detail=f"Заказ с id {order_id} не найден")

    await database.orders.delete_one({"_id": order_id})

    # Отправляем сообщение об отмене заказа в Kafka
    kafka_cancel_data = {
        "order_id": order_id,
        "cancelled_at": datetime.utcnow().isoformat(),
        "products": order["products"]
    }

    await send_to_kafka(kafka_cancel_data)

    return "Заказ успешно удален"
