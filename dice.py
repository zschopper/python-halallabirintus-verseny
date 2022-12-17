from random import random

def roll(dices, add=0):
    result = 0

    i = 0
    while i < dices:
        result += int(random() * 6) + 1
        i += 1

    return result + add
