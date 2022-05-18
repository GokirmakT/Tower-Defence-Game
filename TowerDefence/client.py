import sys
from TowerDefence.buton import buton
import random
import pygame
import pygame.font
import os
from random import sample
from TowerDefence.unit import Unit

pygame.init()

SCREEN = pygame.display.set_mode((1350, 715))
pygame.display.set_caption("Menu")

#Manaimg = pygame.transform.scale(pygame.image.load(os.path.join("MANA.png")), (20, 20))

BG = pygame.transform.scale(pygame.image.load("Background2.jpg"), (1350,715))
text_type = pygame.font.SysFont(None, 30)

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

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def play():
    import random

    import pygame
    import pygame.font

    from TowerDefence.monster import Monster

    player_mana = 100
    unit_cost = 10
    text_type = pygame.font.SysFont(None, 30)

    player_mana2 = 100
    unit_cost2 = 10

    middle_road = pygame.transform.scale(pygame.image.load('road_5.png'), (30, 30))
    upper_road = pygame.transform.scale(pygame.image.load('road_2.png'), (30, 30))
    under_road = pygame.transform.scale(pygame.image.load('road_8.png'), (30, 30))
    left_road = pygame.transform.scale(pygame.image.load('road_4.png'), (30, 30))
    right_road = pygame.transform.scale(pygame.image.load('road_6.png'), (30, 30))
    corner_road1 = pygame.transform.scale(pygame.image.load('road_3.png'), (30, 30))
    corner_road2 = pygame.transform.scale(pygame.image.load('road_9.png'), (30, 30))
    corner_road3 = pygame.transform.scale(pygame.image.load('road_13.png'), (30, 30))
    corner_road4 = pygame.transform.scale(pygame.image.load('road_10.png'), (30, 30))
    corner_road5 = pygame.transform.scale(pygame.image.load('road_1.png'), (30, 30))
    corner_road6 = pygame.transform.scale(pygame.image.load('road_7.png'), (30, 30))
    corner_road7 = pygame.transform.scale(pygame.image.load('road_12.png'), (30, 30))
    corner_road8 = pygame.transform.scale(pygame.image.load('road_11.png'), (30, 30))
    castle_1 = pygame.transform.scale(pygame.image.load('castle_1.png'), (100, 100))
    castle_2 = pygame.transform.scale(pygame.image.load('castle_2.png'), (100, 100))

    Cursor_rec_x = 330
    Cursor_rec_y = 330

    Cursor_rec_x_player2 = 980
    Cursor_rec_y_player2 = 330

    SCREEN_WIDTH = 1350
    SCREEN_HEIGHT = 715

    BLOCK_SIZE = 60

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 60
    HEIGHT = 60

    # This sets the margin between each cell
    MARGIN = 5

    grid = []
    grid_player2 = []

    for row in range(5):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        grid_player2.append([])

        for column in range(3):
            grid[row].append(None)  # Append a cell
            grid_player2[row].append(None)

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_rect = screen.get_rect()

    heart = [pygame.rect.Rect(10,680,20,20), pygame.rect.Rect(40,680,20,20), pygame.rect.Rect(70,680,20,20)]
    heart_player2 = [pygame.rect.Rect(1260,680,20,20), pygame.rect.Rect(1290,680,20,20), pygame.rect.Rect(1320,680,20,20)]


    monsters = []
    monsters_player2 = []

    units = []
    units2 = []

    types = [RED, BROWN, YELLOW, CYAN, ORANGE, GREEN, DARK_GREEN, PURPLE, GRAY, LIGHT_GREEN]
    deck_type_player1 = sample(types, 5)
    deck_type_player2 = sample(types, 5)

    unit_drag = None
    dragging = False
    dragging_player2 = False

    neighbor = 0
    neighbor2 = 0

    monster_health_max = 115
    monster_health = 115
    monster = Monster(0, 60, monster_health, 1)
    monsters.append(monster)
    created_monsters = 1

    monster_health_max_player2 = 115
    monster_health_player2 = 115
    monster_player2 = Monster(1300, 60, monster_health_player2, 2)
    monsters_player2.append(monster_player2)
    created_monsters_player2 = 1

    # --- mainloop ---

    clock = pygame.time.Clock()
    is_running = True

    def create_unit_player1():

        column = random.randint(0, 2)
        row = random.randint(0, 4)
        if grid[row][column] != None:
            create_unit_player1()
            print(grid[row][column])
        else:

            print("Grid coordinates: ", row, column)

            rect_x = ((column + 4) * 65) + 5
            rect_y = ((row + 3) * 65) + 5
            print(rect_x, rect_y)
            type = random.choice(deck_type_player1)
            unit = Unit(rect_x, rect_y, type)
            units.append(unit)
            grid[row][column] = unit

    def create_unit_player2():

        column = random.randint(0, 2)
        row = random.randint(0, 4)
        if grid_player2[row][column] != None:
            create_unit_player2()
            print(grid_player2[row][column])
        else:

            print("Grid coordinates: ", row, column)

            rect_x = ((column + 14) * 65) + 5
            rect_y = ((row + 3) * 65) + 5
            print(rect_x, rect_y)
            type = random.choice(deck_type_player2)
            unit = Unit(rect_x, rect_y, type)
            units2.append(unit)
            grid_player2[row][column] = unit

    def random_hit(arr, player, n, health):

        if player == 1:

            kill = random.randint(0, len(arr) - 1)
            if kill == len(arr) - 1:
                random_hit(arr, 1, n, health)
            else:
                current_monster_health = monsters[kill].health
                current_monster_health = Unit.hit(unit_fire, current_monster_health, unit_fire.merge_level, n, health)
                monsters[kill].health = current_monster_health

        if player == 2:

            kill = random.randint(0, len(arr) - 1)
            if kill == len(arr) - 1:
                random_hit(arr, 2, n, health)
            else:
                current_monster_health_player2 = monsters_player2[kill].health
                current_monster_health_player2 = Unit.hit(unit_fire_player2, current_monster_health_player2, unit_fire_player2.merge_level, n, health)
                monsters_player2[kill].health = current_monster_health_player2


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

                # player 1
                # -------------------------------------------------------------------------------------------------------------------------------

                if event.key == pygame.K_RCTRL and len(units2) <= 14 and player_mana2 >= unit_cost2:
                    create_unit_player2()
                    player_mana2 = player_mana2 - unit_cost2
                    unit_cost2 += 10

                if event.key == pygame.K_UP and Cursor_rec_y_player2 > 230:
                    Cursor_rec_y_player2 -= 65

                if event.key == pygame.K_LEFT and Cursor_rec_x_player2 > 915:
                    Cursor_rec_x_player2 -= 65

                if event.key == pygame.K_DOWN and Cursor_rec_y_player2 < 460:
                    Cursor_rec_y_player2 += 65

                if event.key == pygame.K_RIGHT and Cursor_rec_x_player2 < 1000:
                    Cursor_rec_x_player2 += 65

                if event.key == pygame.K_RSHIFT:

                    for i, unit in enumerate(units2):
                        if unit.x == Cursor_rec_x_player2 and unit.y == Cursor_rec_y_player2:

                            hold_Cursor_rerc_x_player2 = Cursor_rec_x_player2
                            hold_Cursor_rerc_y_player2 = Cursor_rec_y_player2

                            cursor_column = ((Cursor_rec_x_player2) // (WIDTH + MARGIN)) - 14
                            cursor_row = ((Cursor_rec_y_player2) // (HEIGHT + MARGIN)) - 3

                            if grid_player2[cursor_row][cursor_column] is not None and dragging is False:
                                unit_drag = grid_player2[cursor_row][cursor_column]
                                print(unit_drag)
                                grid_player2[cursor_row][cursor_column] = None
                                dragging_player2 = True

                if event.key == pygame.K_q and len(units) <= 14 and player_mana >= unit_cost:
                    create_unit_player1()
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

                            if grid[cursor_row][cursor_column] is not None and dragging_player2 is False:
                                unit_drag = grid[cursor_row][cursor_column]
                                print(unit_drag)
                                grid[cursor_row][cursor_column] = None
                                dragging = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RSHIFT and dragging_player2:

                    dragging = False

                    unit_drag.x = Cursor_rec_x_player2
                    unit_drag.y = Cursor_rec_y_player2

                    column = ((unit_drag.x) // (WIDTH + MARGIN)) - 14
                    row = ((unit_drag.y) // (HEIGHT + MARGIN)) - 3

                    if grid_player2[row][column] is not None:

                        if grid_player2[row][column].merge_level == unit_drag.merge_level:

                            if grid_player2[row][column].type == unit_drag.type or unit_drag.type == GREEN or unit_drag.type == PURPLE:

                                if unit_drag.type == PURPLE:

                                    if grid_player2[row][column].type == unit_drag.type:

                                        units2.remove(grid_player2[row][column])
                                        grid_player2[row][column] = None
                                        unit_drag.merge_level += 1
                                        unit_drag.type = random.choice(deck_type_player2)
                                        grid_player2[row][column] = unit_drag

                                    else:

                                        grid_player2[cursor_row][cursor_column] = unit_drag
                                        unit_drag.x = hold_Cursor_rerc_x_player2
                                        unit_drag.y = hold_Cursor_rerc_y_player2
                                        unit_copy = grid_player2[row][column]
                                        unit_drag.type = unit_copy.type

                                elif grid_player2[row][column].type == CYAN and unit_drag.type == CYAN:

                                    units2.remove(grid_player2[row][column])
                                    grid_player2[row][column] = None
                                    unit_drag.merge_level += 1
                                    unit_drag.type = random.choice(deck_type_player2)
                                    grid_player2[row][column] = unit_drag
                                    player_mana += 80 * (unit_drag.merge_level - 1)

                                elif unit_drag.type == GREEN:

                                    if grid_player2[row][column].type == CYAN:

                                        unit_merge_level_up = grid_player2[row][column]
                                        units2.remove(grid_player2[row][column])
                                        grid_player2[row][column] = None
                                        unit_drag.merge_level += 1
                                        unit_drag.type = unit_merge_level_up.type
                                        grid_player2[row][column] = unit_drag
                                        player_mana += 80 * (unit_drag.merge_level - 1)

                                    else:
                                        unit_merge_level_up = grid_player2[row][column]
                                        units2.remove(grid_player2[row][column])
                                        grid_player2[row][column] = None
                                        unit_drag.merge_level += 1
                                        unit_drag.type = unit_merge_level_up.type
                                        grid_player2[row][column] = unit_drag

                                else:

                                    units2.remove(grid_player2[row][column])
                                    grid_player2[row][column] = None
                                    unit_drag.merge_level += 1
                                    unit_drag.type = random.choice(deck_type_player2)
                                    grid_player2[row][column] = unit_drag

                            else:
                                grid_player2[cursor_row][cursor_column] = unit_drag
                                unit_drag.x = hold_Cursor_rerc_x_player2
                                unit_drag.y = hold_Cursor_rerc_y_player2
                        else:
                            grid_player2[cursor_row][cursor_column] = unit_drag
                            unit_drag.x = hold_Cursor_rerc_x_player2
                            unit_drag.y = hold_Cursor_rerc_y_player2

                    if grid_player2[row][column] is None:
                        grid_player2[cursor_row][cursor_column] = unit_drag
                        unit_drag.x = hold_Cursor_rerc_x_player2
                        unit_drag.y = hold_Cursor_rerc_y_player2

                    dragging_player2 = False

                if event.key == pygame.K_SPACE and dragging:

                    dragging_player2 = False

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
                                        unit_drag.type = random.choice(deck_type_player1)
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
                                    unit_drag.type = random.choice(deck_type_player1)
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
                                    unit_drag.type = random.choice(deck_type_player1)
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
                # -------------------------------------------------------------------------------------------------------------------------------



            # --- objects events ---

            '''
           button.handle_event(event)
           '''

        # --- updates ---

        # empty

        # --- draws ---

        screen.fill(BLACK)

        #display deck
        for i, x in enumerate(deck_type_player1):
            y = 270 + (i * 50)
            pygame.draw.rect(screen, x, (110, y, 40, 40))

        mana = text_type.render(str(player_mana), True, (255, 255, 255))
        screen.blit(mana, (35, 205))

        display_unit_cost = text_type.render(str(unit_cost), True, (255, 255, 255))
        screen.blit(display_unit_cost, (35, 235))


        # display deck2
        for i, x in enumerate(deck_type_player2):
            y = 270 + (i * 50)
            pygame.draw.rect(screen, x, (1210, y, 40, 40))

        mana = text_type.render(str(player_mana2), True, (255, 255, 255))
        screen.blit(mana, (1260, 205))

        display_unit_cost = text_type.render(str(unit_cost2), True, (255, 255, 255))
        screen.blit(display_unit_cost, (1260, 235))

        # --------------------------------------------------------------------

#--------------------------------------------------------------------
        # upper road
        for x in range(0, 600, 30):
            screen.blit(upper_road, (x, 45))

        for x in range(0, 540, 30):
            screen.blit(upper_road, (x, 585))
        ####

        # middle road
        for x in range(0, 600, 30):
            screen.blit(middle_road, (x, 75))

        for x in range(75, 630, 30):
            screen.blit(middle_road, (570, x))

        for x in range(0, 600, 30):
            screen.blit(middle_road, (x, 615))
        ####

        # under road
        for x in range(0, 540, 30):
            screen.blit(under_road, (x, 105))

        for x in range(0, 600, 30):
            screen.blit(under_road, (x, 645))
        ####

        # left road
        for x in range(135, 570, 30):
            screen.blit(left_road, (540, x))
        ####

        # right
        for x in range(60, 660, 30):
            screen.blit(right_road, (600, x))
        ####

        screen.blit(corner_road1, (600, 45))
        screen.blit(corner_road2, (600, 645))
        screen.blit(corner_road3, (540, 585))
        screen.blit(corner_road4, (540, 105))
# --------------------------------------------------------------------

        # upper road
        for x in range(730, 1360, 30):
            screen.blit(upper_road, (x, 45))

        for x in range(790, 1360, 30):
            screen.blit(upper_road, (x, 585))
        ####

        # middle road
        for x in range(730, 1360, 30):
            screen.blit(middle_road, (x, 75))

        for x in range(75, 630, 30):
            screen.blit(middle_road, (730, x))

        for x in range(730, 1360, 30):
            screen.blit(middle_road, (x, 615))
        ####

         # under road
        for x in range(790, 1360, 30):
            screen.blit(under_road, (x, 105))

        for x in range(730, 1360, 30):
            screen.blit(under_road, (x, 645))

        # left road
        for x in range(75, 630, 30):
            screen.blit(left_road, (700, x))
        ####

        # right
        for x in range(105, 570, 30):
            screen.blit(right_road, (760, x))
        ####

        screen.blit(corner_road5, (700, 45))
        screen.blit(corner_road7, (760, 585))
        screen.blit(corner_road8, (760, 105))
        screen.blit(corner_road4, (540, 105))
        screen.blit(corner_road6, (700, 645))

        pygame.draw.rect(screen, (255, 255, 255), (80, 594, 2, 70))
        pygame.draw.rect(screen, (255, 255, 255), (1259, 594, 2, 70))

        screen.blit(castle_1, (-30, 560))
        screen.blit(castle_2, (1270, 560))

        for x in range(0, len(heart)):
            pygame.draw.rect(screen, (132, 92, 14), heart[x])

        for x in range(0, len(heart_player2)):
            pygame.draw.rect(screen, (132, 92, 14), heart_player2[x])

        # Draw the grid

        for row in range(5):
            for column in range(3):

                color = WHITE
                rec_w = pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 260,
                                                         (MARGIN + HEIGHT) * row + MARGIN + 195, WIDTH, HEIGHT])
                rec_w_player2 = pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN + 910,
                                                                 (MARGIN + HEIGHT) * row + MARGIN + 195, WIDTH, HEIGHT])

                if grid[row][column] != None:
                    for unit_draw in units:
                        Unit.draw(unit_draw, screen)

                if grid_player2[row][column] != None:
                    for unit_draw in units2:
                        Unit.draw(unit_draw, screen)

        pygame.draw.rect(screen, (0, 0, 255,), (Cursor_rec_x, Cursor_rec_y, 60, 60), 5)
        pygame.draw.rect(screen, (0, 0, 255,), (Cursor_rec_x_player2, Cursor_rec_y_player2, 60, 60), 5)

        pygame.draw.rect(screen, (0, 255, 0,), (663, 0, 3, 800))

        for monster_create in monsters:
            if monster_create.x == 102 and monster_create.y == 60:
                if created_monsters % 4 == 0:
                    monster_health_max += 115
                    monster_health += 115
                monster = Monster(0, 60, monster_health, 1)
                monsters.append(monster)
                created_monsters += 1

        for monster_create_player2 in monsters_player2:
            if monster_create_player2.x == 1198 and monster_create_player2.y == 60:
                if created_monsters_player2 % 4 == 0:
                    monster_health_max_player2 += 115
                    monster_health_player2 += 115
                monster_player2 = Monster(1300, 60, monster_health_player2, 2)
                monsters_player2.append(monster_player2)
                created_monsters_player2 += 1

        for monster_move in monsters:
            Monster.move(monster_move, 1)
            if Monster.dead(monster_move, 1):
                monsters.remove(monster_move)
                player_mana += 30
            if Monster.off_screen(monster_move, 1):
                monsters.remove(monster_move)
                player_mana += 30
                heart.pop()
                if len(heart) == 0:
                    gameplay()

        for monster_move_player2 in monsters_player2:
            Monster.move(monster_move_player2, 2)
            if Monster.dead(monster_move_player2, 2):
                monsters_player2.remove(monster_move_player2)
                player_mana2 += 30
            if Monster.off_screen(monster_move_player2, 2):
                monsters_player2.remove(monster_move_player2)
                player_mana2 += 30
                heart_player2.pop(0)
                if len(heart_player2) == 0:
                    gameplay()

        for monster_draw in monsters:
            Monster.draw(monster_draw, screen, 1)

        for monster_draw in monsters_player2:
            Monster.draw(monster_draw, screen, 2)


        for unit_fire in units:
            if len(monsters) >= 1 and (monsters[0].x >= 126 and monsters[0].y == 60) or (monsters[0].x == 558) or (
                    monsters[0].y == 594):

                if unit_fire.type == RED:

                    neighbor = 0

                    for row in range(5):
                        for column in range(3):

                            if column == 1 and row != 0 and row != 4:

                                if grid[row + 1][column] is not None and grid[row][column] is not None:
                                    if grid[row + 1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row - 1][column] is not None and grid[row][column] is not None:
                                    if grid[row - 1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row][column + 1] is not None and grid[row][column] is not None:
                                    if grid[row][column + 1].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row - 1][column] is not None and grid[row][column] is not None:
                                    if grid[row - 1][column].type == unit_fire.type:
                                        neighbor += 1


                            if column == 0 and row != 0 and row != 4:

                                if grid[row + 1][column] is not None and grid[row][column] is not None:
                                    if grid[row + 1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row - 1][column] is not None and grid[row][column] is not None:
                                    if grid[row - 1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row][column + 1] is not None and grid[row][column] is not None:
                                    if grid[row][column + 1].type == unit_fire.type:
                                        neighbor += 1

                            if column == 2 and row != 0 and row != 4:

                                if grid[row + 1][column] is not None and grid[row][column] is not None:
                                    if grid[row + 1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row - 1][column] is not None and grid[row][column] is not None:
                                    if grid[row - 1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row][column - 1] is not None and grid[row][column] is not None:
                                    if grid[row][column - 1].type == unit_fire.type:
                                        neighbor += 1

                            if column == 0 and row == 0:

                                if grid[row + 1][column] is not None and grid[row][column] is not None:
                                    if grid[row + 1][column].type == unit_fire.type:
                                        neighbor += 1

                                    if grid[row + 1][column + 1] is not None and grid[row][column] is not None:
                                        if grid[row + 1][column + 1].type == unit_fire.type:
                                            neighbor += 1


                            if column == 1 and row == 0:

                                if grid[row + 1][column] is not None and grid[row][column] is not None:
                                    if grid[row + 1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row][column + 1] is not None and grid[row][column] is not None:
                                    if grid[row][column + 1].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row][column - 1] is not None and grid[row][column] is not None:
                                    if grid[row][column - 1].type == unit_fire.type:
                                        neighbor += 1


                            if column == 2 and row == 0:

                                if grid[row + 1][column] is not None and grid[row][column] is not None:
                                    if grid[row+1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row][column-1] is not None and grid[row][column] is not None:
                                    if grid[row][column - 1].type == unit_fire.type:
                                        neighbor += 1


                            if column == 0 and row == 4:

                                if grid[row-1][column] is not None and grid[row][column] is not None:
                                    if grid[row-1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row][column + 1] is not None and grid[row][column] is not None:
                                    if grid[row][column + 1].type == unit_fire.type:
                                        neighbor += 1


                            if column == 2 and row == 4:

                                if grid[row - 1][column] is not None and grid[row][column] is not None:
                                    if grid[row-1][column].type == unit_fire.type:
                                        neighbor += 1

                                if grid[row][column - 1] is not None and grid[row][column] is not None:
                                    if grid[row][column - 1].type == unit_fire.type:
                                        neighbor += 1

                    current_monster_health = monsters[0].health
                    current_monster_health = Unit.hit(unit_fire, current_monster_health, unit_fire.merge_level, neighbor, monster_health_max)
                    monsters[0].health = current_monster_health

                if unit_fire.type == GRAY and len(monsters) >= 2:
                    random_hit(monsters, 1, neighbor, monster_health_max)

                if unit_fire.type == BROWN and len(monsters) >= 2:
                    random_hit(monsters, 1, neighbor, monster_health_max)

                if unit_fire.type == YELLOW and len(monsters) >= 3:

                    current_monster_health = monsters[0].health
                    current_monster_health = Unit.hit(unit_fire, current_monster_health, unit_fire.merge_level, neighbor, monster_health_max)
                    monsters[0].health = current_monster_health

                    current_monster_health = monsters[1].health
                    current_monster_health = Unit.hit(unit_fire, current_monster_health, unit_fire.merge_level, neighbor, monster_health_max)
                    monsters[1].health = current_monster_health

                else:
                    current_monster_health = monsters[0].health
                    current_monster_health = Unit.hit(unit_fire, current_monster_health, unit_fire.merge_level, neighbor, monster_health_max)
                    monsters[0].health = current_monster_health

        for unit_fire_player2 in units2:
            if len(monsters_player2) >= 1 and (1198 > monsters_player2[0].x >= 742 and monsters_player2[0].y == 60) or (monsters_player2[0].x == 742) or (
                    monsters_player2[0].y == 594):

                if unit_fire_player2.type == RED:

                    neighbor2 = 0

                    for row in range(5):
                        for column in range(3):

                            if column == 1 and row != 0 and row != 4:

                                if grid_player2[row + 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row + 1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row - 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row - 1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row][column + 1] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row][column + 1].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row - 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row - 1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                            if column == 0 and row != 0 and row != 4:

                                if grid_player2[row + 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row + 1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row - 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row - 1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row][column + 1] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row][column + 1].type == unit_fire_player2.type:
                                        neighbor2 += 1

                            if column == 2 and row != 0 and row != 4:

                                if grid_player2[row + 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row + 1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row - 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row - 1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row][column - 1] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row][column - 1].type == unit_fire_player2.type:
                                        neighbor2 += 1

                            if column == 0 and row == 0:

                                if grid_player2[row + 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row + 1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                    if grid_player2[row + 1][column + 1] is not None and grid_player2[row][column] is not None:
                                        if grid_player2[row + 1][column + 1].type == unit_fire_player2.type:
                                            neighbor2 += 1


                            if column == 1 and row == 0:

                                if grid_player2[row + 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row + 1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row][column + 1] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row][column + 1].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row][column - 1] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row][column - 1].type == unit_fire_player2.type:
                                        neighbor2 += 1


                            if column == 2 and row == 0:

                                if grid_player2[row + 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row+1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row][column-1] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row][column - 1].type == unit_fire_player2.type:
                                        neighbor2 += 1


                            if column == 0 and row == 4:

                                if grid_player2[row-1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row-1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row][column + 1] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row][column + 1].type == unit_fire_player2.type:
                                        neighbor2 += 1


                            if column == 2 and row == 4:

                                if grid_player2[row - 1][column] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row-1][column].type == unit_fire_player2.type:
                                        neighbor2 += 1

                                if grid_player2[row][column - 1] is not None and grid_player2[row][column] is not None:
                                    if grid_player2[row][column - 1].type == unit_fire_player2.type:
                                        neighbor2 += 1

                    current_monster_health_player2 = monsters_player2[0].health
                    current_monster_health_player2 = Unit.hit(unit_fire_player2, current_monster_health_player2, unit_fire_player2.merge_level, neighbor2, monster_health_max_player2)
                    monsters_player2[0].health = current_monster_health_player2

                if unit_fire_player2.type == GRAY and len(monsters_player2) >= 2:
                    random_hit(monsters_player2, 2, neighbor2, monster_health_max_player2)

                if unit_fire_player2.type == BROWN and len(monsters_player2) >= 2:
                    random_hit(monsters_player2, 2, neighbor2, monster_health_max_player2)

                if unit_fire_player2.type == YELLOW and len(monsters_player2) >= 4:

                    current_monster_health_player2 = monsters_player2[0].health
                    current_monster_health_player2 = Unit.hit(unit_fire_player2, current_monster_health_player2, unit_fire_player2.merge_level, neighbor2, monster_health_max_player2)
                    monsters[0].health = current_monster_health_player2

                    current_monster_health_player2_2 = monsters_player2[1].health
                    current_monster_health_player2_2= Unit.hit(unit_fire_player2, current_monster_health_player2_2, unit_fire_player2.merge_level, neighbor2, monster_health_max_player2)
                    monsters_player2[1].health = current_monster_health_player2_2

                else:
                    current_monster_health_player2 = monsters_player2[0].health
                    current_monster_health_player2 = Unit.hit(unit_fire_player2, current_monster_health_player2, unit_fire_player2.merge_level, neighbor2, monster_health_max_player2)
                    monsters_player2[0].health = current_monster_health_player2

        pygame.display.update()

        # --- FPS ---

        clock.tick(25)

    # --- the end ---

    pygame.quit()

