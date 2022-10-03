import pygame
from abc import ABCMeta,abstractmethod


pygame.init()
screen = pygame.display.set_mode((800,600),0)
#Escrevendo os pontos feitos no jogo na tela
fonte = pygame.font.SysFont("arial",32,True,False)
#fim
amarelo = (255,215,0)
preto = (0,0,0)
vermelho = (255,0,0)

springverde = (0,255,127)
velocidade = 1


class Elementojogo (metaclass=ABCMeta):
    @abstractmethod
    def pintar(self,tela):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def processar_eventos(self,eventos):
        pass




#Cenario do pacman
class Cenario(Elementojogo):
    def __init__(self,tamanho, pac):
        self.pacman = pac
        self.tamanho = tamanho
        self.pontos = 0
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def pintar_pontos(self,tela):
        pontos_x = 30 * self.tamanho
        img_pontos = fonte.render(f"Score:{self.pontos}",True,amarelo)
        tela.blit(img_pontos,(pontos_x,50))


    def pintar_linha(self, tela,numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            half = self.tamanho // 2
            cor = preto

            if coluna == 2:
                cor = springverde
            pygame.draw.rect(tela,cor,(x,y,self.tamanho,self.tamanho),0)
            if coluna == 1:

                pygame.draw.circle(tela,amarelo,(x + half,y + half),self.tamanho // 10, 0)

    def pintar(self,tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela,numero_linha,linha)
            self.pintar_pontos(tela)

#Função para verificar se a alguma parede na frente do pacman!
    def calcular_regras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intecao

        if 0 <= col <= 27 and 0 <= lin <= 29:
            if self.matriz[lin][col] != 2:
                self.pacman.aceitar_movimento()
                if self.matriz[lin][col] == 1:
                    self.pontos += 1
                    self.matriz[lin][col] = 0

    def processar_eventos(self,evts):
        for e in evts:
            if e.type == pygame.QUIT:
                exit()
#Fim cenario Pacman

class Pacman (Elementojogo):
    def __init__(self,tamanho ):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.coluna_intencao = self.coluna
        self.linha_intecao = self.linha

    def calcular_regras(self):

        self.coluna_intencao = self.coluna + self.velocidade_x
        self.linha_intecao = self.linha + self.velocidade_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)


#Função para desenhar em Python

    def pintar(self,tela):
        #Desenhar corpo do Pacman
        pygame.draw.circle(tela,amarelo,(self.centro_x,self.centro_y),self.raio,0)


        #Desenho da boca
        canto_boca = (self.centro_x,self.centro_y)
        labio_supelrior = (self.centro_x + self.raio,self.centro_y - self.raio)
        labio_inferior = (self.centro_x * self.raio,self.centro_y)
        pontos = [canto_boca,labio_supelrior,labio_inferior]

        pygame.draw.polygon(tela,preto,pontos,0)


        #Olho do pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela,preto,(olho_x,olho_y),olho_raio,0)

    def processar_eventos(self,eventos):

        #Captura os eventos:
        #Responsavel por capturar se a tecla foi precionada
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = velocidade
#teclas para cima baixo direita:

                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = -velocidade
                elif e.key == pygame.K_UP:
                    self.velocidade_y = -velocidade
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = velocidade

#Responsavel por indetificar se a tecla foi soltada
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_UP:
                    self.velocidade_y = 0
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = 0

    def aceitar_movimento(self):
        self.linha = self.linha_intecao
        self.coluna = self.coluna_intencao

#Desenhando o fantasma na tela
#Classes
class Fantasma(Elementojogo):
    def __init__(self,cor,tamanho):
        self.coluna = 6.0
        self.linha = 8.0
        self.tamanho = tamanho
        self.cor = cor

    def pintar(self,tela):
        fatia = self.tamanho // 8
        pixel_x = int(self.coluna * self.tamanho)
        pixel_y = int(self.linha * self.tamanho)
        contorno = [(pixel_x,pixel_y + self.tamanho),
                    (pixel_x + fatia,pixel_y + fatia * 2),
                    (pixel_x + fatia * 3,pixel_y + fatia // 2),
                    (pixel_x + fatia * 3,pixel_y),
                    (pixel_x + fatia * 5,pixel_y),
                    (pixel_x + fatia * 6,pixel_y + fatia // 2),
                    (pixel_x + fatia * 7,pixel_y + fatia * 2),
                    (pixel_x + self.tamanho,pixel_y + self.tamanho)]

        pygame.draw.polygon(tela,self.cor,contorno,0)
#fim fantasma

    def calcular_regras(self):
        pass

    def processar_eventos(self,evts):
        pass

if __name__ == "__main__":
    size = 600 // 30
    pacman = Pacman(size)
    blinky = Fantasma(vermelho,size)
    cenario = Cenario(size, pacman)

    while True:
        #Calcular as regras:
        pacman.calcular_regras()
        cenario.calcular_regras()

        #pintar a tela:
    #screen. fill limpa a tela
        screen.fill(preto)
        blinky.pintar(screen)
        cenario.pintar(screen)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)


        #Captura os eventos:
        eventos = pygame.event.get()
        cenario.processar_eventos(eventos)
        pacman.processar_eventos(eventos)