import pygame



class Enemy(object):

    enemy_right = [pygame.image.load('sprites/R1E.png'), pygame.image.load('sprites/R2E.png'),
                     pygame.image.load('sprites/R3E.png'), pygame.image.load('sprites/R4E.png'), pygame.image.load('sprites/R5E.png'),
                     pygame.image.load('sprites/R6E.png'), pygame.image.load('sprites/R7E.png'), pygame.image.load('sprites/R8E.png'),
                     pygame.image.load('sprites/R9E.png'), pygame.image.load('sprites/R10E.png'), pygame.image.load('sprites/R11E.png')]

    enemy_left = [pygame.image.load('sprites/L1E.png'), pygame.image.load('sprites/L2E.png'),
                    pygame.image.load('sprites/L3E.png'),pygame.image.load('sprites/L4E.png'), pygame.image.load('sprites/L5E.png'),
                    pygame.image.load('sprites/L6E.png'),pygame.image.load('sprites/L7E.png'), pygame.image.load('sprites/L8E.png'),
                    pygame.image.load('sprites/L9E.png'), pygame.image.load('sprites/L10E.png'), pygame.image.load('sprites/L11E.png')]

    def __init__(self, posicao_x, posicao_y, width, height, end, velocidade):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.width = width
        self.height = height
        self.end = end
        self.velocidade = velocidade
        self.start = 50
        self.contWalk = 0
        self.alive = True
        self.score = 0
        self.life = 10

    def move(self):
        if self.start <= self.posicao_x + self.velocidade <= self.end:
            if self.posicao_x + self.velocidade == self.end:
                self.velocidade = self.velocidade*-1

            if self.posicao_x + self.velocidade == self.start:
                self.velocidade = abs(self.velocidade)

            self.posicao_x += self.velocidade



    def draw(self, tela, hit_box):
        self.move()

        if self.alive:
            if self.contWalk + 1 == len(Enemy.enemy_right):
                self.contWalk = 0

            if self.velocidade > 0:
                tela.blit(self.enemy_right[self.contWalk], (self.posicao_x, self.posicao_y))
                #pygame.draw.rect(tela, (255,0,0), hit_box,1)
                self.contWalk += 1

            if self.velocidade < 0:
                tela.blit(self.enemy_left[self.contWalk], (self.posicao_x, self.posicao_y))
                #pygame.draw.rect(tela, (255, 0, 0), hit_box, 1)
                self.contWalk += 1

            pygame.draw.rect(tela, (255, 0, 0),(self.posicao_x + 25 , self.posicao_y - 6, 30, 5), 0)
            pygame.draw.rect(tela, (0, 125, 0),(self.posicao_x + 25, self.posicao_y - 6, 30 - self.score*5, 5), 0)

        else:
            pass

    def hit(self):
        print("HIT!")