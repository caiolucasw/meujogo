import pygame

class Player:

    ''' player ou sprite que irá aparecer na tela '''

    sprites_right = [pygame.image.load('sprites/R1E.png'), pygame.image.load('sprites/R2E.png'), pygame.image.load('sprites/R3E.png'),
                     pygame.image.load('sprites/R4E.png'),
                     pygame.image.load('sprites/R5E.png'), pygame.image.load('sprites/R6E.png'), pygame.image.load('sprites/R7E.png'),
                     pygame.image.load('sprites/R8E.png'),
                     pygame.image.load('sprites/R9E.png'), pygame.image.load('sprites/R10E.png'), pygame.image.load('sprites/R11E.png')]

    sprites_left = [pygame.image.load('sprites/L1E.png'), pygame.image.load('sprites/L2E.png'), pygame.image.load('sprites/L3E.png'),
                    pygame.image.load('sprites/L4E.png'),
                    pygame.image.load('sprites/L5E.png'), pygame.image.load('sprites/L6E.png'), pygame.image.load('sprites/L7E.png'),
                    pygame.image.load('sprites/L8E.png'),
                    pygame.image.load('sprites/L9E.png'), pygame.image.load('sprites/L10E.png'), pygame.image.load('sprites/L11E.png')]


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

    def draw_images(self, tela, bg):

        tela.blit(bg, (0,0))

        if self.contWalk + 1 == len(Player.sprites_right):
            self.contWalk = 0

        if self.left:
            tela.blit(Player.sprites_left[self.contWalk],(self.posicao_x, self.posicao_y))

        elif self.right or self.straight:
            tela.blit(Player.sprites_right[self.contWalk], (self.posicao_x, self.posicao_y))

        else:
            tela.blit(Player.sprites_right[self.contWalk], (self.posicao_x, self.posicao_y))

        self.contWalk += 1

        pygame.display.update()
