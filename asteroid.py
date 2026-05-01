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

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event('asteroid_split')
            angle = random.uniform(20, 50)
            # Because it takes an ANGLE. use the angle we generated.
            first_movement = self.velocity.rotate(angle)
            second_movement = self.velocity.rotate(-angle)
            smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, smaller_asteroid_radius).velocity = first_movement * 1.2
            Asteroid(self.position.x, self.position.y, smaller_asteroid_radius).velocity = second_movement * 1.2

