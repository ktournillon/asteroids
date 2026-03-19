import random
import pygame

from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    """CircleShape with the ability to split into smaller Asteroids shooting in two directions"""

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle: float = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-1 * random_angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position[0], self.position[1], smaller_radius)
        asteroid_2 = Asteroid(self.position[0], self.position[1], smaller_radius)
        asteroid_1.velocity = new_velocity_1 * 1.2
        asteroid_2.velocity = new_velocity_2 * 1.2
