import pygame as pg
import numpy as np

class Star:

	def __init__(self, x, y, depth):
		self.x = x
		self.y = y
		self.depth = depth

		self.base_size = 5.5 + self.depth * 3
		self.current_size = self.base_size

		self.angle = 0

		self.speed =  0.1 + self.depth * 0.6
		self.max_brightness =  130 + self.depth * 125 #max 255 min 100 + 155 * 0.2

		self.twinkle_timer = 0
		self.twinkle_direction = 1
		self.twinkle_speed = np.random.uniform(1.0, 1.5)

		self.points = []

	def update(self):
		self.x += np.cos(self.angle) * self.speed
		self.y += np.sin(self.angle) * self.speed


	def get_points(self):
		half_size = self.base_size / 2

		left = (self.x - half_size, self.y)
		right = (self.x + half_size, self.y)
		top = (self.x, self.y - half_size)
		bottom = (self.x, self.y + half_size)

		left_top = (self.x - half_size/4, self.y - half_size/4)
		right_top = (self.x + half_size/4, self.y - half_size/4)
		left_bottom = (self.x - half_size/4, self.y + half_size/4)
		right_bottom = (self.x + half_size/4, self.y + half_size/4)

		return [
			left,
			left_top,
			top,
			right_top,
			right,
			right_bottom,
			bottom,
			left_bottom
		]


	def draw(self, screen):
		brightness = int(self.max_brightness)

		glowRect = pg.Rect(0, 0, 4, 4)
		glowRect.center = (self.x, self.y)
		pg.draw.rect(screen, (200, 200, 20), glowRect)

		self.points = self.get_points()
		pg.draw.polygon(screen, (brightness,brightness,brightness), self.points)
