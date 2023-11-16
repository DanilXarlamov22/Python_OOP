class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length
