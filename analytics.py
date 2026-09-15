def running_balance(transactions):
    balance = 0

    for transaction in transactions:
        balance += transaction.amount
        yield balance

from parser import load_transactions

transactions, rejections = load_transactions("data/statement.txt")

print("RUNNING BALANCE:")

for balance in running_balance(transactions):
    print(balance)

def flag_closure(transactions):
    balances = list(running_balance(transactions))

    if not balances:
        return False

    return balances[-1] == 0

print("\nCLOSURE FLAG:")
print(flag_closure(transactions))

def find_duplicates(transactions):
    seen = set()
    duplicates = []

    for transaction in transactions:
        key = (
            transaction.date,
            transaction.description,
            transaction.amount,
            transaction.category
        )

        if key in seen:
            duplicates.append(transaction)
        else:
            seen.add(key)

    return duplicates
duplicates = find_duplicates(transactions)

print("\nDUPLICATES:")

for transaction in duplicates:
    print(transaction)