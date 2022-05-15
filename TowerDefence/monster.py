import pygame
import pygame.font

pygame.init()

HP_type = pygame.font.SysFont(None, 30)


class Monster():
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.speed = 3
        self.health = health


    def draw(self, screen):
        if self.health >= 0:
            pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 60, 60))
            HP = HP_type.render(str(self.health), True, (255, 255, 255))
            screen.blit(HP, (self.x, self.y + 60))

    def move(self):
        # sağ
        if self.x < 557 and self.y == 60:
            self.x += self.speed

        if self.x == 558 and self.y < 592:
            self.y += self.speed

        if self.x > 60 and self.y == 594:
            self.x -= self.speed

    def off_screen(self):
        if (self.x == 60 and self.y == 594) or (self.health <= 0) :
            return True

