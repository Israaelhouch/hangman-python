# Hangman — Step-by-Step Build Guide (for the instructor)

This guide walks your student through building Hangman a little at a time, so
he never faces a blank page or a wall of code. Every step is a **complete,
runnable program** — he types it, runs it, sees it work, then adds the next
piece. Confidence grows with each run.

There are two parts:

- **Part A — the terminal game** (4 steps). Build this first. It uses only what
  he's already learned.
- **Part B — the clickable window** (optional upgrade). The same game with a
  mouse and drawings, using pygame.

A rough pacing suggestion is at the end.

---

## Part A — The terminal game

### Step 1 — Pick a word and show it as blanks
**File:** `terminal/build_steps/step1_pick_word.py`

**Goal:** the program picks a secret word and prints it as `_ _ _ _ _ _`.

**Concepts:** `import random`, `random.choice`, a `for` loop over the letters of
a word, building up a string.

**What he writes:**
```python
import random
words = ["python", "rocket", "guitar", "dragon", "planet", "gamer"]
secret = random.choice(words)

blanks = ""
for letter in secret:
    blanks = blanks + "_ "
print(blanks)
```

**What he should see:** a row of underscores, a different length each time he
runs it. Add a temporary `print(secret)` so you can both see the answer while
testing — remove it later.

**Checkpoint question:** "How would we show 8 blanks instead of 6?" (Answer: use
a longer word — the loop already handles any length.)

---

### Step 2 — Guess letters and reveal them
**File:** `terminal/build_steps/step2_guessing.py`

**Goal:** the player types a letter; if it's in the word, it appears in place of
its blank. Keep going until the whole word shows.

**Concepts:** a list to remember guesses (`guessed = []`), `input()`, a `while`
loop, `if letter in guessed`.

**Key new lines:**
```python
guessed = []
while True:
    # show the word, using letters we've guessed
    shown = ""
    for letter in secret:
        if letter in guessed:
            shown = shown + letter + " "
        else:
            shown = shown + "_ "
    print("Word:", shown)

    guess = input("Guess a letter: ").lower()
    guessed.append(guess)
```

**What he should see:** typing a correct letter fills in the blank. (There's no
"you lose" yet — that's next. There's a simple win check so the loop can stop.)

**Checkpoint question:** "Why do we need the `guessed` list instead of just one
variable?" (Because we must remember *all* the letters tried so far.)

---

### Step 3 — Winning and losing
**File:** `terminal/build_steps/step3_win_lose.py`

**Goal:** the game ends with a win when the word is complete, or a loss after 6
wrong guesses.

**Concepts:** a counter (`wrong = 0`), checking `if guess in secret`, moving the
repeated code into two small functions (`show_word`, `player_won`), and simple
input checks.

**The heart of it:**
```python
if guess in secret:
    print(">> Good guess!")
else:
    wrong = wrong + 1
    print(">> Nope!")
```
and the loop runs `while wrong < 6:`.

**What he should see:** wrong guesses now count down; six wrong ends the game;
completing the word wins it.

**Checkpoint question:** "What happens if he types the same wrong letter twice?"
(Good moment to show the `elif guess in guessed:` check that prevents it.)

---

### Step 4 — The hangman drawing + play again
**File:** `terminal/build_steps/step4_drawing.py` (this is the finished game,
also copied to `terminal/hangman.py`)

**Goal:** show a picture that grows with each wrong guess, and let the player
start a new round.

**Concepts:** a **list of pictures** (one per wrong count) so `pictures[wrong]`
shows the right stage; wrapping everything in a `play()` function so it can be
called again.

**The trick:**
```python
pictures = [ "...", "...", ... ]   # 7 drawings, from empty to full hangman
print(pictures[wrong])             # show the drawing for the current count
```
and at the very bottom:
```python
play()
while input("Play again? (y/n): ").lower() == "y":
    play()
```

**What he should see:** the full game — a drawing that builds up, win/lose
messages, and the option to replay. **He built a complete game!**

---

## Part B — The clickable window (optional upgrade)

Only start this once the terminal game works and he understands it. Sell it as:
*"Let's put a window on the game you already made."* The guessing logic is
identical — we're just adding a mouse and some drawing.

**Before game day:** do a 20–30 minute pygame warm-up. Three tiny programs:
1. open an empty window,
2. draw a circle and a line in it,
3. print a message when the mouse is clicked.

That way the window, drawing, and clicking aren't brand new during the build.

**File:** `gui/hangman_gui.py`. Build it in three passes:

1. **Show the board.** Open the window, draw the title, the word as big blanks,
   and 26 grey letter boxes. Nothing clickable yet — just the picture.
2. **Make clicking work.** In the event loop, when the mouse is pressed, check
   each box with `box.collidepoint(event.pos)`; if it matches, add that letter
   to `guessed`. Reuse the *same* reveal-and-win logic from the terminal game.
   Color a guessed box green if the letter is in the word, red if not.
3. **Draw the hangman + end screens.** Add `draw_man(wrong)` (lines and a circle
   by coordinates) and the win/lose messages, with a click to play again.

**Teaching tip:** the numbers in `draw_man`, like `(230, 145)`, are just screen
positions. Tell him *not* to memorize them — instead, change one and re-run to
watch the head move. That "poke it and see" habit is real programming.

---

## Suggested pacing (3 capstone sessions)

- **Session 10:** Steps 1 and 2 — a word shows as blanks, and guessing reveals
  letters. Runs after each step.
- **Session 11:** Step 3 — winning, losing, wrong-guess counting, input checks.
- **Session 12:** Step 4 — the drawing and play-again (finished terminal game),
  then play-test and celebrate. If time and energy allow, start Part B.

The window version can be a bonus/stretch across the last session or sent home
as "want to make it clickable?" homework.

---

## Stretch goals (if he's flying)

- **Load words from a file.** Read `words.txt` instead of the hard-coded list —
  this is a great use of the file-reading he learns in session 9:
  ```python
  with open("words.txt") as f:
      words = f.read().split()
  ```
- **Add a score or streak** that goes up each win and resets on a loss.
- **Add categories** (animals, sports, space) and let him pick one.
- **Give a hint** — reveal one random letter at the start.
