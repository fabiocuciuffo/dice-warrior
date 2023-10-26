from dice import Dice
from character import Character, Mage, Warrior, Thief
from weapon import Weapon
import random
import time
from rich import print

char1 = None
char2 = None

print('JOUEUR 1')
type1 = input(
    "Choose your character: Warrior, Mage, Thief or custom for create your type: ")
if (type1 == "Warrior" or type1 == "warrior"):
    name1 = input("Choose the name of the character : (string) ")
    dice1 = int(input(
        "The magic dice can help you or destroy you… how many faces you want for it ? (integer only, max 10)"))
    char1 = Warrior(name1, 20, 8, 3, Dice(dice1))
elif (type1 == "Mage" or type1 == "mage"):
    name1 = input("Choose the name of the character : (string) ")
    dice1 = int(input(
        "The magic dice can help you or destroy you… how many faces you want for it ? (integer only, max 10)"))
    char1 = Mage(name1, 20, 8, 3, Dice(dice1))
elif (type1 == "Thief" or type1 == "thief"):
    name1 = input("Choose the name of the character : (string) ")
    dice1 = int(input(
        "The magic dice can help you or destroy you… how many faces you want for it ? (integer only, max 10)"))
    char1 = Thief(name1, 20, 8, 3, Dice(dice1))
elif (type1 == 'custom'):
    nameOfClass = input(
        "Choose the name of the custom type you want to create : ")
    perks = input(
        'What bonus perk you want to add for your custom type character ? (defense, attack or random) : ')
    if (perks == 'defense'):
        nameOfDefense = input(
            'How you want to name your defense perk ? (you can include emoji) : ')
        amountOfDefense = int(input(
            'How much you want your defense perk ? (integer only) : '))

        class Custom(Character):
            _label = nameOfClass

            def compute_defense(self, damages, roll: int):
                print(f"{nameOfDefense} ! (bonus: -{amountOfDefense})")
                return super().compute_defense(damages, roll) - amountOfDefense
    if (perks == 'attack'):
        nameOfAttack = input(
            'How you want to name your attack perk ? (you can include emoji) : ')
        amountOfAttack = int(input(
            'How much you want your attack perk ? (integer only, max 9) : '))

        class Custom(Character):
            _label = nameOfClass

            def compute_damages(self, roll, target):
                print(f"{nameOfAttack} ! (bonus: +{amountOfAttack})")
                return super().compute_damages(roll, target) + amountOfAttack
    else:
        defenseOrAttackNum = random.randint(1, 2)
        if (defenseOrAttackNum == 1):
            randomDefense = random.randint(1, 9)

            class Custom(Character):
                _label = nameOfClass

                def compute_defense(self, damages, roll: int):
                    print(f"🎱 Mystery gift ! (bonus: -{randomDefense})")
                    return super().compute_defense(damages, roll) - randomDefense
        if (defenseOrAttackNum == 1):
            randomAttack = random.randint(1, 9)

            class Custom(Character):
                _label = nameOfClass

                def compute_damages(self, roll, target):
                    print(f"🎱 Mystery gift ! (bonus: +{randomAttack})")
                    return super().compute_damages(roll, target) + randomAttack
    name1 = input("Choose the name of the character : (string) ")
    dice1 = int(input(
        "The magic dice can help you or destroy you… how many faces you want for it ? (integer only, max 10)"))
    maxHealth1 = int(input(
        "How much health points have your character ? (integer only, has you want) "))
    maxAttack1 = int(input(
        "How much attack points have your character ? (integer only, has you want) "))
    maxDefense1 = int(input(
        "How much defense points have your character ? (integer only, has you want) "))
    char1 = Custom(name1, maxHealth1, maxAttack1, maxDefense1, Dice(dice1))

print('JOUEUR 2')
type2 = input(
    "Choose your character: Warrior, Mage, Thief or custom for create your type: ")
if (type2 == "Warrior" or type2 == "warrior"):
    name2 = input("Choose the name of the character : (string) ")
    dice2 = int(input(
        "The magic dice can help you or destroy you… how many faces you want for it ? (integer only, max 10)"))
    char2 = Warrior(name2, 20, 8, 3, Dice(dice2))
elif (type2 == "Mage" or type1 == "mage"):
    name2 = input("Choose the name of the character : (string) ")
    dice2 = int(input(
        "The magic dice can help you or destroy you… how many faces you want for it ? (integer only, max 10)"))
    char2 = Mage(name2, 20, 8, 3, Dice(dice2))
elif (type2 == "Thief" or type1 == "thief"):
    name2 = input("Choose the name of the character : (string) ")
    dice2 = int(input(
        "The magic dice can help you or destroy you… how many faces you want for it ? (integer only, max 10)"))
    char2 = Thief(name2, 20, 8, 3, Dice(dice2))
elif (type2 == 'custom'):
    nameOfClass = input(
        "Choose the name of the custom type you want to create : ")
    perks = input(
        'What bonus perk you want to add for your custom type character ? (defense, attack or random) : ')
    if (perks == 'defense'):
        nameOfDefense = input(
            'How you want to name your defense perk ? (you can include emoji) : ')
        amountOfDefense = int(input(
            'How much you want your defense perk ? (integer only) : '))

        class Custom(Character):
            _label = nameOfClass

            def compute_defense(self, damages, roll: int):
                print(f"{nameOfDefense} ! (bonus: -{amountOfDefense})")
                return super().compute_defense(damages, roll) - amountOfDefense
    if (perks == 'attack'):
        nameOfAttack = input(
            'How you want to name your attack perk ? (you can include emoji) : ')
        amountOfAttack = int(input(
            'How much you want your attack perk ? (integer only, max 9) : '))

        class Custom(Character):
            _label = nameOfClass

            def compute_damages(self, roll, target):
                print(f"{nameOfAttack} ! (bonus: +{amountOfAttack})")
                return super().compute_damages(roll, target) + amountOfAttack
    else:
        defenseOrAttackNum = random.randint(1, 2)
        if (defenseOrAttackNum == 1):
            randomDefense = random.randint(1, 9)

            class Custom(Character):
                _label = nameOfClass

                def compute_defense(self, damages, roll: int):
                    print(f"🎱 Mystery gift ! (bonus: -{randomDefense})")
                    return super().compute_defense(damages, roll) - randomDefense
        if (defenseOrAttackNum == 1):
            randomAttack = random.randint(1, 9)

            class Custom(Character):
                _label = nameOfClass

                def compute_damages(self, roll, target):
                    print(f"🎱 Mystery gift ! (bonus: +{randomAttack})")
                    return super().compute_damages(roll, target) + randomAttack
    name2 = input("Choose the name of the character : (string) ")
    dice2 = int(input(
        "The magic dice can help you or destroy you… how many faces you want for it ? (integer only, max 10)"))
    maxHealth2 = int(input(
        "How much health points have your character ? (integer only, has you want) "))
    maxAttack2 = int(input(
        "How much attack points have your character ? (integer only, has you want) "))
    maxDefense2 = int(input(
        "How much defense points have your character ? (integer only, has you want) "))
    char2 = Custom(name2, maxHealth2, maxAttack2, maxDefense2, Dice(dice2))
tour = 1
while (char1.is_alive() and char2.is_alive()):
    print(f"TOUR {tour}")
    time.sleep(2)
    char1.attack(char2)
    time.sleep(2)
    char2.attack(char1)
    tour = tour + 1
