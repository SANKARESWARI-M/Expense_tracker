import json
import os

FILE = "expenses.json"

def load_data():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return [] 

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(date, category, amount, description):
    data = load_data()
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    data.append(expense)
    save_data(data)

def get_expenses():
    return load_data()