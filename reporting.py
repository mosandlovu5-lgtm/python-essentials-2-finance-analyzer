from parser import load_transactions
from analytics import (
    category_totals,
    find_duplicates,
    find_outliers
)

def transaction_summary(transactions):
    print("\nTRANSACTION SUMMARY")
    print("-" * 30)

    print(f"Total Transactions: {len(transactions)}")

    total_income = sum(
        t.amount for t in transactions if t.amount > 0
    )

    total_expenses = sum(
        t.amount for t in transactions if t.amount < 0
    )

    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")

def category_report(transactions):
    print("\nCATEGORY REPORT")
    print("-" * 30)

    totals = category_totals(transactions)

    for category, total in totals.items():
        print(f"{category}: {total:.2f}") 

def duplicate_report(transactions):
    print("\nDUPLICATE REPORT")
    print("-" * 30)

    duplicates = find_duplicates(transactions)

    if not duplicates:
        print("No duplicates found.")
        return

    for transaction in duplicates:
        print(transaction)

def outlier_report(transactions):
    print("\nOUTLIER REPORT")
    print("-" * 30)

    outliers = find_outliers(transactions)

    if not outliers:
        print("No outliers found.")
        return

    for transaction in outliers:
        print(transaction)

transactions, rejections = load_transactions(
    "data/statement.txt"
)

transaction_summary(transactions)
category_report(transactions)
duplicate_report(transactions)
outlier_report(transactions)