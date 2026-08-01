import pygame as pg

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

def make_level_select_buttons(screen, mouse_pos, title_font, text_font):
    levelAmount = range(1, 7)

    x = 200
    y = 300

    levelButtons = []


    for levelNum in levelAmount:
        buttonText = str(levelNum)

        levelBut = pg.Rect(0, 0, 150, 50)
        levelBut.center = (x,y)

        levelBut_copy = levelBut.copy()

        colour = (60, 220, 100)
        if levelBut.collidepoint(mouse_pos):
            colour = (40, 180, 80)
            levelBut_copy = levelBut.inflate(-7, -3)

        pg.draw.rect(screen, colour, levelBut_copy, border_radius=15)

        levelText = text_font.render(buttonText, True, WHITE)
        screen.blit(levelText,levelText.get_rect(center=levelBut.center))

        if x < 1000:
            x += 400
        else:
            x = 200
            y = 500

        buttonData = {
            "rect": levelBut,
            "level": levelNum
        }

        levelButtons.append(buttonData)

    return levelButtons

def create_level_selection_buttons():
    BackButL = pg.Rect(0, 0, 150, 50)

    BackButL.center = (100, SCREEN_HEIGHT - 75)

    return BackButL

BackButL = (create_level_selection_buttons())

def draw_level_selection(screen, mouse_pos, title_font, text_font):
    screen.fill((15, 15, 30))

    levelButtons = []
    levelButtons = make_level_select_buttons(screen, mouse_pos, title_font, text_font)

    back_colour = (204, 57, 47)
    back_copy_but = BackButL.copy()

    if BackButL.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)
        back_copy_but = BackButL.inflate(-3, -1)

    pg.draw.rect(screen, back_colour, back_copy_but, border_radius=10)

    title_text = title_font.render("Select Level", True, WHITE)
    back_text = text_font.render("Back", True, WHITE)

    screen.blit(title_text,title_text.get_rect(center=(SCREEN_WIDTH // 2, 150)))
    screen.blit(back_text,back_text.get_rect(center=BackButL.center))

    return levelButtons

def handle_level_selection_events(event, levelButtons):
    if event.type == pg.MOUSEBUTTONDOWN:
        if BackButL.collidepoint(event.pos):
            return "menu", None
        else:
            for button in levelButtons:
                if button["rect"].collidepoint(event.pos):
                    level = button["level"]
                    return "playing", level

    return None, None