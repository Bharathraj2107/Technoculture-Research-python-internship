from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from expenses.models import Expense  # Import after Django initialization
from expenses.serializers import ExpenseSchema

router = APIRouter()

class ExpenseCreate(BaseModel):
    name: str
    amount: float
    category: str

@router.post("/expenses/", response_model=ExpenseSchema)
def create_expense(expense: ExpenseCreate):
    new_expense = Expense.objects.create(
        title=expense.name,
        amount=expense.amount,
        category=expense.category,
    )
    return ExpenseSchema.model_validate(new_expense)

@router.get("/expenses/", response_model=List[ExpenseSchema])
def list_expenses():
    expenses = Expense.objects.all()
    return [ExpenseSchema.model_validate(exp) for exp in expenses]