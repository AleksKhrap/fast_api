from fastapi import FastAPI, Depends  # , HTTPException
from typing import List
from sqlalchemy.orm import Session
from OrderService.models import models, schemas
from OrderService.controllers.order import get_orders
from OrderService.models.database import engine
from OrderService.models.database import SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', response_model=List[schemas.Order])
async def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = get_orders(db, skip=skip, limit=limit)
    return orders


@app.post('/')
async def create_order(order: schemas.Order, db: Session = Depends(get_db)):
    db_order = models.Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
