import pygame as pg
from settings import *


def make_level_select_buttons(screen, mouse_pos, title_font, text_font):
    level_amount = range(1, 7)

    x = 200
    y = 300

    level_buttons = []

    for level_num in level_amount:
        button_text = str(level_num)

        level_but = pg.Rect(0, 0, 150, 50)
        level_but.center = (x, y)

        level_but_copy = level_but.copy()

        colour = ACCENT_PURPLE

        if level_but.collidepoint(mouse_pos):
            colour = ACCENT_PURPLE_HOVER
            level_but_copy = level_but.inflate(-7, -3)

        pg.draw.rect(screen, colour, level_but_copy, border_radius=15)

        level_text = text_font.render(button_text, True, BLACK)
        screen.blit(level_text, level_text.get_rect(center=level_but.center))

        button_data = {"rect": level_but, "level": level_num}
        level_buttons.append(button_data)

        if x < 1000:
            x += 400
        else:
            x = 200
            y = 500

    return level_buttons


def create_level_selection_buttons():
    back_but_l = pg.Rect(0, 0, 150, 50)
    back_but_l.center = (100, SCREEN_HEIGHT - 75)
    return back_but_l


BackButL = create_level_selection_buttons()


def draw_level_selection(screen, mouse_pos, title_font, text_font):
    level_buttons = make_level_select_buttons(screen, mouse_pos, title_font, text_font)

    back_colour = ACCENT_RED
    back_copy_but = BackButL.copy()

    if BackButL.collidepoint(mouse_pos):
        back_colour = ACCENT_RED_HOVER
        back_copy_but = BackButL.inflate(-3, -1)

    pg.draw.rect(screen, back_colour, back_copy_but, border_radius=10)

    title_text = title_font.render("Select Level", True, ACCENT_LIGHTBLUE)
    back_text = text_font.render("Back", True, WHITE)

    screen.blit(title_text, title_text.get_rect(center=(SCREEN_WIDTH // 2, 150)))
    screen.blit(back_text, back_text.get_rect(center=BackButL.center))

    return level_buttons


def handle_level_selection_events(event, level_buttons):
    if event.type == pg.MOUSEBUTTONDOWN:

        if BackButL.collidepoint(event.pos):
            return "menu", None

        for button in level_buttons:
            if button["rect"].collidepoint(event.pos):
                return "playing", button["level"]

    return None, None