"""Base class for game objects"""
import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects"""
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
        """To be overridden by child class objects"""

    def update(self, dt):
        """To be overridden by child class objects"""

    def collides_with(self, other) -> bool:
        """Class to determine when two circular objects collide"""
        radius_summary = self.radius + other.radius
        return self.position.distance_to(other.position) < radius_summary
