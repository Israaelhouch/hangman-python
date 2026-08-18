# Hangman

A classic word game written in Python, in two versions that play identically:
a **terminal** game you type into, and a **window** game you click.

The terminal version uses nothing but core Python — variables, lists, loops,
functions and `random`. The window version takes the exact same guessing logic
and puts a mouse and a drawing on top of it with `pygame`.

## What it looks like

**Terminal**

```
==============================
      WELCOME TO HANGMAN
==============================

     +---+
     O   |
     |   |
         |
    =======
Word:  _ o c k e t
Wrong guesses left: 4
Guess a letter:
```

**Window** — the gallows is drawn on the left, the word sits in large blanks in
the middle, and 26 letter buttons run along the bottom. A button turns green
when its letter is in the word and red when it isn't, so you can always see what
you have already tried. Click any letter to guess; when the round ends, click
anywhere to start a new one.

## Run it

The terminal version needs nothing but Python:

```bash
cd terminal
python hangman.py
```

The window version needs pygame, installed once:

```bash
pip install -r requirements.txt
cd gui
python hangman_gui.py
```

## What's inside

```
hangman-python/
├── terminal/
│   ├── hangman.py            the finished terminal game
│   └── build_steps/          the same game, built up in four stages
│       ├── step1_pick_word.py
│       ├── step2_guessing.py
│       ├── step3_win_lose.py
│       └── step4_drawing.py
├── gui/
│   └── hangman_gui.py        the clickable pygame version
├── docs/
│   └── BUILD_GUIDE.md        the reasoning behind each step
├── words.txt                 a longer word list
└── requirements.txt
```

## How it was built

Instead of writing the whole game at once, it was built in four stages. Each
file in `build_steps/` is a complete program that runs on its own and does a
little more than the one before it:

| Step | Adds |
| --- | --- |
| 1 | picks a random word and prints it as blanks |
| 2 | reads letters and reveals them in place |
| 3 | counts wrong guesses, and adds winning and losing |
| 4 | draws the hangman and offers a rematch |

The point of working this way is that there is never a broken, half-finished
program sitting on disk — every stage ends with something you can actually play,
which makes it obvious where a bug was introduced. `docs/BUILD_GUIDE.md` walks
through each stage and the idea it introduces.

The window version came last on purpose. Its guessing logic is the same as the
terminal game's, so the only genuinely new things in it are opening a window,
drawing by coordinate, and reading mouse clicks.

## Concepts used

**Terminal** — `random.choice` to pick the word, a list to remember which
letters have been tried, a `while` loop for the round, `if`/`elif`/`else` for
the input checks, string building to render the blanks, and a list of drawings
indexed by the number of wrong guesses so `pictures[wrong]` is always the right
picture.

**Window** — `pygame`: creating a window and a game loop, `pygame.Rect` plus
`collidepoint` to work out which letter was clicked, and `draw.line` and
`draw.circle` to build the figure one body part at a time.

## Ideas for the next version

- read the words from `words.txt` instead of the hard-coded list
- add categories (animals, space, food) and let the player pick one
- keep a score or a streak across rounds
- add a hint that reveals a letter at the cost of a guess
