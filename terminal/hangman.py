"""
HANGMAN  -  terminal version (final)
Uses only: variables, lists, loops, if/else, functions, and the random module.
Run it:  python hangman.py
"""

import random

# ---- 1. The words to guess ----
words = ["python", "rocket", "guitar", "dragon", "planet", "gamer"]

# ---- 2. The hangman pictures (one for each number of wrong guesses) ----
pictures = [
    """
     +---+
         |
         |
         |
    =======""",
    """
     +---+
     O   |
         |
         |
    =======""",
    """
     +---+
     O   |
     |   |
         |
    =======""",
    """
     +---+
     O   |
    /|   |
         |
    =======""",
    """
     +---+
     O   |
    /|\\  |
         |
    =======""",
    """
     +---+
     O   |
    /|\\  |
    /    |
    =======""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
    =======""",
]


def show_word(secret, guessed):
    """Build the word with blanks, like  p y _ _ _ _"""
    result = ""
    for letter in secret:
        if letter in guessed:
            result = result + letter + " "
        else:
            result = result + "_ "
    return result


def player_won(secret, guessed):
    """Return True only if every letter has been guessed."""
    for letter in secret:
        if letter not in guessed:
            return False
    return True


def play():
    secret = random.choice(words)   # pick a random word
    guessed = []                    # letters the player has tried
    wrong = 0                       # number of wrong guesses

    print("=" * 30)
    print("      WELCOME TO HANGMAN")
    print("=" * 30)

    # ---- the main game loop ----
    while wrong < 6:
        print(pictures[wrong])
        print("Word: ", show_word(secret, guessed))
        print("Wrong guesses left:", 6 - wrong)

        # did the player win?
        if player_won(secret, guessed):
            print("\n YOU WIN! The word was:", secret)
            return

        guess = input("Guess a letter: ").lower()

        # simple checks
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

    # the loop ended because wrong reached 6
    print(pictures[wrong])
    print("\n GAME OVER! The word was:", secret)


# ---- start the game, and let the player play again ----
play()
while input("\nPlay again? (y/n): ").lower() == "y":
    play()
print("Thanks for playing!")
