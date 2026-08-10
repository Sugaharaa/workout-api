import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_URL is None:
    raise RuntimeError(
        "A variável de ambiente DATABASE_URL não foi configurada."
    )


engine = create_async_engine(DATABASE_URL)


SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session():
    async with SessionLocal() as session:
        yield session