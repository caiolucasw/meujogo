import pygame



class Projetil(object):

    def __init__(self, width, height, cor, raio, velocidade, dir):
        self.x = width
        self.y = height
        self.cor = cor
        self.raio = raio
        self.velocidade = velocidade
        self.dir = dir


    def draw(self, tela):

        pygame.draw.circle(tela, self.cor, (self.x,self.y), self.raio)
