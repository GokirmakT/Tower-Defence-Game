import random

import pygame
import pygame.font

from TowerDefence.monster import Monster

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color = RED

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

BLOCK_SIZE = 40

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40

# This sets the margin between each cell
MARGIN = 5

grid = []

for row in range(5):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(3):
        grid[row].append(None)  # Append a cell


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

monster = Monster(screen)

Monster.create_monster(monster)

rects = []
x = 1


selected = None

# --- mainloop ---

clock = pygame.time.Clock()
is_running = True

def draw_unit():

    column = random.randint(0, 2)
    row = random.randint(0, 4)
    if grid[row][column] != None:
        draw_unit()
        print(grid[row][column])
    else:

        print("Grid coordinates: ", row, column)

        rect_x = ((column+3)*45)+ 5
        rect_y = ((row+12)*45)+ 5
        print(rect_x, rect_y)
        rects.append(pygame.Rect(rect_x, rect_y, BLOCK_SIZE, BLOCK_SIZE))
        grid[row][column] = pygame.Rect(rect_x, rect_y, BLOCK_SIZE, BLOCK_SIZE)

while is_running:

    # --- events ---

    for event in pygame.event.get():

        # --- global events ---

        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
            if event.key == pygame.K_a:
                draw_unit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
               for i, r in enumerate(rects):
                    if r.collidepoint(event.pos):
                        selected = i
                        selected_offset_x = r.x - event.pos[0]
                        selected_offset_y = r.y - event.pos[1]
                        print("tutuldu: ", event.pos[0], event.pos[1])
                        column_del = ((event.pos[0]) // (WIDTH + MARGIN)) - 3
                        row_del = ((event.pos[1]) // (HEIGHT + MARGIN)) - 12
                        print(row_del, column_del)



        elif event.type == pygame.MOUSEBUTTONUP:
            if selected is not None:
                if event.button == 1 and 125 <= rects[selected].x <= 345 and 535 <= rects[selected].y <= 660:

                    column = ((rects[selected].x + 20) // (WIDTH + MARGIN)) - 3
                    row = ((rects[selected].y + 20) // (HEIGHT + MARGIN)) - 12

                    rects[selected].x = ((column + 3) * 45) + 5
                    rects[selected].y = ((row + 12) * 45) + 5

                    print("bırakıldı: ", rects[selected])
                    grid[row][column] = rects[selected]
                    grid[row_del][column_del] = None
                    selected = None

        elif event.type == pygame.MOUSEMOTION:
            if selected is not None:  # selected can be `0` so `is not None` is required
                # move object

                rects[selected].x = event.pos[0] + selected_offset_x
                rects[selected].y = event.pos[1] + selected_offset_y
                print("sürükleniyor: ", rects[selected])

        # --- objects events ---

        '''
       button.handle_event(event)
       '''

    # --- updates ---

    # empty

    # --- draws ---

    screen.fill(BLACK)

    # path1
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 405, 500, 60))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 465, 60, 335))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(440, 465, 60, 335))

    # boundry - line
    pygame.draw.rect(screen, (100, 150, 255), pygame.Rect(0, 400, 500, 5))

    # grid empty
    pygame.draw.rect(screen, (0, 100, 255), (60, 465, 380, 285), 5)

    '''
    button.draw(screen)    
    '''

    # Draw the grid
    for row in range(5):
        for column in range(3):

            color = WHITE
            rec_w = pygame.draw.rect(screen, color,
                                     [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH, HEIGHT])

            if grid[row][column] != None:
                for r in rects:
                    color = RED
                    pygame.draw.rect(screen, color, r)

    Monster.draw_monster(monster)

    Monster.path_monster(monster)

    Monster.draw_HP(monster)

    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()
print(grid)
print(rects)