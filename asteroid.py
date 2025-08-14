import pygame
from circleshape import CircleShape
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            first_vec = self.velocity.rotate(angle)
            second_vec = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_ast = Asteroid(self.position.x, self.position.y, new_radius)
            second_ast = Asteroid(self.position.x, self.position.y, new_radius)
            first_ast.velocity = first_vec * 1.2
            second_ast.velocity = second_vec * 1.2
