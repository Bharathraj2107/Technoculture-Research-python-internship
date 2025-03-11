import os
import django
from fastapi import FastAPI
from expenses.views import router as expense_router
from starlette.staticfiles import StaticFiles

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expenses.settings")
django.setup()  # Initialize Django

# Create FastAPI instance
app = FastAPI()

# Include FastAPI router
app.include_router(expense_router)

# Serve static files
app.mount("/static", StaticFiles(directory="expenses/static"), name="static")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Expense Tracker API is running"}
