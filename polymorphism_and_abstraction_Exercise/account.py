class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):

        if transaction_amount > self.amount:
            raise ValueError("sorry cannot go in debt!")

        self.amount -= transaction_amount
        self._transactions.append(transaction_amount)

        return f"New balance: {self.amount}"

    def add_transaction(self, amount):

        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        if self.amount + amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self.amount += amount
        self._transactions.append(amount)

        return f"New balance: {self.amount}"

    def balance(self):
        return self.amount

