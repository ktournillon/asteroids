import pygame

from constants import LINE_WIDTH
from circleshape import CircleShape


class Shot(CircleShape):
    """CircleShape representing bullets from player"""
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
