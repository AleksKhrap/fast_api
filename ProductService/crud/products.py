from sqlalchemy.orm import Session
from ProductService.models import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Products).offset(skip).limit(limit).all()


def get_product_by_name(db: Session, name: str):
    return db.query(models.Products).filter(models.Products.name == name).first()


def get_product_by_id(db: Session, product_id: str):
    return db.query(models.Products).filter(models.Products.product_id == product_id).first()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Products(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def remove_product(db: Session, product: schemas.Product):
    db_product = models.Products('?')  # Чекнуть как именно удалять элемент из базы
    db.delete(db_product)
    db.commit()
    return
