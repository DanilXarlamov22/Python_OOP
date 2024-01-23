class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)

    def __invert__(self):
        inverted_color = tuple(255 - component for component in self.color)
        return ColoredPoint(self.y, self.x, inverted_color)