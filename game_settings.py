import pygame

class GameSettings:
    """Class responsible for game settings."""

    def __init__(self):


        self.screen_width = 1024
        self.screen_height = 800
        self.screen_title = 'Letter Game'



        self.max_frame = 25
        self.falling_speed = 5
        self.next_level_speed = 1.5
        self.points = 1
        self.lives = 3



        self.start_font = pygame.font.Font('graphics/font/AmaticSC-Regular.ttf',60)
        self.game_font = pygame.font.Font('graphics/font/AmaticSC-Regular.ttf',58)
        self.game_over_font = pygame.font.Font('graphics/font/AmaticSC-Regular.ttf',60)

        #background

        self.background = pygame.image.load('graphics/parallax-forest.png')


