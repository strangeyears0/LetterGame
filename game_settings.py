import pygame

class GameSettings:
    """Class responsible for game settings."""

    def __init__(self):

        #Screen
        self.screen_width = 800
        self.screen_height = 600
        self.screen_title = 'Letter Game'

        #Game Setings

        self.max_frame = 30
        self.falling_speed = 5
        self.next_level_speed = 1.5
        self.points = 1
        self.lives = 3

        #Font

        self.start_font = pygame.font.Font('graphics/font/AmaticSC-Regular.ttf',26)
        self.game_font = pygame.font.Font('graphics/font/AmaticSC-Regular.ttf',20)
        self.game_over_font = pygame.font.Font('graphics/font/AmaticSC-Regular.ttf',30)

        #background

        self.background = pygame.image.load('graphics/parallax-forest.png')