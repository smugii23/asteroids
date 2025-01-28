import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        random_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        asteroid1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        asteroid2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
        asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2
        
