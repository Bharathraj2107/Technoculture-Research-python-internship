from fastapi import APIRouter
from expenses.models import Expense
from expenses.serializers import ExpenseSchema
from django.db import transaction

router = APIRouter()

@router.post("/expenses/", response_model=ExpenseSchema)
def create_expense(expense: ExpenseSchema):
    with transaction.atomic():
        new_expense = Expense.objects.create(
            name=expense.name,
            amount=expense.amount,
            category=expense.category,
        )
    return ExpenseSchema.from_orm(new_expense)

@router.get("/expenses/", response_model=list[ExpenseSchema])
def list_expenses():
    expenses = Expense.objects.all()
    return [ExpenseSchema.from_orm(exp) for exp in expenses]
