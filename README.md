Expense Tracker  built using **FastAPI**, **Django ORM**, and **MySQL**. It includes **Mypy**, **Ruff**, and **Poetry** for better code quality and dependency management.

📌 Project Overview

This Expense Tracker allows users to set a budget and track their expenses based on different categories. Users can:

* Set an initial budget.

* Add expenses with details like product name, amount, category, and date.

* Filter expenses based on category.

* Download expenses as a CSV file.

🚀 Technologies Used

* FastAPI (Backend API)

* Django ORM (Database Handling with MySQL)

* MySQL (Database)

* Pydantic (Data Validation)

* Type Hints & Mypy (Static Type Checking)

* Ruff (Linting & Formatting)

* Poetry (Dependency Management)

* HTML & CSS (Frontend)

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone <repository_url>
cd expense-tracker

2️⃣ Install Dependencies with Poetry

poetry install

3️⃣ Configure MySQL Database

Make sure MySQL is installed and running.

Create a database named expense_tracker.

Update DATABASES in settings.py with your MySQL credentials.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'expense_tracker',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

4️⃣ Apply Migrations

python manage.py migrate

5️⃣ Run the Servers in Separate Terminals

Start Django Server (Port 8001)

python manage.py runserver 8001

Start FastAPI Server (Port 9000)

uvicorn main:app --host 127.0.0.1 --port 9000

🎯 Features

1️⃣ Set Budget

Users can input an initial budget.

2️⃣ Add Expenses

Users can enter:

Product Name

Amount

Category (Dropdown: Food, Transport, Entertainment, Shopping, Other)

Date of Expense

Click on Add Expense

3️⃣ Filter Expenses

Users can filter expenses by category.

4️⃣ Expense List

A list displaying all the entered expenses.

5️⃣ Download CSV

Click on Download CSV to export all expenses as an Excel file.

📝 Notes

Mypy and Ruff are ignored in .gitignore, so you need to run them manually:

mypy .
ruff check .

If any issues arise, check database connections and dependencies.

Make sure to run both FastAPI and Django servers separately in the terminal.
