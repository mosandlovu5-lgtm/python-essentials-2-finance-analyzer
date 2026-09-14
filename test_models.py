from models import Transaction, RecurringTransaction

t1 = Transaction(
    "2026-08-01",
    "Salary",
    15000,
    "INCOME"
)

t2 = RecurringTransaction(
    "2026-08-02",
    "Netflix",
    -199,
    "ENTERTAINMENT",
    "monthly"
)

print(t1)
print(t2)

print(t1.is_income())
print(t2.is_income())

print("Transactions:", Transaction.transaction_count)