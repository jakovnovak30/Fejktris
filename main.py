import pygame
import blokovi
import random
#import overlej

pygame.init()
okvir = pygame.display.set_mode((600,800))
pygame.display.set_caption("Fejktris TM")
pygame.display.update()
vura = pygame.time.Clock()
blocks = []


def izbrisi(red):
    global blocks
    for b in blocks[:-1]:
        novi = []
        for koord in b.k:
            if koord[1] >= red-15 and koord[1] <= red+15:
                pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 30, 30])
            else:
                if koord[1] < red+15:
                    novi.append((koord[0], koord[1]+30))
                    pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 30, 30])
                else:
                    pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 30, 30])
                    novi.append(koord)

        b.k = novi

        for koord in b.k:
            pygame.draw.rect(okvir, b.boja, [koord[0], koord[1], 30, 30])
        pygame.display.update()


def provjeri(red):
    brojac = 0
    pxarray = pygame.PixelArray(okvir)
    for i in range(0, 600):
        if pxarray[i][red] != okvir.map_rgb((0, 0, 0)):
            brojac += 1

    if brojac == 600:
        return True

    return False

def igra():
    traje = True
    pada = False
    brzina = 30
    pocetak = False
    global blocks
    blocks.clear()

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
#        overlay = overlej.Overlej(okvir)

        if not pada:
            novi = random.randrange(0,6)

            if novi == 0:
                prvi = blokovi.Blok((300,100), (270,100), (330,100), (300, 70))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 1:
                prvi = blokovi.Blok((240,100), (270,100), (300,100), (330, 100))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 2:
                prvi = blokovi.Blok((300,100), (300,70), (330,100), (360, 100))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 3:
                prvi = blokovi.Blok((300,100), (330,100), (360,100), (360, 70))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 4:
                prvi = blokovi.Blok((300,100), (300,70), (330,100), (330, 70))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 5:
                prvi = blokovi.Blok((270,100), (300,100), (300,70), (330, 70))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)

                print("Tip: ", novi)
            elif novi == 6:
                prvi = blokovi.Blok((270,70), (300,70), (300,100), (330, 100))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)

                print("Tip: ", novi)
            i = 85
            while i < 800:
                if provjeri(i):
                    izbrisi(i)
                i += 30
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
                    blocks[trenutni].rotiraj(okvir, blocks)

        pada = blocks[trenutni].padni(okvir, blocks)

        vura.tick(brzina)
        brzina = 30

    while True:
        okvir.fill((0,0,0))
        mesg = pygame.font.SysFont("timesnewroman", 20).render('Gejm over: press any r to restart or q to quit', True, (0,0,255))
        okvir.blit(mesg, [130, 400])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    igra()

#vuzgi igru
igra()
