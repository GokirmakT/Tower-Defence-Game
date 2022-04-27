import pygame

from TowerDefence.Units import Unit

pygame.init()

win = pygame.display.set_mode((500, 800))

pygame.display.set_caption("First Game")

Unit = Unit(250, 250)

def draw_game():

    win.fill((0,0,0))

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

    #monster
    pygame.draw.rect(win, (255, 0, 0), (10, 760, 40, 40))


    for x in range (len(Unit.units)):
        pygame.draw.rect(win, (255, 0, 0), Unit.units[x])

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