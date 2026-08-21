import pygame as pg
import numpy as np

from settings import BLACK, ACCENT_GREEN


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

        self.speed = 0
        self.speed_x = 0
        self.speed_y = 0

        self.health = 0
        self.radius = 20

        self.shape_points = []

    def update(self):
        self.speed_x = self.speed * np.cos(self.angle)
        self.speed_y = self.speed * np.sin(self.angle)
        self.x += self.speed_x
        self.y += self.speed_y
        #self.radius = 20 + ((self.health - 1) * 5)

    def create_shape(self):
        asteroid_points = []
        crack_points = []

        # Create asteroid shape
        for i in range(10):
            angle = (360 / 10) * i
            angle += np.random.uniform(-10, 10)

            distance = self.radius * np.random.uniform(0.8, 1.1)

            x = np.cos(np.radians(angle)) * distance
            y = np.sin(np.radians(angle)) * distance

            asteroid_points.append((x, y))

        # Create ALL possible cracks
        for _ in range(6):
            angle = np.random.uniform(0, 360)

            start_distance = self.radius * np.random.uniform(0.1, 0.4)

            x1 = np.cos(np.radians(angle)) * start_distance
            y1 = np.sin(np.radians(angle)) * start_distance

            # First part of crack
            crack_length = self.radius * np.random.uniform(0.5, 1.0)

            x2 = x1 + np.cos(np.radians(angle)) * crack_length
            y2 = y1 + np.sin(np.radians(angle)) * crack_length

            # Second part points towards centre
            dx = -x2
            dy = -y2

            angle2 = np.degrees(np.arctan2(dy, dx))

            crack_length2 = self.radius * np.random.uniform(0.4, 0.8)

            x3 = x2 + np.cos(np.radians(angle2)) * crack_length2
            y3 = y2 + np.sin(np.radians(angle2)) * crack_length2

            crack_points.append({
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
                "x3": x3,
                "y3": y3
            })

        self.shape_points = asteroid_points
        self.crack_points = crack_points

    def draw(self, screen):

        # Draw asteroid
        asteroid_points = []

        for x, y in self.shape_points:
            asteroid_points.append((
                self.x + x,
                self.y + y
            ))

        pg.draw.polygon(
            screen,
            (158, 73, 8),
            asteroid_points
        )

        # Decide how many cracks to show
        crack_level = 6 - int(round(self.health / 2))

        # Draw only that many cracks
        for crack in self.crack_points[:crack_level]:
            x1 = self.x + crack["x1"]
            y1 = self.y + crack["y1"]

            x2 = self.x + crack["x2"]
            y2 = self.y + crack["y2"]

            x3 = self.x + crack["x3"]
            y3 = self.y + crack["y3"]

            pg.draw.line(
                screen,
                BLACK,
                (x1, y1),
                (x2, y2),
                width=2
            )

            pg.draw.line(
                screen,
                BLACK,
                (x2, y2),
                (x3, y3),
                width=2
            )