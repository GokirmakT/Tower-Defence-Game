import pygame
import pygame.font

pygame.init()

merge_level_text = pygame.font.SysFont(None, 30)

class Unit():
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.merge_level = 1
        self.type = type

    def draw(self, screen):
        pygame.draw.rect(screen, self.type, (self.x, self.y, 60, 60))
        merge_level_data = merge_level_text.render(str(self.merge_level), True, (0, 0, 0))
        screen.blit(merge_level_data, (self.x + 25, self.y + 25))