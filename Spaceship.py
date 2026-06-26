import pygame as pg
import numpy as np

class Ship1:
    length = 35
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed_x = 0
        self.speed_y = 0

    def rotate_left(self):
        self.angle -= 0.08

    def rotate_right(self):
        self.angle += 0.08

    def bounce_x(self):
        self.speed_x *= -1
        self.angle = np.arctan2(self.speed_y, self.speed_x)

    def bounce_y(self):
        self.speed_y *= -1
        self.angle = np.arctan2(self.speed_y, self.speed_x)

    def thrust(self):
        self.speed_x += np.cos(self.angle) * 0.2
        self.speed_y += np.sin(self.angle) * 0.2

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_x *= 0.99
        self.speed_y *= 0.99

    def draw1(self, screen):
        length = 35

        front = (
            self.x + np.cos(self.angle) * length,
            self.y + np.sin(self.angle) * length
        )

        left = (
            self.x + np.cos(self.angle + 2.5) * length,
            self.y + np.sin(self.angle + 2.5) * length
        )

        right = (
            self.x + np.cos(self.angle - 2.5) * length,
            self.y + np.sin(self.angle - 2.5) * length
        )

        pg.draw.polygon(screen, (80, 220, 120), [front, left, right], 3)