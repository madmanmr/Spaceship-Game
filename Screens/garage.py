import pygame as pg

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

upgradeState = 0

def home_draw(screen, mouse_pos):
    back_button = pg.Rect(0, 0, 150, 50)
    health_button = pg.Rect(0, 0, 220, 70)
    laser_button = pg.Rect(0, 0, 220, 70)
    money_button = pg.Rect(0, 0, 220, 70)

    back_button.center = (100, SCREEN_HEIGHT - 75)
    health_button.center = (300, 305)
    laser_button.center = (300, 425)
    money_button.center = (300, 545)

    back_colour = (204, 57, 47)
    health_colour = (219, 190, 57)
    laser_colour = (219, 190, 57)
    money_colour = (219, 190, 57)

    if back_button.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)
        back_button.inflate(-3, -1)
    if health_button.collidepoint(mouse_pos):
        health_colour = (173, 142, 42)
        health_button = health_button.inflate(-7, -3)
    if laser_button.collidepoint(mouse_pos):
        laser_colour = (173, 142, 42)
        laser_button = laser_button.inflate(-7, -3)
    if money_button.collidepoint(mouse_pos):
        money_colour = (173, 142, 42)
        money_button = money_button.inflate(-7, -3)

    pg.draw.rect(screen, back_colour, back_button, border_radius=10)
    pg.draw.rect(screen, health_colour, health_button, border_radius=15)
    pg.draw.rect(screen, laser_colour, laser_button, border_radius=15)
    pg.draw.rect(screen, money_colour, money_button, border_radius=15)

    return back_button, health_button, laser_button, money_button

back_button, health_button, laser_button, money_button = home_draw(screen, mouse_pos)

def health_upgrades_draw(screen, mouse_pos):
    buy_button = pg.Rect(0, 0, 50, 30)
    back_button = pg.Rect(0, 0, 150, 50)

    buy_button.center = (800, 400)
    back_button.center = (100, SCREEN_HEIGHT - 75)

    buy_colour = (60, 220, 100)
    back_colour = (204, 57, 47)

    if buy_button.collidepoint(mouse_pos):
        buy_colour = (40, 180, 80)
    if back_button.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)

    pg.draw.rect(screen, buy_colour, buy_button, border_radius=5)
    pg.draw.rect(screen, back_colour, back_button, border_radius=10)


def laser_upgrades_draw(screen, mouse_pos):
    buy_button = pg.Rect(0, 0, 50, 30)
    back_button = pg.Rect(0, 0, 150, 50)

    buy_button.center = (800, 400)
    back_button.center = (100, SCREEN_HEIGHT - 75)

    buy_colour = (60, 220, 100)
    back_colour = (204, 57, 47)

    if buy_button.collidepoint(mouse_pos):
        buy_colour = (40, 180, 80)
    if back_button.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)

    pg.draw.rect(screen, buy_colour, buy_button, border_radius=5)
    pg.draw.rect(screen, back_colour, back_button, border_radius=10)

def money_upgrades_draw(screen, mouse_pos):
    buy_button = pg.Rect(0, 0, 50, 30)
    back_button = pg.Rect(0, 0, 150, 50)

    buy_button.center = (800, 400)
    back_button.center = (100, SCREEN_HEIGHT - 75)

    buy_colour = (60, 220, 100)
    back_colour = (204, 57, 47)

    if buy_button.collidepoint(mouse_pos):
        buy_colour = (40, 180, 80)
    if back_button.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)

    pg.draw.rect(screen, buy_colour, buy_button, border_radius=5)
    pg.draw.rect(screen, back_colour, back_button, border_radius=10)

def draw_garage(screen, garageTextFunc, mouse_pos):

    screen.fill((15, 15, 30))

    draw_functions = {
        0: home_draw,
        1: health_upgrades_draw,
        2: laser_upgrades_draw,
        3: money_upgrades_draw
    }

    draw_functions[upgradeState](screen, mouse_pos)
    '''back_colour = (204, 57, 47)
    health_colour = (219, 190, 57)
    laser_colour = (219, 190, 57)
    money_colour = (219, 190, 57)

    back_copy_but = BackButG.copy()
    health_copy_but = health_button.copy()
    laser_copy_but = laser_button.copy()
    money_copy_but = money_button.copy()

    if BackButG.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)
        back_copy_but = BackButG.inflate(-3, -1)
    if health_copy_but.collidepoint(mouse_pos):
        health_colour = (173, 142, 42)
        health_copy_but = health_button.inflate(-7, -3)
    if laser_copy_but.collidepoint(mouse_pos):
        laser_colour = (173, 142, 42)
        laser_copy_but = laser_button.inflate(-7, -3)
    if money_copy_but.collidepoint(mouse_pos):
        money_colour = (173, 142, 42)
        money_copy_but = money_button.inflate(-7, -3)

    if upgradeState == 0:
        pg.draw.rect(screen, back_colour, back_copy_but, border_radius=10)
        pg.draw.rect(screen, health_colour, health_copy_but, border_radius=15)
        pg.draw.rect(screen, laser_colour, laser_copy_but, border_radius=15)
        pg.draw.rect(screen, money_colour, money_copy_but, border_radius=15)

        back_text = text_font.render("Exit", True, BLACK)
        title_text = title_font.render("Garage", True, WHITE)

    elif upgradeState == 1:
        health_upgrades_draw(screen, mouse_pos)

        back_text = text_font.render("Back", True, BLACK)
        title_text = title_font.render("Health Upgrades", True, WHITE)
        health_text = subtitle_font.render("Health", True, BLACK)

    elif upgradeState == 2:
        laser_upgrades_draw(screen, mouse_pos)
        back_text = text_font.render("Back", True, BLACK)
        title_text = title_font.render("Laser Upgrades", True, WHITE)

    elif upgradeState == 3:
        money_upgrades_draw(screen, mouse_pos)
        back_text = text_font.render("Back", True, BLACK)
        title_text = title_font.render("Economic Upgrades", True, WHITE)


    laser_text = subtitle_font.render("Laser", True, BLACK)
    money_text = subtitle_font.render("Money", True, BLACK)

    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
    back_rect = back_text.get_rect(center=BackButG.center)
    health_rect = health_text.get_rect(center=health_copy_but.center)
    laser_rect = laser_text.get_rect(center=laser_copy_but.center)
    money_rect = money_text.get_rect(center=money_copy_but.center)

    screen.blit(title_text, title_rect)
    screen.blit(back_text, back_rect)
    screen.blit(health_text, health_rect)
    screen.blit(laser_text, laser_rect)
    screen.blit(money_text, money_rect) '''

    garageTextFunc()

def handle_garage_events(event):
    global upgradeState
    if event.type == pg.MOUSEBUTTONDOWN:
        if back_button.collidepoint(event.pos):
            if upgradeState == 0:
                return "menu"
            else:
                upgradeState = 0
        elif health_button.collidepoint(event.pos):
            upgradeState = 1
        elif laser_button.collidepoint(event.pos):
            upgradeState = 2
        elif money_button.collidepoint(event.pos):
            upgradeState = 3
    return None