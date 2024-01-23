class Temperature:
    def __init__(self, temperature):
        self.temperature = float(temperature)

    def __repr__(self):
        return f"{round(self.temperature, 2)}°C"

    def to_fahrenheit(self):
        return 9/5 * self.temperature + 32

    @staticmethod
    def from_fahrenheit(temperature):
        return Temperature(5/9 * (temperature - 32))

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())



