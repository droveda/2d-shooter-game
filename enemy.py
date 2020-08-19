import random

import pygame

from constants import Constants


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # self.surf = pygame.Surface((20, 10))
        self.surf = pygame.image.load("images/missile.png")
        self.surf.set_colorkey(Constants.WHITE, pygame.RLEACCEL)
        # self.surf.fill(Constants.WHITE)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Constants.SCREEN_WIDTH + 20, Constants.SCREEN_WIDTH + 100),
                random.randint(0, Constants.SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
