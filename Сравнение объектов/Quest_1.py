class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        if isinstance(other, tuple):
            return (self.x, self.y) == other
        return NotImplemented

a = Vector(1, 2)
b = Vector(3, 4)
c = Vector(5, 6)

vectors = [a, b, c]
print(vectors)