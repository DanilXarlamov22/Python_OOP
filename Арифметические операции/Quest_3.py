class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    def __add__(self, other):
        if isinstance(other, str):
            return SuperString(self.string + other)
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:len(self.string) // other])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other < len(self.string):
                return SuperString(self.string[:len(self.string) - other])
            else:
                return SuperString("")
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other < len(self.string):
                return SuperString(self.string[other:])
            else:
                return SuperString("")
        return NotImplemented








s = SuperString('beegeek')

print(s << 4)
print(s >> 3)