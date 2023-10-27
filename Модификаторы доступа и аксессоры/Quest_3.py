class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
            return self._name

    def set_name(self, name):  # сеттер, используется для изменения имени
        if isinstance(name, str) and name.isalpha():  # проверка имени перед заменой
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, age):  # сеттер, используется для изменения имени
        if isinstance(age, int) and age <= 110 and age >= 0:  # проверка имени перед заменой
            self._age = age
        else:
            raise ValueError('Некорректный возраст')


invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user = User(name, 37)
    except ValueError as e:
        print(e)