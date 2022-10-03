#O que e o pygame e uma biblioteca da linguagem de programação
# python gratuita e de codigo aberto para criar aplicativos multimidia como jogos


# O que e surface: E um tipo de objeto que representa uma imagem na biblioteca pygame

import pygame

pygame.init()
Amarelo = (255,255,0)
Preto = (0,0,0)
Velocidade = 1
velocidade_x = Velocidade
velocidade_y = Velocidade
x = 10
y = 10
raio = 30

tela = pygame.display.set_mode((640,480),0)

while True:
    #Calcula as regras do jogo
    x = x + velocidade_x
    y = y + velocidade_y

    #Eixo X
    if x + raio > 640:
        velocidade_x = - Velocidade
    if x - raio < 0:
        velocidade_x = Velocidade

    #Eixo Y
    elif y + raio > 480:
        velocidade_y = - Velocidade
    elif y + raio < 0:
        velocidade_y = Velocidade


    #Pinta as coisas na tela
    tela.fill(Preto)
                                #Surface na onde sera dsenhado o seu objeto,Raio quantidade de Pixels  
    pygame.draw.circle(tela,Amarelo,(int(x),int(velocidade_y)),raio,0)
    pygame.display.update()

    #Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()