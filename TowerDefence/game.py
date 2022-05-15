import random
import pygame
import pygame.font
from random import sample

from TowerDefence.monster import Monster
from TowerDefence.unit import Unit

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

player_mana = 100
unit_cost = 10
text_type = pygame.font.SysFont(None, 30)

middle_road = pygame.transform.scale(pygame.image.load('road_5.png'), (30, 30))
upper_road = pygame.transform.scale(pygame.image.load('road_2.png'), (30, 30))
under_road = pygame.transform.scale(pygame.image.load('road_8.png'), (30, 30))
left_road = pygame.transform.scale(pygame.image.load('road_4.png'), (30, 30))
right_road = pygame.transform.scale(pygame.image.load('road_6.png'), (30, 30))
corner_road1 = pygame.transform.scale(pygame.image.load('road_3.png'), (30, 30))
corner_road2 = pygame.transform.scale(pygame.image.load('road_9.png'), (30, 30))
corner_road3 = pygame.transform.scale(pygame.image.load('road_13.png'), (30, 30))
corner_road4 = pygame.transform.scale(pygame.image.load('road_10.png'), (30, 30))

Cursor_rec_x = 330
Cursor_rec_y = 330

SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 715

BLOCK_SIZE = 60

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 60
HEIGHT = 60

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

monsters = []
units = []
types = [RED, BROWN, YELLOW, CYAN, ORANGE, GREEN, DARK_GREEN, PURPLE, GRAY, LIGHT_GREEN]
deck_type = sample(types, 5)

unit_drag = None
dragging = False
selected = None

monster_health = 115
monster = Monster(0, 60, monster_health)
monsters.append(monster)
created_monsters = 1

# --- mainloop ---

clock = pygame.time.Clock()
is_running = True

def create_unit():

    column = random.randint(0, 2)
    row = random.randint(0, 4)
    if grid[row][column] != None:
        create_unit()
        print(grid[row][column])
    else:

        print("Grid coordinates: ", row, column)

        rect_x = ((column + 4) * 65) + 5
        rect_y = ((row + 3) * 65) + 5
        print(rect_x, rect_y)
        type = random.choice(deck_type)
        unit = Unit(rect_x, rect_y, type)
        units.append(unit)
        grid[row][column] = unit

def remove(arr):

    kill = random.randint(0, len(arr) - 1)
    if kill == len(arr) - 1:
        remove(arr)
    else:
        current_monster_health = monsters[kill].health
        current_monster_health = Unit.hit(unit_fire, current_monster_health, unit_fire.merge_level)
        monsters[kill].health = current_monster_health

