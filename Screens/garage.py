import pygame as pg

from settings import *

selected_category = "home"

def home_buttons():
    exit_button = pg.Rect(0, 0, 70, 50)
    ship_button = pg.Rect(0, 0, 220, 70)
    laser_button = pg.Rect(0, 0, 220, 70)
    money_button = pg.Rect(0, 0, 220, 70)
    health_button = pg.Rect(0, 0, 220, 70)

    exit_button.center = (265, 392.5)
    ship_button.center = (450, 338.75)
    laser_button.center = (750, 338.75)
    money_button.center = (450, 556.25)
    health_button.center = (750, 556.25)
    return exit_button, ship_button, laser_button, money_button, health_button
exit_button, ship_button, laser_button, money_button, health_button = home_buttons()

def draw_home_interior(screen):
    # CEILING ###########################################################

    top_LighterPoints = [
        (0, 0),
        (300.366, 220),
        (SCREEN_WIDTH - 300.366, 220),
        (SCREEN_WIDTH, 0)
    ]
    pg.draw.polygon(screen, GREY, top_LighterPoints)

    topDarkLine = [
        (80, 106),
        (SCREEN_WIDTH - 80, 106),
        (SCREEN_WIDTH - 83, 114),
        (83, 114)
    ]
    pg.draw.polygon(screen, DARK_GREY, topDarkLine)

    topLeftHighlight = [
        (0, 0),
        (15.366, 0),
        (300.366, 220),
        (285, 220)
    ]
    topRightHighlight = [
        (SCREEN_WIDTH, 0),
        (SCREEN_WIDTH - 15.366, 0),
        (SCREEN_WIDTH - 300.366, 220),
        (SCREEN_WIDTH - 285, 220)
    ]
    pg.draw.polygon(screen, LIGHT_GREY, topLeftHighlight)
    pg.draw.polygon(screen, LIGHT_GREY, topRightHighlight)

    # WINDOWS ##############################################################

    greyWindowPointsL = [
        (0, 0),
        (0, 65),
        (230, 264),
        (157, 527),
        (0, 613),
        (0, 800),
        (285, 665),
        (285, 220)
    ]

    greyWindowPointsR = [
        (SCREEN_WIDTH - 0, 0),
        (SCREEN_WIDTH - 0, 65),
        (SCREEN_WIDTH - 230, 264),
        (SCREEN_WIDTH - 157, 527),
        (SCREEN_WIDTH - 0, 613),
        (SCREEN_WIDTH - 0, 800),
        (SCREEN_WIDTH - 285, 665),
    (SCREEN_WIDTH - 285, 220)
    ]

    pg.draw.polygon(screen, GREY, greyWindowPointsL)
    pg.draw.polygon(screen, GREY, greyWindowPointsR)

    # DARK WINDOW FRAMES

    darkStripL = [
        (0, 79),
        (218, 268),
        (145, 520),
        (0, 600),
        (0, 570),
        (123, 502),
        (188, 277),
        (0, 113)
    ]

    darkStripR = [
        (SCREEN_WIDTH, 79),
        (SCREEN_WIDTH - 218, 268),
        (SCREEN_WIDTH - 145, 520),
        (SCREEN_WIDTH, 600),
        (SCREEN_WIDTH, 570),
        (SCREEN_WIDTH - 123, 502),
        (SCREEN_WIDTH - 188, 277),
        (SCREEN_WIDTH, 113)
    ]

    pg.draw.polygon(screen, DARK_GREY, darkStripL)
    pg.draw.polygon(screen, DARK_GREY, darkStripR)

    # LIGHT GREY HIGHLIGHTS ON THE GREY WALL

    highlightL = [
        (0, 79),
        (218, 268),
        (145, 520),
        (0, 600),
        (0, 613),
        (157, 527),
        (230, 264),
        (0, 65)
    ]

    highlightR = [
        (SCREEN_WIDTH - 0, 79),
        (SCREEN_WIDTH - 218, 268),
        (SCREEN_WIDTH - 145, 520),
        (SCREEN_WIDTH - 0, 600),
        (SCREEN_WIDTH - 0, 613),
        (SCREEN_WIDTH - 157, 527),
        (SCREEN_WIDTH - 230, 264),
        (SCREEN_WIDTH - 0, 65)
    ]

    pg.draw.polygon(screen, LIGHT_GREY, highlightL)
    pg.draw.polygon(screen, LIGHT_GREY, highlightR)

    # WINDOW CREASE LINES

    # LEFT
    pg.draw.line(screen, DARK, (218, 268), (188, 277), 4)
    pg.draw.line(screen, DARK, (145, 520), (123, 502), 4)

    # RIGHT
    pg.draw.line(screen, DARK, (SCREEN_WIDTH - 218, 268), (SCREEN_WIDTH - 188, 277), 4)
    pg.draw.line(screen, DARK, (SCREEN_WIDTH - 145, 520), (SCREEN_WIDTH - 123, 502), 4)

    # VAULT ###############################################################

    darkLockerBack = [
        (285, 220),
        (SCREEN_WIDTH - 285, 220),
        (SCREEN_WIDTH - 285, 665),
        (285, 665)
    ]

    greyBack = [
        (300, 235),
        (SCREEN_WIDTH - 300, 235),
        (SCREEN_WIDTH - 300, 650),
        (300, 650)
    ]

    pg.draw.polygon(screen, DARK_GREY, darkLockerBack)
    pg.draw.polygon(screen, GREY, greyBack)

    vaultTopLeft = [
        (367.5, 235),
        (532.5, 235),
        (600, 302.5),
        (600, 375),
        (532.5, 442.5),
        (367.5, 442.5),
        (300, 375),
        (300, 302.5)
    ]

    vaultTopRight = [
        (667.5, 235),
        (832.5, 235),
        (900, 302.5),
        (900, 375),
        (832.5, 442.5),
        (667.5, 442.5),
        (600, 375),
        (600, 302.5)
    ]

    vaultBottomLeft = [
        (367.5, 442.5),
        (532.5, 442.5),
        (600, 510),
        (600, 582.5),
        (532.5, 650),
        (367.5, 650),
        (300, 582.5),
        (300, 510)
    ]

    vaultBottomRight = [
        (667.5, 442.5),
        (832.5, 442.5),
        (900, 510),
        (900, 582.5),
        (832.5, 650),
        (667.5, 650),
        (600, 582.5),
        (600, 510)
    ]

    pg.draw.polygon(screen, LIGHT_GREY, vaultTopLeft)
    pg.draw.polygon(screen, LIGHT_GREY, vaultTopRight)
    pg.draw.polygon(screen, LIGHT_GREY, vaultBottomLeft)
    pg.draw.polygon(screen, LIGHT_GREY, vaultBottomRight)

    # thick divider lines
    pg.draw.line(screen, GREY, (600, 235), (600, 650), 16)# vert
    pg.draw.line(screen, GREY, (300, 442.5), (900, 442.5), 16)#horz

    centreDiamond = [
        (600, 375),
        (667.5, 442.5),
        (600, 510),
        (532.5, 442.5)
    ]
    pg.draw.polygon(screen, GREY, centreDiamond)

    # Thin divider lines
    pg.draw.line(screen, DARK_GREY, (600, 235), (600, 650), 6)
    pg.draw.line(screen, DARK_GREY, (300, 442.5), (900, 442.5), 6)


    # Thick reinforcement lines
    pg.draw.line(screen, DARK_GREY, (600, 302.5), (600, 375), 11)#verts
    pg.draw.line(screen, DARK_GREY, (600, 510), (600, 582.5), 11)

    pg.draw.line(screen, DARK_GREY, (532.5, 442.5), (365, 442.5), 11)#horz
    pg.draw.line(screen, DARK_GREY, (667.5, 442.5), (835, 442.5), 11)

    # TITLE BOX ###########################################################

    topLightTitleBox = [
        ((SCREEN_WIDTH / 2) - 210, 110),
        ((SCREEN_WIDTH / 2) - 210, 210),
        ((SCREEN_WIDTH / 2) + 210, 210),
        ((SCREEN_WIDTH / 2) + 210, 110)
    ]
    topDarkTitleBox = [
        ((SCREEN_WIDTH / 2) - 200, 120),
        ((SCREEN_WIDTH / 2) - 200, 200),
        ((SCREEN_WIDTH / 2) + 200, 200),
        ((SCREEN_WIDTH / 2) + 200, 120)
    ]
    pg.draw.polygon(screen, LIGHT_GREY, topLightTitleBox)
    pg.draw.polygon(screen, DARK_GREY, topDarkTitleBox)

    # CONTROL PANELS #####################################################

    # Left panel - Exit
    exitPanel = [
        (215, 350),
        (245, 330),
        (295, 330),
        (315, 350),
        (315, 455),
        (295, 475),
        (245, 475),
        (215, 455)
    ]
    pg.draw.polygon(screen, DARK, exitPanel)
    pg.draw.polygon(screen, LIGHT_GREY, exitPanel, 5)

    # Exit button centre: (265, 392.5)

    # Right panel - Coin display
    coinPanel = [
        (SCREEN_WIDTH - 315, 350),
        (SCREEN_WIDTH - 295, 330),
        (SCREEN_WIDTH - 245, 330),
        (SCREEN_WIDTH - 215, 350),
        (SCREEN_WIDTH - 215, 455),
        (SCREEN_WIDTH - 245, 475),
        (SCREEN_WIDTH - 295, 475),
        (SCREEN_WIDTH - 315, 455)
    ]
    pg.draw.polygon(screen, DARK, coinPanel)
    pg.draw.polygon(screen, LIGHT_GREY, coinPanel, 5)

    pg.draw.rect(screen, (10, 25, 45), (SCREEN_WIDTH - 300, 367.5, 70, 50))
    pg.draw.rect(screen, ACCENT_LIGHTBLUE, (SCREEN_WIDTH - 300, 367.5, 70, 50), 3)



    pg.draw.circle(screen, (230, 170, 30), (SCREEN_WIDTH - 273, 392), 11)
    pg.draw.circle(screen, (255, 210, 70), (SCREEN_WIDTH - 273, 392), 8, 2)

    pg.draw.line(screen, ACCENT_LIGHTBLUE, (SCREEN_WIDTH - 280, 438), (SCREEN_WIDTH - 250, 438), 4)
    pg.draw.line(screen, ACCENT_LIGHTBLUE, (280, 438), (250, 438), 4)

    # FLOOR ###############################################################

    bottom_darkPoints = [
        (0, SCREEN_HEIGHT),
        (300, 650),
        (SCREEN_WIDTH - 300, 650),
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    ]
    pg.draw.polygon(screen, DARK_GREY, bottom_darkPoints)

    # Horizontal floor strips
    pg.draw.line(screen, DARK, (205, 700), (SCREEN_WIDTH - 205, 700), 5)
    pg.draw.line(screen, DARK, (90, 770), (SCREEN_WIDTH - 90, 770), 6)

    # Side floor highlights
    floorLeftHighlight = [
        (0, SCREEN_HEIGHT),
        (25, SCREEN_HEIGHT),
        (325, 650),
        (300, 650)
    ]
    floorRightHighlight = [
        (SCREEN_WIDTH, SCREEN_HEIGHT),
        (SCREEN_WIDTH - 25, SCREEN_HEIGHT),
        (SCREEN_WIDTH - 325, 650),
        (SCREEN_WIDTH - 300, 650)
    ]
    pg.draw.polygon(screen, LIGHT_GREY, floorLeftHighlight)
    pg.draw.polygon(screen, LIGHT_GREY, floorRightHighlight)

    # Floor centre strip
    pg.draw.polygon(screen, LIGHT_GREY, [
        (590, 650),
        (610, 650),
        (630, SCREEN_HEIGHT),
        (570, SCREEN_HEIGHT)
    ])
