import pygame
import player
import sys
import projetil
import enemy

clock = pygame.time.Clock()

resolucao = width, height = 500,480
pygame.init()
bg = pygame.image.load('sprites/bg.jpg')
tela = pygame.display.set_mode(resolucao)
pygame.display.set_caption("Meu Jogo")
raio = 5




def main():

    global height, width
    fonte = pygame.font.SysFont('comicsans', 25, True)
    posicao_inicialy = 400
    player1 = player.Player(50,400,5)
    enemy1 = enemy.Enemy(100, 400, width, height, 350, 2)
    clock.tick(11)
    bullets = []
    hit_box = (enemy1.posicao_x + 20, enemy1.posicao_y, 35, 70)

    while True:
        tela

        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        lista = pygame.key.get_pressed()


        if lista[pygame.K_SPACE]:

            if player1.left:
                bullets.append(projetil.Projetil(player1.posicao_x + 15, player1.posicao_y + 40, (0,0,0), 5,5, -1))

            if player1.right:
                bullets.append(projetil.Projetil(player1.posicao_x + 40, player1.posicao_y + 40, (0, 0, 0), 5, 5, 1))



        if lista[pygame.K_LEFT] and player1.posicao_x - player1.veloc >= 0:
            player1.posicao_x -= player1.veloc
            player1.left = True
            player1.right = False
            player1.straight = False
            player1.still = False

        if lista[pygame.K_RIGHT] and player1.posicao_x + player1.veloc <= width - 35:
            player1.posicao_x += player1.veloc
            player1.right = True
            player1.left = False
            player1.straight = False
            player1.still = False

        if lista[pygame.K_UP]:
            player1.isJump = True
            player1.straight = True
            player1.left = False
            player1.right = False
            player.still = False

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

        if not (lista[pygame.K_LEFT] or lista[pygame.K_RIGHT] or lista[pygame.K_SPACE]) and player1.posicao_y == posicao_inicialy:
            if player1.right == True:
                pass
            else:
                player1.right = False


            if player1.left == True:
                pass
            else:
                player1.left = False

            player1.still = True

        hit_box = (enemy1.posicao_x + 20, enemy1.posicao_y, 50, 70)

        player1.draw_images(tela,bg)
        enemy1.draw(tela, hit_box)


        for bullet in bullets:
            if hit_box[0] <= bullet.x <= hit_box[0] + 20 and hit_box[1] <= bullet.y:
                enemy1.hit()
                if enemy1.alive:
                    enemy1.score += 1
                    enemy1.life -= 1
                if enemy1.life <= 0:
                    enemy1.alive = False


            bullet.x += bullet.velocidade * bullet.dir
            bullet.draw(tela)
            texto = fonte.render('SCORE: ' + str(enemy1.score), True, (0,0,0))
            tela.blit(texto, (390,10))

        pygame.display.update()



if __name__ == '__main__':
    main()