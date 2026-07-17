"""
STEP 4 - Add the hangman drawing and a 'play again' option.
Goal: show a picture that grows with each wrong guess, then let the player
      start a new round. This is the finished game!
New idea: a list of pictures (one per wrong count), wrapping it all in a
          play() function so we can call it again.
Run it:  python step4_drawing.py
"""

import random

words = ["python", "rocket", "guitar", "dragon", "planet", "gamer"]

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


def play():
    secret = random.choice(words)
    guessed = []
    wrong = 0

    print("=" * 30)
    print("      WELCOME TO HANGMAN")
    print("=" * 30)

    while wrong < 6:
        print(pictures[wrong])
        print("Word: ", show_word(secret, guessed))
        print("Wrong guesses left:", 6 - wrong)

        if player_won(secret, guessed):
            print("\n YOU WIN! The word was:", secret)
            return

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

    print(pictures[wrong])
    print("\n GAME OVER! The word was:", secret)


play()
while input("\nPlay again? (y/n): ").lower() == "y":
    play()
print("Thanks for playing!")
