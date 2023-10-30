from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ProductService.models import models, schemas
from ProductService.crud.products import get_products, get_product_by_name, create_product  # , get_product_by_id
from ProductService.models.database import engine, SessionLocal


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


@app.post('/', response_model=schemas.Product)
async def post_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = get_product_by_name(db, name=product.name)
    if db_product:
        raise HTTPException(status_code=400, detail="Name already added")
    return create_product(db=db, product=product)


'''
@app.delete('/{product_id}', response_model=schemas.Product)
async def remove_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return "Product deleted"


@app.put('/')
async def update_product(product: schemas.Product, db: Session = Depends(get_db)):
    db_product = db.query(models.Products).filter(models.Products.id == product.id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product
'''
