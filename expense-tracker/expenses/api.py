from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from expenses.models import Expense  # Import after Django initialization

router = APIRouter()

class ExpenseSchema(BaseModel):
    id: int
    name: str
    amount: float
    category: str

    class Config:
        orm_mode = True

@router.post("/expenses/", response_model=ExpenseSchema)
def create_expense(expense: ExpenseSchema):
    new_expense = Expense.objects.create(
        title=expense.name,
        amount=expense.amount,
        category=expense.category,
    )
    return ExpenseSchema.from_orm(new_expense)

@router.get("/expenses/", response_model=List[ExpenseSchema])
def list_expenses():
    expenses = Expense.objects.all()
    return [ExpenseSchema.from_orm(exp) for exp in expenses]