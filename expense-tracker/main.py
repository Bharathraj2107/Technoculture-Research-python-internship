import os
import django
from fastapi import FastAPI

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expense.settings")

# Initialize Django
django.setup()

# Import Django-related components AFTER initializing Django
from expenses.api import router as expense_router

# Create FastAPI app
app = FastAPI()

# Include the Expense API router
app.include_router(expense_router, prefix="/api")