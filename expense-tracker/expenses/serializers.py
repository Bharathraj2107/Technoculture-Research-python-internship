from pydantic import BaseModel
from typing import Optional

class ExpenseSchema(BaseModel):
    id: Optional[int]
    name: str
    amount: float
    category: str
    date: Optional[str]#The Optional keyword means this field is not required. If the field is missing, it will default to None

    class Config:
        from_attributes = True  # This allows the Pydantic model to be created directly from an ORM model ( Django model).It enables automatic mapping of ORM attributes to Pydantic fields.Maps Django ORM models to Pydantic
