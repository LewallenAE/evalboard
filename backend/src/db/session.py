import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from psycopg_pool import AsyncConnectionPool

load_dotenv()

DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_DBNAME = os.environ.get("POSTGRES_DB")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DBNAME}"

pool = AsyncConnectionPool(conninfo = DATABASE_URL, open=False)


@asynccontextmanager
async def establish_db_connection():
    async with pool.connection() as conn:
        yield conn