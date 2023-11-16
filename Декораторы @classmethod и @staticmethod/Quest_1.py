from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

circle = Circle.from_diameter(10)

print(circle.radius)