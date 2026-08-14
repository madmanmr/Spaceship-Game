import pygame as pg

from settings import *


def create_menu_buttons():
    level_selection_button = pg.Rect(0, 0, 220, 70)
    garage_button = pg.Rect(0, 0, 220, 70)

    level_selection_button.center = (
        (SCREEN_WIDTH // 2) - 200,
        400
    )

    garage_button.center = (
        (SCREEN_WIDTH // 2) + 200,
        400
    )

    return level_selection_button, garage_button

levelSelectionBut, GarageBut = create_menu_buttons()


# draw inside of spacehip first
def draw_interior(screen):
   x = 1

def draw_menu(screen, mouse_pos, title_font, subtitle_font, stars):
    level_colour = ACCENT_PURPLE
    garage_colour = ACCENT_PURPLE

    #copies used for drawing
    level_copy_rect = levelSelectionBut.copy()
    garage_copy_rect = GarageBut.copy()

    if levelSelectionBut.collidepoint(mouse_pos):
        level_colour = ACCENT_PURPLE_HOVER
        level_copy_rect = levelSelectionBut.inflate(-7, -3)

    if GarageBut.collidepoint(mouse_pos):
        garage_colour = ACCENT_PURPLE_HOVER
        garage_copy_rect = GarageBut.inflate(-7, -3)

    pg.draw.rect(screen,level_colour,level_copy_rect,border_radius=15)
    pg.draw.rect(screen,garage_colour,garage_copy_rect,border_radius=15)

    title = title_font.render("SPACESHIP GAME",True,ACCENT_LIGHTBLUE)
    levels_text = subtitle_font.render("Levels",True,WHITE)
    garage_text = subtitle_font.render("Garage", True,WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    levels_rect = levels_text.get_rect(center=levelSelectionBut.center)
    garage_rect = garage_text.get_rect(center=GarageBut.center)

    screen.blit(title, title_rect)
    screen.blit(levels_text, levels_rect)
    screen.blit(garage_text, garage_rect)


def handle_menu_events(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        if levelSelectionBut.collidepoint(event.pos):
            return "level selection"

        elif GarageBut.collidepoint(event.pos):
            return "upgrade choice"

    return None