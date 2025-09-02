import asyncpg
import os

def get_db_url():
    return f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@" \
           f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

async def get_all_transactions():
    conn = await asyncpg.connect(get_db_url())
    rows = await conn.fetch("SELECT * FROM transactions")
    await conn.close()
    return [dict(row) for row in rows]
