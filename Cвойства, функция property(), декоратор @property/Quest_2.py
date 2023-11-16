class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self.hours1

    def set_hours(self, hours):
        if isinstance(hours, int) and 1 <= hours <= 12:
            self.hours1 = hours
        else:
            raise ValueError("Некорректное время")

    hours = property(get_hours, set_hours)


time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)
