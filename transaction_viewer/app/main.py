from fastapi import FastAPI
from app.database import get_all_transactions

app = FastAPI()

@app.get("/transactions")
async def read_transactions():
    return await get_all_transactions()
