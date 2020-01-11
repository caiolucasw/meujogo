import pygame

class Player:

    ''' player ou sprite que irá aparecer na tela '''

    sprites_right = [pygame.image.load('sprites/R1.png'), pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png'),
                     pygame.image.load('sprites/R4.png'), pygame.image.load('sprites/R5.png'), pygame.image.load('sprites/R6.png'),
                     pygame.image.load('sprites/R7.png'),  pygame.image.load('sprites/R8.png'), pygame.image.load('sprites/R9.png')]

    sprites_left = [pygame.image.load('sprites/L1.png'), pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png'),
                    pygame.image.load('sprites/L4.png'), pygame.image.load('sprites/L5.png'), pygame.image.load('sprites/L6.png'),
                    pygame.image.load('sprites/L7.png'), pygame.image.load('sprites/L8.png'),  pygame.image.load('sprites/L9.png')]




    def __init__(self, posicao_x, posicao_y, velocidade):

        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.veloc = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.straight = False
        self.contWalk = 0
        self.still = False

    def draw_images(self, tela, bg):

        tela.blit(bg, (0,0))

        if self.contWalk + 1 == len(Player.sprites_right):
            self.contWalk = 0

        if self.left and  (self.still == False):
            tela.blit(Player.sprites_left[self.contWalk],(self.posicao_x, self.posicao_y))
            self.contWalk += 1

        elif self.right and  (self.still == False):
            tela.blit(Player.sprites_right[self.contWalk], (self.posicao_x, self.posicao_y))
            self.contWalk += 1

        if self.straight:
            tela.blit(Player.sprites_right[self.contWalk], (self.posicao_x, self.posicao_y))
            self.contWalk += 1


        if self.still:
            if self.right:
                tela.blit(Player.sprites_right[0], (self.posicao_x, self.posicao_y))

            if self.left:
                tela.blit(Player.sprites_left[0], (self.posicao_x, self.posicao_y))


