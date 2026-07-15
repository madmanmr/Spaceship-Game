import pygame as pg
import numpy as np
from settings import *

def create_menu_buttons():
    levelSelectionBut = pg.Rect(0, 0, 220, 70)
    GarageBut = pg.Rect(0,0,220, 70)

    levelSelectionBut.center = ((SCREEN_WIDTH // 2) - 200, 400)
    GarageBut.center = ((SCREEN_WIDTH // 2) + 200, 400)

    return levelSelectionBut, GarageBut
levelSelectionBut, GarageBut = create_menu_buttons()
def draw_menu(screen, mousePos, title_font, text_font):
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
    if event.type == pg.MOUSEBUTTONDOWN:

        if levelSelectionBut.collidepoint(pg.mouse.get_pos()):
            return LEVEL_SELECT
        elif GarageBut.collidepoint(pg.mouse.get_pos()):
            return GARAGE

    return None