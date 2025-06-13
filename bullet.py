import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position, velocity):
        pygame.sprite.Sprite.__init__(self, *self.__class__.containers)
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt