from models import Transaction


def generate_sample_file():
    with open("data/statement.txt", "w") as file:
        file.write(
    """2026-08-01,Salary,15000,INCOME
2026/08/03,Freelance,2500,INCOME
2026-08-04,Groceries,-450.50,FOOD
hello world
2026-08-05,Electricity,abc,UTILITIES
2026-08-06,Rent,-5000,HOUSING
2026-08-06,Rent,-5000,HOUSING
2026-08-07,Movie,-150,ENTERTAINMENT
2026-08-08,Bonus,1000,EXPENSE
2026-08-09
2026-08-10, Petrol , -800 , TRANSPORT
2026-08-11,Gift,500,INCOME
"""
)

    print("Sample statement file created.")


generate_sample_file()

def load_transactions(path):
    transactions = []
    rejection_reasons = []

    try:
        with open(path, "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        print("File not found.")
        return [], ["File not found"]

    if not lines:
        print("File is empty.")
        return [], ["File is empty"]

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()

        if not line:
            continue

        parts = line.split(",")

        if len(parts) != 4:
            rejection_reasons.append(
                f"Line {line_number}: wrong number of fields"
            )
            continue

        date, description, amount, category = parts

        date = date.strip().replace("/", "-")
        description = description.strip()
        amount = amount.strip()
        category = category.strip()

        if not date or not description or not amount or not category:
            rejection_reasons.append(
                f"Line {line_number}: missing field"
            )
            continue

        try:
            float_amount = float(amount)
        except ValueError:
            rejection_reasons.append(
                f"Line {line_number}: invalid amount"
            )
            continue
        if float_amount > 0 and category == "EXPENSE":
            rejection_reasons.append(
                f"Line {line_number}: income amount cannot have EXPENSE category"
            )
            continue

        if float_amount < 0 and category == "INCOME":
            rejection_reasons.append(
                f"Line {line_number}: expense amount cannot have INCOME category"
            )
            continue

        try:
            from datetime import datetime
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            rejection_reasons.append(
                f"Line {line_number}: invalid date"
            )
            continue

        transaction = Transaction(
            date,
            description,
            float_amount,
            category
        )

        transactions.append(transaction)

    return transactions, rejection_reasons

transactions, rejections = load_transactions("data/statement.txt")

print("\nVALID TRANSACTIONS:")

for transaction in transactions:
    print(transaction)

print("\nREJECTIONS:")

for reason in rejections:
    print(reason)