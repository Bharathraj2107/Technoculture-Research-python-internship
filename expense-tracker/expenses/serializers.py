from pydantic import BaseModel
from typing import Optional

class ExpenseSchema(BaseModel):
    id: Optional[int]
    name: str
    amount: float
    category: str
    date: Optional[str]

    class Config:
        from_attributes = True  # Maps Django ORM models to Pydantic
