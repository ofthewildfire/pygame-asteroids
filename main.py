import pygame
from pygame.time import Clock
from asteroidfield import  AsteroidField
import player

import constants
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from logger import log_event


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    pygame.time.Clock()
    dt = 0



    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    AsteroidField()
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        updatable.update(dt)

        for a in asteroids:
            if a.collides_with():
                pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill("black")
            for obj in drawable:
                obj.draw(screen)
            pygame.display.flip()
        dt = Clock().tick(60) / 1000
        print(dt)

    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
