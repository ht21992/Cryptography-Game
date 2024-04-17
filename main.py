import pygame
import sys

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cryptogram Game")

# Load font
font = pygame.font.SysFont(None, 36)

# Define the mapping for encryption
encryption_mapping = {
    'a': 't', 'b': 'h', 'c': 'i', 'd': 's', 'e': 't', 'f': 'y', 'g': ' ', 'h': 's',
    'i': 'o', 'j': 'l', 'k': 't', 'l': 'm', 'm': 'n', 'n': ' ', 'o': ' ', 'p': ' ',
    'q': ' ', 'r': 'b', 's': 'k', 't': 'l', 'u': ' ', 'v': ' ', 'w': ' ', 'x': 'r',
    'y': 'u', 'z': ' '
}

actual_text = "Here is my text".lower()

user_guess = ['_' if char.isalpha() else ' ' if char == ' ' else char for char in actual_text]

hints = [encryption_mapping[char.lower()] if char.isalpha() else ' ' if char == ' ' else char for char in actual_text]

clicked_index = None
cursor_visible = False
cursor_timer = 0

# Main Loop
while True:
    screen.fill(WHITE)

    text_surface = font.render("Cryptogram", True, BLACK)
    screen.blit(text_surface, (50, 50))

    for i, (guess, hint) in enumerate(zip(user_guess, hints)):
        text = guess + ' ' if guess == '_' else guess
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (50 + i * 30, 100))
        hint_surface = font.render(hint, True, BLACK)
        screen.blit(hint_surface, (50 + i * 30, 150))

    # Blinking cursor
    if cursor_visible and clicked_index != None:
        if actual_text[clicked_index].strip():
            cursor_surface = font.render('|', True, BLACK)
            cursor_position = (30 + clicked_index * 30 + font.size(user_guess[clicked_index])[0], 100)
            screen.blit(cursor_surface, cursor_position)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                clicked_index = (x - 50) // 30 if 50 <= x <= 50 + len(actual_text) * 30 else None
                cursor_visible = True
        elif event.type == pygame.KEYDOWN:

            if clicked_index is not None and event.unicode.isalpha():
                letter = event.unicode.lower()
                if letter == actual_text[clicked_index].lower():
                    user_guess[clicked_index] = actual_text[clicked_index].lower()
                    clicked_index = None
                else:
                    # If the input is incorrect, flash the screen red for 0.5 seconds
                    screen.fill(RED)
                    pygame.display.flip()
                    pygame.time.wait(200)
                    screen.fill(WHITE)
                # clicked_index = None
                cursor_visible = False

    # Check for win condition
    if ''.join(user_guess) == actual_text:
        print("Congratulations! You decrypted the text!")
        pygame.quit()
        sys.exit()

    # Toggle cursor visibility every 500 milliseconds
    cursor_timer += 1
    if cursor_timer >= 200:  # Change this value to adjust blinking speed
        cursor_timer = 0
        cursor_visible = not cursor_visible

    pygame.display.flip()