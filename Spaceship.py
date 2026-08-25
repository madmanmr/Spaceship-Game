import pygame as pg
import numpy as np

class Ship1:
    length = 35
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

        self.speed_incr = 0.2
        self.turn_speed = 0.5
        self.drag = 0.99
        self.brake_incr = 0.1

        self.speed_x = 0
        self.speed_y = 0

    def rotate_left(self):
        self.angle -= np.radians(self.turn_speed)

    def rotate_right(self):
        self.angle += np.radians(self.turn_speed)

    def bounce_x(self):
        self.speed_x *= -1
        self.angle = np.arctan2(self.speed_y, self.speed_x)

    def bounce_y(self):
        self.speed_y *= -1
        self.angle = np.arctan2(self.speed_y, self.speed_x)

    def thrust(self):
        self.speed_x += self.speed_incr * np.cos(self.angle)
        self.speed_y += self.speed_incr * np.sin(self.angle)

    def reverse_thrust(self):
        self.speed_x -= self.brake_incr * np.cos(self.angle)
        self.speed_y -= self.brake_incr * np.sin(self.angle)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_x *= self.drag
        self.speed_y *= self.drag

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