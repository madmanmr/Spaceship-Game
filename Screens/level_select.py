import pygame as pg
from settings import *


def make_level_select_buttons(screen, mouse_pos, title_font, text_font):
    level_amount = range(1, 7)
    xinc = 300
    x = 300
    y = 270
    dif = x - xinc

    level_buttons = []

    for level_num in level_amount:
        button_text = str(level_num)

        level_but = pg.Rect(0, 0, 150, 50)
        level_but.center = (x, y)

        level_but_copy = level_but.copy()

        colour = ACCENT_PURPLE

        if level_but.collidepoint(mouse_pos):
            colour = ACCENT_PURPLE_HOVER

        if level_but.collidepoint(mouse_pos):
            level_but_copy = level_but.inflate(-7, -3)

        pg.draw.rect(screen, colour, level_but_copy, )

        level_text = text_font.render(button_text, True, BLACK)
        screen.blit(level_text, level_text.get_rect(center=level_but.center))

        button_data = {"rect": level_but, "level": level_num}
        level_buttons.append(button_data)

        if x < (300 + dif) + 2 * xinc + dif:
            x += xinc
        else:
            x = 350
            xinc = 250
            y = 420

    return level_buttons

def draw_interior(screen):
   top_points = [
       (0, 0),
       (140, 120),
       (SCREEN_WIDTH / 2, 200),
       (SCREEN_WIDTH - 140, 120),
       (SCREEN_WIDTH, 0)
   ]

   bottom_points = [
       (0, SCREEN_HEIGHT),
       (0, SCREEN_HEIGHT - 140),
       (260, SCREEN_HEIGHT - 280),
       (SCREEN_WIDTH - 260, SCREEN_HEIGHT - 280),
       (SCREEN_WIDTH, SCREEN_HEIGHT - 140),
       (SCREEN_WIDTH, SCREEN_HEIGHT),
   ]
   pg.draw.polygon(screen, DARK_GREY, top_points)#top
   pg.draw.polygon(screen, DARK_GREY, bottom_points)#bottom

   pg.draw.line(screen, DARK_GREY, (140,100), (260, SCREEN_HEIGHT - 270), width=30)#left
   pg.draw.line(screen, DARK_GREY, (SCREEN_WIDTH - 140, 100), (SCREEN_WIDTH - 260, SCREEN_HEIGHT - 270), width=30)#right

   #grey polygon
   grey_polygon = [
       (23.5, 0),# top left start
       (133.186, 94.151), #top left of left pillar
       (257.750, 542), #bottom left of left pillar
       (260.000, 540.000),
       (267.412, 540.000), #bottom right of left pillar
       (145.453, 100.948), #top right of left pillar
       (SCREEN_WIDTH / 2, 180), # centre of top shape
       (1054.547, 100.948), #top left of right pillar
       (932.588, 540), # bottom left of right pillar
       (260, SCREEN_HEIGHT - 260), #point where left pillar meets bottom control desk
       (0, SCREEN_HEIGHT - 120), #top left of control panel
       (0, SCREEN_HEIGHT), # bottom left corner
       (70, SCREEN_HEIGHT), #bottom left to the right a bit
       (295, 660), # first top left intersection
       (295, 727.34), #down that left vertical to intersection
       (185.985, 800.000), #bottom left of bottom left line
       (203.039, 800.000), #bottom right point of l;ine
       (301.514, 735.000),
       (895, 735.000),
       (895.000, 725.00),
       (305.000, 725.000),
       (305.000, 660.000),
       (895, 660),
       (895, 735.000),
       (996.961, 800.000),
       (1014.015, 800.000),
       (905.000, 727.324),
       (905.000, 660.000),
       (SCREEN_WIDTH - 70, SCREEN_HEIGHT), # bottom right minus some
       (SCREEN_WIDTH, SCREEN_HEIGHT), # bottom right corner
       (SCREEN_WIDTH, SCREEN_HEIGHT - 120), #coming back up right side
       (942.581, 541.390), # bottom right of right pillar intersection
       (1066.814, 94.151), #top right of right pillar
       (SCREEN_WIDTH - 23.5, 0),
   ]
   pg.draw.polygon(screen, GREY, grey_polygon)

   pg.draw.rect(screen, LIGHT_GREY, (146, 10, 910, 91), ) #higlight
   pg.draw.rect(screen, DARK_GREY, (160, 20, 880, 70), )

   #button backs
   pg.draw.rect(screen, DARK_GREY, ((SCREEN_WIDTH // 2) + 60, 555, 240, 90))
   pg.draw.rect(screen, DARK_GREY, ((SCREEN_WIDTH // 2) - 300, 555, 240, 90))

   #draw light around control top
   light_grey_top = [
       (0, SCREEN_HEIGHT - 115),
       (260, SCREEN_HEIGHT - 255),
       (940, SCREEN_HEIGHT - 255),
       (1200, SCREEN_HEIGHT - 115),
       (1200, SCREEN_HEIGHT - 106),
       (1195, SCREEN_HEIGHT - 106),
       (937, SCREEN_HEIGHT - 245),
       (263, SCREEN_HEIGHT - 245),
       (5, SCREEN_HEIGHT - 106),
       (0, SCREEN_HEIGHT - 106),
   ]
   light_grey_bottom = [
       (70, SCREEN_HEIGHT),
       (295, 660),
       (905, 660),
       (SCREEN_WIDTH - 70, SCREEN_HEIGHT),
       (1148.929, SCREEN_HEIGHT),
       (910.283, 650),
       (289.717, 650),
       (51.071, SCREEN_HEIGHT),
   ]
   middle_line = [
       (595, 555),
       (595, 649),
       (605, 649),
       (605, 555)
   ]


   pg.draw.polygon(screen, LIGHT_GREY, light_grey_top)
   pg.draw.polygon(screen, LIGHT_GREY, light_grey_bottom)
   pg.draw.polygon(screen, LIGHT_GREY, middle_line)


   #dark lines
   left_dark = [
       (263, SCREEN_HEIGHT - 244),
       (270, SCREEN_HEIGHT - 244),
       (296.717, 649),
       (289.717, 649),
   ]
   right_dark = [
       (937, SCREEN_HEIGHT - 244),
       (930, SCREEN_HEIGHT - 244),
       (903.283, 649),
       (910.283, 649),
   ]
   pg.draw.polygon(screen, DARK_GREY, left_dark)
   pg.draw.polygon(screen, DARK_GREY, right_dark)

   #draw seats + middle part
   left_back = [
       ((SCREEN_WIDTH // 2) - 240, SCREEN_HEIGHT),
       ((SCREEN_WIDTH // 2) - 240, SCREEN_HEIGHT - 130),
       ((SCREEN_WIDTH // 2) - 80, SCREEN_HEIGHT - 130),
       ((SCREEN_WIDTH // 2) - 80, SCREEN_HEIGHT)
   ]
   right_back = [
       ((SCREEN_WIDTH // 2) + 240, SCREEN_HEIGHT),
       ((SCREEN_WIDTH // 2) + 240, SCREEN_HEIGHT - 130),
       ((SCREEN_WIDTH // 2) + 80, SCREEN_HEIGHT - 130),
       ((SCREEN_WIDTH // 2) + 80, SCREEN_HEIGHT)
   ]
   left = [
       ((SCREEN_WIDTH // 2) - 230, SCREEN_HEIGHT),
       ((SCREEN_WIDTH // 2) - 230, SCREEN_HEIGHT - 120),
       ((SCREEN_WIDTH // 2) - 90, SCREEN_HEIGHT - 120),
       ((SCREEN_WIDTH // 2) - 90, SCREEN_HEIGHT)
   ]
   right = [
       ((SCREEN_WIDTH // 2) + 230, SCREEN_HEIGHT),
       ((SCREEN_WIDTH // 2) + 230, SCREEN_HEIGHT - 120),
       ((SCREEN_WIDTH // 2) + 90, SCREEN_HEIGHT - 120),
       ((SCREEN_WIDTH // 2) + 90, SCREEN_HEIGHT)
   ]
   pg.draw.polygon(screen, GREY, left_back)
   pg.draw.polygon(screen, GREY, right_back)
   pg.draw.polygon(screen, LIGHT_GREY, left)
   pg.draw.polygon(screen, LIGHT_GREY, right)
   #middle
   middle_box_dark = [
       ((SCREEN_WIDTH // 2) + 65, SCREEN_HEIGHT),
       ((SCREEN_WIDTH // 2) + 65, SCREEN_HEIGHT - 100),
       ((SCREEN_WIDTH // 2) - 65, SCREEN_HEIGHT - 100),
       ((SCREEN_WIDTH // 2) - 65, SCREEN_HEIGHT)
   ]
   middle_box_light = [
       ((SCREEN_WIDTH // 2) + 55, SCREEN_HEIGHT),
       ((SCREEN_WIDTH // 2) + 55, SCREEN_HEIGHT - 100),
       ((SCREEN_WIDTH // 2) - 55, SCREEN_HEIGHT - 100),
       ((SCREEN_WIDTH // 2) - 55, SCREEN_HEIGHT)
   ]
   pg.draw.polygon(screen, LIGHT_GREY, middle_box_dark)
   pg.draw.polygon(screen, GREY, middle_box_light)


   #chair highlights
   pg.draw.line(screen, ACCENT_LIGHTBLUE,  ((SCREEN_WIDTH // 2) + 160, SCREEN_HEIGHT),
                ((SCREEN_WIDTH // 2) + 160, SCREEN_HEIGHT - 120), width=8)
   pg.draw.line(screen, ACCENT_LIGHTBLUE, ((SCREEN_WIDTH // 2) - 160, SCREEN_HEIGHT),
                ((SCREEN_WIDTH // 2) - 160, SCREEN_HEIGHT - 120), width=8)

def create_level_selection_buttons():
    back_but_l = pg.Rect(0, 0, 200, 70)
    back_but_l.center = ((SCREEN_WIDTH // 2) - 180, 600)
    play_level = pg.Rect(0, 0, 200, 70)
    play_level.center = ((SCREEN_WIDTH // 2) + 180, 600)
    return back_but_l, play_level


BackButL, play_level = create_level_selection_buttons()


def draw_level_selection(screen, mouse_pos, title_font, text_font, selected_level):
    draw_interior(screen)
    level_buttons = make_level_select_buttons(screen, mouse_pos, title_font, text_font)

    back_colour = ACCENT_RED
    back_copy_but = BackButL.copy()
    play_level_colour = ACCENT_TURQUOISE
    play_level_copy = play_level.copy()

    if BackButL.collidepoint(mouse_pos):
        back_colour = ACCENT_RED_HOVER
        back_copy_but = BackButL.inflate(-7, -3)
    if play_level.collidepoint(mouse_pos):
        play_level_colour = ACCENT_TURQUOISE_HOVER
        play_level_copy = play_level.inflate(-7, -3)

    pg.draw.rect(screen, back_colour, back_copy_but, )
    pg.draw.rect(screen, play_level_colour, play_level_copy, )

    title_text = title_font.render("LEVEL SELECTION", True, ACCENT_LIGHTBLUE)
    back_text = text_font.render("Back", True, WHITE)
    play_text = text_font.render(f"Play {selected_level}" if selected_level is not None else "Play", True, WHITE)

    screen.blit(title_text, title_text.get_rect(center=(SCREEN_WIDTH // 2, 60)))
    screen.blit(back_text, back_text.get_rect(center=BackButL.center))
    screen.blit(play_text, play_text.get_rect(center=play_level.center))

    return level_buttons


def handle_level_selection_events(event, level_buttons, selected_level):
    if event.type == pg.MOUSEBUTTONDOWN:

        if BackButL.collidepoint(event.pos):
            return "menu", None

        if play_level.collidepoint(event.pos) and selected_level is not None:
            return "playing", selected_level

        for button in level_buttons:
            if button["rect"].collidepoint(event.pos):
                return None, button["level"]

    return None, None