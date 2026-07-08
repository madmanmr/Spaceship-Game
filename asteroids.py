import pygame as pg
import numpy as np

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0#np.radians(np.random.randint(-20, 21))
        self.speed = 0#np.random.randint(5, 10)
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 10
    def update(self):
        self.speed_x = self.speed * np.cos(self.angle)
        self.speed_y = self.speed * np.sin(self.angle)
        self.x += self.speed_x
        self.y += self.speed_y
    def draw(self, screen):
        pg.draw.circle(screen,(158, 73, 8),(self.x,self.y),self.radius )