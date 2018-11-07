

#Imports
import random
import time

#Variables
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
time.sleep (1)
print("Start guessing!")
time.sleep (0.5)

#Words
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

#Chooses the random words
word = random.choice(WORDS)
guesses = ''

#Number of turns
turns = 10

#Else statement
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char),
        else:
            print("_"),
            failed += 1
            if failed == 0:
        print("You won")
        break
        print

# Turns and how they work
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Lost :(")
            print("The word was" + ' '  +  (word))
