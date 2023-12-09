class IPAddress:
    def __init__(self, ipaddres):
        self.ipaddres = ipaddres

    def __str__(self):
        if type(self.ipaddres) is str:
            return self.ipaddres
        return '.'.join(str(x) for x in self.ipaddres)

    def __repr__(self):
        if type(self.ipaddres) is str:
            return f"IPAddress('{self.ipaddres}')"
        return f"IPAddress('{'.'.join(map(str, self.ipaddres))}')"


ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))
ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))
