import pygame as pg

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

upgradeState = 0

def home_buttons():
    exit_button = pg.Rect(0, 0, 150, 50)
    ship_button = pg.Rect(0, 0, 220, 70)
    laser_button = pg.Rect(0, 0, 220, 70)
    money_button = pg.Rect(0, 0, 220, 70)

    exit_button.center = (100, SCREEN_HEIGHT - 75)
    ship_button.center = (300, 255)
    laser_button.center = (300, 400)
    money_button.center = (300, 545)
    return exit_button, ship_button, laser_button, money_button
exit_button, ship_button, laser_button, money_button = home_buttons()
def home_draw(screen, mouse_pos, title_font, subtitle_font, text_font):

    back_but_copy = exit_button.copy()
    ship_but_copy = ship_button.copy()
    laser_but_copy = laser_button.copy()
    money_but_copy = money_button.copy()


    back_colour = (204, 57, 47)
    ship_colour = (219, 190, 57)
    laser_colour = (219, 190, 57)
    money_colour = (219, 190, 57)

    if exit_button.collidepoint(mouse_pos):
        back_colour = (173, 44, 35)
        back_but_copy = exit_button.inflate(-3, -1)
    if ship_button.collidepoint(mouse_pos):
        ship_colour = (173, 142, 42)
        ship_but_copy = ship_button.inflate(-7, -3)
    if laser_button.collidepoint(mouse_pos):
        laser_colour = (173, 142, 42)
        laser_but_copy = laser_button.inflate(-7, -3)
    if money_button.collidepoint(mouse_pos):
        money_colour = (173, 142, 42)
        money_but_copy = money_button.inflate(-7, -3)

    pg.draw.rect(screen, back_colour, back_but_copy, border_radius=10)
    pg.draw.rect(screen, ship_colour, ship_but_copy, border_radius=15)
    pg.draw.rect(screen, laser_colour, laser_but_copy, border_radius=15)
    pg.draw.rect(screen, money_colour, money_but_copy, border_radius=15)

    title = title_font.render("Garage", True, WHITE)
    exitText = text_font.render("Exit", True, WHITE)
    shipText = subtitle_font.render("Ship", True, WHITE)
    laserText = subtitle_font.render("Laser", True, WHITE)
    moneyText = subtitle_font.render("Money", True, WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
    exit_rect = exitText.get_rect(center=exit_button.center)
    shipText_rect = shipText.get_rect(center=ship_button.center)
    laserText_rect = laserText.get_rect(center=laser_button.center)
    moneyText_rect = moneyText.get_rect(center=money_button.center)

    screen.blit(title, title_rect)
    screen.blit(exitText, exit_rect)
    screen.blit(shipText, shipText_rect)
    screen.blit(laserText, laserText_rect)
    screen.blit(moneyText, moneyText_rect)

def ship_buttons():
    buy_button_h1 = pg.Rect(0, 0, 50, 30)
    back_button_h = pg.Rect(0, 0, 150, 50)

    buy_button_h1.center = ((SCREEN_WIDTH / 2) + 50, 255)
    back_button_h.center = (100, SCREEN_HEIGHT - 75)

    return buy_button_h1, back_button_h
buy_button_h1, back_button_h = ship_buttons()
def ship_upgrades_draw(screen, mouse_pos, title_font, subtitle_font, text_font, upgrade_data, upgrades, player):

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

    pg.draw.rect(screen, (173, 142, 42), ship_button, border_radius=15)
    pg.draw.rect(screen, buy_colour_1, buy_but_h1_copy, border_radius=5)
    pg.draw.rect(screen, back_colour, back_but_h_copy, border_radius=10)

    title = title_font.render("Ship Upgrades", True, WHITE)
    backText = text_font.render("Back", True, WHITE)
    shipText = subtitle_font.render("Ship", True, WHITE)
    buyText = text_font.render("Buy", True, WHITE)

    #max health upgrade text
    name1Text = subtitle_font.render("Increase Health", True, WHITE)
    bracketText = text_font.render(f"({upgrades["healthUpgrade"] + 1}/{upgrade_data["health"]["values"][len(healthMaxValues)]}", True, WHITE)
    currentLevelText = text_font.render(f"Current Level: {upgrade_data["health"]["values"][healthMaxValues] + 1}", True, WHITE)
    nextLevelText = text_font.render(f"Current Level: {upgrade_data["health"]["values"][healthMaxValues] + 2}", True, WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
    backText_rect = backText.get_rect(center=(back_button_h.center))
    shipText_rect = shipText.get_rect(center=ship_button.center)
    buyText_rect = buyText.get_rect(center=(buy_button_h1.center))

    name1Text_rect = name1Text.get_rect(center=((SCREEN_WIDTH / 2) + 250, 270))
    bracketText_rect = bracketText.get_rect(center=(name1Text.x + 150, name1Text.y))
    currentLevelText_rect = currentLevelText.get_rect(center=(name1Text.x, name1Text.y + 40))
    nextLevelText_rect = nextLevelText.get_rect(center=(name1Text.x, name1Text.y + 80))

    screen.blit(title, title_rect)
    screen.blit(backText, backText_rect)
    screen.blit(shipText, shipText_rect)
    screen.blit(buyText, buyText_rect)

    screen.blit(name1Text, name1Text_rect)
    screen.blit(bracketText, bracketText_rect)
    screen.blit(currentLevelText, currentLevelText_rect)
    if (upgrade_data["health"]["values"][healthMaxValues] + 1) < upgrade_data["health"]["values"][len(healthMaxValues)]:
        screen.blit(nextLevelText, nextLevelText_rect)

def laser_buttons():
    buy_button_l1 = pg.Rect(0, 0, 50, 30)
    back_button_l = pg.Rect(0, 0, 150, 50)

    buy_button_l1.center = ((SCREEN_WIDTH / 2) + 50, 255)
    back_button_l.center = (100, SCREEN_HEIGHT - 75)

    return buy_button_l1, back_button_l
buy_button_l1, back_button_l = laser_buttons()
def laser_upgrades_draw(screen, mouse_pos, title_font, subtitle_font, text_font,  upgrade_data, upgrades, player):
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

    pg.draw.rect(screen, (173, 142, 42), laser_button, border_radius=15)
    pg.draw.rect(screen, buy_colour_1, buy_but_l1_copy, border_radius=5)
    pg.draw.rect(screen, back_colour, back_but_l_copy, border_radius=10)

    title = title_font.render("Laser Upgrades", True, WHITE)
    backText = text_font.render("Back", True, WHITE)
    laserText = subtitle_font.render("Laser", True, WHITE)
    buyText = text_font.render("Buy", True, WHITE)
    name1Text = subtitle_font.render("Laser Speed", True, WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
    backText_rect = backText.get_rect(center=(back_button_l.center))
    laserText_rect = laserText.get_rect(center=laser_button.center)
    buyText_rect = buyText.get_rect(center=(buy_button_l1.center))
    name1Text_rect = name1Text.get_rect(center=(buy_button_l1.x + 200, buy_button_l1.y + 15))

    screen.blit(title, title_rect)
    screen.blit(backText, backText_rect)
    screen.blit(laserText, laserText_rect)
    screen.blit(buyText, buyText_rect)
    screen.blit(name1Text, name1Text_rect)


def money_buttons():
    buy_button_m1 = pg.Rect(0, 0, 50, 30)
    back_button_m = pg.Rect(0, 0, 150, 50)

    buy_button_m1.center = ((SCREEN_WIDTH / 2) + 50, 255)
    back_button_m.center = (100, SCREEN_HEIGHT - 75)

    return buy_button_m1, back_button_m
buy_button_m1, back_button_m = money_buttons()
def money_upgrades_draw(screen, mouse_pos, title_font, subtitle_font, text_font,  upgrade_data, upgrades, player):
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

    pg.draw.rect(screen, (173, 142, 42), money_button, border_radius=15)
    pg.draw.rect(screen, buy_colour_1, buy_but_m1_copy, border_radius=5)
    pg.draw.rect(screen, back_colour, back_but_m_copy, border_radius=10)

    title = title_font.render("Economic Upgrades", True, WHITE)
    backText = text_font.render("Back", True, WHITE)
    moneyText = subtitle_font.render("Money", True, WHITE)
    buyText = text_font.render("Buy", True, WHITE)
    name1Text = subtitle_font.render("Earn More Coins", True, WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
    backText_rect = backText.get_rect(center=(back_button_m.center))
    moneyText_rect = moneyText.get_rect(center=money_button.center)
    buyText_rect = buyText.get_rect(center=(buy_button_m1.center))
    name1Text_rect = name1Text.get_rect(center=(buy_button_m1.x + 200, buy_button_m1.y + 15))

    screen.blit(title, title_rect)
    screen.blit(backText, backText_rect)
    screen.blit(moneyText, moneyText_rect)
    screen.blit(buyText, buyText_rect)
    screen.blit(name1Text, name1Text_rect)

def draw_garage(screen, mouse_pos, garageTextFunc, title_font, subtitle_font, text_font,  upgrade_data, upgrades, player):

    screen.fill((15, 15, 30))

    draw_functions = {
        0: home_draw,
        1: ship_upgrades_draw,
        2: laser_upgrades_draw,
        3: money_upgrades_draw
    }

    draw_functions[upgradeState](screen, mouse_pos, title_font, subtitle_font, text_font, upgrade_data)

    garageTextFunc()

def handle_garage_events(event, upgrade_data, upgrades, player):
    global upgradeState
    if event.type == pg.MOUSEBUTTONDOWN:
        if upgradeState == 0:
            if exit_button.collidepoint(event.pos):
                return "menu"
            elif ship_button.collidepoint(event.pos):
                upgradeState = 1
            elif laser_button.collidepoint(event.pos):
                upgradeState = 2
            elif money_button.collidepoint(event.pos):
                upgradeState = 3
        elif exit_button.collidepoint(event.pos):
            upgradeState = 0
        elif upgradeState == 1:
            if buy_button_h1.collidepoint(event.pos):
                level = upgrades["healthUpgrade"]

                if level < len(upgrade_data["health"]["costs"]):
                    cost = upgrade_data["health"]["costs"][level]

                    if player["coins"] >= cost:
                        player["coins"] -= cost
                        upgrades["healthUpgrade"] += 1
                        return "updateUpgrades"

        elif upgradeState == 2:
            if buy_button_l1.collidepoint(event.pos):
                level = upgrades["laserSpeedUpgrade"]

                if level < len(upgrade_data["laser_speed"]["costs"]):
                    cost = upgrade_data["laser_speed"]["costs"][level]

                    if player["coins"] >= cost:
                        player["coins"] -= cost
                        upgrades["laserSpeedUpgrade"] += 1
                        return "updateUpgrades"

        elif upgradeState == 3:
            if buy_button_m1.collidepoint(event.pos):
                level = upgrades["coinUpgrade"]

                if level < len(upgrade_data["coin_reward"]["costs"]):
                    cost = upgrade_data["coin_reward"]["costs"][level]

                    if player["coins"] >= cost:
                        player["coins"] -= cost
                        upgrades["coinUpgrade"] += 1
                        return "updateUpgrades"
    return None