from pydantic import BaseModel

class TransactionIn(BaseModel):
    username: str
    transaction_id: str
    amount: float

class Transaction(TransactionIn):
    pass
