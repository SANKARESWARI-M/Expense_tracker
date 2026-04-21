import data_handler as dh
import analysis as an

def menu():
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Analysis")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food/Travel/Bills/etc): ")
            amount = float(input("Enter amount: "))
            desc = input("Enter description: ")

            dh.add_expense(date, category, amount, desc)
            print(" Expense added!")

        elif choice == "2":
            expenses = dh.get_expenses()
            for e in expenses:
                print(e)

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            an.monthly_summary(month)

        elif choice == "4":
            an.category_analysis()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

menu()