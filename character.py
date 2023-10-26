from __future__ import annotations
from dice import Dice, RiggedDice
from weapon import Weapon
import random

from rich import print

# geoffroy@gl-conseil.dev


class Character:

    _label = "Character"

    def __init__(self, name: str, max_health: int, attack: int, defense: int, dice: Dice, weapon: Weapon = None):
        self._name = name
        self._max_health = max_health
        self._health = max_health
        self._attack_value = attack
        self._defense_value = defense
        self._dice: Dice = dice
        self._weapon = weapon

    def __str__(self):
        return f"{type(self)._label} {self._name} is starting the fight with {self._max_health}hp (atk {self._attack_value} / def {self._defense_value})"

    def is_alive(self):
        return self._health > 0

    def regenerate(self):
        self._health = self._max_health

    def get_name(self):
        return self._name

    def get_defense(self):
        return self._defense_value

    def show_healthbar(self):
        print(f"[{'●' * self._health}{'○' * (self._max_health -
              self._health)}] {self._health}/{self._max_health}hp")

    def decrease_health(self, amount):
        if (self._health - amount < 0):
            amount = self._health
        self._health = self._health - amount
        self.show_healthbar()

    def compute_damages(self, roll, target: Character):
        return self._attack_value + roll

    def attack(self, target: Character):
        if (self.is_alive()):
            x = random.randint(1, 100)
            if (x <= 20 and self._weapon != None):
                damages = self._weapon.get_damage()
                print(f"✨{type(self)._label} {self._name} special attack with {
                      self._weapon.get_name()} {damages} damages")
                target.defense(target, damages)
            else:
                roll = self._dice.roll()
                damages = self.compute_damages(roll, target)
                print(f"{type(self)._label} {
                      self._name} attack with {damages} damages")
                target.defense(target, damages)

    def compute_defense(self, damages, roll):
        return damages - self._defense_value - roll

    def defense(self, attacker: Character, damages):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll)
        if (wounds < 0):
            wounds = 0
        print(f"{type(self)._label} {self._name} defend against {damages} damages and take {wounds} wounds by {
              attacker.get_name()} ! (damages: {damages}, defense: {self.get_defense()} roll: {roll})")
        self.decrease_health(wounds)


class Warrior(Character):
    _label = "Warrior"

    def compute_damages(self, roll: int, target) -> int:
        print(f"🪓 Axe in face ! (bonus: +3)")
        return super().compute_damages(roll, target) + 3


class Mage(Character):
    _label = "Mage"

    def compute_defense(self, damages, roll: int):
        print(f"🐢Turtle shell ! (bonus: -3)")
        return super().compute_defense(damages, roll) - 3


class Thief(Character):
    _label = "Thief"

    def compute_damages(self, roll, target):
        print(f"Ignore Defense ! (bonus: {target._defense_value})")
        return super().compute_damages(roll, target) + target._defense_value


class Tank(Character):
    _label = "Tank"

    def compute_defense(self, damages, roll: int):
        print(f"🛡️ I'm a tank ! (bonus: -10)")
        return super().compute_defense(damages, roll) - 10


if __name__ == "__main__":
    sword = Weapon("Sword", 13)
    breatOfFire = Weapon("Breath of Fire", 16)
    char_1 = Thief("James", 20, 8, 3, Dice(6), sword)
    char_2 = Mage("Dina", 20, 8, 3, Dice(6), breatOfFire)

    while (char_1.is_alive() and char_2.is_alive()):
        char_1.attack(char_2)
        char_2.attack(char_1)
