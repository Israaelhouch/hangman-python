"""
STEP 1 - Pick a random word and show it as blanks.
Goal: get a word and print it like  _ _ _ _ _ _
New idea: import random, random.choice, a loop over letters.
Run it:  python step1_pick_word.py
"""

import random

words = ["python", "rocket", "guitar", "dragon", "planet", "gamer"]

secret = random.choice(words)   # pick one word at random

# build a line of blanks, one "_" per letter
blanks = ""
for letter in secret:
    blanks = blanks + "_ "

print("The secret word has", len(secret), "letters:")
print(blanks)

# (for testing only - remove this later so it's not a giveaway)
print("(psst... the word is:", secret, ")")
