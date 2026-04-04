"""Defines player object"""
import pygame

from circleshape import CircleShape
from shot import Shot
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    SHOT_RADIUS
)


class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.cooldown_timer: float = 0

    def triangle(self) -> list[float]:
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        right: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a: float = self.position + forward * self.radius
        b: float = self.position - forward * self.radius - right
        c: float = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: int) -> None:
        self.rotation += dt

    def update(self, dt: int) -> None:
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(PLAYER_TURN_SPEED * dt * -1)
        if keys[pygame.K_d]:
            self.rotate(PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            if self.cooldown_timer <= 0:
                self.shoot()
                self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        self.cooldown_timer -= dt

    def move(self, dt: int) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        shot.velocity = rotated_vector * PLAYER_SHOT_SPEED
