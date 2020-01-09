import pygame
import sys

def main():

    resolucao = height, width = 800, 600
    COR = (0,255,0)
    POSICAO_CIRCULO = (400, 400)
    RAIO = 20

    pygame.init()
    tela = pygame.display.set_mode(resolucao)

    while True:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()

            if pygame.type == pygame.K_DOWN:
                POSICAO_CIRCULO[1] += 30



            print(evento.type)

        pygame.draw.circle(tela,COR,(POSICAO_CIRCULO[0], POSICAO_CIRCULO[1]),RAIO)
        pygame.display.update()


if __name__ == '__main__':
    main()



