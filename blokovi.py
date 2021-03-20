import pygame
import random
import math

class Blok:
    def __init__(self, color, *koord):
        self.k = []

        self.boja = color

        for koordinate in koord:
            self.k.append((koordinate[0], koordinate[1]))

    def spawn(self, okvir, blocks):
        for b in blocks[:-1]:
            for koord2 in b.k:
                for koord in self.k:
                    if koord[0] >= koord2[0]-20 and koord[0] <= koord2[0]+20 and koord[1] >= koord2[1]-20 and koord[1] <= koord2[1]+20:
                        return False
        for koord in self.k:
            pygame.draw.rect(okvir, self.boja, [koord[0], koord[1], 20, 20])

        return True

    def padni(self, okvir, blocks):
        novi = []
        for koord in self.k:
            novi.append((koord[0],koord[1]+5))
            if koord[1] >= 770:
                return False
        self.k = novi
        for koord in novi:
            pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1]-5, 20, 20])

        for b in blocks[:-1]:
            for koord2 in b.k:
                for koord in self.k:
                    if koord2[0] == koord[0] and koord2[1] == koord[1]+20:
                        return False

        return True

    def nacrtaj(self, okvir):
        for koord in self.k:
            pygame.draw.rect(okvir, self.boja, [koord[0], koord[1], 20, 20])

    def levo(self, okvir, blocks):
        novi = []
        brojac = 0
        for koord in self.k:
            if koord[0] <= 20: brojac += 1

            novi.append((koord[0]-20,koord[1]))
            pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 20, 20])

        if brojac >= 1: return

        for b in blocks[:-1]:
            for koord1 in b.k:
                for koord2 in novi:
                    if koord1[0] == koord2[0] and koord2[1] >= koord1[1]-20 and koord2[1] <= koord1[1]+20:
                        return
        self.k = novi

    def desno(self, okvir, blocks):
        novi = []
        for koord in self.k:
            if koord[0]+20 >= 400: return
            novi.append((koord[0]+20,koord[1]))
            pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 20, 20])


        for b in blocks[:-1]:
            for koord1 in b.k:
                for koord2 in novi:
                    if koord1[0] == koord2[0] and koord2[1] >= koord1[1]-20 and koord2[1] <= koord1[1]+20:
                        return
        self.k = novi

    def rotiraj(self, okvir, blocks):
        novi = []
        prvi = self.k[0]
        novi.append(prvi)
        for koord in self.k:
            pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 20, 20])
            angle = math.pi / 2
            dx = koord[0] - prvi[0]
            dy = koord[1] - prvi[1]
            x = math.cos(angle) * dx - math.sin(angle) * dy + prvi[0]
            y = math.sin(angle) * dx + math.cos(angle) * dy + prvi[1]
            if x <= 0 or x >= 380 or y <= 0 or y >= 780:
                return
            novi.append((x,y))

        for b in blocks[:-1]:
            for koord2 in b.k:
                for koord in novi:
                    if koord[0] >= koord2[0]-20 and koord[0] <= koord2[0]+20 and koord[1] >= koord2[1]-20 and koord[1] <= koord2[1]+20:
                        return
        self.k = novi
        self.padni(okvir, blocks)
