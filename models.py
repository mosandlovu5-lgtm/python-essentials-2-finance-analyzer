class Transaction:
    transaction_count = 0

    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = float(amount)
        self.category = category

        Transaction.transaction_count += 1

    def is_income(self):
        return self.amount > 0

    def formatted(self):
        return f"{self.date} {self.description} {self.amount:.2f} {self.category}"

    def __str__(self):
        return self.formatted()


class RecurringTransaction(Transaction):
    def __init__(self, date, description, amount, category, interval):
        super().__init__(date, description, amount, category)
        self.interval = interval

    def __str__(self):
        return (
            f"{self.date} {self.description} "
            f"{self.amount:.2f} {self.category} "
            f"(Repeats every {self.interval})"
        )