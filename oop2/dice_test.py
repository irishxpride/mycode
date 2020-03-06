#!/usr/bin/python3
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
import random

cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()

cheater1.roll()
cheater2.roll()

cheater1.cheat()
cheater2.cheat()

print ("Cheater 1 rolled " + str(cheater1.get_dice()))
print ("Cheater 2 rolled " + str(cheater2.get_dice()))

if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
    print("Draw!")

if sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
    print("Cheater1 wins!")

else:
    print("Cheater2 wins!")
