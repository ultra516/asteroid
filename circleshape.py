import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(
            screen,                 # The screen surface to draw on
            "white",                # The color
            self.triangle(),        # The list of points
            2                       # The line width
        )
        

    def update(self, dt):
        # sub-classes must override
        pass