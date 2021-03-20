import pygame
import blokovi
import random
import overlej
import time

pygame.init()
okvir = pygame.display.set_mode((700,800))
pygame.display.set_caption("Fejktris TM")
pygame.display.update()
vura = pygame.time.Clock()
blocks = []

def izbrisi(red):
    global blocks
    for b in blocks[:-1]:
        novi = []
        for koord in b.k:
            if koord[1] >= red-10 and koord[1] <= red+10:
                pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 20, 20])
            else:
                if koord[1] < red+10:
                    novi.append((koord[0], koord[1]+20))
                    pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 20, 20])
                else:
                    pygame.draw.rect(okvir, (0,0,0), [koord[0], koord[1], 20, 20])
                    novi.append(koord)
        b.k = novi

    for b in blocks[:-1]:
        b.nacrtaj(okvir)


def provjeri(red):
    brojac = 0
    pxarray = pygame.PixelArray(okvir)
    for i in range(20, 400):
        if pxarray[i][red] != okvir.map_rgb((0, 0, 0)):
            brojac += 1

    if brojac == 380:
        return True

    return False

def igra():
    traje = True
    pada = False
    brzina = 30
    pocetak = False
    skor = 0
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
    rubovi = overlej.Overlej(okvir, skor)

    red = random.randrange(0, 255)
    green = random.randrange(0, 255)
    blue = random.randrange(0, 255)
    next_color = (red, green, blue)
    next = random.randrange(0,6)
    while traje:
        if not pada:
            novi = next
            color = next_color

            next = random.randrange(0,6)
            red = random.randrange(0, 255)
            green = random.randrange(0, 255)
            blue = random.randrange(0, 255)
            next_color = (red, green, blue)

            if novi == 0:
                prvi = blokovi.Blok(color, (200,100), (180,100), (220,100), (200, 80))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)
            elif novi == 1:
                prvi = blokovi.Blok(color, (140,100), (160,100), (180,100), (200, 100))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)
            elif novi == 2:
                prvi = blokovi.Blok(color,(200,100), (200,80), (220,100), (240, 100))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)
            elif novi == 3:
                prvi = blokovi.Blok(color, (200,100), (220,100), (240,100), (240, 80))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)
            elif novi == 4:
                prvi = blokovi.Blok(color, (200,100), (200,80), (220,100), (220, 80))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)
            elif novi == 5:
                prvi = blokovi.Blok(color, (180,100), (200,100), (200,80), (220, 80))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)
            elif novi == 6:
                prvi = blokovi.Blok(color, (280,80), (300,80), (300,100), (320, 100))
                traje = prvi.spawn(okvir, blocks)
                blocks.append(prvi)

            pygame.draw.rect(okvir, (0,0,0), [420, 350, 200, 150])
            #preview sledeceg
            if next == 0:
                sledeci = blokovi.Blok(next_color, (500,400), (480,400), (520,400), (500,380))
                sledeci.spawn(okvir, blocks)
            elif next == 1:
                sledeci = blokovi.Blok(next_color, (440,400), (460,400), (480,400), (500, 400))
                sledeci.spawn(okvir, blocks)
            elif next == 2:
                sledeci = blokovi.Blok(next_color, (500,400), (500,380), (520,400), (540, 400))
                sledeci.spawn(okvir, blocks)
            elif next == 3:
                sledeci = blokovi.Blok(next_color, (500,400), (520,400), (540,400), (540, 380))
                sledeci.spawn(okvir, blocks)
            elif next == 4:
                sledeci = blokovi.Blok(next_color, (500,400), (500,380), (520,400), (520, 380))
                sledeci.spawn(okvir, blocks)
            elif next == 5:
                sledeci = blokovi.Blok(next_color, (480,400), (500,400), (500,380), (520, 380))
                sledeci.spawn(okvir, blocks)
            elif next == 6:
                sledeci = blokovi.Blok(next_color, (580,380), (600,380), (600,400), (620, 400))
                sledeci.spawn(okvir, blocks)

            i = 90
            while i < 800:
                if provjeri(i):
                    skor = skor + 100
                    print('Trebal bi brisati red. Skor: ' + str(skor))
                    izbrisi(i)
                    rubovi.update(okvir, skor)
                i += 20
            pada = True

        trenutni = len(blocks)-1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            brzina = 120
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
                    vura.tick(20)

        pada = blocks[trenutni].padni(okvir, blocks)
        blocks[trenutni].nacrtaj(okvir)

        pygame.display.update()
        vura.tick(brzina)
        brzina = 15

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
