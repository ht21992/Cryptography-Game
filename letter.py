import pygame

pygame.font.init()
font = pygame.font.SysFont(None, 36)
cursor_font = pygame.font.SysFont(None, 22)
hint_font = pygame.font.SysFont(None, 18)

class Color:
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (60, 179, 113)


class Letter(pygame.sprite.Sprite):

    def __init__(self, x, y, char, actual_char, hint, hint_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.char = char.strip()
        self.actual_char = actual_char.strip()
        self.hint = hint.strip()
        self.hint_y = hint_y
        self.clicked = False
        self.update_time = pygame.time.get_ticks()
        self.text_surface = font.render(char, True, Color.BLACK)
        self.hint_surface = hint_font.render(hint, True, Color.BLACK)
        self.cursor_surface = self.cursor_surface = cursor_font.render('', True, Color.GREEN)
        self.rect = self.text_surface.get_rect()
        self.rect.topleft = (x, y)


    def click(self,value):
        self.clicked = value

    def update(self,screen):
        # blink_animation_cool_down = 500  #  blink animation cooldown
        # if pygame.time.get_ticks() - self.update_time > blink_animation_cool_down:
        #     self.update_time = pygame.time.get_ticks()
        self.draw_cursor(screen)
        self.update_char(screen)

    def draw_cursor(self,screen):
        if self.clicked:
            self.cursor_surface = cursor_font.render('|', True, Color.GREEN)
            cursor_rect = self.cursor_surface.get_rect(center=(self.rect.centerx - 10, self.rect.centery))
            screen.blit(self.cursor_surface, cursor_rect)
            

    def update_char(self,screen):
        screen.blit(self.text_surface, (self.x, self.y))


    def draw(self, screen):
        screen.blit(self.text_surface, (self.x, self.y))
        screen.blit(self.hint_surface, (self.x, self.hint_y))