import random
from rich import print
from dice import Dice
from character import Character, Mage, Warrior, Thief

def main():
    warrior = Warrior("Conan", 20, 8, 3, Dice(6))
    mage = Mage("Gandalf", 20, 8, 3, Dice(6))
    thief = Thief("James", 20, 8, 3, Dice(6))
    farmer = Character("Bob", 20, 8, 3, Dice(6))

    characters = [warrior, mage, thief, farmer]
    char1: Character = random.choice(characters)
    characters.remove(char1)
    char2: Character = random.choice(characters)
    characters.remove(char2)
    char3: Character = random.choice(characters)
    characters.remove(char3)
    char4: Character = random.choice(characters)
    characters.remove(char4)

    stats = {}

    stats[char1.get_name()] = 0
    stats[char2.get_name()] = 0

    print(stats)

    for i in range(100):
        while(char1.is_alive() and char2.is_alive()):
            char1.attack(char2)
            char2.attack(char1)
        if(char1.is_alive()):
            stats[char1.get_name()] += 1
        else:
            stats[char2.get_name()] += 1
        char1.regenerate()
        char2.regenerate()
        if(i == 99):
            print(stats)

if __name__ == "__main__":
    main()