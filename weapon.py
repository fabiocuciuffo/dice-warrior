import random

class Weapon:
    def __init__(self, name, damage):
        self._name = name
        self._damage = damage

    def get_damage(self):
        return self._damage

    def get_name(self):
        return self._name

    def __str__(self):
        return f"Name :{self._name} Damage : {self._damage}"

if __name__ == "__main__":

    pass