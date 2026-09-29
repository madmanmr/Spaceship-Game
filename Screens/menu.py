import pygame as pg

from settings import *


def create_menu_buttons():
    level_selection_button = pg.Rect(0, 0, 220, 70)
    garage_button = pg.Rect(0, 0, 220, 70)

    level_selection_button.center = (
        (SCREEN_WIDTH // 2) - 180,
        600
    )

    garage_button.center = (
        (SCREEN_WIDTH // 2) + 180,
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

def draw_menu(screen, mouse_pos, title_font, subtitle_font):
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

    pg.draw.rect(screen,level_colour,level_copy_rect)
    pg.draw.rect(screen,garage_colour,garage_copy_rect)

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