class Coffee:
    def cost(self):
        return 100


class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 20


coffee = Coffee()
milk_coffee = MilkDecorator(coffee)

print("Cost:", milk_coffee.cost())