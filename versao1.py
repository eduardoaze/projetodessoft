#imports
import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
<<<<<<< HEAD
pygame.display.set_caption('Mario game')
=======
pygame.display.set_caption('Luigi')
>>>>>>> 6991abff787cc42d32b34348fc039fecea2e4087
screen = pygame.display.set_mode((500, 500),0,32)
font = pygame.font.SysFont(None, 20)

# ----- Inicia assets
obstaculo_WIDTH = 50
obstaculo_HEIGHT = 38
luigi_WIDTH = 50
luigi_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('imagens\ofundo.jpg').convert()
#obstaculo_img = pygame.image.load('').convert_alpha()
#obstaculo_img = pygame.transform.scale(obstaculo_img, (obstaculo_WIDTH, obstaculo_HEIGHT))
luigi_img = pygame.image.load('imagens\parado.jpg').convert_alpha()
luigi_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
luigiparadopoder_img = pygame.image.load('imagens\paradopoder.jpg').convert_alpha()
luigiparadopoder_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
luigiesquerda_img = pygame.image.load('imagens\esquerda.jpg').convert_alpha()
luigiesquerda_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
luigidireita_img = pygame.image.load('imagens\direita.jpg').convert_alpha()
luigidireita_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
<<<<<<< HEAD
#tartaruga_img = pygame.image.load('').convert_alpha()

game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
=======
#tartaruga_img = pygame.image.load('').convert_alpha()
>>>>>>> 6991abff787cc42d32b34348fc039fecea2e4087
