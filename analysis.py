import data_handler as dh
import matplotlib.pyplot as plt

def monthly_summary(month):
    data = dh.get_expenses()
    total = 0

    for e in data:
        if e["date"].startswith(month):
            total += e["amount"]

    print(f"Total expense for {month}: {total}")


def category_analysis():
    data = dh.get_expenses()
    categories = {}

    for e in data:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]

    print("\nCategory-wise spending:")
    for k, v in categories.items():
        print(k, ":", v)

    # Highest spending category
    max_cat = max(categories, key=categories.get)
    print(f"\nHighest spending category: {max_cat}")

    # Pie Chart
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()