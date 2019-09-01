from sys import exit
import time
import random


from enum import Enum
class Player_Option(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

computer_Option = random.choice(list(Player_Option))
print (computer_Option)

numbers = [1,2,3,4,5,6]
print (numbers[2])

human_option = Player_Option.ROCK
fav_colour = {Player_Option.ROCK: "red", Player_Option.SCISSORS: "black"}
print (fav_colour[human_option])


def moremaths (d, e, f):
    number = f - e - d
    return (number)

a = 2
b = 3
c = 4
num = moremaths(a, b, c)
print (num)