from fastapi import APIRouter
from expenses.models import Expense
from expenses.serializers import ExpenseSchema
from django.db import transaction
from django.shortcuts import render
router = APIRouter()#here we are creating the instance of the router


def index(request):
    return render(request, "index.html")

@router.post("/expenses/", response_model=ExpenseSchema)#Ensures the API returns data in the correct format.
def create_expense(expense: ExpenseSchema):#expense = ExpenseSchema(name="Groceries", amount=50.0, category="Food")

    with transaction.atomic():#prevent data inconsistencies.Ensures that either all changes are saved or none at all.Prevents incomplete data from being saved if something fails.
        new_expense = Expense.objects.create(
            name=expense.name,#from above instance we are taking the data
            amount=expense.amount,
            category=expense.category,
        )
    return ExpenseSchema.from_orm(new_expense)#Converts the Django model (new_expense) into a Pydantic schema.Ensures the API response matches the expected format.

@router.get("/expenses/", response_model=list[ExpenseSchema])#Returns a list of expenses, each formatted using ExpenseSchema.
def list_expenses():
    expenses = Expense.objects.all()
    return [ExpenseSchema.from_orm(exp) for exp in expenses]#Converts each Django ORM object into a Pydantic schema.Ensures the response is properly structured as JSON.
