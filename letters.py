import pygame


class Alphabet:
    """Change letter into png letter"""
    def __init__(self):
        self.alphabet_images = {}
        letters=['A','B','C','D','E','F','G','H','I','J',
                 'K','L','M','N','O','P','Q','R','S','T',
                 'U','W','X','Y','Z']
        for letter in letters:
            filename = f"graphics/letters/{letter}.png"
            image = pygame.image.load(filename)

            image = pygame.transform.scale(image,(image.get_width() // 1, image.get_height() // 1))
            self.alphabet_images[letter] = image

    def get_letter_image(self,letter):
        return self.alphabet_images.get(letter.upper())

    def get_letter(self,image):
        for letter, img in self.alphabet_images.items():
            if img == image:
                return letter
        return None