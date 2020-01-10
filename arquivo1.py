import pygame
import sys

# -------------------------------------------------------------------- IMAGES ---------------------------------------------------------------

sprites_right = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'),
                 pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'),
                 pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]

sprites_left = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'),
                pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'),  pygame.image.load('L8E.png'),
                pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]


# ---------------------------------------------------------------------------------------------------------------------------------------------


# global variables

bg = pygame.image.load('bg.jpg')
resolucao = width, height = (500,480)
posicao_circ = [50, 400]
COR = (0, 255, 0)
raio = 20
veloc = 5
PRETO = (0,0,0)
isJump = False
jumpCount = 10
tela = pygame.display.set_mode(resolucao)
pygame.init()
left = False
right = False
straight = False
contWalk = 0
clock = pygame.time.Clock()



def draw_images():
    global tela
    global contWalk
    global left
    global right
    global straight

    tela.blit(bg, (0,0))

    if contWalk + 1 == len(sprites_right):
        contWalk = 0

    if left:
        tela.blit(sprites_left[contWalk],(posicao_circ[0], posicao_circ[1]))

    elif right or straight:
        tela.blit(sprites_right[contWalk], (posicao_circ[0], posicao_circ[1]))

    else:
        tela.blit(sprites_right[contWalk], (posicao_circ[0], posicao_circ[1]))

    contWalk += 1

    pygame.display.update()


def main():
    global isJump
    global jumpCount
    global tela
    global right
    global left
    global straight
    global clock

    clock.tick(11)

    while True:

        tela

        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        lista = pygame.key.get_pressed()

        if lista[pygame.K_LEFT] and posicao_circ[0] - veloc >= raio:
            posicao_circ[0] -= veloc
            left = True
            right = False
            straight = False


        if lista[pygame.K_RIGHT] and posicao_circ[0] + veloc <= width - raio:
            posicao_circ[0] += veloc
            right = True
            left = False
            straight = False

        if lista[pygame.K_SPACE]:
            isJump = True
            straight = True
            left = False
            right = False

        if isJump:
            flag = 1
            if jumpCount < 0:
                flag = -1
            if jumpCount >= -10:
                posicao_circ[1] -= round(abs(jumpCount*5)*0.5*flag)
                jumpCount -= 1

            else:
                jumpCount = 10
                isJump = False


        draw_images()



if __name__ == '__main__':
    main()