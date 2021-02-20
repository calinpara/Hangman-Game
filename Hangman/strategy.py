import pygame


class Strategy:

    def __init__(self):
        self.images = list()

    def execute(self, hangman_num):
        img = True
        while img:
            for num in range(hangman_num):
                image = pygame.image.load('hangman' + str(num) + '.png')
                self.images.append(image)
            img = False
        return self.images

    def execute_replacement(self, hangman_num):
        for self.img in range(hangman_num):
            image = pygame.image.load('hangman' + str(self.img) + '.png')
            self.images.append(image)
        return self.images


strategy0 = Strategy().execute_replacement(7)
strategy1 = Strategy().execute(7)
