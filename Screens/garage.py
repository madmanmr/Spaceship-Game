import pygame as pg

from settings import *

selected_category = "home"

def home_buttons():
    exit_button = pg.Rect(0, 0, 150, 50)
    ship_button = pg.Rect(0, 0, 220, 70)
    laser_button = pg.Rect(0, 0, 220, 70)
    money_button = pg.Rect(0, 0, 220, 70)

    exit_button.center = (100, SCREEN_HEIGHT - 75)
    ship_button.center = ((SCREEN_WIDTH / 2), 255)
    laser_button.center = ((SCREEN_WIDTH / 2), 400)
    money_button.center = ((SCREEN_WIDTH / 2), 545)
    return exit_button, ship_button, laser_button, money_button
exit_button, ship_button, laser_button, money_button = home_buttons()
def home_draw(screen, mouse_pos, title_font, subtitle_font, text_font):

    back_but_copy = exit_button.copy()
    ship_but_copy = ship_button.copy()
    laser_but_copy = laser_button.copy()
    money_but_copy = money_button.copy()


    back_colour = ACCENT_RED
    ship_colour = ACCENT_PURPLE
    laser_colour = ACCENT_PURPLE
    money_colour = ACCENT_PURPLE

    if exit_button.collidepoint(mouse_pos):
        back_colour = ACCENT_RED_HOVER
        back_but_copy = exit_button.inflate(-3, -1)
    if ship_button.collidepoint(mouse_pos):
        ship_colour = ACCENT_PURPLE_HOVER
        ship_but_copy = ship_button.inflate(-7, -3)
    if laser_button.collidepoint(mouse_pos):
        laser_colour = ACCENT_PURPLE_HOVER
        laser_but_copy = laser_button.inflate(-7, -3)
    if money_button.collidepoint(mouse_pos):
        money_colour = ACCENT_PURPLE_HOVER
        money_but_copy = money_button.inflate(-7, -3)

    pg.draw.rect(screen, back_colour, back_but_copy, border_radius=10)
    pg.draw.rect(screen, ship_colour, ship_but_copy, border_radius=15)
    pg.draw.rect(screen, laser_colour, laser_but_copy, border_radius=15)
    pg.draw.rect(screen, money_colour, money_but_copy, border_radius=15)

    title = title_font.render("GARAGE", True, ACCENT_LIGHTBLUE)
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

def create_back_button():
    back_button = pg.Rect(0, 0, 150, 50)
    back_button.center = (100, SCREEN_HEIGHT - 75)

    return back_button
back_button = create_back_button()
def upgrade_page_draw(screen, selected_category, mouse_pos, upgrade_data, upgrades, title_font, subtitle_font, text_font, player):
    category_data = upgrade_data[selected_category]

    #draw title
    titleText = title_font.render(category_data["title"], True, ACCENT_LIGHTBLUE)
    title_rect = titleText.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(titleText, title_rect)


    #back button
    back_button_copy = back_button.copy()

    backColour = (204, 57, 47)
    if back_button.collidepoint(mouse_pos):
        backColour = (173, 44, 35)
        back_button_copy = back_button.inflate(-3, -1)

    pg.draw.rect(screen, backColour, back_button_copy, border_radius=10)

    backText = text_font.render("Back", True, BLACK)
    backText_rect = backText.get_rect(center=back_button.center)
    screen.blit(backText, backText_rect)

    y = 180
    x = 60
    buy_buttons = []

    #buyText = "Buy"
    #buyColour = (60, 220, 100)


    for upgrade_key, upgrade in category_data["upgrades"].items():
        buyText = "Buy"
        buyColour = (60, 220, 100)

        level = upgrades[upgrade["level_key"]]
        values = upgrade["values"]
        costs = upgrade["costs"]
        current_value = values[level]

        # draw blocks for upgrades to go over
        card_rect = pg.Rect(x, y - 32, 520, 184)
        pg.draw.rect(screen, PANEL_SCIFI, card_rect, border_radius=12)
        pg.draw.rect(screen, PANEL_SCIFI_BORDER, card_rect, width=2, border_radius=12)

        nameText = subtitle_font.render(upgrade["name"], True, ACCENT_TURQUOISE)
        nameText_rect = nameText.get_rect(topleft=(x + 40, y))
        screen.blit(nameText, nameText_rect)

        currentText = text_font.render(f"Current: {current_value}", True, WHITE)
        currentText_rect = currentText.get_rect(topleft=(x + 40, y + 40))
        screen.blit(currentText, currentText_rect)

        if level < len(values) - 1:
            next_value = values[level + 1]

            nextText = text_font.render(f"Next: {next_value}", True, ACCENT_GREEN)
            nextText_rect = nextText.get_rect(topleft=(x + 40, y + 67))
            screen.blit(nextText, nextText_rect)

            cost = costs[level]

            costText = text_font.render(f"Cost: {cost}", True, ACCENT_YELLOW)
            costText_rect = costText.get_rect(topleft=(x + 40, y + 97))
            screen.blit(costText, costText_rect)
            if player["coins"] < cost:
                buyColour = GREY

        else:
            maxText = text_font.render("MAX LEVEL", True, ACCENT_RED)
            maxText_rect = maxText.get_rect(topleft=(x + 40, y + 65))
            screen.blit(maxText, maxText_rect)
            buyText = "MAX"
            buyColour = DISABLED

        buy_button = pg.Rect(0, 0, 80, 35)
        buy_button.center = (x + 440, y + 97)

        if buy_button.collidepoint(mouse_pos) and buyColour == (60, 220, 100):
            buyColour = (40, 180, 80)
            buy_button.inflate_ip(-1, -0.33)

        pg.draw.rect(screen, buyColour, buy_button, border_radius=5)

        buy_text = text_font.render(buyText, True, BLACK)
        screen.blit(buy_text, buy_text.get_rect(center=buy_button.center))

        if y == 450:
            y = 180
            x = 620
        else:
            y = 450
        button_data = {
            "rect": buy_button,
            "data": upgrade
        }
        buy_buttons.append(button_data)

    return buy_buttons


def draw_garage(screen, selected_category, mouse_pos, upgrade_data, upgrades, title_font, subtitle_font, text_font, garageTextFunc, player):

    screen.fill((15, 15, 30))

    buy_buttons = []

    if selected_category == "home":
        home_draw(screen, mouse_pos, title_font, subtitle_font, text_font)
    else:
        buy_buttons = upgrade_page_draw(screen, selected_category, mouse_pos, upgrade_data, upgrades, title_font, subtitle_font, text_font, player)

    garageTextFunc()

    return buy_buttons

def handle_garage_events(event, buy_buttons, upgrade_data, upgrades, player):
    global selected_category
    if event.type == pg.MOUSEBUTTONDOWN:
        if selected_category == "home":
            if exit_button.collidepoint(event.pos):
                return "menu"
            elif ship_button.collidepoint(event.pos):
                selected_category = "ship"
            elif laser_button.collidepoint(event.pos):
                selected_category = "laser"
            elif money_button.collidepoint(event.pos):
                selected_category = "money"
        else:
            # back button
            if back_button.collidepoint(event.pos):
                    selected_category = "home"
            # buy buttons
            for button in buy_buttons:
                if button["rect"].collidepoint(event.pos):
                    upgrade = button["data"]

                    level = upgrades[upgrade["level_key"]]

                    if level < len(upgrade["values"]) - 1:

                        cost = upgrade["costs"][level]

                        if player["coins"] >= cost:
                            player["coins"] -= cost
                            upgrades[upgrade["level_key"]] += 1

                            return "updateUpgrades"
    return None