"""
If you need make new migration:
    For this file work Mark directory as sources root microservices/ProductService/product_app.
    In file models/models/py change import from:
        from ProductService.product_app.db.database import Base
    To:
        from product_app.db.database import Base
    Then input command:
        alembic revision --autogenerate -m "something migration name"
    Check generated file and if it's OK - input:
        alembic upgrade head
    And finally unmark all directories without microservices and return correct import in file models/models.py
"""
import asyncio
from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from product_app.models.models import Base

target_metadata = Base.metadata


def do_run_migrations(connection):
    context.configure(
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
        connection=connection,
        target_metadata=target_metadata,
        include_schemas=True,
        version_table_schema=target_metadata.schema,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost:5432/products", future=True)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


asyncio.run(run_migrations_online())

