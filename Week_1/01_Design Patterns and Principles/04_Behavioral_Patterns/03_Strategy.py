class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


payment = Payment(UPI())
payment.make_payment(500)