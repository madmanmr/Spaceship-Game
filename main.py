'''
    24/06/26
    started new game that I will be working on for a while to improve more skills. As of now my idea is to have a spaceship survival type game.
    A spaceship of choice will spawn in the centre of the screen while playing. Asteroids will spawn randomly around it. They will be moving and if they hit the spaceship,
    game over. You get points for shooting asteroids.

'''

#imports
import pygame as pg
import numpy as np

from Spaceship import Ship1
from settings import *
from asteroids import Asteroid
from lasers import Laser

from Screens import menu, level_select, garage, playing, game_over

#basics
pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
keys = pg.key.get_pressed()

title_font = pg.font.SysFont("bahnschrift", 80, bold=True)
subtitle_font = pg.font.SysFont("bahnschrift", 45, bold=True)
text_font = pg.font.SysFont("consolas", 30)
small_font = pg.font.SysFont("segoe ui", 22)

print(pg.font.get_fonts())
# states
MENU = "menu"
LEVEL_SELECT = "level selection"
GARAGE = "upgrade choice"
PLAYING = "playing"
GAME_OVER = "game over"

state = MENU

lose = False


# game things
ship = Ship1(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

asteroids = []
laser = []
buy_buttons = []

# player
player = {
    "health": 100,
    "coins": 0
}
# game
game = {
    "hitCooldown": 0,
    "shootCooldown": 0,
    "coinsChangeYes": 0,
    "asteroidCount": 0,
    "asteroidsSpawned": 0,
    "asteroidCountMax": 0,
    "asteroidSpawnTimer": 0,
    "asteroidsLeft": 0
}
# level
level = 1

# upgrades pass to garage
upgrades = {
    "healthUpgrade": 0,

    "laserSpeedUpgrade": 0,
    "fireRateUpgrade": 0,
    "laserDamageUpgrade": 0,

    "coinUpgrade": 0
}

#upgrade lists
#have all of the data used in garage stored here now so i only need 1 draw function in garage
#add upgrades here in future
upgrade_data = {
    "ship": {
        "title": "Ship Upgrades",
        "button": "Ship",
        "upgrades": {
            "max_health": {
                "name": "Increase Health",
                "level_key": "healthUpgrade",
                "values": [100,125,150,175,200],
                "costs": [100,150,200,300]
            }
        }
    },

    "laser": {
        "title": "Laser Upgrades",
        "button": "Laser",
        "upgrades": {
            "laser_speed": {
                "name": "Laser Speed",
                "level_key": "laserSpeedUpgrade",
                "values": [10,15,20,25],
                "costs": [150,200,300]
            },
            "fire_rate": {
                "name": "Fire Rate",
                "level_key": "fireRateUpgrade",
                "values": [60,30,15,6,3],
                "costs": [150,200,400,750]
            },
            "laser_damage": {
                "name": "Laser Damage",
                "level_key": "laserDamageUpgrade",
                "values": [1,2,3,4,5],
                "costs": [500,750,1100,1500]
            }
        }
    },

    "money": {
        "title": "Economic Upgrades",
        "button": "Money",
        "upgrades": {
            "coin_reward": {
                "name": "Earn More Coins",
                "level_key": "coinUpgrade",
                "values": [1,1.25,1.5,2,3],
                "costs": [100,150,250,400]
            }
        }
    }
}

# calculated upgrade values
healthMax = upgrade_data["ship"]["upgrades"]["max_health"]["values"][upgrades["healthUpgrade"]]

laserSpeedCalc = upgrade_data["laser"]["upgrades"]["laser_speed"]["values"][upgrades["laserSpeedUpgrade"]]
fireRateCalc = upgrade_data["laser"]["upgrades"]["fire_rate"]["values"][upgrades["fireRateUpgrade"]]
laserDamageCalc = upgrade_data["laser"]["upgrades"]["laser_damage"]["values"][upgrades["laserDamageUpgrade"]]

coinRewardMultiplierCalc = upgrade_data["money"]["upgrades"]["coin_reward"]["values"][upgrades["coinUpgrade"]]

#level values
levelDamage = [10, 20, 50, 100, 150, 200]
asteroidSpeedMax = [10, 15, 20, 30, 45, 60]
asteroidSpeedMin = [5, 8, 15, 20, 35, 45]
asteroidSpawnInterval = [180, 120, 60, 30, 15, 6]
backgroundColour = [ # used gpt to expand colours
    (15, 15, 30),   # Level 1
    (36, 29, 58),   # Level 2 (between 1 & 3)
    (58, 43, 87),   # Level 3
    (69, 43, 92),   # Level 4 (between 3 & 5)
    (79, 43, 97),   # Level 5
    (100, 43, 110)  # Level 6 (slightly more vibrant)
]
coinLevelReward = [100, 300, 500, 750, 1000, 1500]

#calculate level values
damage = levelDamage[level - 1]
asteroidCalcMax = asteroidSpeedMax[level - 1]
asteroidCalcMin = asteroidSpeedMin[level - 1]
asteroidSpawnIntervalCalc = asteroidSpawnInterval[level -1]
backgroundColourCalc = backgroundColour[level - 1]
coinLevelRewardCalc = coinLevelReward[level - 1]

#funcs
#calc all different vals for start of each level
def set_level_values():
    global damage, asteroidCalcMax, asteroidCalcMin, asteroidSpawnIntervalCalc, backgroundColourCalc, coinLevelRewardCalc

    damage = levelDamage[level - 1]
    asteroidCalcMax = asteroidSpeedMax[level - 1]
    asteroidCalcMin = asteroidSpeedMin[level - 1]
    asteroidSpawnIntervalCalc = asteroidSpawnInterval[level - 1]
    backgroundColourCalc = backgroundColour[level - 1]
    coinLevelRewardCalc = coinLevelReward[level - 1]

#calc vals of upgrades before level starts
def set_upgrade_values():
    global healthMax, laserSpeedCalc, fireRateCalc, coinRewardMultiplierCalc, laserDamageCalc

    healthMax = upgrade_data["ship"]["upgrades"]["max_health"]["values"][upgrades["healthUpgrade"]]

    laserSpeedCalc = upgrade_data["laser"]["upgrades"]["laser_speed"]["values"][upgrades["laserSpeedUpgrade"]]
    fireRateCalc = upgrade_data["laser"]["upgrades"]["fire_rate"]["values"][upgrades["fireRateUpgrade"]]
    laserDamageCalc = upgrade_data["laser"]["upgrades"]["laser_damage"]["values"][upgrades["laserDamageUpgrade"]]

    coinRewardMultiplierCalc = upgrade_data["money"]["upgrades"]["coin_reward"]["values"][upgrades["coinUpgrade"]]

#creat number of asteroids
def create_asteroids():
    x = 100
    y = np.random.randint(0, SCREEN_HEIGHT)

    asteroid = Asteroid(x, y)

    asteroid.angle = np.radians(np.random.randint(-20, 21))
    asteroid.speed = np.random.randint(asteroidCalcMin, asteroidCalcMax)

    asteroids.append(asteroid)

#move ship to centre and stop
def reset_ship():

    ship.x = SCREEN_WIDTH // 2
    ship.y = SCREEN_HEIGHT // 2

    ship.speed_x = 0
    ship.speed_y = 0

#start x level using vals set earlier
def start_level(selected_level):

    global level, state, lose

    level = selected_level

    player["health"] = healthMax

    game["coinsChangeYes"] = 0
    game["hitCooldown"] = 0

    # asteroid spawning setup
    game["asteroidsSpawned"] = 0
    game["asteroidCount"] = 0
    game["asteroidCountMax"] = level * 5
    game["asteroidSpawnTimer"] = asteroidSpawnIntervalCalc
    game["asteroidsLeft"] = game["asteroidCountMax"]

    lose = False

    laser.clear()
    asteroids.clear()

    reset_ship()
    set_level_values()
    set_upgrade_values()

    state = PLAYING

#for when game is done and want to play again with same level vars
def start_new_game():

    start_level(level)

#text on screen while playing
def playingTextFunc():
    level_text = subtitle_font.render(f"{level}", True, WHITE)
    coinsOwn_text = text_font.render(f"Coins: {player["coins"]}", True, ACCENT_YELLOW)
    asteroidsLeft_text = text_font.render(f"Asteroids left: {game["asteroidsLeft"]}", True, WHITE)
    health_text = text_font.render(f"Health: {player["health"]}", True, WHITE)

    screen.blit(level_text, ((SCREEN_WIDTH / 2), 20))
    screen.blit(coinsOwn_text, (20, 20))
    screen.blit(asteroidsLeft_text, (20, 75))
    screen.blit(health_text, (20, 110))

#garage texas
def garageTextFunc():
    coinsOwn_text = text_font.render(f"Coins: {player['coins']}", True, ACCENT_YELLOW)

    screen.blit(coinsOwn_text, (20, 20))

#text when game done
def gameOverTextFunc():
    coinsOwn_text = text_font.render(f"Coins: {player['coins']}", True, ACCENT_YELLOW)
    win_text = title_font.render("YOU WIN!", True, WHITE)
    lose_text = title_font.render("YOU LOSE!", True, WHITE)

    TextRect = win_text.get_rect(center=(SCREEN_WIDTH // 2, 150))

    if lose:
        screen.blit(lose_text, TextRect)
        reward = coinLevelRewardCalc * coinRewardMultiplierCalc / 5
    else:
        screen.blit(win_text, TextRect)
        reward = coinLevelRewardCalc * coinRewardMultiplierCalc

    if game["coinsChangeYes"] == 0:
        game["coinsChangeYes"] += 1
        player["coins"] += reward
    screen.blit(coinsOwn_text, (20, 20))

#move spaceship
def spaceshipmainfunc():
    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
        ship.rotate_left()
    if keys[pg.K_d]:
        ship.rotate_right()
    if keys[pg.K_w]:
        ship.thrust()

    if ship.x >= SCREEN_WIDTH:
        ship.x = SCREEN_WIDTH
        ship.bounce_x()
    if ship.x <= 0:
        ship.x = 0
        ship.bounce_x()

    if ship.y >= SCREEN_HEIGHT:
        ship.y = SCREEN_HEIGHT
        ship.bounce_y()
    if ship.y <= 0:
        ship.y = 0
        ship.bounce_y()

    ship.update()

#,ove lasers
def lasermainfunc():
    keys = pg.key.get_pressed()

    for laser_obj in laser[:]:
        laser_obj.update()

        #if laser_obj.off_screen: #saves potatoes
            #laser.remove(laser_obj)

    if keys[pg.K_SPACE] and game["shootCooldown"] <= 0:
        laser.append(Laser(
            ship.x + np.cos(ship.angle) * ship.length,
            ship.y + np.sin(ship.angle) * ship.length,
            ship.angle,
            laserSpeedCalc
        ))
        game["shootCooldown"] = fireRateCalc

    if game["shootCooldown"] > 0:
        game["shootCooldown"] -= 1

#detect collision with laser and asteroid and move asteroids
def asteroidsmainfunc():
    #asteroid spawning
    if game["asteroidsSpawned"] < game["asteroidCountMax"]:
        if game["asteroidSpawnTimer"] > 0:
            game["asteroidSpawnTimer"] -= 1
        else:
            create_asteroids()
            game["asteroidsSpawned"] += 1
            game["asteroidCount"] += 1
            game["asteroidSpawnTimer"] = asteroidSpawnIntervalCalc

    for asteroid in asteroids[:]:
        asteroid.update()

        destroyed = False

        for laser_obj in laser[:]:
            for point in laser_obj.points:
                dx = point[0] - asteroid.x
                dy = point[1] - asteroid.y

                distance = np.sqrt(dx ** 2 + dy ** 2)

                if distance <= asteroid.radius:
                    asteroids.remove(asteroid)
                    laser.remove(laser_obj)

                    game["asteroidCount"] = len(asteroids)
                    game["asteroidsLeft"] -= 1
                    destroyed = True
                    break

            if destroyed:
                break

        if destroyed:
            continue

        if asteroid.x > SCREEN_WIDTH:
            asteroid.x = 0
        elif asteroid.x < 0:
            asteroid.x = SCREEN_WIDTH
        if asteroid.y > SCREEN_HEIGHT or asteroid.y < 0:
            asteroid.angle = -asteroid.angle

#change health when hit and change gamemode when health == 0
def healthmainfunc():
    global state, lose

    if game["hitCooldown"] > 0:
        game["hitCooldown"] -= 1

    for asteroid in asteroids:
        dx = ship.x - asteroid.x
        dy = ship.y - asteroid.y
        distance = np.sqrt(dx ** 2 + dy ** 2)

        if distance < ship.length + asteroid.radius and game["hitCooldown"] == 0:
            player["health"] -= damage
            game["hitCooldown"] = 60

            if player["health"] <= 0:
                state = GAME_OVER
                lose = True

running = True
while running:
    clock.tick(60)

    mouse_pos = pg.mouse.get_pos()

    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif state == MENU:
            new_state = menu.handle_menu_events(event)

            if new_state is not None:
                state = new_state

        elif state == LEVEL_SELECT:
            new_state, selected_level = (level_select.handle_level_selection_events(event, levelButtons))

            if selected_level is not None:
                start_level(selected_level)

            elif new_state is not None:
                state = new_state


        elif state == GARAGE:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    player["coins"] = 5000

            new_state = garage.handle_garage_events(event, buy_buttons, upgrade_data, upgrades, player)

            if new_state  == "updateUpgrades":
                set_upgrade_values()
            elif new_state is not None:
                state = new_state

        elif state == PLAYING:
            new_state = playing.handle_game_events(event, game)

            if new_state is not None:
                state = new_state

        elif state == GAME_OVER:
            action = game_over.handle_game_over_events(event)

            if action == "new_game":
                start_new_game()

            elif action == "menu":
                state = MENU

    if state == MENU:
        menu.draw_menu(screen, mouse_pos, title_font, subtitle_font)

    elif state == LEVEL_SELECT:
        levelButtons = level_select.draw_level_selection(screen, mouse_pos, title_font, text_font)

    elif state == GARAGE:
        buy_buttons = garage.draw_garage(screen, garage.selected_category, mouse_pos, upgrade_data, upgrades, title_font, subtitle_font, text_font, garageTextFunc, player)

    elif state == PLAYING:
        playing.update_game(screen,backgroundColourCalc,spaceshipmainfunc,asteroidsmainfunc,lasermainfunc,healthmainfunc)

        playing.draw_game(screen,ship,asteroids,laser,playingTextFunc)

    elif state == GAME_OVER:
        game_over.draw_game_over(screen, mouse_pos, text_font, gameOverTextFunc)

    pg.display.flip()

pg.quit()