def home_draw(screen, mouse_pos, title_font, subtitle_font, text_font):

    draw_home_interior(screen) #interior design

    back_but_copy = exit_button.copy()
    ship_but_copy = ship_button.copy()
    laser_but_copy = laser_button.copy()
    money_but_copy = money_button.copy()
    health_button_copy = health_button.copy()


    back_colour = ACCENT_RED
    ship_colour = ACCENT_PURPLE
    laser_colour = ACCENT_PURPLE
    money_colour = ACCENT_PURPLE
    health_colour = ACCENT_PURPLE

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
    if health_button.collidepoint(mouse_pos):
        health_colour = ACCENT_PURPLE_HOVER
        health_button_copy = health_button.inflate(-7, -3)

    pg.draw.rect(screen, back_colour, back_but_copy, )
    pg.draw.rect(screen, ship_colour, ship_but_copy, )
    pg.draw.rect(screen, laser_colour, laser_but_copy, )
    pg.draw.rect(screen, money_colour, money_but_copy, )
    pg.draw.rect(screen, health_colour, health_button_copy, )

    title = title_font.render("GARAGE", True, ACCENT_LIGHTBLUE)
    exitText = text_font.render("Exit", True, WHITE)
    shipText = subtitle_font.render("Ship", True, WHITE)
    laserText = subtitle_font.render("Laser", True, WHITE)
    moneyText = subtitle_font.render("Money", True, WHITE)
    healthText = subtitle_font.render("Health", True, WHITE)

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 160))
    exit_rect = exitText.get_rect(center=exit_button.center)
    shipText_rect = shipText.get_rect(center=ship_button.center)
    laserText_rect = laserText.get_rect(center=laser_button.center)
    moneyText_rect = moneyText.get_rect(center=money_button.center)
    healthText_rect = healthText.get_rect(center=health_button.center)

    screen.blit(title, title_rect)
    screen.blit(exitText, exit_rect)
    screen.blit(shipText, shipText_rect)
    screen.blit(laserText, laserText_rect)
    screen.blit(moneyText, moneyText_rect)
    screen.blit(healthText, healthText_rect)

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
            maxText_rect = maxText.get_rect(topleft=(x + 40, y + 70))
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
            elif health_button.collidepoint(event.pos):
                selected_category = "health"
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