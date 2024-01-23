class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattr__(self, name):
        return object.__getattribute__(self, name)

    def __setattr__(self, key, value):
        if key == 'name':
            value = value.title()
        object.__setattr__(self, key, value)

    @property
    def total(self):
        return self.price * self.quantity


fruit = Item('banana', 15, 5)

print(fruit.name)
print(fruit.total)