while is_running:

    # --- events ---

    for event in pygame.event.get():

        # --- global events ---

        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                print("tutuldu: ", event.pos[0], event.pos[1])


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

            if event.key == pygame.K_q and len(units) <= 14 and player_mana >= unit_cost:
                create_unit()
                player_mana = player_mana - unit_cost
                unit_cost += 10

            if event.key == pygame.K_w and Cursor_rec_y > 230:
                Cursor_rec_y -= 65

            if event.key == pygame.K_a and Cursor_rec_x > 265:
                Cursor_rec_x -= 65

            if event.key == pygame.K_s and Cursor_rec_y < 460:
                Cursor_rec_y += 65

            if event.key == pygame.K_d and Cursor_rec_x < 395:
                Cursor_rec_x += 65

            if event.key == pygame.K_SPACE:

                for i, unit in enumerate(units):
                    if unit.x == Cursor_rec_x and unit.y == Cursor_rec_y:

                        hold_Cursor_rerc_x = Cursor_rec_x
                        hold_Cursor_rerc_y = Cursor_rec_y

                        cursor_column = ((Cursor_rec_x) // (WIDTH + MARGIN)) - 4
                        cursor_row = ((Cursor_rec_y) // (HEIGHT + MARGIN)) - 3

                        if grid[cursor_row][cursor_column] is not None:

                            unit_drag = grid[cursor_row][cursor_column]
                            print(unit_drag)
                            grid[cursor_row][cursor_column] = None
                            dragging = True

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_SPACE and dragging:

                unit_drag.x = Cursor_rec_x
                unit_drag.y = Cursor_rec_y

                column = ((unit_drag.x) // (WIDTH + MARGIN)) - 4
                row = ((unit_drag.y) // (HEIGHT + MARGIN)) - 3

                if grid[row][column] is not None:

                    if grid[row][column].merge_level == unit_drag.merge_level:

                        if grid[row][column].type == unit_drag.type or unit_drag.type == GREEN or unit_drag.type == PURPLE:

                            if unit_drag.type == PURPLE:

                                if grid[row][column].type == unit_drag.type:

                                    units.remove(grid[row][column])
                                    grid[row][column] = None
                                    unit_drag.merge_level += 1
                                    unit_drag.type = random.choice(deck_type)
                                    grid[row][column] = unit_drag

                                else:

                                    grid[cursor_row][cursor_column] = unit_drag
                                    unit_drag.x = hold_Cursor_rerc_x
                                    unit_drag.y = hold_Cursor_rerc_y
                                    unit_copy = grid[row][column]
                                    unit_drag.type = unit_copy.type

                            elif grid[row][column].type == CYAN and unit_drag.type == CYAN:

                                units.remove(grid[row][column])
                                grid[row][column] = None
                                unit_drag.merge_level += 1
                                unit_drag.type = random.choice(deck_type)
                                grid[row][column] = unit_drag
                                player_mana += 80 * (unit_drag.merge_level - 1)

                            elif unit_drag.type == GREEN:

                                if grid[row][column].type == CYAN:

                                    unit_merge_level_up = grid[row][column]
                                    units.remove(grid[row][column])
                                    grid[row][column] = None
                                    unit_drag.merge_level += 1
                                    unit_drag.type = unit_merge_level_up.type
                                    grid[row][column] = unit_drag
                                    player_mana += 80 * (unit_drag.merge_level - 1)

                                else:
                                    unit_merge_level_up = grid[row][column]
                                    units.remove(grid[row][column])
                                    grid[row][column] = None
                                    unit_drag.merge_level += 1
                                    unit_drag.type = unit_merge_level_up.type
                                    grid[row][column] = unit_drag

                            else:

                                units.remove(grid[row][column])
                                grid[row][column] = None
                                unit_drag.merge_level += 1
                                unit_drag.type = random.choice(deck_type)
                                grid[row][column] = unit_drag

                        else:
                            grid[cursor_row][cursor_column] = unit_drag
                            unit_drag.x = hold_Cursor_rerc_x
                            unit_drag.y = hold_Cursor_rerc_y
                    else:
                        grid[cursor_row][cursor_column] = unit_drag
                        unit_drag.x = hold_Cursor_rerc_x
                        unit_drag.y = hold_Cursor_rerc_y

                if grid[row][column] is None:
                    grid[cursor_row][cursor_column] = unit_drag
                    unit_drag.x = hold_Cursor_rerc_x
                    unit_drag.y = hold_Cursor_rerc_y

                dragging = False

        # --- objects events ---

        '''
       button.handle_event(event)
       '''

    # --- updates ---

    # empty

    # --- draws ---

    screen.fill(BLACK)

    pygame.draw.rect(screen, (255, 255, 255), (30, 200, 190, 320), 5)

    mana = text_type.render(str(player_mana), True, (255, 255, 255))
    screen.blit(mana, (35, 205))

    display_unit_cost = text_type.render(str(unit_cost), True, (255, 255, 255))
    screen.blit(display_unit_cost, (35, 235))


    '''
    button.draw(screen)    
    '''
    #upper road
    for x in range(0, 600, 30):
        screen.blit(upper_road, (x, 45))

    for x in range(0, 540, 30):
        screen.blit(upper_road, (x, 585))
    ####

    #middle road
    for x in range(0, 600, 30):
        screen.blit(middle_road, (x, 75))

    for x in range(75, 630, 30):
        screen.blit(middle_road, (570,x))

    for x in range(0, 600, 30):
        screen.blit(middle_road, (x, 615))
    ####

    #under road
    for x in range(0, 540, 30):
        screen.blit(under_road, (x, 105))

    for x in range(0, 600, 30):
        screen.blit(under_road, (x, 645))
    ####

    #left road
    for x in range(135, 570, 30):
        screen.blit(left_road, (540, x))
    ####

    #right
    for x in range(60, 660, 30):
        screen.blit(right_road, (600, x))
    ####

    screen.blit(corner_road1, (600, 45))
    screen.blit(corner_road2, (600, 645))
    screen.blit(corner_road3, (540, 585))
    screen.blit(corner_road4, (540, 105))


    # Draw the grid
    for row in range(5):
        for column in range(3):

            color = WHITE
            rec_w = pygame.draw.rect(screen, color,
                                     [(MARGIN + WIDTH) * column + MARGIN + 260, (MARGIN + HEIGHT) * row + MARGIN + 195,
                                      WIDTH, HEIGHT])

            if grid[row][column] != None:
                for unit_draw in units:
                    Unit.draw(unit_draw, screen)



    pygame.draw.rect(screen, (0, 0, 255,), (Cursor_rec_x, Cursor_rec_y, 60, 60), 5)

    pygame.draw.rect(screen, (0, 255, 0,), (674, 0, 3, 800))

    for monster_create in monsters:
        if monster_create.x == 126 and monster_create.y == 60:
            if created_monsters % 4 == 0:
                monster_health += 115
            monster = Monster(0, 60, monster_health)
            monsters.append(monster)
            created_monsters += 1

    for monster_move in monsters:
        Monster.move(monster_move)
        if Monster.off_screen(monster_move):
            monsters.remove(monster_move)
            player_mana += 30


    for monster_draw in monsters:
        Monster.draw(monster_draw, screen)

    #ateş etme koşulu

    for unit_fire in units:
        if len(monsters) >= 1 and (monsters[0].x >= 126 and monsters[0].y == 60) or (monsters[0].x == 558) or (monsters[0].y == 594):
            if unit_fire.type == GRAY and len(monsters) >= 2:
                index = len(monsters)
                remove(monsters)

            else:
                current_monster_health = monsters[0].health
                current_monster_health = Unit.hit(unit_fire, current_monster_health, unit_fire.merge_level)
                monsters[0].health = current_monster_health

    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()
print(grid)
print(units)
print(len(units))
