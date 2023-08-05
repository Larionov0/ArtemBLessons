import pygame
from pyGameMy.colors import *

pygame.init()

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000


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

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
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


class GameObject:
    def __init__(self, coords, width, height, color, mass=1, velocity=Vector(0, 0), acceleration=Vector(0, 0)):
        self.coords = coords
        self.width = width
        self.height = height
        self.color = color
        self.mass = mass
        self.velocity = velocity
        self.acceleration = acceleration

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.coords.x, self.coords.y, self.width, self.height))

    def update(self, tdelta):
        self.acceleration = Vector(0, 10)
        self.velocity += self.acceleration

        self.coords += self.velocity * tdelta

        if self.coords.y > SCREEN_HEIGHT - self.height:
            self.coords.y = SCREEN_HEIGHT - self.height
            self.velocity.y = 0


class Mech(GameObject):
    def __init__(self, coords, width, height, color, speed, mass=1):
        super().__init__(coords, width, height, color, mass)
        self.speed = speed

    def move(self, direction):
        self.velocity += direction * self.speed


class Player(Mech):
    def __init__(self, coords, width, height, color, speed, mass):
        super().__init__(coords, width, height, color, speed)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player(Vector(100, 100), 50, 50, CYAN, 5, 1)
        self.player.velocity = Vector(300, -330)

    def run(self):
        while True:
            self.screen.fill(WHITE)
            self.player.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move(Vector(0, -1))
            if keys[pygame.K_s]:
                self.player.move(Vector(0, 1))
            if keys[pygame.K_a]:
                self.player.move(Vector(-1, 0))
            if keys[pygame.K_d]:
                self.player.move(Vector(1, 0))

            self.player.update(1 / 60)

            self.clock.tick(60)


if __name__ == '__main__':
    Game().run()
