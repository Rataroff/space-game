import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity: pygame.Vector2):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            1
        )
