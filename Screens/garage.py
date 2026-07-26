import pygame as pg

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, YELLOW, LIGHTBLUE

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

def create_back_button():
    back_button = pg.Rect(0, 0, 150, 50)
    back_button.center = (100, SCREEN_HEIGHT - 75)

    return back_button
back_button = create_back_button()
def upgrade_page_draw(screen, selected_category, mouse_pos, upgrade_data, upgrades, title_font, subtitle_font, text_font):
    category_data = upgrade_data[selected_category]

    #draw title
    titleText = title_font.render(category_data["title"], True, WHITE)
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
    buy_buttons = []

    for upgrade_key, upgrade in category_data["upgrades"].items():
        level = upgrades[upgrade["level_key"]]
        values = upgrade["values"]
        costs = upgrade["costs"]
        current_value = values[level]

        nameText = subtitle_font.render(upgrade["name"], True, LIGHTBLUE)
        nameText_rect = nameText.get_rect(center=(200, y))
        screen.blit(nameText, nameText_rect)

        currentText = text_font.render(f"Current: {current_value}", True, WHITE)
        currentText_rect = currentText.get_rect(center=(200, y + 40))
        screen.blit(currentText, currentText_rect)

        if level < len(values) - 1:
            next_value = values[level + 1]

            nextText = text_font.render(f"Next: {next_value}", True, WHITE)
            nextText_rect = nextText.get_rect(center=(200, y + 67))
            screen.blit(nextText, nextText_rect)

            cost = costs[level]

            costText = text_font.render(f"Cost: {cost}", True, YELLOW)
            costText_rect = costText.get_rect(center=(200, y + 97))
            screen.blit(costText, costText_rect)

        else:
            maxText = text_font.render("MAX LEVEL", True, WHITE)
            maxText_rect = maxText.get_rect(center=(200, y + 65))
            screen.blit(maxText, maxText_rect)

        buy_button = pg.Rect(0, 0, 80, 35)
        buy_button.center = (500, y + 48.5)

        buyColour = (60, 220, 100)
        if buy_button.collidepoint(mouse_pos):
            buyColour = (40, 180, 80)
            buy_button.inflate_ip(-1, -0.33)

        pg.draw.rect(screen, buyColour, buy_button, border_radius=5)

        buy_text = text_font.render("Buy", True, BLACK)
        screen.blit(buy_text, buy_text.get_rect(center=buy_button.center))

        y += 140
        button_data = {
            "rect": buy_button,
            "data": upgrade
        }
        buy_buttons.append(button_data)

    return buy_buttons


def draw_garage(screen, selected_category, mouse_pos, upgrade_data, upgrades, title_font, subtitle_font, text_font, garageTextFunc):

    screen.fill((15, 15, 30))

    buy_buttons = []

    if selected_category == "home":
        home_draw(screen, mouse_pos, title_font, subtitle_font, text_font)
    else:
        buy_buttons = upgrade_page_draw(screen, selected_category, mouse_pos, upgrade_data, upgrades, title_font, subtitle_font, text_font)

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