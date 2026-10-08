
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime


FILE_NAME = "expenses.csv"


# ---------------------------------------------------------
# Create CSV file if it does not exist
# ---------------------------------------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        data = pd.DataFrame(columns=[
            "Date",
            "Type",
            "Category",
            "Amount",
            "Description"
        ])
        data.to_csv(FILE_NAME, index=False)


# ---------------------------------------------------------
# Add a transaction
# ---------------------------------------------------------
def add_transaction():
    print("\n========== ADD TRANSACTION ==========")

    transaction_type = input("Enter type (Income/Expense): ").strip().title()

    if transaction_type not in ["Income", "Expense"]:
        print("Invalid type. Please enter Income or Expense.")
        return

    category = input("Enter category: ").strip().title()

    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    description = input("Enter description: ").strip()

    date = datetime.now().strftime("%Y-%m-%d")

    new_data = pd.DataFrame([{
        "Date": date,
        "Type": transaction_type,
        "Category": category,
        "Amount": amount,
        "Description": description
    }])

    data = pd.read_csv(FILE_NAME)
    data = pd.concat([data, new_data], ignore_index=True)
    data.to_csv(FILE_NAME, index=False)

    print("\nTransaction added successfully!")


# ---------------------------------------------------------
# Display all transactions
# ---------------------------------------------------------
def view_transactions():
    print("\n========== ALL TRANSACTIONS ==========")

    data = pd.read_csv(FILE_NAME)

    if data.empty:
        print("No transactions found.")
        return

    print(data.to_string(index=False))


# ---------------------------------------------------------
# Show financial summary
# ---------------------------------------------------------
def show_summary():
    print("\n========== FINANCIAL SUMMARY ==========")

    data = pd.read_csv(FILE_NAME)

    if data.empty:
        print("No transactions available.")
        return

    income = data.loc[data["Type"] == "Income", "Amount"].sum()
    expenses = data.loc[data["Type"] == "Expense", "Amount"].sum()
    balance = income - expenses

    print(f"Total Income   : ₹{income:.2f}")
    print(f"Total Expenses : ₹{expenses:.2f}")
    print(f"Balance        : ₹{balance:.2f}")

    if balance > 0:
        print("Status         : You are within your income.")
    elif balance == 0:
        print("Status         : Income and expenses are equal.")
    else:
        print("Status         : Expenses are higher than income.")


# ---------------------------------------------------------
# Show expense category analysis
# ---------------------------------------------------------
def category_analysis():
    print("\n========== EXPENSE CATEGORY ANALYSIS ==========")

    data = pd.read_csv(FILE_NAME)

    expense_data = data[data["Type"] == "Expense"]

    if expense_data.empty:
        print("No expenses available.")
        return

    category_totals = expense_data.groupby(
        "Category"
    )["Amount"].sum().sort_values(ascending=False)

    print(category_totals.to_string())

    print("\nHighest spending category:")
    print(f"{category_totals.index[0]} - ₹{category_totals.iloc[0]:.2f}")


# ---------------------------------------------------------
# Generate expense chart
# ---------------------------------------------------------
def generate_chart():
    print("\n========== GENERATING CHART ==========")

    data = pd.read_csv(FILE_NAME)

    expense_data = data[data["Type"] == "Expense"]

    if expense_data.empty:
        print("No expense data available.")
        return

    category_totals = expense_data.groupby(
        "Category"
    )["Amount"].sum()

    plt.figure(figsize=(9, 6))

    category_totals.plot(
        kind="bar",
        title="Expense by Category"
    )

    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("expense_chart.png")

    print("Chart saved as 'expense_chart.png'.")

    plt.show()


# ---------------------------------------------------------
# Search transactions
# ---------------------------------------------------------
def search_transactions():
    print("\n========== SEARCH TRANSACTIONS ==========")

    keyword = input("Enter category or description to search: ").strip().lower()

    data = pd.read_csv(FILE_NAME)

    if data.empty:
        print("No transactions available.")
        return

    results = data[
        data["Category"].str.lower().str.contains(keyword, na=False)
        |
        data["Description"].str.lower().str.contains(keyword, na=False)
    ]

    if results.empty:
        print("No matching transactions found.")
    else:
        print("\nMatching transactions:")
        print(results.to_string(index=False))


# ---------------------------------------------------------
# Main menu
# ---------------------------------------------------------
def main():
    initialize_file()

    while True:
        print("\n")
        print("==========================================")
        print("       SMART EXPENSE TRACKER")
        print("==========================================")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Financial Summary")
        print("4. Category Analysis")
        print("5. Generate Expense Chart")
        print("6. Search Transactions")
        print("7. Exit")
        print("==========================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_transaction()

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            show_summary()

        elif choice == "4":
            category_analysis()

        elif choice == "5":
            generate_chart()

        elif choice == "6":
            search_transactions()

        elif choice == "7":
            print("\nThank you for using Smart Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()