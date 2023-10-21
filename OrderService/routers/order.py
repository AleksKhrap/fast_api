from fastapi import FastAPI, Depends  # , HTTPException
from typing import List
from sqlalchemy.orm import Session
from OrderService.models import models, schemas
# from OrderService.controllers.order import get_order
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


'''
@app.get('/', response_model=List[schemas.Product])
async def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products(db, skip=skip, limit=limit)
    return products


@app.post('/')
async def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    db_product = models.Products(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
    '''
