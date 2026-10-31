Spaceship Shooter

A Python/Pygame asteroid survival game. Pilot a ship, destroy asteroids, and try to complete the selected level before collisions drain your health. Coins earned at the end of a run can be spent on ship, laser, economy, and health upgrades in the garage.


## Controls

| Input | Action |
| --- | --- |
| **A** | Turn left |
| **D** | Turn right |
| **W** | Thrust forward |
| **S** | Apply reverse thrust |
| **Space** | Fire a laser in the direction the ship is facing |
| **Esc** | Toggle pause while playing |
| Mouse click | Choose **Resume** or **Exit** on the pause screen |

The main menu, level selection, and garage also receive input events, but their handlers were not included in the available files. Their exact controls need confirmation.

### Debug shortcut

While the garage is open, **P** sets the player's coin balance to 5,000. 

## How a run works

1. Choose a level and start a run. The ship is placed in the middle of the screen with its health set to the current maximum-health upgrade value.
2. Asteroids spawn from the left edge at random heights. They move across the screen; they wrap around horizontally and bounce at the top and bottom edges.
3. Steer, accelerate or reverse, and shoot asteroids. Destroying an asteroid reduces the level's remaining-asteroid count.
4. Asteroid collisions reduce health. The game applies a 60-frame hit cooldown between collision damage events. Health regeneration is also applied during play.
5. The game has a win/loss screen and awards coins when a run ends. For a run to end you must destroy all of the asteroids or lose all of your health, (win/lose)

The main loop is configured for 60 frames per second. Each level schedules five asteroids per level number, for up to 30 asteroids at level 6.

## Levels and rewards

| Level | Asteroids scheduled | Damage per collision hit | Configured spawn interval | Base coins for a win |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 5 | 10 | 100 frames | 100 |
| 2 | 10 | 20 | 100 frames | 300 |
| 3 | 15 | 50 | 60 frames | 500 |
| 4 | 20 | 100 | 30 frames | 750 |
| 5 | 25 | 150 | 15 frames | 1,000 |
| 6 | 30 | 200 | 6 frames | 1,500 |

The configured asteroid health and speed also increase with level. The spawn interval is measured in frames; at the configured 60 FPS, shorter intervals mean more frequent spawns. The first spawn countdown may use the previously active level's interval because the main file initializes that timer before refreshing the selected level's settings.

The end-of-run coin reward uses the selected level's base reward and the coin-reward upgrade multiplier. A loss pays one-fifth of the base reward before that multiplier is applied. The supplied main file awards this currency at the end of a run; it does not implement a points-per-asteroid score.

## Garage upgrades

Upgrade values and purchase costs are configured in the main game file. Costs below are listed in purchase order, starting from the default upgrade level.

| Category | Upgrade | Configured values by level | Purchase costs |
| --- | --- | --- | --- |
| Ship | Turn speed | 2.5, 3.5, 5, 6.5 | 150, 200, 300 |
| Ship | Thrust | 0.2, 0.3, 0.4, 0.5, 0.7 | 150, 200, 300, 450 |
| Ship | Reverse thrust | 0.1, 0.2, 0.3, 0.4, 0.5 | 100, 150, 250, 350 |
| Laser | Laser speed | 10, 15, 20, 25 | 150, 200, 300 |
| Laser | Fire-rate cooldown (frames; lower is faster) | 60, 30, 15, 6, 3 | 150, 200, 400, 750 |
| Laser | Laser damage | 1, 2, 3, 4, 5 | 500, 750, 1,100, 1,500 |
| Money | Coin reward multiplier | 1×, 1.25×, 1.5×, 2×, 3× | 100, 150, 250, 400 |
| Health | Maximum health | 100, 125, 150, 175, 200 | 100, 150, 200, 300 |
| Health | Regeneration setting | 1, 2, 3, 5, 15 | 100, 250, 400, 600 |

The main file adds the regeneration setting divided by 60 on each game-loop frame, which is intended to represent health per second at 60 FPS. However, the supplied code currently looks up this setting using the maximum-health upgrade index instead of the regeneration upgrade index. As a result, the regeneration upgrade may not work as intended until that lookup is corrected and verified.

## Screens

The main game file defines these states:

- **Menu** — starting screen.
- **Level selection** — choose a level from 1 to 6.
- **Garage** — browse and purchase upgrades.
- **Playing** — control the ship and fight asteroids.
- **Game over** — shows a win or loss result and the coin balance; the imported handler also exposes a new-game action and a return-to-menu action.
- **Pause overlay** — shown during a run, with Resume and Exit buttons.


## Requirements

- Python 3.12 or newer. The supplied main file reuses the outer f-string's double quotes inside expressions, syntax enabled in Python 3.12 ([official Python documentation](https://docs.python.org/3.12/whatsnew/3.12.html#pep-701-syntactic-formalization-of-f-strings)).
- Pygame
- NumPy

Install the imported third-party packages with:

```bash
python -m pip install pygame numpy
```

No dependency file or pinned package versions were present in the available project files.

## Run the game

Run the main game script from the project folder—the folder that contains `settings.py`, `Spaceship.py`, `asteroids.py`, `lasers.py`, `stars.py`, and the `Screens` package:

```bash
python <main-game-file>.py
```

Replace `<main-game-file>.py` with the actual entry-point filename. That filename was not available in the supplied files. The modules imported by the main file include `Screens.menu`, `Screens.level_select`, `Screens.garage`, `Screens.playing`, and `Screens.game_over`.

