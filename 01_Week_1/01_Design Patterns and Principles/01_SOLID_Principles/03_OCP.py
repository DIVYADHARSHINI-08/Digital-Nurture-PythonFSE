from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass


class RegularDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.90


class PremiumDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.80


amount = 1000

print("Regular:", RegularDiscount().apply_discount(amount))
print("Premium:", PremiumDiscount().apply_discount(amount))