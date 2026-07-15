'''
    24/06/26
    started new game that I will be working on for a while to improve more skills. As of now my idea is to have a spaceship survival type game.
    A spaceship of choice will spawn in the centre of the screen while playing. Asteroids will spawn randomly around it. They will be moving and if they hit the spaceship,
    game over. You get points for shooting asteroids.

'''

import pygame as pg
import numpy as np
from Spaceship import Ship1
from settings import *
import sys
from asteroids import Asteroid
from lasers import Laser

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()



ship = Ship1(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

MENU = "menu"
LEVEL_SELECT = "level selection"
GARAGE = "upgrade choice"
PLAYING = "playing"
GAME_OVER = "game over"
state = MENU

#vars
prevMouseClick = False
mousePos = pg.mouse.get_pos()
mousePress = mousePos[0]
title_font = pg.font.SysFont(None, 80)
subtitle_font = pg.font.SysFont(None, 48)
text_font = pg.font.SysFont(None, 35)

#vars changeable by level
level = 1
laserLevel = 1

#lists
leveldamage = [10,20,50] #number of elements in list is number of levels there are
asteroidSpeedMax = [10,15,20]
asteroidSpeedMin = [5,8,15]
laserSpeed = [15,20,25,30]
backgroundColour = [(15, 15, 30),(58, 43, 87),(79, 43, 97)]

#calcs
damage = leveldamage[level-1]
asteroidCalcMax = asteroidSpeedMax[level-1]
asteroidCalcMin = asteroidSpeedMin[level-1]
laserSpeedCalc = laserSpeed[laserLevel-1]
backgroundcolourcalc = backgroundColour[level-1]

#health
health = 100
hit_cooldown = 0

#asteroid
asteroid_count: int = level * 5

#laser

#asteroid vars
asteroids = []
laser = []

for i in range(asteroid_count):
    x = np.random.randint(0, SCREEN_WIDTH)
    y = np.random.randint(0, SCREEN_HEIGHT)

    asteroid = Asteroid(x, y)
    asteroid.angle = np.radians(np.random.randint(-20, 21))
    asteroid.speed = np.random.randint(asteroidCalcMin, asteroidCalcMax)

    asteroids.append(asteroid)

#create buttons outside of draw funcs

#menu
def create_menu_buttons():
    levelSelectionBut = pg.Rect(0, 0, 220, 70)
    GarageBut = pg.Rect(0,0,220, 70)

    levelSelectionBut.center = ((SCREEN_WIDTH // 2) - 200, 400)
    GarageBut.center = ((SCREEN_WIDTH // 2) + 200, 400)

    return levelSelectionBut, GarageBut
levelSelectionBut, GarageBut = create_menu_buttons()
def draw_menu():
    screen.fill((15, 15, 30))

    # Play button
    colour = (40, 180, 80)
    if levelSelectionBut.collidepoint(mousePos):
        colour = (60, 220, 100)
    colour2 = (40, 180, 80)
    if GarageBut.collidepoint(mousePos):
        colour2 = (60, 220, 100)

    pg.draw.rect(screen, colour, levelSelectionBut, border_radius=15)
    pg.draw.rect(screen, colour2, GarageBut, border_radius=15)

    # Title
    title = title_font.render("SPACESHIP GAME", True, WHITE)
    levels_text = text_font.render("Levels", True, BLACK)
    garage_text = text_font.render("Garage", True, BLACK)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    play_rect = levels_text.get_rect(center=levelSelectionBut.center)
    garage_rect = garage_text.get_rect(center=GarageBut.center)

    screen.blit(title, title_rect)
    screen.blit(levels_text, play_rect)
    screen.blit(garage_text, garage_rect)
def handle_menu_events(event):
    global state

    if event.type == pg.MOUSEBUTTONDOWN:
        if levelSelectionBut.collidepoint(pg.mouse.get_pos()):
            state = LEVEL_SELECT
        elif GarageBut.collidepoint(pg.mouse.get_pos()):
            state = GARAGE
#level selection
def create_level_selection_buttons():
    level1But = pg.Rect(0, 0, 220, 70)
    level2But = pg.Rect(0, 0, 220, 70)
    level3But = pg.Rect(0, 0, 220, 70)
    BackButL = pg.Rect(0, 0, 150, 50)

    level1But.center = (200, 400)
    level2But.center = (SCREEN_WIDTH // 2, 400)
    level3But.center = (SCREEN_WIDTH - 200, 400)
    BackButL.center = (100, SCREEN_HEIGHT - 75)

    return level1But, level2But, level3But, BackButL
level1But, level2But, level3But, BackButL = create_level_selection_buttons()
def draw_level_selection():
    screen.fill((15, 15, 30))
    #hovercolour
    colour1 = (40, 180, 80)
    if level1But.collidepoint(mousePos):
        colour1 = (60, 220, 100)
    colour2 = (40, 180, 80)
    if level2But.collidepoint(mousePos):
        colour2 = (60, 220, 100)
    colour3 = (40, 180, 80)
    if level3But.collidepoint(mousePos):
        colour3 = (60, 220, 100)
    colour4 = (40, 180, 80)
    if BackButL.collidepoint(mousePos):
        colour4 = (60, 220, 100)

    #draw buttons
    pg.draw.rect(screen, colour1, level1But, border_radius=15)
    pg.draw.rect(screen, colour2, level2But, border_radius=15)
    pg.draw.rect(screen, colour3, level3But, border_radius=15)
    pg.draw.rect(screen, colour4, BackButL, border_radius=10)

    #text make
    titleText = title_font.render("Select Level", True, WHITE)
    one = text_font.render("1", True, BLACK)
    two = text_font.render("2", True, BLACK)
    three = text_font.render("3", True, BLACK)
    Backtext = text_font.render("Back", True, (180, 180, 180))

    #text rects
    title_rect = titleText.get_rect(center=(SCREEN_WIDTH // 2, 150))
    oneRect = one.get_rect(center=level1But.center)
    twoRect = two.get_rect(center=level2But.center)
    threeRect = three.get_rect(center=level3But.center)
    BackRect = Backtext.get_rect(center=BackButL.center)

    #draw
    screen.blit(titleText, title_rect)
    screen.blit(one, oneRect)
    screen.blit(two, twoRect)
    screen.blit(three, threeRect)
    screen.blit(Backtext, BackRect)
def handle_level_selection_events(event):
    global state, level

    if event.type == pg.MOUSEBUTTONDOWN:
        if level1But.collidepoint(pg.mouse.get_pos()):
            level = 1
            current_level()
            state = PLAYING
        elif level2But.collidepoint(pg.mouse.get_pos()):
            level = 2
            current_level()
            state = PLAYING
        elif level3But.collidepoint(pg.mouse.get_pos()):
            level = 3
            current_level()
            state = PLAYING
        elif BackButL.collidepoint(pg.mouse.get_pos()):
            state = MENU
            level = 0

#garage
def create_garage_buttons():
    BackButG = pg.Rect(0, 0, 150, 50)

    BackButG.center = (100, SCREEN_HEIGHT - 75)
    return BackButG
BackButG = create_garage_buttons()
def draw_garage():
    screen.fill((15, 15, 30))

    colour4 = (40, 180, 80)
    if BackButG.collidepoint(mousePos):
        colour4 = (60, 220, 100)

    pg.draw.rect(screen, colour4, BackButG, border_radius=10)

    titleText = title_font.render("Garage", True, WHITE)
    Backtext = text_font.render("Back", True, (180, 180, 180))

    title_rect = titleText.get_rect(center=(SCREEN_WIDTH // 2, 150))
    BackRect = Backtext.get_rect(center=BackButG.center)

    screen.blit(titleText, title_rect)
    screen.blit(Backtext, BackRect)
        #handle events in different states seperately so not doing all in start of running loop
def handle_garage_events(event):
    global state

    if event.type == pg.MOUSEBUTTONDOWN:
        if BackButG.collidepoint(pg.mouse.get_pos()):
            state = MENU

#game
def draw_game_buttons():
    BackButGame = pg.Rect(0, 0, 150, 50)
    BackButGame.center = (100, SCREEN_HEIGHT - 75)
    return BackButGame
BackButGame = draw_game_buttons()
def draw_game():
    ship.draw1(screen)
    asteroid.draw(screen)
    playingTextFunc()
def update_game():
    screen.fill(backgroundcolourcalc)

    spaceshipmainfunc()
    asteroidsmainfunc()
    laserdrawfunc()
    healthmainfunc()
def handle_game_events():
    global state

#game over
def draw_game_over_buttons():
    NewGameBut = pg.Rect(0, 0, 150, 50)
    MenuBut = pg.Rect(0, 0, 150, 50)

    NewGameBut.center = (100, SCREEN_HEIGHT - 75)
    MenuBut.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    return NewGameBut, MenuBut
NewGameBut, MenuBut = draw_game_over_buttons()
def draw_game_over():
    screen.fill((15, 15, 30))
    colour1 = (40, 180, 80)
    if NewGameBut.collidepoint(mousePos):
        colour1 = (60, 220, 100)
    colour2 = (40, 180, 80)
    if NewGameBut.collidepoint(mousePos):
        colour2 = (60, 220, 100)

    pg.draw.rect(screen, colour1, NewGameBut, border_radius=15)
    pg.draw.rect(screen, colour2, MenuBut, border_radius=15)

    new_text = text_font.render("New Game", True, BLACK)
    menu_text = text_font.render("Menu", True, BLACK)

    screen.blit(new_text, new_text.get_rect(center=NewGameBut.center))
    screen.blit(menu_text, menu_text.get_rect(center=MenuBut.center))
def handle_game_over_events():
    global state

def current_level():
    global asteroids
    global asteroid_count

    asteroids.clear()

    asteroid_count = level * 5

    for i in range(asteroid_count):
        x = np.random.randint(0, SCREEN_WIDTH)
        y = np.random.randint(0, SCREEN_HEIGHT)

        asteroid = Asteroid(x, y)
        asteroid.angle = np.radians(np.random.randint(-20, 21))
        asteroid.speed = np.random.randint(
            asteroidSpeedMin[level-1],
            asteroidSpeedMax[level-1]
        )

        asteroids.append(asteroid)

def playingTextFunc():
    health_text = text_font.render(f"Health: {health}", True, WHITE)
    level_text = subtitle_font.render(f"{level}", True, WHITE)
    asteroidsleft_text = text_font.render(f"Asteroids left: {asteroid_count}", True, WHITE)

    screen.blit(level_text, ((SCREEN_WIDTH / 2), 20))
    screen.blit(health_text, (20, 20))
    screen.blit(asteroidsleft_text, (20, 55))
def spaceshipmainfunc():
    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
        ship.rotate_left()
    if keys[pg.K_d]:
        ship.rotate_right()
    if keys[pg.K_w]:
        ship.thrust()

    if ship.x >= SCREEN_WIDTH:
        ship.x = SCREEN_WIDTH
        ship.bounce_x()
    if ship.x <= 0:
        ship.x = 0
        ship.bounce_x()

    if ship.y >= SCREEN_HEIGHT:
        ship.y = SCREEN_HEIGHT
        ship.bounce_y()
    if ship.y <= 0:
        ship.y = 0
        ship.bounce_y()

    ship.update()
def asteroidsmainfunc():
    global asteroid_count
    for asteroid in asteroids[:]:
        asteroid.update()

        destroyed = False

        for laser_obj in laser[:]:
            for point in laser_obj.points:
                dx = point[0] - asteroid.x
                dy = point[1] - asteroid.y

                distance = np.sqrt(dx ** 2 + dy ** 2)

                if distance <= asteroid.radius:
                    asteroids.remove(asteroid)
                    laser.remove(laser_obj)
                    destroyed = True
                    break

            if destroyed:
                break

        if destroyed:
            asteroid_count -= 1
            continue

        # wrap asteroid
        if asteroid.x > SCREEN_WIDTH:
            asteroid.x = 0
        elif asteroid.x < 0:
            asteroid.x = SCREEN_WIDTH

        if asteroid.y > SCREEN_HEIGHT or asteroid.y < 0:
            asteroid.angle = -asteroid.angle
def laserdrawfunc():
    for laser_obj in laser:
        laser_obj.update()
        laser_obj.draw(screen)
def healthmainfunc():
    global health, hit_cooldown, state

    if hit_cooldown > 0:
        hit_cooldown -= 1

    for asteroid in asteroids:
        dx = ship.x - asteroid.x
        dy = ship.y - asteroid.y
        distance = np.sqrt(dx ** 2 + dy ** 2)

        if distance < ship.length + asteroid.radius and hit_cooldown == 0:
            health -= damage
            hit_cooldown = 60
            print(health)

            if health <= 0:
                state = GAME_OVER

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if state == MENU:
            handle_menu_events(event)

        elif state == LEVEL_SELECT:
            handle_level_selection_events(event)

        elif state == GARAGE:
            handle_garage_events(event)

        elif state == PLAYING:
            handle_game_events()

        elif state == GAME_OVER:
            handle_game_over_events()

    if state == MENU:
        draw_menu()

    elif state == LEVEL_SELECT:
        draw_level_selection()

    elif state == GARAGE:
        draw_garage()

    elif state == PLAYING:
        update_game()
        draw_game()

    elif state == GAME_OVER:
        draw_game_over()

    pg.display.flip()

pg.quit()