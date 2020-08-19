import pygame

from cloud import Cloud
from enemy import Enemy

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)


class EventProcessor:
    def __init__(self, enemies, clouds, all_sprites, player, shoots):
        self.enemies = enemies
        self.clouds = clouds
        self.all_sprites = all_sprites
        self.player = player
        self.shoots = shoots

    def process_events(self):
        running = True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    self.player.shoot(self.all_sprites, self.shoots)
            elif event.type == pygame.QUIT:
                running = False
            # Add a new enemy?
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                enemy = Enemy()
                self.enemies.add(enemy)
                self.all_sprites.add(enemy)
            # Add a new cloud?
            elif event.type == ADDCLOUD:
                # Create the new cloud and add it to sprite groups
                cloud = Cloud()
                self.clouds.add(cloud)
                self.all_sprites.add(cloud)

        return running
