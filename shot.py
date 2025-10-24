import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
         
    def draw(self, screen):
        pygame.draw.circle(
            screen,                # surface
            "red",               # color
            self.position,         # position (Vector2)
            self.radius,           # radius
            2                      # line width
        )
    
    def update(self, dt):
        # Move asteroid in a straight line at constant speed
        self.position += self.velocity * dt