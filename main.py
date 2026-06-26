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
text_font = pg.font.SysFont(None, 35)
level = 1
leveldamage = [10,20,50]
damage = leveldamage[level-1]
health = 100

#asteroid vars
asteroids = []

for i in range((level*5)):
    x = np.random.randint(0, SCREEN_WIDTH)
    y = np.random.randint(0, SCREEN_HEIGHT)
    angle = np.random.randint(0, 360)
    asteroids.append(Asteroid(x, y))

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
def asteroidsmainfunc():
    for asteroid in asteroids:
        asteroid.update()

        if asteroid.x > SCREEN_WIDTH:
            asteroid.x = 0
        elif asteroid.x < 0:
            asteroid.x = SCREEN_WIDTH

        if asteroid.y > SCREEN_HEIGHT:
            asteroid.y = 0
        elif asteroid.y < 0:
            asteroid.y = SCREEN_HEIGHT

        asteroid.draw(screen)
def healthmainfunc():
    global health, damage

    for asteroid in asteroids:
        dx = ship.x - asteroid.x
        dy = ship.y - asteroid.y
        distance = np.sqrt(dx ** 2 + dy ** 2)

        if distance < ship.length + asteroid.radius:
            health -= damage
            damage = 0
            print(health)
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

    if state == MENU:
        play_button = Menu()

        if mousePress and play_button.collidepoint(mousePos):
            state = PLAYING

    elif state == PLAYING:
        keys = pg.key.get_pressed()

        screen.fill(BACKGROUND_COLOR)

        spaceshipmainfunc()
        ship.update()
        ship.draw1(screen)

        asteroidsmainfunc()

        healthmainfunc()

    elif state == GAME_OVER:
        screen.fill(BLACK)
        game_over_text = title_font.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)

    pg.display.flip()

pg.quit()