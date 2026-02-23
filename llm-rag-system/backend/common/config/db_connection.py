import asyncpg
from backend.common.config.db_config import POSTGRES_CONFIG

async def get_db_connection():
    try:
        conn = await asyncpg.connect(
            host=POSTGRES_CONFIG["host"],
            port=POSTGRES_CONFIG["port"],
            user=POSTGRES_CONFIG["user"],
            password=POSTGRES_CONFIG["password"],
            database=POSTGRES_CONFIG["database"]
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise e