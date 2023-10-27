from collections import OrderedDict


class Postman:
    def __init__(self):
        self.delivery_data = []
        self.order_dict = OrderedDict()

    def add_delivery(self, street, num, apart):
        delivery = (street, num, apart)
        if delivery not in self.delivery_data:
            self.delivery_data.append(delivery)
            self.order_dict = OrderedDict(((s, n), []) for s, n, _ in self.delivery_data)
            for s, n, a in self.delivery_data:
                self.order_dict[(s, n)].append(a)

    def get_houses_for_street(self, s):
        return [n for (street, n), _ in self.order_dict.items() if street == s]

    def get_flats_for_house(self, s, num):
        return self.order_dict.get((s, num), [])


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
