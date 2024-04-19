import pygame
import sys
from cipher import encryption_mapping
from letter import Letter
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()


# Groups
letter_group = pygame.sprite.Group()

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
actual_list = list(actual_text)
user_guess = ['_' if char.isalpha() else ' ' if char == ' ' else char for char in actual_text]

hints = [encryption_mapping[char.lower()] if char.isalpha() else ' ' if char == ' ' else char for char in actual_text]
offset = 1.2

cursor_timer = 0
clicked_letter = None

# Main Loop
while True:


    screen.fill(WHITE)

    text_surface = font.render("Cryptogram", True, BLACK)
    screen.blit(text_surface, (50, 50))

    text_x = 50
    text_y = 100
    hint_y = 130



    for  guess, hint, actual_char in zip(user_guess, hints,actual_list):
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


        new_letter = Letter(text_x, text_y, text,actual_char, hint, hint_y)
        letter_group.add(new_letter)
        offset = 1.2
        new_letter.draw(screen)

        # Update x position for next iteration
        text_x += text_surface.get_width() + 10  # Add some space between text and hint

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for letter in letter_group:
                    # check the collision between the click and the LETTER
                    if letter.rect.collidepoint(event.pos):
                        letter.click(True)
                        clicked_letter = letter

                    else:
                        letter.click(False)

        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha() and clicked_letter:
                if event.unicode.lower() == clicked_letter.actual_char.lower():
                    clicked_letter.char = event.unicode.lower()
                    clicked_letter.text_surface = font.render(event.unicode.lower(), True, (0,0,0))
                    clicked_letter.click(False)
                    clicked_letter = None


                else:
                    screen.fill(RED)
                    pygame.display.flip()
                    pygame.time.wait(200)
                    screen.fill(WHITE)

    # Update and draw
    for letter in letter_group:
        letter.update(screen)

    pygame.display.flip()
