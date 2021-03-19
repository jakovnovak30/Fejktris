import pygame

class Overlej:
    def __init__(self, okvir):
        pygame.draw.rect(okvir, (255,255,255), [300, 300, 250, 250])
        pygame.draw.rect(okvir, (0,0,0), [300,300, 230, 230])
        pygame.display.update()
