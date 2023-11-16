class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._x1 = None
        self._x2 = None


    @property
    def x1(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant > 0:
            self._x1 = (-self.b - discriminant ** 0.5) / (2 * self.a)
        elif discriminant == 0:
            self._x1 = -self.b / (2 * self.a)
        else:
            self._x1 = None
        return self._x1


    @property
    def x2(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant > 0:
            self._x2 = (-self.b + discriminant ** 0.5) / (2 * self.a)
        elif discriminant == 0:
            self._x2 = -self.b / (2 * self.a)
        else:
            self._x2 = None
        return self._x2

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, x):
        self.a = x[0]
        self.b = x[1]
        self.c = x[2]



polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)