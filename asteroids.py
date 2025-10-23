import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
         super().__init__(x, y, radius)
         
    def draw(self, screen):
        pygame.draw.circle(
            screen,                # surface
            "white",               # color
            self.position,         # position (Vector2)
            self.radius,           # radius
            2                      # line width
        )

    def update(self, dt):
        # Move asteroid in a straight line at constant speed
        self.position += self.velocity * dt