import random

import pygame
import pygame.font


pygame.init()

merge_level_text = pygame.font.SysFont(None, 30)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (27, 161, 226)
ORANGE = (250, 104, 0)
YELLOW = (227, 200, 0)
BROWN = (130, 90, 44)
GRAY = (128, 128, 128)
PURPLE = (128, 0, 128)
DARK_GREEN = (0, 100, 0)
LIGHT_GREEN = (144, 238, 144)



class Unit():
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.level = 1
        self.merge_level = 1
        self.type = type
        self.damage = 10
        self.cool_down_count = 0
        self.unit_hit = False
        #types = [RED, BROWN, YELLOW, CYAN, ORANGE, **** GREEN, DARK_GREEN, PURPLE, GRAY, LIGHT_GREEN]
        self.unit_speeds = [18, 20, 20, 25, 25, 19, 18, 25, 25, 11]
        self.LIGHT_GREEN_count = 0
        self.LIGHT_GREEN_damage = 150
        self.LIGHT_GREEN_limit = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.type, (self.x, self.y, 60, 60))
        merge_level_data = merge_level_text.render(str(self.merge_level), True, (0, 0, 0))
        screen.blit(merge_level_data, (self.x + 25, self.y + 25))

    def cooldown(self, merge_level):

        if self.type == RED:
            order = 0
        if self.type == BROWN:
            order = 1
        if self.type == YELLOW:
            order = 2
        if self.type == CYAN:
            order = 3
        if self.type == ORANGE:
            order = 4
        if self.type == GREEN:
            order = 5
        if self.type == DARK_GREEN:
            order = 6
        if self.type == PURPLE:
            order = 7
        if self.type == GRAY:
            order = 8
        if self.type == LIGHT_GREEN:
            order = 9

        if self.cool_down_count >= self.unit_speeds[order] / merge_level:
            self.cool_down_count = 0
            self.unit_hit = True

        elif self.cool_down_count < 25:
            self.cool_down_count += 1
            self.unit_hit = False


    def hit(self, monster_health, merge_level, neighbor, max_health):

        self.cooldown(merge_level)
        if self.type == RED and self.unit_hit == True:
            monster_health -= 50 * neighbor

        if self.type == BROWN and self.unit_hit == True:
            monster_health -= 250

        if self.type == YELLOW and self.unit_hit == True:
            monster_health -= 100

        if self.type == CYAN and self.unit_hit == True:
            monster_health -= 80

        if self.type == ORANGE and self.unit_hit == True:
            if max_health >= monster_health * 100 / 30:
                monster_health -= 977283642983
            else:
                monster_health -= 140

        if self.type == GREEN and self.unit_hit == True:
            monster_health -= 28

        if self.type == DARK_GREEN and self.unit_hit == True:
            monster_health -= self.LIGHT_GREEN_damage
            self.LIGHT_GREEN_count += 1
            if self.LIGHT_GREEN_count == 5 and self.LIGHT_GREEN_limit <= 8:
                self.LIGHT_GREEN_count = 0
                self.LIGHT_GREEN_damage = self.LIGHT_GREEN_damage * 11 / 10
                monster_health -= self.LIGHT_GREEN_damage
                self.LIGHT_GREEN_limit += 1


        if self.type == PURPLE and self.unit_hit == True:
            monster_health -= 42

        if self.type == GRAY and self.unit_hit == True:

            kill = random.randint(1, 50)
            if kill <= 3:
                monster_health -= 920374903274
            else:
                monster_health -= 60


        if self.type == LIGHT_GREEN and self.unit_hit == True:
            monster_health -= 60

        return monster_health
