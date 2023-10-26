class Scales:
    def __init__(self):
        self.scale_right = 0
        self.scale_left = 0

    def add_right(self, n):
        self.scale_right += n

    def add_left(self, n):
        self.scale_left += n

    def get_result(self):
        if self.scale_right > self.scale_left:
            return f'Правая чаша тяжелее'
        elif self.scale_right < self.scale_left:
            return f'Левая чаша тяжелее'
        else:
            return f'Весы в равновесии'