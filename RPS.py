# Imports

import random
import time

#  Introduction text

print("You will be playing against a pro player...")
time.sleep(1)
print("Found a player!")
time.sleep(1)

# First variables that save your name

pname = input("What is your name? ")
time.sleep(1)
print("Nice to meet you, " + pname, "Time to play rock paper scissors!")
time.sleep(1)
print("The game will start in....")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

# Random number (1 = rock), (2 = paper), (3 = scissors)
cpu = random.randint(1,3)

# The winner variable is used to determine whether a game is won or not
winner = False

# If CPU chooses rock
# The while loop will stop if one of the conditions of winner is true

while not winner:
    rps = input("rock, paper or scissors: ")
    if (not winner) and cpu == 1 and rps == ("rock"):
        print("Tie! Well done, please play again.")
    elif (not winner) and cpu == 1 and rps == ("paper"):
        print("Victory! Pro player chose rock and you chose scissors!")
        winner = True
    elif (not winner) and cpu == 1 and rps == ("scissors"):
        print("Defeat, CPU chose rock and you chose scissors! Please play again.")



    # If CPU chooses Paper

    if (not winner) and cpu == 2 and rps == ("rock"):
        print("Defeat, Pro Player chose  and you chose paper and you chose rock. Please play again.")
    elif (not winner) and cpu == 2 and rps ==("paper"):
        print("Tie, Well done! Please play again.")
    elif (not winner) and cpu == 2 and rps == ("scissors"):
        print("Victory! Pro player has chosen paper and you have chosen rock.")
        winner = True

    # if CPU chooses scissors

    if (not winner) and cpu == 3 and rps == ("rock"):
        print("Well done, Pro Player has chosen scissors and you have chosen rock.")
        winner = True
    elif (not winner) and cpu == 3 and rps == ("paper)"):
        print("Defeat, Pro player has chosen scissors and you have chosen paper. Please play again.")
    elif (not winner) and cpu == 3 and rps == ("scissors"):
        print("Tie, Well done! Please play again.")
