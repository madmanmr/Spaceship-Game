import pygame as pg

from settings import *


def create_menu_buttons():
    level_selection_button = pg.Rect(0, 0, 220, 70)
    garage_button = pg.Rect(0, 0, 220, 70)

    level_selection_button.center = (
        (SCREEN_WIDTH // 2) - 200,
        600
    )

    garage_button.center = (
        (SCREEN_WIDTH // 2) + 200,
        600
    )

    return level_selection_button, garage_button

levelSelectionBut, GarageBut = create_menu_buttons()


# draw inside of spacehip first
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
       (257.419, 541.390), #bottom left of left pillar
       (266.448, 536.528), #bottom right of left pillar
       (145.453, 100.948), #top right of left pillar
       (SCREEN_WIDTH / 2, 180), # centre of top shape
       (1054.547, 100.948), #top left of right pillar
       (932.588, 540), # bottom left of right pillar
       (260, SCREEN_HEIGHT - 260), #point where left pillar meets bottom control desk
       (0, SCREEN_HEIGHT - 120), #top left of control panel
       (0, SCREEN_HEIGHT), # bottom left corner
       (70, SCREEN_HEIGHT), #bottom left to the right a bit
       (295, 663.043), # first top left intersection
       (295, 727.34), #down that left vertical to intersection
       (192.226, 795.840), #bottom left of bottom left line
       (197.774, 804.160), #bottom right point of l;ine
       (301.514, 735.000),
       (895, 735.000),
       (895.000, 725.00),
       (305.000, 725.000),
       (305.000, 660.000),
       (895, 660),
       (895, 735.000),
       (1002.226, 804.160),
       (1007.774, 795.840),
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

def draw_menu(screen, mouse_pos, title_font, subtitle_font, stars):
    draw_interior(screen)
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

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 60))
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