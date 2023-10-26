class Numbers:
    def __init__(self):
        self.lst = []

    def add_number(self, n):
        self.lst.append(n)

    def get_even(self):
        return [x for x in self.lst if x % 2 == 0]

    def get_odd(self):
        return [x for x in self.lst if x % 2]