def gameplay():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(14).render("How to play: Create new units to defend your tower. If enemies reach tower game over.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_TEXT2 = get_font(14).render("Gameplay: Press E to create a new unit", True, "White")
        OPTIONS_RECT2 = OPTIONS_TEXT.get_rect(center=(640, 110))
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        OPTIONS_TEXT3 = get_font(14).render("Press ESC to Quit", True, "White")
        OPTIONS_RECT3 = OPTIONS_TEXT.get_rect(center=(780, 140))
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)
        OPTIONS_BACK = buton(image=None, pos=(640, 680),text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")

        #rectangles in gameplay menu
        pygame.draw.rect(SCREEN, RED, pygame.Rect(125, 250, 40, 40))
        pygame.draw.rect(SCREEN, BROWN, pygame.Rect(375, 250, 40, 40))
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(625, 250, 40, 40))
        pygame.draw.rect(SCREEN, CYAN, pygame.Rect(875, 250, 40, 40))
        pygame.draw.rect(SCREEN, ORANGE, pygame.Rect(1125, 250, 40, 40))
        pygame.draw.rect(SCREEN, GREEN, pygame.Rect(125, 450, 40, 40))
        pygame.draw.rect(SCREEN, DARK_GREEN, pygame.Rect(375, 450, 40, 40))
        pygame.draw.rect(SCREEN, PURPLE, pygame.Rect(625, 450, 40, 40))
        pygame.draw.rect(SCREEN, GRAY, pygame.Rect(875, 450, 40, 40))
        pygame.draw.rect(SCREEN, LIGHT_GREEN, pygame.Rect(1125, 450, 40, 40))

        #rectangle names
        Red_name = get_font(14).render("Fire Mage", True, "Red")
        Red_RECT1 = OPTIONS_TEXT.get_rect(center=(680, 210))
        Brown_name = get_font(14).render("Hunter", True, (130, 90, 44))
        Brown_RECT1 = OPTIONS_TEXT.get_rect(center=(950, 210))
        Yellow_name = get_font(14).render("Thunderer", True, "Yellow")
        Yellow_RECT1 = OPTIONS_TEXT.get_rect(center=(1180, 210))
        Cyan_name = get_font(14).render("Priestess", True, "Cyan")
        Cyan_RECT1 = OPTIONS_TEXT.get_rect(center=(1430, 210))
        Orange_name = get_font(14).render("Executioner", True, "Orange")
        Orange_RECT1 = OPTIONS_TEXT.get_rect(center=(1660, 210))
        Green_name = get_font(14).render("Dryad", True, "Green")
        Green_RECT1 = OPTIONS_TEXT.get_rect(center=(705, 410))
        Dgreen_name = get_font(14).render("Sentry", True, "Dark green")
        Dgreen_RECT1 = OPTIONS_TEXT.get_rect(center=(950, 410))
        Purple_name = get_font(14).render("Clone", True, "Purple")
        Purple_RECT1 = OPTIONS_TEXT.get_rect(center=(1200, 410))
        Gray_name = get_font(14).render("Reaper", True, "Gray")
        Gray_RECT1 = OPTIONS_TEXT.get_rect(center=(1450, 410))
        Lgreen_name = get_font(14).render("Archer", True, "Light green")
        Lgreen_RECT1 = OPTIONS_TEXT.get_rect(center=(1700, 410))
        SCREEN.blit(Red_name, Red_RECT1)
        SCREEN.blit(Brown_name, Brown_RECT1)
        SCREEN.blit(Yellow_name, Yellow_RECT1)
        SCREEN.blit(Cyan_name, Cyan_RECT1)
        SCREEN.blit(Orange_name, Orange_RECT1)
        SCREEN.blit(Green_name, Green_RECT1)
        SCREEN.blit(Dgreen_name, Dgreen_RECT1)
        SCREEN.blit(Purple_name, Purple_RECT1)
        SCREEN.blit(Gray_name, Gray_RECT1)
        SCREEN.blit(Lgreen_name, Lgreen_RECT1)


        #rectangle explanations
        Red_TEXT = get_font(8).render("This unit powers up if his near", True, "White")
        Red_RECT2 = OPTIONS_TEXT.get_rect(center=(610, 315))
        Red_TEXT2 = get_font(8).render("blocks are the same unit.", True, "White")
        Red_RECT3 = OPTIONS_TEXT.get_rect(center=(630, 335))
        Brown_TEXT = get_font(8).render("This unit has powerful attacks", True, "White")
        Brown_RECT2 = OPTIONS_TEXT.get_rect(center=(880, 315))
        Brown_TEXT2 = get_font(8).render("but, it shoots randomly.", True, "White")
        Brown_RECT3 = OPTIONS_TEXT.get_rect(center=(900, 335))
        Yellow_TEXT = get_font(8).render("This unit fires two bullets", True, "White")
        Yellow_RECT2 = OPTIONS_TEXT.get_rect(center=(1150, 315))
        Yellow_TEXT2 = get_font(8).render("at the same time.", True, "White")
        Yellow_RECT3 = OPTIONS_TEXT.get_rect(center=(1190, 335))
        Cyan_TEXT = get_font(8).render("This unit gives mana when", True, "White")
        Cyan_RECT2 = OPTIONS_TEXT.get_rect(center=(1380, 315))
        Cyan_TEXT2 = get_font(8).render("it's merge level increased.", True, "White")
        Cyan_RECT3 = OPTIONS_TEXT.get_rect(center=(1380, 335))
        Orange_TEXT = get_font(8).render("This unit kills an enemy directly", True, "White")
        Orange_RECT2 = OPTIONS_TEXT.get_rect(center=(1600, 315))
        Orange_TEXT2 = get_font(8).render("if enemy HP is under %30", True, "White")
        Orange_RECT3 = OPTIONS_TEXT.get_rect(center=(1640, 335))
        Green_TEXT = get_font(8).render("This unit increases the merge", True, "White")
        Green_RECT2 = OPTIONS_TEXT.get_rect(center=(600, 520))
        Green_TEXT2 = get_font(8).render("level of merged unit by one.", True, "White")
        Green_RECT3 = OPTIONS_TEXT.get_rect(center=(610, 540))
        Dgreen_TEXT = get_font(8).render("This unit gains %10 Attack Damage", True, "White")
        Dgreen_RECT2 = OPTIONS_TEXT.get_rect(center=(850, 520))
        Dgreen_TEXT2 = get_font(8).render("each 5 hit. (It can stack 8 times)", True, "White")
        Dgreen_RECT3 = OPTIONS_TEXT.get_rect(center=(850, 540))
        Purple_TEXT = get_font(8).render("This unit copies the ally", True, "White")
        Purple_RECT2 = OPTIONS_TEXT.get_rect(center=(1150, 520))
        Purple_TEXT2 = get_font(8).render("you merge when you merge them.", True, "White")
        Purple_RECT3 = OPTIONS_TEXT.get_rect(center=(1140, 540))
        Gray_TEXT = get_font(8).render("This unit has %6 chance to kill", True, "White")
        Gray_RECT2 = OPTIONS_TEXT.get_rect(center=(1390, 520))
        Gray_TEXT2 = get_font(8).render("an enemy directly. (shoots randomly)", True, "White")
        Gray_RECT3 = OPTIONS_TEXT.get_rect(center=(1390, 540))
        Lgreen_TEXT = get_font(8).render("This unit has very high", True, "White")
        Lgreen_RECT2 = OPTIONS_TEXT.get_rect(center=(1670, 520))
        Lgreen_TEXT2 = get_font(8).render("attack speed.", True, "White")
        Lgreen_RECT3 = OPTIONS_TEXT.get_rect(center=(1710, 540))

        SCREEN.blit(Red_TEXT, Red_RECT2)
        SCREEN.blit(Red_TEXT2, Red_RECT3)
        SCREEN.blit(Brown_TEXT, Brown_RECT2)
        SCREEN.blit(Brown_TEXT2, Brown_RECT3)
        SCREEN.blit(Yellow_TEXT, Yellow_RECT2)
        SCREEN.blit(Yellow_TEXT2, Yellow_RECT3)
        SCREEN.blit(Cyan_TEXT, Cyan_RECT2)
        SCREEN.blit(Cyan_TEXT2, Cyan_RECT3)
        SCREEN.blit(Orange_TEXT, Orange_RECT2)
        SCREEN.blit(Orange_TEXT2, Orange_RECT3)
        SCREEN.blit(Green_TEXT, Green_RECT2)
        SCREEN.blit(Green_TEXT2, Green_RECT3)
        SCREEN.blit(Dgreen_TEXT, Dgreen_RECT2)
        SCREEN.blit(Dgreen_TEXT2, Dgreen_RECT3)
        SCREEN.blit(Purple_TEXT, Purple_RECT2)
        SCREEN.blit(Purple_TEXT2, Purple_RECT3)
        SCREEN.blit(Gray_TEXT, Gray_RECT2)
        SCREEN.blit(Gray_TEXT2, Gray_RECT3)
        SCREEN.blit(Lgreen_TEXT, Lgreen_RECT2)
        SCREEN.blit(Lgreen_TEXT2, Lgreen_RECT3)

        #Features of units
        Red_ad = get_font(8).render("Attack Damage: 50", True, "Red")
        Red_RECT4 = OPTIONS_TEXT.get_rect(center=(660, 360))
        Brown_ad = get_font(8).render("Attack Damage: 250", True, (130, 90, 44))
        Brown_RECT4 = OPTIONS_TEXT.get_rect(center=(920, 360))
        Yellow_ad = get_font(8).render("Attack Damage: 100", True, "Yellow")
        Yellow_RECT4 = OPTIONS_TEXT.get_rect(center=(1180, 360))
        Cyan_ad = get_font(8).render("Attack Damage: 80", True, "Cyan")
        Cyan_RECT4 = OPTIONS_TEXT.get_rect(center=(1410, 360))
        Orange_ad = get_font(8).render("Attack Damage: 140", True, "Orange")
        Orange_RECT4 = OPTIONS_TEXT.get_rect(center=(1660, 360))
        Green_ad = get_font(8).render("Attack Damage: 28", True, "Green")
        Green_RECT4 = OPTIONS_TEXT.get_rect(center=(660, 565))
        Dgreen_ad = get_font(8).render("Attack Damage: 150", True, "Dark green")
        Dgreen_RECT4 = OPTIONS_TEXT.get_rect(center=(920, 565))
        Purple_ad = get_font(8).render("Attack Damage: 42", True, "Purple")
        Purple_RECT4 = OPTIONS_TEXT.get_rect(center=(1180, 565))
        Gray_ad = get_font(8).render("Attack Damage: 60", True, "Gray")
        Gray_RECT4 = OPTIONS_TEXT.get_rect(center=(1410, 565))
        Lgreen_ad = get_font(8).render("Attack Damage: 60", True, "Light green")
        Lgreen_RECT4 = OPTIONS_TEXT.get_rect(center=(1660, 565))
        Red_as = get_font(8).render("Attack Speed: 100", True, "Red")
        Red_RECT5 = OPTIONS_TEXT.get_rect(center=(660, 380))
        Brown_as = get_font(8).render("Attack Speed: 100", True, (130, 90, 44))
        Brown_RECT5 = OPTIONS_TEXT.get_rect(center=(920, 380))
        Yellow_as = get_font(8).render("Attack Speed: 100", True, "Yellow")
        Yellow_RECT5 = OPTIONS_TEXT.get_rect(center=(1180, 380))
        Cyan_as = get_font(8).render("Attack Speed: 100", True, "Cyan")
        Cyan_RECT5 = OPTIONS_TEXT.get_rect(center=(1410, 380))
        Orange_as = get_font(8).render("Attack Speed: 100", True, "Orange")
        Orange_RECT5 = OPTIONS_TEXT.get_rect(center=(1660, 380))
        Green_as = get_font(8).render("Attack Speed: 100", True, "Green")
        Green_RECT5 = OPTIONS_TEXT.get_rect(center=(660, 585))
        Dgreen_as = get_font(8).render("Attack Speed: 100", True, "Dark green")
        Dgreen_RECT5 = OPTIONS_TEXT.get_rect(center=(920, 585))
        Purple_as = get_font(8).render("Attack Speed: 100", True, "Purple")
        Purple_RECT5 = OPTIONS_TEXT.get_rect(center=(1180, 585))
        Gray_as = get_font(8).render("Attack Speed: 100", True, "Gray")
        Gray_RECT5 = OPTIONS_TEXT.get_rect(center=(1410, 585))
        Lgreen_as = get_font(8).render("Attack Damage: 100", True, "Light green")
        Lgreen_RECT5 = OPTIONS_TEXT.get_rect(center=(1660, 585))
        SCREEN.blit(Red_ad, Red_RECT4)
        SCREEN.blit(Brown_ad, Brown_RECT4)
        SCREEN.blit(Yellow_ad, Yellow_RECT4)
        SCREEN.blit(Cyan_ad, Cyan_RECT4)
        SCREEN.blit(Orange_ad, Orange_RECT4)
        SCREEN.blit(Green_ad, Green_RECT4)
        SCREEN.blit(Dgreen_ad, Dgreen_RECT4)
        SCREEN.blit(Purple_ad, Purple_RECT4)
        SCREEN.blit(Gray_ad, Gray_RECT4)
        SCREEN.blit(Lgreen_ad, Lgreen_RECT4)
        SCREEN.blit(Red_as, Red_RECT5)
        SCREEN.blit(Brown_as, Brown_RECT5)
        SCREEN.blit(Yellow_as, Yellow_RECT5)
        SCREEN.blit(Cyan_as, Cyan_RECT5)
        SCREEN.blit(Orange_as, Orange_RECT5)
        SCREEN.blit(Green_as, Green_RECT5)
        SCREEN.blit(Dgreen_as, Dgreen_RECT5)
        SCREEN.blit(Purple_as, Purple_RECT5)
        SCREEN.blit(Gray_as, Gray_RECT5)
        SCREEN.blit(Lgreen_as, Lgreen_RECT5)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("TOWER DEFENCE", True, "#660099")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = buton(image=pygame.image.load("Play Rect.jpg"), pos=(640, 250),text_input="PLAY", font=get_font(75), base_color="#2E8B57", hovering_color="White")
        GAMEPLAY_BUTTON = buton(image=pygame.image.load("Gameplay Rect.jpg"), pos=(640, 400),text_input="GAMEPLAY", font=get_font(75), base_color="#2E8B57", hovering_color="White")
        QUIT_BUTTON = buton(image=pygame.image.load("Quit Rect.jpg"), pos=(640, 550),text_input="QUIT", font=get_font(75), base_color="#2E8B57", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, GAMEPLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if GAMEPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    gameplay()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()