import pygame

import random
import circleshape
import constants
from constants import ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, constants.LINE_WIDTH )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if ASTEROID_MIN_RADIUS <= self.radius:
            return
        else:
            log_event('asteroid_split')
            angle = random.uniform(20, 50)
            # Because it takes an ANGLE. use the angle we generated.
            first_movement = self.velocity.rotate(angle)
            second_movement = self.velocity.rotate(-angle)


