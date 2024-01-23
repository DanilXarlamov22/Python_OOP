class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 1
        for key, value in kwargs.items():
            setattr(self, key, value)
        setattr(self, 'attrs_num', len(self.__dict__.keys()))

    def __setattr__(self, key, value):
        if key not in self.__dict__keys():
            self.__dict__['attrs_num'] += 1

    def __getattr__(self, item):
        return item