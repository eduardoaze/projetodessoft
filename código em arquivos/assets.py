import pygame
from pygame.locals import *
from config import luigi_HEIGHT, luigi_WIDTH


def loadassets ():
    font = pygame.font.SysFont(None, 20)
    assets = {}
    assets['vida_perde'] = pygame.mixer.Sound('sons/Nope (Construction Worker TF2) - Gaming Sound Effect (HD) (1).wav')
    assets['vida_ganha'] = pygame.mixer.Sound('sons/Mario Coin Sound - Sound Effect (HD).wav')
    assets['menu'] = pygame.mixer.Sound('sons\menu.wav')
    assets['fim'] = pygame.mixer.Sound('sons\Super Mario Dies Sound Effect.wav')
    assets['morre'] = pygame.mixer.Sound('sons\Splat - Gaming Sound Effect (HD).wav')
    assets['pulo'] = pygame.mixer.Sound('sons\Mario Jump - Gaming Sound Effect (HD).wav')
    assets['background'] = pygame.image.load('imagens/ofundo.jpg').convert()
    assets['luigi_img'] = pygame.image.load('imagens/luigi00.png').convert_alpha()
    assets['luigi_img'] = pygame.transform.scale(assets['luigi_img'], (luigi_WIDTH, luigi_HEIGHT))
    assets['luigidireita_img'] = pygame.image.load('imagens/luigi02.png').convert()
    assets['luigidireita_img'] = pygame.image.load('imagens/luigi02.png').convert_alpha()
    assets['luigidireita_img'] = pygame.transform.scale(assets['luigidireita_img'], (luigi_WIDTH, luigi_HEIGHT))
    assets['luigi_pulando_direita'] = pygame.image.load('imagens\luigi_voando.png').convert_alpha()
    assets['luigi_pulando_direita'] = pygame.transform.scale(assets['luigi_pulando_direita'], (luigi_WIDTH, luigi_HEIGHT))
    assets['luigi_pulando_esquerda'] = pygame.image.load('imagens\luigi_voando2.png').convert_alpha()
    assets['luigi_pulando_esquerda'] = pygame.transform.scale(assets['luigi_pulando_esquerda'], (luigi_WIDTH+13, luigi_HEIGHT+13)) #As imagens não estavam do mesmo tamanho
        
    #Lista animação bixo
    bixo = []
    for i in range(0,2):
        filename = 'imagens/bixo0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (50,38))
        bixo.append(img)
    assets['bixo'] = bixo

    luigi_esquerda_anim = []
    for i in range(3, 5):
        filename = 'imagens/luigi0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (50,38))
        luigi_esquerda_anim.append(img)

    #Lista para a animação de andar para a direita e ficar parado

    luigi_direita_anim = []
    for i in range(0, 3):
        filename = 'imagens/luigi0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (50,38))
        luigi_direita_anim.append(img)

    #Lista para a animação da tartaruga

    tartaruga_anim = []
    for i in range(1, 4):
        filename = 'imagens/tartaruga0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (50,38))
        tartaruga_anim.append(img)
    assets['tartaruga_anim'] = tartaruga_anim
    assets["score_font"] = font
    return assets