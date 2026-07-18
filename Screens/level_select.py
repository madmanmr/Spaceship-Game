import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK


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

level1But, level2But, level3But, BackButL = (create_level_selection_buttons())

def draw_level_selection(screen, mouse_pos, title_font, text_font):
    screen.fill((15, 15, 30))

    colour1 = (60, 220, 100)
    colour2 = (60, 220, 100)
    colour3 = (60, 220, 100)
    back_colour = (204, 57, 47)

    level1_copy_but = level1But.copy()
    level2_copy_but = level2But.copy()
    level3_copy_but = level3But.copy()
    back_copy_but = BackButL.copy()

    if level1But.collidepoint(mouse_pos):
        colour1 = (40, 180, 80)
        level1_copy_but = level1But.inflate(-7, -3)

    if level2But.collidepoint(mouse_pos):
        colour2 = (40, 180, 80)
        level2_copy_but = level2But.inflate(-7, -3)

    if level3But.collidepoint(mouse_pos):
        colour3 = (40, 180, 80)
        level3_copy_but = level3But.inflate(-7, -3)

    if BackButL.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)
        back_copy_but = BackButL.inflate(-3, -1)

    pg.draw.rect(screen, colour1, level1_copy_but, border_radius=15)
    pg.draw.rect(screen, colour2, level2_copy_but, border_radius=15)
    pg.draw.rect(screen, colour3, level3_copy_but, border_radius=15)
    pg.draw.rect(screen, back_colour, back_copy_but, border_radius=10)

    title_text = title_font.render("Select Level", True, WHITE)
    level1_text = text_font.render("1", True, BLACK)
    level2_text = text_font.render("2", True, BLACK)
    level3_text = text_font.render("3", True, BLACK)
    back_text = text_font.render("Back", True, WHITE)

    screen.blit(title_text,title_text.get_rect(center=(SCREEN_WIDTH // 2, 150)))
    screen.blit(level1_text,level1_text.get_rect(center=level1But.center))
    screen.blit(level2_text,level2_text.get_rect(center=level2But.center))
    screen.blit(level3_text,level3_text.get_rect(center=level3But.center))
    screen.blit(back_text,back_text.get_rect(center=BackButL.center))

def handle_level_selection_events(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        if level1But.collidepoint(event.pos):
            return "playing", 1

        elif level2But.collidepoint(event.pos):
            return "playing", 2

        elif level3But.collidepoint(event.pos):
            return "playing", 3

        elif BackButL.collidepoint(event.pos):
            return "menu", None

    return None, None