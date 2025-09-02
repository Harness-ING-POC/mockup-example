import asyncpg
import os
from app.models import TransactionIn

def get_db_url():
    return f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@" \
           f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

async def init_db():
    conn = await asyncpg.connect(get_db_url())
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            username TEXT,
            transaction_id TEXT PRIMARY KEY,
            amount FLOAT
        )
    """)
    await conn.close()

async def insert_transaction(transaction: TransactionIn):
    conn = await asyncpg.connect(get_db_url())
    await conn.execute("""
        INSERT INTO transactions (username, transaction_id, amount)
        VALUES ($1, $2, $3)
    """, transaction.username, transaction.transaction_id, transaction.amount)
    await conn.close()
