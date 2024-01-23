class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                setattr(self, key, -value)
            else:
                setattr(self, key, value)