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

#calcs
damage = leveldamage[level-1]
asteroidCalcMax = asteroidSpeedMax[level-1]
asteroidCalcMin = asteroidSpeedMin[level-1]
laserSpeedCalc = laserSpeed[laserLevel-1]

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
#draw screens funcs
def draw_menu():
    screen.fill((15, 15, 30))

    #buttons
    levelSelectionBut = pg.Rect(0, 0, 220, 70)
    levelSelectionBut.center = (SCREEN_WIDTH // 2, 400)

    # Play button
    colour = (40, 180, 80)
    if levelSelectionBut.collidepoint(mousePos):
        colour = (60, 220, 100)

    pg.draw.rect(screen, colour, levelSelectionBut, border_radius=15)

    # Title
    title = title_font.render("SPACESHIP GAME", True, WHITE)
    play_text = text_font.render("PLAY", True, BLACK)
    subtitle = text_font.render("Press Play to Begin", True, (180, 180, 180))

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    play_rect = play_text.get_rect(center=levelSelectionBut.center)
    subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 220))

    screen.blit(title, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(subtitle, subtitle_rect)

    return levelSelectionBut
def draw_level_selection():
    level1But = pg.Rect(0, 0, 220, 70)
    level2But = pg.Rect(0, 0, 220, 70)
    level3But = pg.Rect(0, 0, 220, 70)
    BackBut = pg.Rect(0, 0, 150, 50)

    level1But.center = (200, 400)
    level2But.center = (SCREEN_WIDTH // 2, 400)
    level2But.center = (SCREEN_WIDTH - 200, 400)
    BackBut.center = (100, SCREEN_HEIGHT - 75)

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
    if BackBut.collidepoint(mousePos):
        colour4 = (60, 220, 100)

    #draw buttons
    pg.draw.rect(screen, colour1, level1But, border_radius=15)
    pg.draw.rect(screen, colour2, level2But, border_radius=15)
    pg.draw.rect(screen, colour3, level3But, border_radius=15)
    pg.draw.rect(screen, colour4, BackBut, border_radius=10)

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
    threeRect = three.get_rect(center=level2But.center)
    BackRect = Backtext.get_rect(center=BackBut.center)

    #draw
    screen.blit(titleText, title_rect)
    screen.blit(one, oneRect)
    screen.blit(two, twoRect)
    screen.blit(three, threeRect)
    screen.blit(Backtext, BackRect)

    #returns for event func
    return level1But, level2But, level3But
def draw_garage():

#handle events in different states seperately so not doing all in start of running loop
def handle_menu_events(event, levelSelectionBut):
    global state

    if event.type == pg.MOUSEBUTTONDOWN:
        if levelSelectionBut.collidepoint(pg.mouse.get_pos()):
            state = LEVEL_SELECT
def handle_level_selection_events(event, level1But, level2But, level3But):
    global state, level

    if event.type == pg.MOUSEBUTTONDOWN:
        if level1But.collidepoint(pg.mouse.get_pos()):
            state = LEVEL_SELECT
            level = 1
        elif level2But.collidepoint(pg.mouse.get_pos()):
            state = LEVEL_SELECT
            level = 2
        elif level3But.collidepoint(pg.mouse.get_pos()):
            state = LEVEL_SELECT
            level = 3

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
    ship.draw1(screen)
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
        asteroid.draw(screen)
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
            handle_game_events(event)

        elif state == GAME_OVER:
            handle_game_over_events(event)

    if state == MENU:
        draw_menu()

    elif state == LEVEL_SELECT:
        draw_level_selection()

    elif state == PLAYING:
        update_game(current_level)
        draw_game()

    elif state == GAME_OVER:
        draw_game_over()

    pg.display.flip()

pg.quit()