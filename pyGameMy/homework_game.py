import pygame
import time
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1530
HEIGHT = 800


def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def get_vector_length(vector: list):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


class Hero():
    def __init__(self, name, speed, x, y, color=BLUE, radius=15):
        self.name = name
        self.speed = speed
        self.basic_speed = speed
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed_boost_start_time = 0

    def update(self, keys, enemies, hero):
        current_time = time.time()
        if current_time < self.speed_boost_start_time + 0.2:
            self.speed = 40
        else:
            self.speed = self.basic_speed

        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_SPACE]:
            self.activate_speed_boost()

    def activate_speed_boost(self):
        self.speed_boost_start_time = time.time()

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.radius)


class Enemy():
    def __init__(self, x, y, speed, vision_range=200, radius=20, color=RED):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = color
        self.vision_range = vision_range

    def update(self, keys, enemies, hero):
        vector = [hero.x - self.x, hero.y - self.y]
        vector_length = get_vector_length(vector)

        mini_vector = [vector[0] * self.speed / vector_length, vector[1] * self.speed / vector_length]

        self.x += mini_vector[0]
        self.y += mini_vector[1]

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.radius)

    @classmethod
    def spawn_random(cls):
        return cls(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 3),
                   vision_range=random.randint(150, 250),
                   radius=random.randint(15, 25),
                   color=(random.randint(200, 255), random.randint(0, 100), random.randint(0, 100)))

    def die(self, enemies):
        enemies.remove(self)


class Camera:
    def __init__(self, hero, width=WIDTH, height=HEIGHT):
        self.hero = hero
        self.width = width
        self.height = height
        self.mouse_coords = [0, 0]
        self.k = 0.3

    def get_center_coords(self):
        hero_coords = [self.hero.x, self.hero.y]
        vector = [self.mouse_coords[0] - hero_coords[0], self.mouse_coords[1] - hero_coords[1]]
        small_vector = [vector[0] * self.k, vector[1] * self.k]
        return [hero_coords[0] + small_vector[0], hero_coords[1] + small_vector[1]]

    def get_left_up_coords(self):
        center = self.get_center_coords()
        return [center[0] - self.width // 2, center[1] - self.height // 2]

    def calc_coords(self, global_coords):
        coords = self.get_left_up_coords()
        return [global_coords[0] - coords[0], global_coords[1] - coords[1]]

    def local_to_global(self, local_coords):
        coords = self.get_left_up_coords()
        return [coords[0] + local_coords[0], coords[1] + local_coords[1]]

    def set_mouse_coords(self, coords):
        self.mouse_coords = coords


class Game:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    hero = Hero('Bob', 5, 400, 400)
    camera = Camera(hero=hero)
    enemies = [Enemy.spawn_random() for _ in range(5)]
    clock = pygame.time.Clock()

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            self.camera.set_mouse_coords(self.camera.local_to_global(pygame.mouse.get_pos()))

            keys = pygame.key.get_pressed()

            for obj in self.enemies + [self.hero]:
                obj.update(keys, self.enemies, self.hero)

            self.screen.fill(WHITE)

            for obj in self.enemies + [self.hero]:
                obj.draw(self.screen, self.camera)

            pygame.display.flip()

            self.clock.tick(60)


if __name__ == '__main__':
    Game().run()
