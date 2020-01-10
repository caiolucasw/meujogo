import pygame
import player
import sys


clock = pygame.time.Clock()

resolucao = width, height = 500,480
pygame.init()
bg = pygame.image.load('bg.jpg')
tela = pygame.display.set_mode(resolucao)
raio = 5


def main():

    global height, width
    player1 = player.Player(50,400,5)
    clock.tick(11)


    while True:

        tela

        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        lista = pygame.key.get_pressed()

        if lista[pygame.K_LEFT] and player1.posicao_x - player1.veloc >= 0:
            player1.posicao_x -= player1.veloc
            player1.left = True
            player1.right = False
            player1.straight = False

        if lista[pygame.K_RIGHT] and player1.posicao_x + player1.veloc <= width - 35:
            player1.posicao_x += player1.veloc
            player1.right = True
            player1.left = False
            player1.straight = False

        if lista[pygame.K_SPACE]:
            player1.isJump = True
            player1.straight = True
            player1.left = False
            player1.right = False

        if player1.isJump:
            flag = 1
            if player1.jumpCount < 0:
                flag = -1
            if player1.jumpCount >= -10:
                player1.posicao_y -= round(abs(player1.jumpCount*5)*0.5*flag)
                player1.jumpCount -= 1

            else:
                player1.jumpCount = 10
                player1.isJump = False


        player1.draw_images(tela,bg)



if __name__ == '__main__':
    main()