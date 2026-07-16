import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

def create_garage_buttons():
    back_button = pg.Rect(0, 0, 150, 50)
    back_button.center = (100, SCREEN_HEIGHT - 75)

    return back_button

BackButG = create_garage_buttons()

def draw_garage(screen, mouse_pos, title_font, text_font):
    screen.fill((15, 15, 30))

    back_colour = (204, 57, 47)

    if BackButG.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)

    pg.draw.rect(
        screen,
        back_colour,
        BackButG,
        border_radius=10
    )

    title_text = title_font.render("Garage", True, WHITE)
    back_text = text_font.render("Back", True, (180, 180, 180))

    title_rect = title_text.get_rect(
        center=(SCREEN_WIDTH // 2, 150)
    )

    back_rect = back_text.get_rect(
        center=BackButG.center
    )

    screen.blit(title_text, title_rect)
    screen.blit(back_text, back_rect)

def handle_garage_events(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        if BackButG.collidepoint(event.pos):
            return "menu"

    return None