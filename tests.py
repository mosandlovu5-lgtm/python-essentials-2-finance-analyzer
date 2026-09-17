import os
import tempfile

from models import Transaction
from parser import load_transactions
from analytics import running_balance, make_flagger, find_duplicates


def create_test_file(contents):
    file = tempfile.NamedTemporaryFile(
        mode="w",
        delete=False,
        suffix=".txt"
    )
    file.write(contents)
    file.close()
    return file.name


# Valid rows, amount conversion, cleaning, and date normalization
valid_file = create_test_file(
    "2026-08-01, Salary , 15000 , INCOME\n"
    "2026/08/03, Groceries , -450.50 , FOOD\n"
)

transactions, rejections = load_transactions(valid_file)

assert len(transactions) == 2, "Two valid rows should load"
assert len(rejections) == 0, "Valid rows should not be rejected"
assert transactions[0].date == "2026-08-01", "First date should be correct"
assert transactions[0].amount == 15000.0, "Amount should be converted to float"
assert transactions[0].category == "INCOME", "Whitespace should be stripped"
assert transactions[1].date == "2026-08-03", "Slash date must be normalised"
assert transactions[1].description == "Groceries", "Description whitespace should be stripped"

os.remove(valid_file)


# Broken rows must be rejected safely
invalid_file = create_test_file(
    "hello world\n"
    "2026-08-05,Electricity,abc,UTILITIES\n"
    "2026-08-09\n"
    "2026-08-08,Bonus,1000,EXPENSE\n"
)

transactions, rejections = load_transactions(invalid_file)

assert len(transactions) == 0, "Broken rows must not become transactions"
assert len(rejections) == 4, "Every broken row should have a rejection reason"
assert "wrong number of fields" in rejections[0], "Junk line should be rejected"
assert "invalid amount" in rejections[1], "Non-numeric amount should be rejected"
assert "wrong number of fields" in rejections[2], "Missing fields should be rejected"
assert "income amount cannot have EXPENSE category" in rejections[3], "Sign mismatch should be rejected"

os.remove(invalid_file)


# Transaction methods
income = Transaction("2026-08-01", "Salary", 1000, "INCOME")
expense = Transaction("2026-08-02", "Food", -50, "FOOD")

assert income.is_income() is True, "Positive amount should be income"
assert expense.is_income() is False, "Negative amount should not be income"


# Running-balance generator
ledger = [
    Transaction("2026-08-01", "Salary", 1000, "INCOME"),
    Transaction("2026-08-02", "Food", -200, "FOOD"),
    Transaction("2026-08-03", "Petrol", -100, "TRANSPORT"),
]

balances = list(running_balance(ledger))

assert balances == [1000, 800, 700], "Running balance sequence is incorrect"


# Closure: make_flagger
flag_large_transaction = make_flagger(1000)

large_transaction = Transaction("2026-08-06", "Rent", -5000, "HOUSING")
small_transaction = Transaction("2026-08-05", "Coffee", -50, "FOOD")

assert flag_large_transaction(large_transaction) is True, "5000 transaction should be flagged"
assert flag_large_transaction(small_transaction) is False, "50 transaction should not be flagged"


# Duplicate detection
duplicate = Transaction("2026-08-06", "Rent", -5000, "HOUSING")
duplicates = find_duplicates([large_transaction, duplicate, small_transaction])

assert len(duplicates) == 1, "One duplicate should be found"
assert duplicates[0].description == "Rent", "The duplicate should be Rent"

clean_duplicates = find_duplicates([income, expense, small_transaction])
assert len(clean_duplicates) == 0, "Clean list should have no duplicates"


print("All tests passed")