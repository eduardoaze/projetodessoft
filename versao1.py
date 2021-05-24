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
pygame.display.set_caption('')
# ----- Inicia assets
obstaculo_WIDTH = 50
obstaculo_HEIGHT = 38
luigi_WIDTH = 50
luigi_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('imagens\ofundo.jpg').convert()
#obstaculo_img = pygame.image.load('').convert_alpha()
#obstaculo_img = pygame.transform.scale(obstaculo_img, (obstaculo_WIDTH, obstaculo_HEIGHT))
luigi_img = pygame.image.load('C:\projetodessoft\imagens\parado.jpg').convert_alpha()
luigi_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
luigiparadopoder_img = pygame.image.load('C:\projetodessoft\imagens\paradopoder.jpg').convert_alpha()
luigiparadopoder_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
luigiesquerda_img = pygame.image.load('C:\projetodessoft\imagens\esquerda.jpg').convert_alpha()
luigiesquerda_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
luigidireita_img = pygame.image.load('C:\projetodessoft\imagens\direita.jpg').convert_alpha()
luigidireita_img = pygame.transform.scale(luigi_img, (luigi_WIDTH, luigi_HEIGHT))
#tartaruga_img = pygame.image.load('').convert_alpha()