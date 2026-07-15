import pygame as pg
import numpy as np
from settings import *

def create_garage_buttons():
    BackButG = pg.Rect(0, 0, 150, 50)

    BackButG.center = (100, SCREEN_HEIGHT - 75)
    return BackButG
BackButG = create_garage_buttons()
def draw_garage(screen, mousePos, title_font, text_font):
    screen.fill((15, 15, 30))

    colour4 = (204, 57, 47)
    if BackButG.collidepoint(mousePos):
        colour4 = (173, 44, 35)

    pg.draw.rect(screen, colour4, BackButG, border_radius=10)

    titleText = title_font.render("Garage", True, WHITE)
    Backtext = text_font.render("Back", True, (180, 180, 180))

    title_rect = titleText.get_rect(center=(SCREEN_WIDTH // 2, 150))
    BackRect = Backtext.get_rect(center=BackButG.center)

    screen.blit(titleText, title_rect)
    screen.blit(Backtext, BackRect)
        #handle events in different states seperately so not doing all in start of running loop
def handle_garage_events(event):

    if event.type == pg.MOUSEBUTTONDOWN:
        if BackButG.collidepoint(pg.mouse.get_pos()):
            return MENU
    return None