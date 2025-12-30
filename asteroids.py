import sys
import pygame
from logger import log_event
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            
            return
        else:
            
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity_1 = self.velocity.rotate(angle)
            velocity_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = velocity_1 * 1.2
            asteroid_2.velocity = velocity_2 * 1.2
            return asteroid_1, asteroid_2
    
        