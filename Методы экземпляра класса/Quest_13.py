class Postman:
    def __init__(self, delivery_data=[]):
        self.delivery_data = delivery_data

    def add_delivery(self, street, num, apart):
        self.delivery_data.append((street, num, apart))

    def get_houses_for_street(self, s):
        return [b for a, b, _ in self.delivery_data if a == s]

    def get_flats_for_house(self, s, num):
        return [c for a, b, c in self.delivery_data if a == s and b == num]
