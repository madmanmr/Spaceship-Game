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
   #-----dark grey
   top_points = [
       (0, 0),
       (140, 120),
       (SCREEN_WIDTH / 2, 200),
       (SCREEN_WIDTH - 140, 120),
       (SCREEN_WIDTH, 0)
   ]

   top_highlight = [
       (0, 0),
       (23.5, 0),
       (140, 100),
       (SCREEN_WIDTH / 2, 180),
       (SCREEN_WIDTH - 140, 100),
       (SCREEN_WIDTH - 23.5, 0),
       (SCREEN_WIDTH, 0),
       (SCREEN_WIDTH - 140, 120),
       (SCREEN_WIDTH / 2, 200),
       (140, 120),
   ]
   bottom_points = [
       (0, SCREEN_HEIGHT),
       (0, SCREEN_HEIGHT - 140),
       (260, SCREEN_HEIGHT - 280),
       (SCREEN_WIDTH - 260, SCREEN_HEIGHT - 280),
       (SCREEN_WIDTH, SCREEN_HEIGHT - 140),
       (SCREEN_WIDTH, SCREEN_HEIGHT),
   ]
   pg.draw.polygon(screen, GREY, top_points)  # top medium
   pg.draw.polygon(screen, DARK_GREY, top_highlight)#top
   pg.draw.polygon(screen, DARK_GREY, bottom_points)#bottom

   pg.draw.line(screen, DARK_GREY, (140,100), (260, SCREEN_HEIGHT - 270), width=30)#left
   pg.draw.line(screen, DARK_GREY, (SCREEN_WIDTH - 140, 100), (SCREEN_WIDTH - 260, SCREEN_HEIGHT - 270), width=30)#right

   #--------middle grey
   #top box
   pg.draw.rect(screen, LIGHT_GREY, (140, 0, 920, 110), )#higlight drawn before dont judge
   pg.draw.rect(screen, GREY, (160, 20, 880, 70), )

   #highlight pillar lines
   pg.draw.line(screen, GREY, (140, 100), (265, SCREEN_HEIGHT - 250), width=10)#left
   pg.draw.line(screen, GREY, (SCREEN_WIDTH - 140, 100), (SCREEN_WIDTH - 265, SCREEN_HEIGHT - 250), width=10)#right

   #control panel background
   control_panel_background = [
       (0, SCREEN_HEIGHT),
       (0, SCREEN_HEIGHT - 120),
       (260, SCREEN_HEIGHT - 260),
       (SCREEN_WIDTH - 260, SCREEN_HEIGHT - 260),
       (SCREEN_WIDTH, SCREEN_HEIGHT - 120),
       (SCREEN_WIDTH, SCREEN_HEIGHT),
       (SCREEN_WIDTH - 60, SCREEN_HEIGHT),
       (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 140),
       (300, SCREEN_HEIGHT - 140),
       (60, SCREEN_HEIGHT),
   ]
   pg.draw.polygon(screen, GREY, control_panel_background)


   #-------light grey

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