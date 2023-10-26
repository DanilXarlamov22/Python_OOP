class Todo:
    def __init__(self, things=[]):
        self.things = things
        self.min_priority = 0
        self.max_priority = 0

    def add(self, name, priority):
        self.things.append((name, priority))

    def get_by_priority(self, n):
        return [name for name, priority in self.things if priority == n]

    def get_low_priority(self):
        if self.things:
            self.min_priority = min(self.things, key=lambda x: x[1])[1]
            return [name for name, priority in self.things if priority == self.min_priority]
        return self.things

    def get_high_priority(self):
        if self.things:
            self.max_priority = max(self.things, key=lambda x: x[1])[1]
            return [name for name, priority in self.things if priority == self.max_priority]
        return self.things

todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())