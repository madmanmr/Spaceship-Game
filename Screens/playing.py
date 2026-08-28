import pygame as pg

from settings import *


def draw_game_buttons():
    pauseBut = pg.Rect(0, 0, 150, 50)
    pauseBut.center = (100, SCREEN_HEIGHT - 75)

    return pauseBut

pauseBut = draw_game_buttons()

def draw_game(screen, ship, asteroids, lasers, playingTextFunc, mouse_pos, text_font):
    ship.draw1(screen)

    for asteroid in asteroids:
        asteroid.draw(screen)
    for laser_obj in lasers:
        laser_obj.draw(screen)

    playingTextFunc()

    #buts
    pauseBut_copy = pauseBut.copy()

    pauseColour = (204, 57, 47)
    if pauseBut.collidepoint(mouse_pos):
        pauseColour = (173, 44, 35)
        pauseBut_copy = pauseBut.inflate(-3, -1)

    pg.draw.rect(screen, pauseColour, pauseBut_copy, border_radius=10)

    pauseText = text_font.render("PAUSE", True, WHITE)
    pauseRect = pauseText.get_rect(center=pauseBut_copy.center)
    screen.blit(pauseText, pauseRect)

def handle_game_events(event, game):
    if game["asteroidsSpawned"] == game["asteroidCountMax"] and game["asteroidCount"] == 0:
        return "game over"
    if event.type == pg.MOUSEBUTTONDOWN:
        if pauseBut.collidepoint(event.pos):
            game["pause"] = True



    return None