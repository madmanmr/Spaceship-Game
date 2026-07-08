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
PLAYING = "playing"
GAME_OVER = "game_over"
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
#functions
def Menu():
    screen.fill((15, 15, 30))

    #buttons
    play_button = pg.Rect(0, 0, 220, 70)
    play_button.center = (SCREEN_WIDTH // 2, 400)

    # Play button
    colour = (40, 180, 80)
    if play_button.collidepoint(mousePos):
        colour = (60, 220, 100)

    pg.draw.rect(screen, colour, play_button, border_radius=15)

    # Title
    title = title_font.render("SPACESHIP GAME", True, WHITE)
    play_text = text_font.render("PLAY", True, BLACK)
    subtitle = text_font.render("Press Play to Begin", True, (180, 180, 180))

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    play_rect = play_text.get_rect(center=play_button.center)
    subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 220))

    screen.blit(title, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(subtitle, subtitle_rect)

    return play_button
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
            dx = laser_obj.x - asteroid.x
            dy = laser_obj.y - asteroid.y
            distance = np.sqrt(dx ** 2 + dy ** 2)

            if distance <= asteroid.radius:
                asteroids.remove(asteroid)
                laser.remove(laser_obj)
                destroyed = True
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
def playingTextFunc():
    health_text = text_font.render(f"Health: {health}", True, WHITE)
    level_text = subtitle_font.render(f"{level}", True, WHITE)
    asteroidsleft_text = text_font.render(f"Asteroids left: {asteroid_count}", True, WHITE)

    screen.blit(level_text, ((SCREEN_WIDTH / 2), 20))
    screen.blit(health_text, (20, 20))
    screen.blit(asteroidsleft_text, (20, 55))
running = True
while running:
    dt = clock.tick(60)

    mousePos = pg.mouse.get_pos()
    mouseClick = pg.mouse.get_pressed()[0]
    mousePress = mouseClick and not prevMouseClick
    prevMouseClick = mouseClick

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN and state == PLAYING:
            if event.key == pg.K_SPACE:
                laser.append(Laser(
                    ship.x + np.cos(ship.angle) * ship.length,
                    ship.y + np.sin(ship.angle) * ship.length,
                    ship.angle,
                    laserSpeedCalc
                ))
    if state == MENU:
        play_button = Menu()

        if mousePress and play_button.collidepoint(mousePos):
            state = PLAYING

    elif state == PLAYING:
        screen.fill(BACKGROUND_COLOR)

        spaceshipmainfunc()
        asteroidsmainfunc()
        laserdrawfunc()
        healthmainfunc()

        playingTextFunc()

    elif state == GAME_OVER:
        screen.fill(BLACK)
        game_over_text = title_font.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)

    pg.display.flip()

pg.quit()