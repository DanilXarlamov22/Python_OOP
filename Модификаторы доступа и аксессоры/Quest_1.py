from math import pi


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * radius ** 2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area

# TEST_6:
circle = Circle(10)
print(hasattr(circle, '_radius'))
print(hasattr(circle, '_diameter'))
print(hasattr(circle, '_area'))