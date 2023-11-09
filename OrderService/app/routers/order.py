from fastapi import APIRouter, Depends
from OrderService.app.models import models, schemas
from OrderService.app.db.database import AsyncSessionLocal, engine
from OrderService.app.db import crud
from sqlalchemy.ext.asyncio import AsyncSession
from main import CustomException

router = APIRouter()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.get('/', response_model=list[schemas.Order])
async def read_orders(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    pass


@router.post('/', response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate, db: AsyncSession = Depends(get_db)):
    pass


@router.put('/{order_id}', response_model=schemas.Order)
async def change_order(order_id: int, order: schemas.OrderUpdate, db: AsyncSession = Depends(get_db)):
    pass


@router.delete('/')
async def remove_order(order_id: int, order: schemas.Order, db: AsyncSession = Depends(get_db)):
    pass
