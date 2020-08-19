class GameSound:
    def __init__(self, pygame):
        self.pygame = pygame

        # Setup for sounds. Defaults are good.
        self.pygame.mixer.init()

        # Load and play background music
        # Sound source: http://ccmixter.org/files/Apoxode/59262
        # License: https://creativecommons.org/licenses/by/3.0/
        pygame.mixer.music.load("sounds/Apoxode_-_Electric_1.mp3")
        pygame.mixer.music.play(loops=-1)

        # Load all sound files
        # Sound sources: Jon Fincher
        self.move_up_sound = pygame.mixer.Sound("sounds/Rising_putter.ogg")
        self.move_down_sound = pygame.mixer.Sound("sounds/Falling_putter.ogg")
        self.collision_sound = pygame.mixer.Sound("sounds/Collision.ogg")
