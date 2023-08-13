import pygame
import time
from pyGameMy.colors import *
import random

pygame.init()

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000

DRAW_VELOCITY = False


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # +
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # -
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):  # *
        return Vector(self.x * number, self.y * number)

    def __truediv__(self, number):  # /
        return Vector(self.x / number, self.y / number)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'<{self.__str__()}>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):  # -self
        return Vector(-self.x, -self.y)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        if self.length() == 0:
            return Vector(0, 0)
        return self / self.length()

    def to_tuple(self):
        return self.x, self.y

    @classmethod
    def from_tuple(cls, tuple):
        return cls(tuple[0], tuple[1])

    @classmethod
    def create_vector_from_points(cls, start, end):
        return cls(end.x - start.x, end.y - start.y)


# lst = [1, 2]
# v = Vector.from_tuple(lst)
# print(v)

# v = Vector.create_vector_from_points(Vector(1, 1), Vector(10, 10))
# print(v)


def bar(current_value, max_value, width, height, color, background_color, surface, start_coords):
    pygame.draw.rect(surface, background_color, (start_coords[0], start_coords[1], width, height))  # Фонова полоска
    filled_width = (current_value / max_value) * width  # Обчислення ширини заповненої частини
    pygame.draw.rect(surface, color, (start_coords[0], start_coords[1], filled_width, height))  # Заповнена полоска


class GameObject:
    def __init__(self, coords, width, height, color, mass=1, velocity=Vector(0, 0), acceleration=Vector(0, 0)):
        self.coords = coords
        self.width = width
        self.height = height
        self.color = color
        self.mass = mass
        self.velocity = velocity
        self.acceleration = acceleration
        self.is_alive = True

    def get_center(self):
        return Vector(self.coords.x + self.width / 2, self.coords.y + self.height / 2)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.coords.x, self.coords.y, self.width, self.height))
        if DRAW_VELOCITY:
            center = self.get_center()
            pygame.draw.line(screen, RED, center.to_tuple(), (center + self.velocity).to_tuple(), 3)

    def update(self, tdelta):
        self.acceleration = Vector(0, 20)
        self.velocity += self.acceleration

        self.coords += self.velocity * tdelta

        if self.is_on_surface():
            self.coords.y = SCREEN_HEIGHT - self.height
            self.velocity.y = 0

            friction_force = self.get_friction_force()
            if friction_force.length() > self.velocity.length():
                self.velocity = Vector(0, 0)
            else:
                self.velocity += friction_force

        if self.velocity.length() < 1:
            self.velocity = Vector(0, 0)

    def get_friction_force(self, k=0.1):
        if self.velocity.length() == 0:
            return Vector(0, 0)
        return -self.velocity.normalize() * k * self.mass * 10

    def is_on_surface(self):
        return self.coords.y >= SCREEN_HEIGHT - self.height

    def die(self):
        self.is_alive = False


class Bullet(GameObject):
    def __init__(self, coords, width, height, color, mass, velocity, game_objects, does_have_sub_bullets=False):
        super().__init__(coords, width, height, color, mass, velocity)
        self.game_objects = game_objects
        self.does_have_sub_bullets = does_have_sub_bullets

    def update(self, tdelta):
        super().update(tdelta)
        if self.is_on_surface():
            self.velocity = Vector(0, 0)
            self.boom()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.get_center().to_tuple(), self.width)

    def boom(self):
        for obj in self.game_objects:
            if obj != self:
                if (self.get_center() - obj.get_center()).length() < 1000:
                    d = obj.get_center() - self.get_center()
                    obj.velocity += d.normalize() * 1000 * (50/d.length())**(1)
        self.die()
        if self.does_have_sub_bullets:
            for _ in range(10):
                new_bullet = Bullet(self.get_center() + Vector(0, -50), 10, 10, RED, 1, Vector(random.randint(-100, 100), random.randint(-1000, -800)), self.game_objects)
                self.game_objects.append(new_bullet)


class Mech(GameObject):
    def __init__(self, coords, width, height, color, speed, mass=1, fuel=100, fuel_consumption=0.8, fuel_recovery=0.5):
        super().__init__(coords, width, height, color, mass)
        self.speed = speed
        self.fuel = fuel
        self.max_fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.fuel_recovery = fuel_recovery

    def move(self, direction, speed):
        self.velocity += direction * speed

    def fly(self):
        if self.fuel > 0:
            self.fuel -= self.fuel_consumption
            self.move(Vector(0, -1), self.speed / 2)

    def update(self, tdelta):
        super().update(tdelta)
        if self.is_on_surface():
            if self.fuel < self.max_fuel:
                self.fuel += self.fuel_recovery

    def draw(self, screen):
        super().draw(screen)
        bar(self.fuel, self.max_fuel, self.width + 20, 8, GREEN, BLACK, screen, (self.coords.x-10, self.coords.y - 20))

    def shoot(self, game_objects, pos):
        bullet = Bullet(self.get_center(), 10, 10, RED, 1, Vector.create_vector_from_points(self.get_center(), pos).normalize() * 1000, game_objects, True)
        game_objects.append(bullet)


class Player(Mech):
    def __init__(self, coords, width, height, color, speed, mass, jump_speed=500):
        super().__init__(coords, width, height, color, speed, mass)
        self.jump_speed = jump_speed

    def jump(self):
        if self.is_on_surface():
            self.velocity += Vector(0, -self.jump_speed)

    def player_update(self, pressed):
        if self.is_on_surface():
            speed = self.speed
            is_flying = False
        else:
            speed = self.speed / 6
            is_flying = True

        if pressed[pygame.K_w]:
            self.move(Vector(0, -1), speed)
        if pressed[pygame.K_s]:
            self.move(Vector(0, 1), speed)
        if pressed[pygame.K_a]:
            self.move(Vector(-1, 0), speed)
        if pressed[pygame.K_d]:
            self.move(Vector(1, 0), speed)

        if pressed[pygame.K_SPACE] and is_flying:
            self.fly()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player(Vector(100, 100), 50, 50, CYAN, 60, 25)
        self.player.velocity = Vector(300, -330)

        self.game_objects = [self.player]

    @property
    def alive_game_objects(self):
        return [obj for obj in self.game_objects if obj.is_alive]

    def run(self):
        while True:
            self.screen.fill(WHITE)
            for obj in self.alive_game_objects:
                obj.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.player.shoot(self.game_objects, Vector(*event.pos))

            self.player.player_update(pygame.key.get_pressed())

            time_delta = 1/60
            for obj in self.alive_game_objects:
                obj.update(time_delta)

            self.clock.tick(60)


if __name__ == '__main__':
    Game().run()
