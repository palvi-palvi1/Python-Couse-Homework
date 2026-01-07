import random
def roll_dice():
    return random.randint(1,6)
dice = 0
while dice != 6:
    dice = roll_dice()
    print(dice)