import pygame as pg
import numpy as np

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed_x = np.random.randint(1, 10)
        self.speed_y = np.random.randint(1, 10)
        self.radius = 10
    def move(self):
        self.speed_x += np.cos(self.angle) * 0.2
        self.speed_y += np.sin(self.angle) * 0.2
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
    def draw(self, screen):
        pg.draw.circle(screen,(158, 73, 8),(self.x,self.y),self.radius )