import pygame as pg
import numpy as np

from settings import *



class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.angle = 0
        self.speed = 0
        self.speed_x = 0
        self.speed_y = 0

        self.max_health = 0
        self.health = 0
        self.radius = 20

        self.shape_points = []
        self.crack_points = []
        self.border_points = []

    def update(self):
        self.speed_x = self.speed * np.cos(self.angle)
        self.speed_y = self.speed * np.sin(self.angle)
        self.x += self.speed_x
        self.y += self.speed_y

    def create_shape(self):
        asteroid_points = []
        border_points = []
        num_vertices = 10

        for i in range(num_vertices):
            angle = (360 / num_vertices) * i + np.random.uniform(-8, 8)
            distance = self.radius * np.random.uniform(0.85, 1.15)
            distance2 = distance - 3 #border width
            x = np.cos(np.radians(angle)) * distance
            y = np.sin(np.radians(angle)) * distance
            x2 = np.cos(np.radians(angle)) * distance2
            y2 = np.sin(np.radians(angle)) * distance2
            asteroid_points.append((x, y))
            border_points.append((x2, y2))


        self.shape_points = asteroid_points
        self.border_points = border_points
        self.crack_points = []

        num_stems = 6
        crack_vertices = np.random.choice(len(asteroid_points), num_stems, replace=False)

        for crack_number in range(num_stems):
            n = crack_vertices[crack_number]

            x1 = asteroid_points[n][0]
            y1 = asteroid_points[n][1]

            centre_angle = np.degrees(np.arctan2(-y1, -x1))
            current_angle = centre_angle + np.random.uniform(-15, 15)

            segments = np.random.randint(4, 7)
            crack_length = self.radius + np.random.uniform(-1, 1)
            step_length = crack_length / segments

            current_x = x1
            current_y = y1

            segment_data = []

            for s in range(segments):
                current_angle += np.random.uniform(-20, 20)

                next_x = current_x + np.cos(np.radians(current_angle)) * step_length
                next_y = current_y + np.sin(np.radians(current_angle)) * step_length

                branch = [(current_x, current_y), (next_x, next_y)]

                twig = None

                if np.random.rand() < 0.3:
                    twig_angle = current_angle + np.random.choice([-45, 45])
                    twig_length = step_length * np.random.uniform(0.4, 0.7)

                    twig_end_x = next_x + np.cos(np.radians(twig_angle)) * twig_length
                    twig_end_y = next_y + np.sin(np.radians(twig_angle)) * twig_length

                    twig = [(next_x, next_y), (twig_end_x, twig_end_y)]

                segment_data.append({
                    "branch": branch,
                    "twig": twig
                })

                current_x = next_x
                current_y = next_y

            self.crack_points.append(segment_data)

    def draw(self, screen):
        world_points = [(self.x + x, self.y + y) for x, y in self.shape_points]
        world_points_border = [(self.x + x2, self.y + y2) for x2, y2 in self.border_points]

        pg.draw.polygon(screen, ASTEROID_CRACK, world_points)
        pg.draw.polygon(screen, ASTEROID, world_points_border)

        damage_taken = max(0, self.max_health - self.health)

        for stem in self.crack_points:
            segments_to_show = min(damage_taken, len(stem))

            for segment_number in range(segments_to_show):
                segment = stem[segment_number]

                branch = segment["branch"]

                branch_world = [
                    (self.x + point[0], self.y + point[1])
                    for point in branch
                ]

                pg.draw.line(
                    screen,
                    ASTEROID_CRACK,
                    branch_world[0],
                    branch_world[1],
                    width=3
                )

                if segment["twig"] is not None:
                    twig = segment["twig"]

                    twig_world = [
                        (self.x + point[0], self.y + point[1])
                        for point in twig
                    ]

                    pg.draw.line(
                        screen,
                        ASTEROID_CRACK,
                        twig_world[0],
                        twig_world[1],
                        width=2
                    )