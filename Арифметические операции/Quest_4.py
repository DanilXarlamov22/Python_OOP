class Time:
    def __init__(self, hours, minutes):
        self.hours = (hours + minutes // 60) % 24
        self.minutes = minutes % 60

    def __add__(self, other):
        if isinstance(other, Time):
            total_hours = self.hours + other.hours
            total_minutes = self.minutes + other.minutes
            return Time(total_hours, total_minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours = (self.hours + other.hours + (self.minutes + other.minutes) // 60) % 24
            self.minutes = (self.minutes + other.minutes) % 60
            return self
        return NotImplemented

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

# TEST_9:
t1 = Time(15, 50)
t2 = Time(2, 20)
print(t1 + t2)

t1 += Time(2, 20)
print(t1)
