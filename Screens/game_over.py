import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK

def create_game_over_buttons():
    new_game_button = pg.Rect(0, 0, 200, 60)
    menu_button = pg.Rect(0, 0, 200, 60)

    new_game_button.center = (SCREEN_WIDTH // 2, 400)
    menu_button.center = (SCREEN_WIDTH // 2, 500)

    return new_game_button, menu_button

NewGameBut, MenuBut = create_game_over_buttons()

def draw_game_over(screen, mouse_pos, text_font):
    screen.fill((15, 15, 30))

    new_game_colour = (40, 180, 80)
    menu_colour = (40, 180, 80)

    if NewGameBut.collidepoint(mouse_pos):
        new_game_colour = (60, 220, 100)

    if MenuBut.collidepoint(mouse_pos):
        menu_colour = (60, 220, 100)

    pg.draw.rect(
        screen,
        new_game_colour,
        NewGameBut,
        border_radius=15
    )

    pg.draw.rect(
        screen,
        menu_colour,
        MenuBut,
        border_radius=15
    )

    new_text = text_font.render("New Game", True, BLACK)
    menu_text = text_font.render("Menu", True, BLACK)

    screen.blit(
        new_text,
        new_text.get_rect(center=NewGameBut.center)
    )

    screen.blit(
        menu_text,
        menu_text.get_rect(center=MenuBut.center)
    )

def handle_game_over_events(event):
    if event.type == pg.MOUSEBUTTONDOWN:

        if NewGameBut.collidepoint(event.pos):
            return "new_game"

        if MenuBut.collidepoint(event.pos):
            return "menu"

    return None