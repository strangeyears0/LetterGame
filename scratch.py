import pygame
from sys import exit
import random

class Alphabet():
    def __init__(self):
        self.alphabet_images = {}
        for letter in 'ABCDEFGHIJKLMNOPQRSTUWXYZ':
            filename = f''

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Caption")
clock = pygame.time.Clock()

background = pygame.image.load('scratch/parallax-forest.png')
background = pygame.transform.scale(background,(800,800))
letter_A = pygame.image.load(f'scratch/C.png').convert_alpha()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(background,(0,0))
    screen.blit(letter_A,(400,400))

    pygame.display.update()
    clock.tick(60)