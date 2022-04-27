import pygame
import random

class Unit:
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.units = []
        self.list_x = [80, 156, 232, 308, 382]
        self.list_y = [482, 552, 622, 692]

    def unit_fire(self, win, userInput):

        if userInput[pygame.K_e]:
            pygame.draw.rect(win, (255, 0, 0), pygame.Rect(50, 50, 40, 40))

    def draw_unit(self, win):

        self.x = random.choice(self.list_x)
        self.y = random.choice(self.list_y)
        unit = pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.x, self.y, 40, 40))

        for x in range(len(self.units)):
            if self.units[x] == unit:
                unit = pygame.draw.rect(win, (255, 34, 250), pygame.Rect(self.x, self.y, 40, 40))
                self.draw_unit(win)
                break

        self.units.append(unit)
        print(unit)
