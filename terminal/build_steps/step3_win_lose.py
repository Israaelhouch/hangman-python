"""
STEP 3 - Count wrong guesses, add winning and losing.
Goal: the game ends when the word is complete (win) or after 6 wrong (lose).
New idea: a 'wrong' counter, checking if a letter is in the word, input checks.
We also move the win check into its own function to keep things tidy.
Run it:  python step3_win_lose.py
"""

import random

words = ["python", "rocket", "guitar", "dragon", "planet", "gamer"]


def show_word(secret, guessed):
    result = ""
    for letter in secret:
        if letter in guessed:
            result = result + letter + " "
        else:
            result = result + "_ "
    return result


def player_won(secret, guessed):
    for letter in secret:
        if letter not in guessed:
            return False
    return True


secret = random.choice(words)
guessed = []
wrong = 0

while wrong < 6:
    print("Word: ", show_word(secret, guessed))
    print("Wrong guesses left:", 6 - wrong)

    if player_won(secret, guessed):
        print("YOU WIN! The word was:", secret)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print(">> Please type just ONE letter.")
    elif guess in guessed:
        print(">> You already tried that letter.")
    else:
        guessed.append(guess)
        if guess in secret:
            print(">> Good guess!")
        else:
            wrong = wrong + 1
            print(">> Nope!")

if wrong >= 6:
    print("GAME OVER! The word was:", secret)
