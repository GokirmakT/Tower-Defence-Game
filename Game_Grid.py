import pygame

class Game_Grid:

    def draw_grid(win):
        #path1
        pygame.draw.rect(win, (255, 255, 255), pygame.Rect(0, 405, 500, 60))
        pygame.draw.rect(win, (255, 255, 255), pygame.Rect(0, 465, 60, 335))
        pygame.draw.rect(win, (255, 255, 255), pygame.Rect(440, 465, 60, 335))

        #button1
        pygame.draw.rect(win, (0, 0, 255), pygame.Rect(200, 750, 100, 50))

        #boundry - line
        pygame.draw.rect(win, (100, 150, 255), pygame.Rect(0, 400, 500, 5))

        #grid empty
        pygame.draw.rect(win, (0, 100, 255), (60, 465, 380, 285), 5)

        #grid col
        pygame.draw.rect(win, (0, 100, 255), (136, 465, 5, 285))
        pygame.draw.rect(win, (0, 100, 255), (212, 465, 5, 285))
        pygame.draw.rect(win, (0, 100, 255), (288, 465, 5, 285))
        pygame.draw.rect(win, (0, 100, 255), (364, 465, 5, 285))

        #grid row
        pygame.draw.rect(win, (0, 100, 255), (60, 535, 380, 5))
        pygame.draw.rect(win, (0, 100, 255), (60, 605, 380, 5))
        pygame.draw.rect(win, (0, 100, 255), (60, 675, 380, 5))