import pygame as pg
import numpy as np
from settings import *

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
    if MenuBut.collidepoint(mousePos):
        colour2 = (60, 220, 100)

    pg.draw.rect(screen, colour1, NewGameBut, border_radius=15)
    pg.draw.rect(screen, colour2, MenuBut, border_radius=15)

    new_text = text_font.render("New Game", True, BLACK)
    menu_text = text_font.render("Menu", True, BLACK)

    screen.blit(new_text, new_text.get_rect(center=NewGameBut.center))
    screen.blit(menu_text, menu_text.get_rect(center=MenuBut.center))
def handle_game_over_events():
    global state, level, health, asteroid_count
    if event.type == pg.MOUSEBUTTONDOWN:
        if NewGameBut.collidepoint(pg.mouse.get_pos()):
            start_new_game()
        elif MenuBut.collidepoint(pg.mouse.get_pos()):
            state = MENU
            level = 0
def start_new_game():
    global state, health, hit_cooldown, laser

    health = 100
    hit_cooldown = 0
    laser.clear()

    current_level()

    ship.x = SCREEN_WIDTH // 2
    ship.y = SCREEN_HEIGHT // 2
    ship.speed_x = 0
    ship.speed_y = 0

    state = PLAYING