class Pet:
    pet_list = []

    def __init__(self, name):
        self.name = name
        Pet.pet_list.append(self)

    @classmethod
    def first_pet(cls):
        if len(cls.pet_list) > 0:
            return cls.pet_list[0]
        else:
            return None

    @classmethod
    def last_pet(cls):
        if len(cls.pet_list) > 0:
            return cls.pet_list[-1]
        else:
            return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pet_list)

