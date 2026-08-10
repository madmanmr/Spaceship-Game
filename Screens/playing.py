import pygame as pg

from settings import *


def draw_game_buttons():
    BackButGame = pg.Rect(0, 0, 150, 50)
    BackButGame.center = (100, SCREEN_HEIGHT - 75)
    return BackButGame

BackButGame = draw_game_buttons()

def draw_game(screen, ship, asteroids, laser, playingTextFunc):
    ship.draw1(screen)

    for asteroid in asteroids:
        asteroid.draw(screen)

    for laser_obj in laser:
        laser_obj.draw(screen)

    playingTextFunc()

def update_game(screen, background_colour, spaceship_main_func, asteroids_main_func, laser_main_func, health_main_func):
    screen.fill(background_colour)

    spaceship_main_func()
    asteroids_main_func()
    laser_main_func()
    health_main_func()

def handle_game_events(event, game):
    if (game["asteroidsSpawned"] == game["asteroidCountMax"] and game["asteroidCount"] == 0):
        return "game over"

    return None