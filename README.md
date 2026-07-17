# Hangman — Python Course Capstone

A beginner-friendly Hangman game, built in two versions: a simple **terminal**
game (typing) and an **interactive window** game (clicking with the mouse).


Both versions play the same way — guess the secret word one letter at a time
before the hangman is fully drawn — and they share the exact same game logic.
The only difference is how the player interacts with it.

## What's in this repo

```
hangman-python/
├── README.md                  <- you are here
├── requirements.txt           <- what to install (only needed for the window version)
├── words.txt                  <- extra words (used in a stretch exercise)
│
├── terminal/                  <- the simple TYPING version
│   ├── hangman.py             <- the finished terminal game
│   └── build_steps/           <- build it up in 4 small, working stages
│       ├── step1_pick_word.py
│       ├── step2_guessing.py
│       ├── step3_win_lose.py
│       └── step4_drawing.py   <- (same as the finished game)
│
├── gui/                       <- the CLICKABLE window version
│   └── hangman_gui.py         <- click letters with the mouse
│
└── docs/
    └── BUILD_GUIDE.md         <- step-by-step teaching guide
```

## How to run it

**Terminal version** (needs nothing but Python):

```
cd terminal
python hangman.py
```

**Window version** (needs pygame — install it once):

```
pip install -r requirements.txt
cd gui
python hangman_gui.py
```

## The learning path

The idea is to build the **terminal version first**, one small step at a time —
each file in `terminal/build_steps/` runs on its own and does a little more than
the last:

1. **Step 1** — pick a random word and show it as blanks
2. **Step 2** — let the player type letters and reveal them
3. **Step 3** — count wrong guesses; add winning and losing
4. **Step 4** — draw the hangman and allow "play again" (the finished game)

Once the terminal game works and is understood, the **window version** in `gui/`
is the fun upgrade: it's the same logic with a mouse and drawings added on top.

Full teaching notes are in [`docs/BUILD_GUIDE.md`](docs/BUILD_GUIDE.md).

## Concepts used

Everything here is built from beginner Python: variables, lists, `if`/`else`,
`while` loops, functions, and the `random` module. The window version adds a
first taste of `pygame` (a window, a game loop, mouse clicks, and drawing).
