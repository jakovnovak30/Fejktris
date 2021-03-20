import pygame

class Overlej:
    def __init__(self, okvir, skor):
        pygame.draw.rect(okvir,(0,0,0),[500, 30, 150, 80])
        pygame.display.update()

        pygame.draw.line(okvir, (255,255,255), (15,50), (15,800), 10) #levo
        pygame.draw.line(okvir, (255,255,255), (15,50), (405, 50), 10) #gore
        pygame.draw.line(okvir, (255,255,255), (405,50), (405,800), 10) #desno
        pygame.draw.line(okvir, (255,255,255), (15,795), (405,795), 10) #dole

        mesg = pygame.font.SysFont("comicsansms", 30).render('Skor: ' + str(skor), True, (0,0,255))
        okvir.blit(mesg, [420, 40])
        mesg = pygame.font.SysFont("arial", 25).render('Controls:', True, (0,255,0))
        okvir.blit(mesg, [420, 80])

        mesg = pygame.font.SysFont("arial", 25).render('UP - rotate', True, (0,255,0))
        okvir.blit(mesg, [420,110])

        mesg = pygame.font.SysFont("arial", 25).render('DOWN - speed up', True, (0,255,0))
        okvir.blit(mesg, [420, 140])

        mesg = pygame.font.SysFont("arial", 25).render('LEFT - go left', True, (0,255,0))
        okvir.blit(mesg, [420, 170])

        mesg = pygame.font.SysFont("arial", 25).render('RIGHT - go right', True, (0,255,0))
        okvir.blit(mesg, [420,200])

        pygame.display.update()
