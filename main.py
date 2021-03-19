import pygame
import blokovi

pygame.init()
okvir = pygame.display.set_mode((600,600))
pygame.display.set_caption("Fejktris TM")
pygame.display.update()
vura = pygame.time.Clock()
traje = True
pada = False
while traje:
    if not pada:
        prvi = blokovi.Blok((300,300), (290,300), (310,300), (300, 290))
        prvi.spawn(okvir)
        pada = True


    prvi.padni()    
    vura.tick(25)
