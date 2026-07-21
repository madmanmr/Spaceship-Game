import pygame as pg

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

upgradeState = 0

def home_buttons():
    exit_button = pg.Rect(0, 0, 150, 50)
    health_button = pg.Rect(0, 0, 220, 70)
    laser_button = pg.Rect(0, 0, 220, 70)
    money_button = pg.Rect(0, 0, 220, 70)

    exit_button.center = (100, SCREEN_HEIGHT - 75)
    health_button.center = (300, 305)
    laser_button.center = (300, 425)
    money_button.center = (300, 545)
    return exit_button, health_button, laser_button, money_button
exit_button, health_button, laser_button, money_button = home_buttons()
def home_draw(screen, mouse_pos, title_font, subtitle_font, text_font):

    back_but_copy = exit_button.copy()
    health_but_copy = health_button.copy()
    laser_but_copy = laser_button.copy()
    money_but_copy = money_button.copy()


    back_colour = (204, 57, 47)
    health_colour = (219, 190, 57)
    laser_colour = (219, 190, 57)
    money_colour = (219, 190, 57)

    if exit_button.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)
        back_but_copy = exit_button.inflate(-3, -1)
    if health_button.collidepoint(mouse_pos):
        health_colour = (173, 142, 42)
        health_but_copy = health_button.inflate(-7, -3)
    if laser_button.collidepoint(mouse_pos):
        laser_colour = (173, 142, 42)
        laser_but_copy = laser_button.inflate(-7, -3)
    if money_button.collidepoint(mouse_pos):
        money_colour = (173, 142, 42)
        money_but_copy = money_button.inflate(-7, -3)

    pg.draw.rect(screen, back_colour, back_but_copy, border_radius=10)
    pg.draw.rect(screen, health_colour, health_but_copy, border_radius=15)
    pg.draw.rect(screen, laser_colour, laser_but_copy, border_radius=15)
    pg.draw.rect(screen, money_colour, money_but_copy, border_radius=15)

    title = title_font.render("Garage", True, WHITE)
    exitText = text_font.render("Exit", True, WHITE)
    healthText = subtitle_font.render("Health", True, WHITE)
    laserText = subtitle_font.render("Laser", True, WHITE)
    moneyText = subtitle_font.render("Money", True, WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    exit_rect = exitText.get_rect(center=exit_button.center)
    healthText_rect = healthText.get_rect(center=health_button.center)
    laserText_rect = laserText.get_rect(center=laser_button.center)
    moneyText_rect = moneyText.get_rect(center=money_button.center)

    screen.blit(title, title_rect)
    screen.blit(exitText, exit_rect)
    screen.blit(healthText, healthText_rect)
    screen.blit(laserText, laserText_rect)
    screen.blit(moneyText, moneyText_rect)

def health_buttons():
    buy_button_h1 = pg.Rect(0, 0, 50, 30)
    back_button_h = pg.Rect(0, 0, 150, 50)

    buy_button_h1.center = (400, 400)
    back_button_h.center = (100, SCREEN_HEIGHT - 75)

    return buy_button_h1, back_button_h
buy_button_h1, back_button_h = health_buttons()
def health_upgrades_draw(screen, mouse_pos, title_font, subtitle_font, text_font):

    buy_but_h1_copy = buy_button_h1.copy()
    back_but_h_copy = back_button_h.copy()

    buy_colour_1 = (60, 220, 100)
    back_colour = (204, 57, 47)

    if buy_button_h1.collidepoint(mouse_pos):
        buy_colour_1 = (40, 180, 80)
        buy_but_h1_copy = buy_button_h1.inflate(-1, -0.3)
    if back_button_h.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)
        back_but_h_copy = back_button_h.inflate(-3, -1)

    pg.draw.rect(screen, buy_colour_1, buy_but_h1_copy, border_radius=5)
    pg.draw.rect(screen, back_colour, back_but_h_copy, border_radius=10)

    title = title_font.render("Health Upgrades", True, WHITE)
    backText = text_font.render("Back", True, WHITE)
    buyText = text_font.render("Buy", True, WHITE)
    name1Text = subtitle_font.render("Increase Health", True, WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    backText_rect = backText.get_rect(center=(back_button_h.center))
    buyText_rect = buyText.get_rect(center=(buy_button_h1.center))
    name1Text_rect = name1Text.get_rect(center=(buy_button_h1.x - 150, buy_button_h1.y + 15))

    screen.blit(title, title_rect)
    screen.blit(backText, backText_rect)
    screen.blit(buyText, buyText_rect)
    screen.blit(name1Text, name1Text_rect)


def laser_buttons():
    buy_button_l1 = pg.Rect(0, 0, 50, 30)
    back_button_l = pg.Rect(0, 0, 150, 50)

    buy_button_l1.center = (800, 400)
    back_button_l.center = (100, SCREEN_HEIGHT - 75)

    return buy_button_l1, back_button_l
buy_button_l1, back_button_l = laser_buttons()
def laser_upgrades_draw(screen, mouse_pos, title_font, subtitle_font, text_font):
    buy_but_l1_copy = buy_button_l1.copy()
    back_but_l_copy = back_button_l.copy()

    buy_colour_1 = (60, 220, 100)
    back_colour = (204, 57, 47)

    if buy_button_l1.collidepoint(mouse_pos):
        buy_colour_1 = (40, 180, 80)
        buy_but_l1_copy = buy_button_l1.inflate(-1, -0.3)
    if back_button_l.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)
        back_but_l_copy = back_button_l.inflate(-3, -1)

    pg.draw.rect(screen, buy_colour_1, buy_but_l1_copy, border_radius=5)
    pg.draw.rect(screen, back_colour, back_but_l_copy, border_radius=10)

    title = title_font.render("Laser Upgrades", True, WHITE)
    backText = text_font.render("Back", True, WHITE)
    buyText = text_font.render("Buy", True, WHITE)
    name1Text = subtitle_font.render("Laser Speed", True, WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    backText_rect = backText.get_rect(center=(back_button_l.center))
    buyText_rect = buyText.get_rect(center=(buy_button_l1.center))
    name1Text_rect = name1Text.get_rect(center=(buy_button_l1.x - 150, buy_button_l1.y + 15))

    screen.blit(title, title_rect)
    screen.blit(backText, backText_rect)
    screen.blit(buyText, buyText_rect)
    screen.blit(name1Text, name1Text_rect)


def money_buttons():
    buy_button_m1 = pg.Rect(0, 0, 50, 30)
    back_button_m = pg.Rect(0, 0, 150, 50)

    buy_button_m1.center = (800, 400)
    back_button_m.center = (100, SCREEN_HEIGHT - 75)

    return buy_button_m1, back_button_m
buy_button_m1, back_button_m = money_buttons()
def money_upgrades_draw(screen, mouse_pos, title_font, subtitle_font, text_font):
    buy_but_m1_copy = buy_button_m1.copy()
    back_but_m_copy = back_button_m.copy()

    buy_colour_1 = (60, 220, 100)
    back_colour = (204, 57, 47)

    if buy_button_m1.collidepoint(mouse_pos):
        buy_colour_1 = (40, 180, 80)
        buy_but_m1_copy = buy_button_m1.inflate(-1, -0.3)
    if back_button_m.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)
        back_but_m_copy = back_button_m.inflate(-3, -1)

    pg.draw.rect(screen, buy_colour_1, buy_but_m1_copy, border_radius=5)
    pg.draw.rect(screen, back_colour, back_but_m_copy, border_radius=10)

    title = title_font.render("Economic Upgrades", True, WHITE)
    backText = text_font.render("Back", True, WHITE)
    buyText = text_font.render("Buy", True, WHITE)
    name1Text = subtitle_font.render("Earn More Coins", True, WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    backText_rect = backText.get_rect(center=(back_button_m.center))
    buyText_rect = buyText.get_rect(center=(buy_button_m1.center))
    name1Text_rect = name1Text.get_rect(center=(buy_button_m1.x - 150, buy_button_m1.y + 15))

    screen.blit(title, title_rect)
    screen.blit(backText, backText_rect)
    screen.blit(buyText, buyText_rect)
    screen.blit(name1Text, name1Text_rect)

def draw_garage(screen, mouse_pos, garageTextFunc, title_font, subtitle_font, text_font):

    screen.fill((15, 15, 30))

    draw_functions = {
        0: home_draw,
        1: health_upgrades_draw,
        2: laser_upgrades_draw,
        3: money_upgrades_draw
    }

    draw_functions[upgradeState](screen, mouse_pos, title_font, subtitle_font, text_font)

    garageTextFunc()

def handle_garage_events(event):
    global upgradeState
    if event.type == pg.MOUSEBUTTONDOWN:
        if upgradeState == 0:
            if exit_button.collidepoint(event.pos):
                return "menu"
            elif health_button.collidepoint(event.pos):
                upgradeState = 1
            elif laser_button.collidepoint(event.pos):
                upgradeState = 2
            elif money_button.collidepoint(event.pos):
                upgradeState = 3
        elif exit_button.collidepoint(event.pos):
            upgradeState = 0
    return None