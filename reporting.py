import os
import platform
from datetime import datetime

from analytics import category_totals, find_duplicates, find_outliers


def transaction_summary(transactions):
    total_income = sum(
        transaction.amount
        for transaction in transactions
        if transaction.amount > 0
    )

    total_expenses = sum(
        transaction.amount
        for transaction in transactions
        if transaction.amount < 0
    )

    print("\nTRANSACTION SUMMARY")
    print("-" * 30)
    print(f"Total Transactions: {len(transactions)}")
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")


def category_report(transactions):
    print("\nCATEGORY REPORT")
    print("-" * 30)

    for category, total in category_totals(transactions).items():
        print(f"{category}: {total:.2f}")


def duplicate_report(transactions):
    duplicates = find_duplicates(transactions)

    print("\nDUPLICATE REPORT")
    print("-" * 30)

    if not duplicates:
        print("No duplicates found.")
        return

    for transaction in duplicates:
        print(transaction)


def outlier_report(transactions):
    outliers = find_outliers(transactions)

    print("\nOUTLIER REPORT")
    print("-" * 30)

    if not outliers:
        print("No outliers found.")
        return

    for transaction in outliers:
        print(transaction)


def rejection_report(rejections):
    print("\nREJECTION REPORT")
    print("-" * 30)

    if not rejections:
        print("No rejected transactions.")
        return

    for rejection in rejections:
        print(rejection)


def monthly_summary(transactions, rejections=None):
    if rejections is None:
        rejections = []

    os.makedirs("data", exist_ok=True)

    totals = category_totals(transactions)
    duplicates = find_duplicates(transactions)
    outliers = find_outliers(transactions)

    total_income = sum(
        transaction.amount
        for transaction in transactions
        if transaction.amount > 0
    )

    total_expenses = sum(
        transaction.amount
        for transaction in transactions
        if transaction.amount < 0
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("data/report.txt", "w") as file:
        file.write("FINANCE ANALYZER MONTHLY SUMMARY\n")
        file.write("=" * 35 + "\n")
        file.write(f"Generated: {timestamp}\n")
        file.write(f"Operating System: {platform.system()}\n")
        file.write(f"Platform: {platform.platform()}\n\n")

        file.write(f"Total Transactions: {len(transactions)}\n")
        file.write(f"Rejected Transactions: {len(rejections)}\n")
        file.write(f"Total Income: {total_income:.2f}\n")
        file.write(f"Total Expenses: {total_expenses:.2f}\n")
        file.write(f"Net Balance: {total_income + total_expenses:.2f}\n\n")

        file.write("CATEGORY TOTALS\n")
        file.write("-" * 20 + "\n")
        for category, total in totals.items():
            file.write(f"{category}: {total:.2f}\n")

        file.write("\nDUPLICATES\n")
        file.write("-" * 20 + "\n")
        file.write(f"Duplicates Found: {len(duplicates)}\n")

        file.write("\nOUTLIERS\n")
        file.write("-" * 20 + "\n")
        file.write(f"Outliers Found: {len(outliers)}\n")

        file.write("\nREJECTION REASONS\n")
        file.write("-" * 20 + "\n")
        if rejections:
            for rejection in rejections:
                file.write(f"{rejection}\n")
        else:
            file.write("No rejected transactions.\n")

    with open("data/analyzer_runs.log", "a") as log_file:
        log_file.write(
            f"{timestamp} | "
            f"transactions={len(transactions)} | "
            f"rejections={len(rejections)}\n"
        )

    print("Report saved to data/report.txt")


def save_report(transactions, rejections=None):
    monthly_summary(transactions, rejections)