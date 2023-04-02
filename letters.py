import pygame


class Alphabet:
    """Change letter into png letter"""
    def __init__(self):
        self.alphabet_images = {}
        for letter in 'ABCDEFGHIJKLMNOPQRSTUWXYZ':
            filename = f"graphics/letters/{letter}.png"
            image = pygame.image.load(filename)
            # Change size images
            image = pygame.transform.scale(image,(image.get_width() // 2, image.get_height() // 2))
            self.alphabet_images[letter] = image

    def get_letter_image(self,letter):
        return self.alphabet_images.get(letter.upper())

    def get_letter(self,image):
        for letter, img in self.alphabet_images.items():
            if img == image:
                return letter
        return None