import pygame

from constants import Constants
from player_shoot import PlayerShoot


class Player(pygame.sprite.Sprite):
    def __init__(self, game_sound):
        super(Player, self).__init__()
        # self.surf = pygame.Surface((75, 25))
        self.surf = pygame.image.load("images/jet.png").convert()
        self.surf.set_colorkey(Constants.WHITE, pygame.RLEACCEL)
        # self.surf.fill(Constants.WHITE)
        self.rect = self.surf.get_rect()
        self.game_sound = game_sound

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
            self.game_sound.move_up_sound.play()
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
            self.game_sound.move_down_sound.play()
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Constants.SCREEN_WIDTH:
            self.rect.right = Constants.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Constants.SCREEN_HEIGHT:
            self.rect.bottom = Constants.SCREEN_HEIGHT

    def shoot(self, all_sprites, shoots):
        # print("Shooting...")
        shoot = PlayerShoot(self)
        all_sprites.add(shoot)
        shoots.add(shoot)
        self.game_sound.collision_sound.play()
