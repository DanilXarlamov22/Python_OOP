class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iter):
        return cls(iter[0], iter[1], iter[2])

    @classmethod
    def from_str(cls, s):
        lst = list(map(float, s.split()))
        return cls(lst[0], lst[1], lst[2])
