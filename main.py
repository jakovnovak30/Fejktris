import pygame
import blokovi
import random

pygame.init()
okvir = pygame.display.set_mode((600,800))
pygame.display.set_caption("Fejktris TM")
pygame.display.update()
vura = pygame.time.Clock()

def igra():
    traje = True
    pada = False
    blocks = []
    brzina = 30
    pocetak = False

    okvir.fill((0,0,0))
    mesg = pygame.font.SysFont("timesnewroman", 20).render('Fejktris: press any key to start', True, (0,0,255))
    okvir.blit(mesg, [200, 400])
    pygame.display.update()
    while not pocetak:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pocetak = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        vura.tick(25)

    okvir.fill((0,0,0))    
    while traje:
        if not pada:
            novi = random.randrange(0,6)

            if novi == 0:
                prvi = blokovi.Blok((300,100), (270,100), (330,100), (300, 70))
                prvi.spawn(okvir)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 1:
                prvi = blokovi.Blok((240,100), (270,100), (300,100), (330, 100))
                prvi.spawn(okvir)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 2:
                prvi = blokovi.Blok((300,100), (300,70), (330,100), (360, 100))
                prvi.spawn(okvir)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 3:
                prvi = blokovi.Blok((300,100), (330,100), (360,100), (360, 70))
                prvi.spawn(okvir)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 4:
                prvi = blokovi.Blok((300,100), (300,70), (330,100), (330, 70))
                prvi.spawn(okvir)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 5:
                prvi = blokovi.Blok((270,100), (300,100), (300,70), (330, 70))
                prvi.spawn(okvir)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 6:
                prvi = blokovi.Blok((270,70), (300,70), (300,100), (330, 100))
                prvi.spawn(okvir)
                blocks.append(prvi)

                print("Tip: ", novi)
            pada = True

        trenutni = len(blocks)-1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            brzina = 200
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    blocks[trenutni].desno(okvir, blocks)
                if event.key == pygame.K_LEFT:
                    blocks[trenutni].levo(okvir, blocks)
                if event.key == pygame.K_UP:
                    blocks[trenutni].rotiraj(okvir)

        pada = blocks[trenutni].padni(okvir, blocks)
        vura.tick(brzina)
        brzina = 30

igra()
