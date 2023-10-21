from fastapi import FastAPI, Depends  # , HTTPException
from typing import List
from sqlalchemy.orm import Session
from ProductService.models import models, schemas
from ProductService.controllers.products import get_products
from ProductService.models.database import engine
from ProductService.models.database import SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


'''@app.delete('/{id}')
async def remove_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return "Product deleted"


@app.put('/')
async def update_product(product: schemas.Products, db: Session = Depends(get_db)):
    db_product = db.query(models.Products).filter(models.Products.id == product.id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product'''
