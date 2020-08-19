import pygame

from constants import Constants


class PlayerShoot(pygame.sprite.Sprite):
    def __init__(self, player):
        super(PlayerShoot, self).__init__()
        self.surf = pygame.Surface((10, 5))
        self.surf.fill(Constants.BLACK)

        self.rect = self.surf.get_rect(
            center=(player.rect.right, player.rect.top + 13)
        )
        self.speed = 15

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > Constants.SCREEN_WIDTH:
            self.kill()
