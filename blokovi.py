import pygame
import random

class Blok:
    k = []
    def __init__(self, *koord):
        red = random.randrange(0, 255)
        green = random.randrange(0, 255)
        blue = random.randrange(0, 255)

        self.boja = (red, green, blue)

        for koordinate in koord:
            self.k.append((koordinate[0], koordinate[1]))

    def spawn(self, okvir):
        for koord in self.k:
            pygame.draw.rect(okvir, self.boja, [koord[0], koord[1], 10, 10])
        pygame.display.update()

    def padni(self):
        for koord in self.k:
            self.k.append((koord[0]-10,koord[1]-10))
            del self.k[0]
            pygame.draw.rect(okvir, self.boja, [koord[0], koord[1], 10, 10])
