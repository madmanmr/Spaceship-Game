import pygame as pg
import numpy as np

from settings import BLACK, ACCENT_GREEN, ASTEROID_CRACK


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
        num_vertices = 10

        for i in range(num_vertices):
            angle = (360 / num_vertices) * i + np.random.uniform(-8, 8)
            distance = self.radius * np.random.uniform(0.85, 1.15)

            x = np.cos(np.radians(angle)) * distance
            y = np.sin(np.radians(angle)) * distance
            asteroid_points.append((x, y))

        self.shape_points = asteroid_points

        self.crack_points = []
        max_cracks = 6

        #pick random outer points for start
        start_indices = np.random.choice(num_vertices, size=max_cracks, replace=True)

        for idx in start_indices:
            start_x, start_y = asteroid_points[idx]

            #crack travels from corner towards center with magic
            target_angle = np.degrees(np.arctan2(-start_y, -start_x))

            segments = np.random.randint(3, 5)  # 3 to 4 jagged segments
            total_length = self.radius * np.random.uniform(0.7, 1.2)
            step_length = total_length / segments

            current_x, current_y = start_x, start_y
            main_path = [(current_x, current_y)]
            branches = []

            current_angle = target_angle

            for s in range(segments):
                # Add random variation to direction at each segment joint
                current_angle += np.random.uniform(-35, 35)

                next_x = current_x + np.cos(np.radians(current_angle)) * step_length
                next_y = current_y + np.sin(np.radians(current_angle)) * step_length
                main_path.append((next_x, next_y))

                #30 percent for twigs
                if s > 0 and np.random.rand() < 0.3:
                    branch_angle = current_angle + np.random.choice([-45, 45])
                    branch_len = step_length * np.random.uniform(0.5, 0.8)
                    branch_end_x = next_x + np.cos(np.radians(branch_angle)) * branch_len
                    branch_end_y = next_y + np.sin(np.radians(branch_angle)) * branch_len
                    branches.append([(next_x, next_y), (branch_end_x, branch_end_y)])

                current_x, current_y = next_x, next_y

            self.crack_points.append({"path": main_path, "branches": branches})

    def draw(self, screen):
        world_points = [(self.x + x, self.y + y) for x, y in self.shape_points] #ai efficiency
        pg.draw.polygon(screen, (158, 73, 8), world_points)

        health_ratio = max(0, self.health / getattr(self, "max_health", 10)) # holy ai
        cracks_to_show = int((1.0 - health_ratio) * len(self.crack_points))

        for crack in self.crack_points[:cracks_to_show]:
            main_world = [(self.x + px, self.y + py) for px, py in crack["path"]]
            pg.draw.lines(screen, ASTEROID_CRACK, False, main_world, width=3)

            for branch in crack["branches"]:
                branch_world = [
                    (self.x + bx, self.y + by) for bx, by in branch
                ]
                pg.draw.lines(screen, ASTEROID_CRACK, False, branch_world, width=2)