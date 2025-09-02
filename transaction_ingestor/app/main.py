from fastapi import FastAPI, HTTPException
from app.models import Transaction, TransactionIn
from app.database import insert_transaction, init_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/transaction")
async def create_transaction(transaction: TransactionIn):
    try:
        await insert_transaction(transaction)
        return {"status": "success"}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

