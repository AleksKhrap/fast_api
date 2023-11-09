from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from OrderService.app.models import models, schemas


async def get_orders(db: AsyncSession, skip: int, limit: int):
    db_products = await db.execute(select(models.Order).offset(skip).limit(limit))
    return db_products.scalars().all()
