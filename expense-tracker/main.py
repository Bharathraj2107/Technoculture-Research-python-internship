from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import csv
from fastapi.responses import FileResponse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

expenses = []  # Reset expenses on restart
budget = 0

logger.info("Server started. Expenses list reset.")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Expense(BaseModel):
    name: str
    amount: float
    category: str
    date: str

class Budget(BaseModel):
    amount: float

# Reset data on server restart
expenses = []  # This should be empty when the server starts
budget = 0  # Reset budget

@app.post("/api/expenses/budget/")
async def set_budget(data: Budget):
    global budget
    budget = data.amount
    return {"budget": budget}

@app.post("/api/expenses/add/")
async def add_expense(expense: Expense):
    global budget
    total_spent = sum(exp.amount for exp in expenses)
    remaining_budget = budget - total_spent  # Remaining budget

    if expense.amount > remaining_budget:
        raise HTTPException(status_code=400, detail=f"Cannot add expense! Remaining budget: ${remaining_budget:.2f}")

    expenses.append(expense)
    return {"message": "Expense added successfully!", "remaining_budget": remaining_budget - expense.amount}

@app.get("/api/expenses/list/")
async def get_expenses(category: str = "All"):
    if category == "All":
        return expenses
    return [exp for exp in expenses if exp.category == category]

@app.get("/api/expenses/download/")
async def download_expenses():
    filename = "expenses.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Amount", "Category", "Date"])
        for exp in expenses:
            writer.writerow([exp.name, exp.amount, exp.category, exp.date])
    return FileResponse(filename, media_type='text/csv', filename="expenses.csv")
