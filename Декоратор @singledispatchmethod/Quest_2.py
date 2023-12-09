from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(float)
    @neg.register(int)
    @staticmethod
    def _numeric_process(data):
        return -data

    @neg.register(bool)
    @staticmethod
    def _bool_process(data):
        return not data
