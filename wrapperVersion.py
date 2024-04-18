import pygame
import sys
from cipher import encryption_mapping

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
hint_font = pygame.font.SysFont(None, 18)

# Define the mapping for encryption
encryption_mapping = encryption_mapping()

actual_text = "Here is my text and I do not know what is the solution".lower()

user_guess = ['_' if char.isalpha() else ' ' if char == ' ' else char for char in actual_text]

hints = [encryption_mapping[char.lower()] if char.isalpha() else ' ' if char == ' ' else char for char in actual_text]
offset = 1.2



# Main Loop
while True:
    screen.fill(WHITE)

    text_surface = font.render("Cryptogram", True, BLACK)
    screen.blit(text_surface, (50, 50))

    text_x = 50
    text_y = 100
    hint_y = 130

    for guess, hint in zip(user_guess, hints):
        text = guess + ' ' if guess == '_' else guess
        text_surface = font.render(text, True, BLACK)
        hint_surface = hint_font.render(hint, True, BLACK)

        # Check if adding text surface width exceeds screen width
        if text_x + text_surface.get_width() > WIDTH - 50:
            # Move to the next line
            offset += 1
            text_x = 50
            text_y += text_surface.get_height() + 10
            hint_y += hint_surface.get_height() + offset * 10

        offset = 1.2
        screen.blit(text_surface, (text_x, text_y))
        screen.blit(hint_surface, (text_x, hint_y))

        # Update x position for next iteration
        text_x += text_surface.get_width() + 10  # Add some space between text and hint

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.flip()