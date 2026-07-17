"""
CLICKABLE HANGMAN  -  Python + Pygame (interactive version)
Same game as the terminal one, but you click letters with the mouse.
Only uses: variables, lists, if, loops, and functions (no classes).

Install once:   pip install pygame-ce
Run the game:   python hangman_gui.py
"""

import random
import pygame

# ---- 1. Start pygame and make a window ----
pygame.init()
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Hangman")
clock = pygame.time.Clock()

# ---- 2. Colors (Red, Green, Blue values from 0 to 255) ----
BACKGROUND = (25, 28, 45)
WHITE      = (240, 240, 245)
GRAY       = (90, 98, 130)
GREEN      = (60, 200, 120)
RED        = (230, 80, 90)
YELLOW     = (250, 200, 60)

# ---- 3. Text sizes ----
big_font   = pygame.font.SysFont("Arial", 55, bold=True)
small_font = pygame.font.SysFont("Arial", 24, bold=True)

# ---- 4. Our words and game variables ----
words   = ["PYTHON", "ROCKET", "GUITAR", "DRAGON", "PLANET", "GAMER"]
secret  = random.choice(words)   # the word to guess
guessed = []                     # letters the player has clicked
wrong   = 0                      # how many wrong guesses so far

# ---- 5. Make a clickable box for every letter A to Z ----
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
boxes   = []                     # one box (rectangle) per letter
x = 30
y = 430
for letter in letters:
    box = pygame.Rect(x, y, 45, 45)
    boxes.append(box)
    x = x + 52
    if x > 650:                  # start a new row
        x = 30
        y = y + 52


def draw_man(wrong):
    """Draw the gallows, then one body part for each wrong guess."""
    pygame.draw.line(screen, WHITE, (80, 350), (200, 350), 5)   # base
    pygame.draw.line(screen, WHITE, (140, 350), (140, 90), 5)   # pole
    pygame.draw.line(screen, WHITE, (140, 90), (230, 90), 5)    # top
    pygame.draw.line(screen, WHITE, (230, 90), (230, 120), 3)   # rope
    if wrong >= 1:
        pygame.draw.circle(screen, RED, (230, 145), 25, 4)      # head
    if wrong >= 2:
        pygame.draw.line(screen, RED, (230, 170), (230, 250), 4)  # body
    if wrong >= 3:
        pygame.draw.line(screen, RED, (230, 190), (200, 225), 4)  # left arm
    if wrong >= 4:
        pygame.draw.line(screen, RED, (230, 190), (260, 225), 4)  # right arm
    if wrong >= 5:
        pygame.draw.line(screen, RED, (230, 250), (205, 300), 4)  # left leg
    if wrong >= 6:
        pygame.draw.line(screen, RED, (230, 250), (255, 300), 4)  # right leg


def player_won():
    """Return True if every letter of the secret word has been guessed."""
    for letter in secret:
        if letter not in guessed:
            return False
    return True


# ---- 6. The main game loop ----
running = True
while running:

    # -- check for mouse clicks --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the game is over, a click starts a new game
            if wrong >= 6 or player_won():
                secret = random.choice(words)
                guessed = []
                wrong = 0
            else:
                # otherwise, see which letter was clicked
                for i in range(26):
                    if boxes[i].collidepoint(event.pos):
                        letter = letters[i]
                        if letter not in guessed:
                            guessed.append(letter)
                            if letter not in secret:
                                wrong = wrong + 1

    # -- draw everything --
    screen.fill(BACKGROUND)

    # title
    title = big_font.render("HANGMAN", True, YELLOW)
    screen.blit(title, (250, 20))

    # the hangman drawing
    draw_man(wrong)

    # the word with blanks, like  P Y _ _ _ _
    shown = ""
    for letter in secret:
        if letter in guessed:
            shown = shown + letter + " "
        else:
            shown = shown + "_ "
    word_text = big_font.render(shown, True, WHITE)
    screen.blit(word_text, (330, 200))

    # the letter buttons
    for i in range(26):
        letter = letters[i]
        box = boxes[i]
        if letter in guessed and letter in secret:
            color = GREEN
        elif letter in guessed:
            color = RED
        else:
            color = GRAY
        pygame.draw.rect(screen, color, box)
        text = small_font.render(letter, True, WHITE)
        screen.blit(text, (box.x + 12, box.y + 8))

    # win or lose message
    if player_won():
        msg = big_font.render("YOU WIN!", True, GREEN)
        screen.blit(msg, (240, 350))
    elif wrong >= 6:
        msg = big_font.render("GAME OVER", True, RED)
        screen.blit(msg, (210, 350))
        answer = small_font.render("Word was: " + secret, True, WHITE)
        screen.blit(answer, (270, 410))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
