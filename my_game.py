import pygame  #importar para os jogos
from pygame.locals import * #locals é sub modulo de pygame
from sys import exit #funçao fechar janela

pygame.init()

largura = 640
altura = 480


tela = pygame.display.set_mode((largura, altura))

while True:
    #O FOR TA PEGANDO O EVENTO DE FECHAR QUANDO CLICO NO X
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()