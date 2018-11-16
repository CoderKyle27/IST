# Imports
import random
random.seed()
# What they answers are going to be
answerlist = ["Python", "Hello", "Ist", "John"]
# Chooses the word randomly
# and Splits the word up EG: "P", "Y", "T", "H", "O", "N"
answer = list(random.choice(answerlist).lower())
display = ['_'] * len(answer)

# keeps asking the user until all the letters are guessed
while display.count('_') > 0:
    print(' '.join(display))
    guess = input("Please guess a letter: ").lower()
    if len(guess) > 1:
        print('You can only guess 1 letter at a time')
        if guess not in answer:
            wrong_guesses += 1
        elif:
            guess == 10
            break
            continue
    # Goes through the letters in the answers
    for i in range(len(answer)):
        # replaces an underscore with the correct letter
        if answer[i] == guess:
            display[i] = guess
    # print out the new string with the guessed letters in itself.
    print()

print("Well done, you guessed the word '{''.join(display)}' correctly")
