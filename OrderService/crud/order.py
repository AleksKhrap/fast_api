from sqlalchemy.orm import Session
from OrderService.models import models, schemas


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()


def create_order(db: Session, product: schemas.OrderCreate):
    db_order = models.Order(**product.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderItem).offset(skip).limit(limit).all()


def create_order_item(db: Session, item: schemas.OrderItem, order_id: int):
    db_order_item = models.OrderItem(**item.model_dump(), order_item_id=order_id)
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item
