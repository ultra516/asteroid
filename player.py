import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
class Player(CircleShape):
    def __init__(self, x, y):
         super().__init__(x, y, PLAYER_RADIUS)
         self.rotation = 0
         self.shoot_cooldown = 0.25  # seconds between shots
         self.time_since_last_shot = 0  # timer accumulator
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        self.time_since_last_shot += dt
        if keys[pygame.K_SPACE] and self.time_since_last_shot >= self.shoot_cooldown:
            self.shoot()
            self.time_since_last_shot = 0


    def shoot(self):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.copy(), velocity)
        if hasattr(Shot, 'containers'):
            for group in Shot.containers:
                group.add(shot)
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def rotate(self, dt):
       self.rotation += PLAYER_TURN_SPEED * dt