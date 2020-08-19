import pygame

from constants import Constants
from event_processor import EventProcessor
from game_sound import GameSound
from player import Player


def init_game():
    pygame.init()

    # Set up the clock for a decent framerate
    clock = pygame.time.Clock()

    game_sound = GameSound(pygame)

    # set up the drawing window
    screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

    player = Player(game_sound)

    # Create groups to hold enemy sprites and all sprites
    # - enemies is used for collision detection and position updates
    # - clouds is used for position updates
    # - all_sprites is used for rendering
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # game loop
    running = True
    event_processor = EventProcessor(enemies, clouds, all_sprites, player, shoots)

    while running:
        running = event_processor.process_events()

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        clouds.update()
        shoots.update()

        # fill the background with white
        screen.fill(Constants.SKY_BLUE)

        # drawn all sprites
        for entity in all_sprites:
            if not isinstance(entity, Player):
                screen.blit(entity.surf, entity.rect)
        for entity in all_sprites:
            if isinstance(entity, Player):
                screen.blit(entity.surf, entity.rect)

        if len(shoots.spritedict) > 0:
            for shoot in shoots:
                enemy_hit = pygame.sprite.spritecollideany(shoot, enemies)
                if enemy_hit is not None:
                    print("Enemy hit...")
                    enemy_hit.kill()
                    shoot.kill()

        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            player.kill()

            # Stop any moving sounds and play the collision sound
            game_sound.move_up_sound.stop()
            game_sound.move_down_sound.stop()
            channel = game_sound.collision_sound.play()

            # while channel.get_busy():
            #    continue

            # running = False

        # flip the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(45)

    pygame.mixer.music.stop()
    pygame.mixer.quit()


if __name__ == '__main__':
    init_game()
    pygame.quit()
