import pygame as pg
import numpy as np

class Star:
	size = 3

	def __init__(self, x, y, depth):
		self.x = x
		self.y = y
		self.depth = depth

		self.base_size = 2 + self.depth * 4
		self.current_size = self.base_size

		self.angle = 0

		self.speed =  0.3 + self.depth * 1.1
		self.max_brightness =  100 + self.depth * 155 #max 255 min 100 + 155 * 0.2

		self.twinkle_timer = 0
		self.twinkle_direction = 1
		self.twinkle_speed = np.random.uniform(1.0, 1.5)

		self.points = []

	def update(self):
		self.x += np.cos(self.angle) * self.speed
		self.y += np.sin(self.angle) * self.speed


	def get_points(self):
		half_size = self.size / 2

		left_x = self.x - half_size
		left_y = self.y

		top_x = self.x
		top_y = self.y - half_size

		return [
			(left_x, left_y),
			(top_x, top_y),
			(left_x + self.size, left_y),
			(top_x, top_y + self.size),
		]


	def draw(self, screen):
		glowRect = pg.Rect(0, 0, 3, 3)
		glowRect.center = (self.x, self.y)
		pg.draw.rect(screen, (200, 200, 20), glowRect)

		self.points = self.get_points()
		pg.draw.polygon(screen, (255,255,255), self.points)
