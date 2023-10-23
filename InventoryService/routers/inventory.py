from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from InventoryService.models import models, schemas
from InventoryService.models.database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


@app.get('', response_model=List[schemas.Inventory])
async def get_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()


@app.post('/new_inventory_item')
async def create_inventory_item(inventory: schemas.Inventory, db: Session = Depends(get_db)):
    db_inventory = models.Inventory(**inventory.model_dump())
    db.add(inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory
