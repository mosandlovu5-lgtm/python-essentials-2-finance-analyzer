import statistics


def running_balance(transactions, start=0.0):
    balance = start

    for transaction in transactions:
        balance += transaction.amount
        yield balance


def make_flagger(threshold):
    def flag_transaction(transaction):
        return abs(transaction.amount) > threshold

    return flag_transaction


def flag_closure(transactions):
    balances = list(running_balance(transactions))

    if not balances:
        return False

    return balances[-1] == 0


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


def category_totals(transactions):
    totals = {}

    for transaction in transactions:
        category = transaction.category

        if category not in totals:
            totals[category] = 0

        totals[category] += transaction.amount

    return totals


def find_outliers(transactions):
    if len(transactions) < 2:
        return []

    amounts = [transaction.amount for transaction in transactions]
    average = statistics.mean(amounts)
    deviation = statistics.stdev(amounts)

    if deviation == 0:
        return []

    return [
        transaction
        for transaction in transactions
        if abs(transaction.amount - average) > 2 * deviation
    ]