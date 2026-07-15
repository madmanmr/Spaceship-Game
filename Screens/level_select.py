import pygame as pg
import numpy as np
from settings import *

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
def draw_level_selection(screen, mousePos, title_font, text_font):
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
    colour4 = (204, 57, 47)
    if BackButL.collidepoint(mousePos):
        colour4 = (173, 44, 35)

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
    if event.type == pg.MOUSEBUTTONDOWN:

        if level1But.collidepoint(event.pos):
            return PLAYING, 1

        elif level2But.collidepoint(event.pos):
            return PLAYING, 2

        elif level3But.collidepoint(event.pos):
            return PLAYING, 3

        elif BackButL.collidepoint(event.pos):
            return MENU, None

    return None, None