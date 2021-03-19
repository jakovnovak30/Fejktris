import pygame
import random
import math

class Blok:
    def __init__(self, *koord):
        self.k = []
        red = random.randrange(0, 255)
        green = random.randrange(0, 255)
        blue = random.randrange(0, 255)

        self.boja = (red, green, blue)

        for koordinate in koord:
            self.k.append((koordinate[0], koordinate[1]))

    def spawn(self, okvir):
        for koord in self.k:
            pygame.draw.rect(okvir, self.boja, [koord[0], koord[1], 30, 30])
        pygame.display.update()

    def padni(self, okvir, blocks):
        novi = []
        for koord in self.k:
            novi.append((koord[0],koord[1]+1))

            pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 30, 30])
            pygame.draw.rect(okvir, self.boja, [koord[0], koord[1]+1, 30, 30])
            pygame.display.update()

            if koord[1] >= 770:
                return False
        self.k = novi
        for b in blocks[:-1]:
            for koord2 in b.k:
                for koord in self.k:
                    if koord2[0] == koord[0] and koord2[1] == koord[1]+30:
                        return False
        return True

    def levo(self, okvir, blocks):
        novi = []
        brojac = 0
        for koord in self.k:
            if koord[0] <= 0: brojac += 1

            novi.append((koord[0]-30,koord[1]))
            pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 30, 30])

        if brojac >= 1: return

        for b in blocks[:-1]:
            for koord1 in b.k:
                for koord2 in novi:
                    if koord1[0] == koord2[0] and koord2[1] >= koord1[1]-30 and koord2[1] <= koord1[1]+30:
                        return
        self.k = novi

    def desno(self, okvir, blocks):
        novi = []
        for koord in self.k:
            if koord[0]+30 >= 600: return
            novi.append((koord[0]+30,koord[1]))
            pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 30, 30])


        for b in blocks[:-1]:
            for koord1 in b.k:
                for koord2 in novi:
                    if koord1[0] == koord2[0] and koord2[1] >= koord1[1]-30 and koord2[1] <= koord1[1]+30:
                        return
        self.k = novi

    def rotiraj(self, okvir):
        novi = []
        prvi = self.k[0]
        novi.append(prvi)
        for koord in self.k:
            pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 30, 30])
            angle = math.pi / 2
            dx = koord[0] - prvi[0]
            dy = koord[1] - prvi[1]
            x = math.cos(angle) * dx - math.sin(angle) * dy + prvi[0]
            y = math.sin(angle) * dx + math.cos(angle) * dy + prvi[1]
            if x <= 0 or x >= 600 or y <= 0 or y >= 800:
                return
            novi.append((x,y))
        self.k = novi
