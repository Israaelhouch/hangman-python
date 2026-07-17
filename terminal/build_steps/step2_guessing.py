"""
STEP 2 - Let the player type letters and reveal them in the word.
Goal: keep asking for letters until the whole word is revealed.
New idea: a list to remember guesses, a while loop, input().
(No wrong-guess counting yet - we add that in step 3.)
Run it:  python step2_guessing.py
"""

import random

words = ["python", "rocket", "guitar", "dragon", "planet", "gamer"]

secret = random.choice(words)
guessed = []          # letters the player has tried

while True:
    # show the word with blanks for letters not guessed yet
    shown = ""
    for letter in secret:
        if letter in guessed:
            shown = shown + letter + " "
        else:
            shown = shown + "_ "
    print("Word:", shown)

    # have we revealed every letter?
    won = True
    for letter in secret:
        if letter not in guessed:
            won = False
    if won:
        print("You got it! The word was:", secret)
        break

    guess = input("Guess a letter: ").lower()
    guessed.append(guess)
