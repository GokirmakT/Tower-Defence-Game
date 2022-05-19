import pygame
import pygame.font
import os
pygame.init()

HP_type = pygame.font.SysFont(None, 30)

left_enemy = [pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L1E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L2E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L3E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L4E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L5E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L6E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L7E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L8E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L9E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L10E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L11E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L12E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L13E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L14E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L15E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L16E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L17E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L18E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L19E.png")), (80, 80)),
              pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "L20E.png")), (80, 80)),
              ]

right_enemy = [pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R1E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R2E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R3E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R4E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R5E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R6E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R7E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R8E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R9E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R10E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R11E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R12E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R13E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R14E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R15E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R16E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R17E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R18E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R19E.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("Enemy_images", "R20E.png")), (80, 80)),
               ]

class Monster():
    def __init__(self, x, y, health, player):
        self.x = x
        self.y = y
        self.speed = 3
        self.health = health
        self.stepIndex = 0
        self.stepIndex_player2 = 0

        if player == 1:
            self.direction = left_enemy
        if player == 2:
            self.direction = right_enemy

    def step(self, player):
        if player == 1:
            if self.stepIndex >= 20:
                self.stepIndex = 0

        if player == 2:
            if self.stepIndex_player2 >= 20:
                self.stepIndex_player2 = 0

    def draw(self, screen, player):
        if player == 1:
            if self.health >= 0:
                self.step(player)
                screen.blit(self.direction[self.stepIndex], (self.x - 20, self.y - 20))
                self.stepIndex += 1
                if 700 >= self.x >= 555:
                    self.direction = right_enemy
                HP = HP_type.render(str(int(self.health)), True, (255, 255, 255))
                screen.blit(HP, (self.x, self.y + 60))

        if player == 2:
            if self.health >= 0:
                self.step(player)
                screen.blit(self.direction[self.stepIndex_player2], (self.x - 20, self.y - 20))
                self.stepIndex_player2 += 1
                if self.x <= 745:
                    self.direction = left_enemy
                HP = HP_type.render(str(int(self.health)), True, (255, 255, 255))
                screen.blit(HP, (self.x, self.y + 60))

    def move(self, player):

        if player == 1:

            if self.x < 557 and self.y == 60:
                self.x += self.speed

            if self.x == 558 and self.y < 592:
                self.y += self.speed

            if self.x > 60 and self.y == 594:
                self.x -= self.speed

        if player == 2:

            if self.x > 743 and self.y == 60:
                self.x -= self.speed

            if self.x == 742 and self.y < 592:
                self.y += self.speed

            if self.x < 1240 and self.y == 594:
                self.x += self.speed

    def off_screen(self, player):
        if player == 1:
            if (self.x == 60 and self.y == 594):
                return True

        if player == 2:
            if (self.x >= 1239 and self.y == 594):
                return True

    def dead(self, player):
        if player == 1:
            if self.health <= 0:
                return True

        if player == 2:
            if self.health <= 0:
                return True

