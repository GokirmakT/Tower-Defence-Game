import pygame

from TowerDefence.Units import Unit
from TowerDefence.Game_Grid import Game_Grid

pygame.init()

win = pygame.display.set_mode((500, 800))

pygame.display.set_caption("First Game")

Unit = Unit(250, 250)

def draw_game():

    win.fill((0,0,0))

    Game_Grid.draw_grid(win)

    #monster
    pygame.draw.rect(win, (255, 0, 0), (10, 760, 40, 40))


    for x in range (len(Unit.units)):
        pygame.draw.rect(win, (255, 0, 0), Unit.units[x])

    #call unit
    if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        if mx >= 200 and mx <= 300 and my >= 750 and my <= 800:
            Unit.draw_unit(win)

    pygame.time.delay(70)

    pygame.display.update()

rectangle_draging = False
run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if len(Unit.units) >= 1:
                    if Unit.units[0].collidepoint(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = Unit.units[0].x - mouse_x
                        offset_y = Unit.units[0].y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                Unit.units[0].x = mouse_x + offset_x
                Unit.units[0].y = mouse_y + offset_y

    userInput = pygame.key.get_pressed()

    draw_game()