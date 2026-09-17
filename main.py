import subprocess
import sys

from parser import generate_sample_file, load_transactions
from analytics import running_balance
from reporting import (
    transaction_summary,
    category_report,
    duplicate_report,
    outlier_report,
    rejection_report,
    monthly_summary,
)


def show_menu():
    print("\n===== FINANCE TRANSACTION ANALYZER =====")
    print("1. Generate a messy sample statement file")
    print("2. Load & validate transactions")
    print("3. Show running balance")
    print("4. Category breakdown")
    print("5. Detect duplicate transactions")
    print("6. Flag unusual transactions")
    print("7. Monthly summary report -> file")
    print("8. Run self-tests")
    print("9. Exit")


def main():
    transactions = []
    rejections = []

    while True:
        show_menu()

        try:
            choice = input("Choose an option (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nProgram closed.")
            break

        if choice == "1":
            generate_sample_file()

        elif choice == "2":
            try:
                path = input(
                    "Statement path (press Enter for data/statement.txt): "
                ).strip()

                if not path:
                    path = "data/statement.txt"

                transactions, rejections = load_transactions(path)

                print(f"\nValid transactions loaded: {len(transactions)}")
                print(f"Rejected rows: {len(rejections)}")

                transaction_summary(transactions)
                rejection_report(rejections)

            except Exception as error:
                print(f"Could not load transactions: {error}")

        elif choice == "3":
            if not transactions:
                print("Load transactions first using option 2.")
                continue

            print("\nRUNNING BALANCE")
            print("-" * 30)

            for balance in running_balance(transactions):
                print(f"{balance:.2f}")

        elif choice == "4":
            if not transactions:
                print("Load transactions first using option 2.")
                continue

            category_report(transactions)

        elif choice == "5":
            if not transactions:
                print("Load transactions first using option 2.")
                continue

            duplicate_report(transactions)

        elif choice == "6":
            if not transactions:
                print("Load transactions first using option 2.")
                continue

            outlier_report(transactions)

        elif choice == "7":
            if not transactions:
                print("Load transactions first using option 2.")
                continue

            monthly_summary(transactions, rejections)

        elif choice == "8":
            try:
                subprocess.run(
                    [sys.executable, "tests.py"],
                    check=True
                )
                print("\nSelf-tests completed successfully.")

            except subprocess.CalledProcessError:
                print("\nSelf-tests failed. Read the error above.")

        elif choice == "9":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()