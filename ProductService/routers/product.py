from fastapi import FastAPI
from ProductService.models import models
from ProductService.models.database import engine
from ProductService.models.schemas import Products

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

products: list[Products] = []


@app.get('/')
async def index():
    return 'ProductService работает'


@app.post('/')
async def create_product(product: Products):
    product.id = len(products) + 1
    products.append(product)
    return product


@app.delete('/{id}')
async def remove_product(id: int):
    for p in products:
        if id == p.id:
            products.remove(p)
    return products


@app.put('/')
async def update_product(product: Products):
    for i, p in enumerate(products):
        if product.id == p.id:
            products[i] = product
    return products
