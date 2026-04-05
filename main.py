import pygame
from pygame.time import Clock
import player

import constants
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    pygame.time.Clock()
    dt = 0

    while True:
        log_state()
        player_info = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill("black")
            player_info.draw(screen)
            pygame.display.flip()
        dt = Clock().tick(60) / 1000
        print(dt)

    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
