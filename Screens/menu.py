import pygame as pg

from settings import SCREEN_WIDTH, WHITE, BLACK


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

def draw_menu(screen, mouse_pos, title_font, subtitle_font):
    screen.fill((15, 15, 30))

    level_colour = (60, 220, 100)
    garage_colour = (60, 220, 100)

    #copies used for drawing
    level_copy_rect = levelSelectionBut.copy()
    garage_copy_rect = GarageBut.copy()

    if levelSelectionBut.collidepoint(mouse_pos):
        level_colour = (40, 180, 80)
        level_copy_rect = levelSelectionBut.inflate(-7, -3)

    if GarageBut.collidepoint(mouse_pos):
        garage_colour = (40, 180, 80)
        garage_copy_rect = GarageBut.inflate(-7, -3)

    pg.draw.rect(screen,level_colour,level_copy_rect,border_radius=15)
    pg.draw.rect(screen,garage_colour,garage_copy_rect,border_radius=15)

    title = title_font.render("SPACESHIP GAME",True,WHITE)
    levels_text = subtitle_font.render("Levels",True,BLACK)
    garage_text = subtitle_font.render("Garage", True,BLACK)

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