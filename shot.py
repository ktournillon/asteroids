import pygame

from constants import LINE_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
