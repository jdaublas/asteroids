import pygame
from constants import *
from circleshape import CircleShape
class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers) 
        CircleShape.__init__(self, x, y, radius) 
        self.velocity = pygame.Vector2(0, -PLAYER_SHOOT_SPEED)
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.center = self.position

    def update(self,dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
            
