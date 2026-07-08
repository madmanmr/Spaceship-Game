import pygame as pg
import numpy as np

class Laser:
    length = 18
    width = 6

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 15

    def update(self):
        self.x += np.cos(self.angle) * self.speed
        self.y += np.sin(self.angle) * self.speed

    def draw(self, screen):
        half_width = self.width / 2

        front_x = self.x + np.cos(self.angle) * self.length
        front_y = self.y + np.sin(self.angle) * self.length

        back_x = self.x
        back_y = self.y

        offset_x = np.cos(self.angle + np.pi / 2) * half_width
        offset_y = np.sin(self.angle + np.pi / 2) * half_width

        point1 = (front_x + offset_x, front_y + offset_y)
        point2 = (front_x - offset_x, front_y - offset_y)
        point3 = (back_x - offset_x, back_y - offset_y)
        point4 = (back_x + offset_x, back_y + offset_y)

        pg.draw.polygon(screen, (114, 237, 223), [point1, point2, point3, point4])