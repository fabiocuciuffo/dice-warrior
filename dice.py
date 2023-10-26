import random

class Dice:
    def __init__(self, faces):
        self._faces = faces

    def roll(self):
        return random.randint(1, self._faces)
    
    def __str__(self):
        return f"i'm a dice with {self._faces} faces"
    
class RiggedDice(Dice):
    def roll(self, rigged = False):
        return self._faces if rigged else super().roll()
        # if(rigged):
        #     return self._faces
        # else:
        #     return super().roll()
        
if __name__ == "__main__":

    a_dice = Dice(10)

    b_dice = RiggedDice(5)
    print(b_dice.roll(False))